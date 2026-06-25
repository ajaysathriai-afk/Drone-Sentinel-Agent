"""
alert_engine.py — Rule-based security alert engine for drone surveillance.

Processes analyzed frames and generates real-time security alerts based on
configurable rules covering time-based, zone-based, and behavior-based triggers.
"""

from datetime import datetime
from typing import Optional


class AlertEngine:
    """Generates security alerts based on configurable rules and analyzed frame data."""

    # Severity levels in order
    SEVERITY_ORDER = {"low": 1, "medium": 2, "high": 3, "critical": 4}

    def __init__(self):
        self.alerts: list[dict] = []
        self.vehicle_tracker: dict[str, list] = {}  # Track vehicle entries by identifier
        self.person_tracker: dict[str, list] = {}   # Track person sightings by location

    def _get_hour(self, timestamp: str) -> int:
        """Extract hour from ISO timestamp."""
        try:
            dt = datetime.fromisoformat(timestamp)
            return dt.hour
        except (ValueError, TypeError):
            return -1

    def _is_nighttime(self, timestamp: str) -> bool:
        """Check if timestamp falls in nighttime hours (22:00 - 06:00)."""
        hour = self._get_hour(timestamp)
        return hour >= 22 or hour < 6

    def _is_restricted_zone(self, location: str) -> bool:
        """Check if location is a restricted/sensitive zone."""
        restricted = ["perimeter_north", "perimeter_south", "warehouse", "loading_dock"]
        return location in restricted

    def _create_alert(self, frame_analysis: dict, rule_name: str,
                      message: str, severity: str) -> dict:
        """Create a structured alert object."""
        alert = {
            "alert_id": f"ALT-{len(self.alerts) + 1:04d}",
            "timestamp": frame_analysis.get("timestamp", "unknown"),
            "location": frame_analysis.get("location", "unknown"),
            "frame_id": frame_analysis.get("frame_id", "unknown"),
            "rule_triggered": rule_name,
            "severity": severity,
            "message": message,
            "threat_level": frame_analysis.get("threat_level", "unknown"),
            "objects_involved": frame_analysis.get("objects", []),
            "raw_description": frame_analysis.get("raw_description", ""),
        }
        self.alerts.append(alert)
        return alert

    def check_nighttime_person(self, analysis: dict) -> Optional[dict]:
        """Rule: Person detected during nighttime = HIGH alert."""
        if not self._is_nighttime(analysis.get("timestamp", "")):
            return None

        categories = analysis.get("object_categories", [])
        objects = analysis.get("objects", [])
        description = analysis.get("raw_description", "").lower()

        has_person = ("person" in categories or
                      any("person" in str(o).lower() for o in objects) or
                      "person" in description)

        if has_person:
            location = analysis.get("location", "unknown")
            return self._create_alert(
                analysis,
                rule_name="NIGHTTIME_PERSON",
                message=f"Person detected at {location} during nighttime hours. "
                        f"Details: {analysis.get('summary', 'N/A')}",
                severity="high"
            )
        return None

    def check_repeated_vehicle(self, analysis: dict) -> Optional[dict]:
        """Rule: Same vehicle entering more than once = MEDIUM alert."""
        identifiers = analysis.get("identifiers", [])
        objects = analysis.get("objects", [])
        activity = analysis.get("activity_type", "")

        if activity not in ["vehicle_entry", "vehicle_movement"]:
            return None

        # Build a vehicle key from identifiers or object descriptions
        vehicle_key = None
        for identifier in identifiers:
            if isinstance(identifier, str) and len(identifier) > 3:
                vehicle_key = identifier.lower()
                break

        if not vehicle_key:
            for obj in objects:
                if isinstance(obj, str) and any(v in obj.lower() for v in ["ford", "toyota", "truck", "sedan", "van"]):
                    vehicle_key = obj.lower()
                    break

        if not vehicle_key:
            return None

        if vehicle_key not in self.vehicle_tracker:
            self.vehicle_tracker[vehicle_key] = []

        self.vehicle_tracker[vehicle_key].append(analysis.get("timestamp", ""))

        if len(self.vehicle_tracker[vehicle_key]) > 1:
            count = len(self.vehicle_tracker[vehicle_key])
            return self._create_alert(
                analysis,
                rule_name="REPEATED_VEHICLE_ENTRY",
                message=f"Vehicle '{vehicle_key}' has entered the property {count} times today. "
                        f"Latest entry at {analysis.get('location', 'unknown')}.",
                severity="medium"
            )
        return None

    def check_restricted_zone(self, analysis: dict) -> Optional[dict]:
        """Rule: Unknown person in restricted zone = HIGH alert."""
        if not self._is_restricted_zone(analysis.get("location", "")):
            return None

        categories = analysis.get("object_categories", [])
        objects = analysis.get("objects", [])
        description = analysis.get("raw_description", "").lower()

        has_person = ("person" in categories or
                      any("person" in str(o).lower() for o in objects) or
                      "person" in description)

        # Check if it's suspicious activity
        suspicious_keywords = ["unknown", "unidentified", "photographing", "loitering", "checking"]
        is_suspicious = any(kw in description for kw in suspicious_keywords)

        if has_person and is_suspicious:
            return self._create_alert(
                analysis,
                rule_name="RESTRICTED_ZONE_INTRUSION",
                message=f"Suspicious person detected in restricted zone: {analysis.get('location', 'unknown')}. "
                        f"Details: {analysis.get('summary', 'N/A')}",
                severity="high"
            )
        return None

    def check_loitering(self, analysis: dict) -> Optional[dict]:
        """Rule: Person staying in same location across multiple frames = MEDIUM/HIGH alert."""
        location = analysis.get("location", "unknown")
        description = analysis.get("raw_description", "").lower()

        has_person = "person" in description

        if not has_person:
            return None

        if location not in self.person_tracker:
            self.person_tracker[location] = []

        self.person_tracker[location].append(analysis.get("timestamp", ""))

        if len(self.person_tracker[location]) > 1:
            severity = "high" if self._is_nighttime(analysis.get("timestamp", "")) else "medium"
            return self._create_alert(
                analysis,
                rule_name="LOITERING_DETECTED",
                message=f"Person detected at {location} multiple times. "
                        f"Possible loitering behavior. Sightings: {len(self.person_tracker[location])}.",
                severity=severity
            )
        return None

    def check_unidentified_vehicle_night(self, analysis: dict) -> Optional[dict]:
        """Rule: Unidentified vehicle at night = CRITICAL alert."""
        if not self._is_nighttime(analysis.get("timestamp", "")):
            return None

        description = analysis.get("raw_description", "").lower()
        has_vehicle = any(v in description for v in ["van", "truck", "car", "vehicle"])
        is_suspicious = any(kw in description for kw in ["unidentified", "unmarked", "no markings", "dark van", "unknown"])

        if has_vehicle and is_suspicious:
            return self._create_alert(
                analysis,
                rule_name="UNIDENTIFIED_VEHICLE_NIGHT",
                message=f"Unidentified vehicle detected at night near {analysis.get('location', 'unknown')}. "
                        f"Details: {analysis.get('summary', 'N/A')}",
                severity="critical"
            )
        return None

    def check_llm_alert(self, analysis: dict) -> Optional[dict]:
        """Rule: Use LLM's own threat assessment if it flagged an alert."""
        if analysis.get("requires_alert") and analysis.get("alert_message"):
            # Avoid duplicate alerts by checking if we already have one for this frame
            existing_frame_ids = [a["frame_id"] for a in self.alerts]
            if analysis["frame_id"] not in existing_frame_ids:
                return self._create_alert(
                    analysis,
                    rule_name="AI_THREAT_DETECTION",
                    message=analysis["alert_message"],
                    severity=analysis.get("threat_level", "medium")
                )
        return None

    def process_frame(self, analysis: dict) -> list[dict]:
        """Process a single analyzed frame through all alert rules. Returns list of triggered alerts."""
        triggered = []

        checks = [
            self.check_nighttime_person,
            self.check_repeated_vehicle,
            self.check_restricted_zone,
            self.check_loitering,
            self.check_unidentified_vehicle_night,
            self.check_llm_alert,
        ]

        for check in checks:
            alert = check(analysis)
            if alert:
                triggered.append(alert)

        return triggered

    def process_all_frames(self, analyses: list[dict]) -> list[dict]:
        """Process all analyzed frames and return all triggered alerts."""
        all_alerts = []
        for analysis in analyses:
            alerts = self.process_frame(analysis)
            all_alerts.extend(alerts)
        return all_alerts

    def get_alerts_by_severity(self, severity: str) -> list[dict]:
        """Get all alerts of a specific severity level."""
        return [a for a in self.alerts if a["severity"] == severity]

    def get_alert_summary(self) -> dict:
        """Get a summary of all alerts."""
        return {
            "total_alerts": len(self.alerts),
            "critical": len(self.get_alerts_by_severity("critical")),
            "high": len(self.get_alerts_by_severity("high")),
            "medium": len(self.get_alerts_by_severity("medium")),
            "low": len(self.get_alerts_by_severity("low")),
            "alerts": self.alerts,
        }


if __name__ == "__main__":
    print("=== Alert Engine Test ===\n")

    # Test with sample analyzed frames
    test_analyses = [
        {
            "frame_id": "FRM-020",
            "timestamp": "2024-01-15T00:01:00",
            "location": "main_gate",
            "raw_description": "Person walking slowly near main gate at midnight.",
            "summary": "Person loitering at main gate at midnight",
            "objects": ["person in dark hoodie"],
            "object_categories": ["person"],
            "activity_type": "suspicious",
            "threat_level": "high",
            "requires_alert": True,
            "alert_message": "Person loitering at main gate during nighttime.",
            "identifiers": [],
        },
        {
            "frame_id": "FRM-008",
            "timestamp": "2024-01-15T10:00:00",
            "location": "main_gate",
            "raw_description": "Blue Ford F150 pickup truck entering through main gate.",
            "summary": "Blue Ford F150 entering property",
            "objects": ["Blue Ford F150"],
            "object_categories": ["vehicle"],
            "activity_type": "vehicle_entry",
            "threat_level": "none",
            "requires_alert": False,
            "alert_message": None,
            "identifiers": ["Blue Ford F150", "XYZ-5678"],
        },
        {
            "frame_id": "FRM-015",
            "timestamp": "2024-01-15T16:00:00",
            "location": "main_gate",
            "raw_description": "Blue Ford F150 entering again through main gate for the second time today.",
            "summary": "Blue Ford F150 second entry today",
            "objects": ["Blue Ford F150"],
            "object_categories": ["vehicle"],
            "activity_type": "vehicle_entry",
            "threat_level": "low",
            "requires_alert": True,
            "alert_message": "Same vehicle entered twice today.",
            "identifiers": ["Blue Ford F150", "XYZ-5678"],
        },
    ]

    engine = AlertEngine()
    alerts = engine.process_all_frames(test_analyses)

    print(f"Triggered {len(alerts)} alerts:\n")
    for alert in alerts:
        print(f"  [{alert['severity'].upper()}] {alert['message']}")
        print(f"    Rule: {alert['rule_triggered']}, Frame: {alert['frame_id']}\n")
