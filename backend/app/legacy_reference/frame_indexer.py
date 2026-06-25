"""
frame_indexer.py — Frame-by-frame indexing system using ChromaDB.

Stores analyzed frames as embeddings in a vector database, enabling semantic
search across historical surveillance data. Users can query by object, time,
location, or event type to retrieve relevant frames.
"""

import chromadb
from chromadb.config import Settings
import json
from datetime import datetime


class FrameIndexer:
    """Indexes drone surveillance frames in ChromaDB for semantic search and retrieval."""

    def __init__(self, persist_directory: str = "./chroma_db", collection_name: str = "drone_frames"):
        self.client = chromadb.Client(Settings(
            persist_directory=persist_directory,
            anonymized_telemetry=False,
        ))

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"description": "Drone surveillance frame index"}
        )

        self.indexed_count = 0

    def _build_document(self, analysis: dict) -> str:
        """Build a searchable document string from frame analysis."""
        parts = [
            f"Frame {analysis.get('frame_id', 'unknown')}",
            f"Time: {analysis.get('timestamp', 'unknown')}",
            f"Location: {analysis.get('location', 'unknown')}",
            f"Description: {analysis.get('raw_description', '')}",
            f"Summary: {analysis.get('summary', '')}",
            f"Objects: {', '.join(analysis.get('objects', []))}",
            f"Activity: {analysis.get('activity_type', 'unknown')}",
            f"Threat Level: {analysis.get('threat_level', 'none')}",
        ]

        identifiers = analysis.get("identifiers", [])
        if identifiers:
            parts.append(f"Identifiers: {', '.join(str(i) for i in identifiers)}")

        return " | ".join(parts)

    def _build_metadata(self, analysis: dict) -> dict:
        """Build metadata dictionary for ChromaDB storage."""
        timestamp = analysis.get("timestamp", "")
        hour = -1
        try:
            hour = datetime.fromisoformat(timestamp).hour
        except (ValueError, TypeError):
            pass

        return {
            "frame_id": analysis.get("frame_id", "unknown"),
            "timestamp": timestamp,
            "location": analysis.get("location", "unknown"),
            "activity_type": analysis.get("activity_type", "unknown"),
            "threat_level": analysis.get("threat_level", "none"),
            "hour": hour,
            "requires_alert": str(analysis.get("requires_alert", False)),
            "objects_json": json.dumps(analysis.get("objects", [])),
            "categories_json": json.dumps(analysis.get("object_categories", [])),
        }

    def index_frame(self, analysis: dict) -> None:
        """Index a single analyzed frame into ChromaDB."""
        frame_id = analysis.get("frame_id", f"frame_{self.indexed_count}")
        document = self._build_document(analysis)
        metadata = self._build_metadata(analysis)

        self.collection.upsert(
            documents=[document],
            metadatas=[metadata],
            ids=[frame_id],
        )
        self.indexed_count += 1

    def index_batch(self, analyses: list[dict]) -> int:
        """Index a batch of analyzed frames. Returns count of indexed frames."""
        for analysis in analyses:
            self.index_frame(analysis)
        return len(analyses)

    def search_by_query(self, query: str, n_results: int = 5) -> list[dict]:
        """Semantic search across indexed frames using natural language query."""
        results = self.collection.query(
            query_texts=[query],
            n_results=min(n_results, self.collection.count()),
        )

        formatted = []
        if results and results["documents"]:
            for i, doc in enumerate(results["documents"][0]):
                entry = {
                    "document": doc,
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results["distances"] else None,
                    "id": results["ids"][0][i] if results["ids"] else None,
                }
                formatted.append(entry)
        return formatted

    def search_by_location(self, location: str, n_results: int = 10) -> list[dict]:
        """Search frames by location."""
        results = self.collection.get(
            where={"location": location},
            limit=n_results,
        )

        formatted = []
        if results and results["documents"]:
            for i, doc in enumerate(results["documents"]):
                formatted.append({
                    "document": doc,
                    "metadata": results["metadatas"][i] if results["metadatas"] else {},
                    "id": results["ids"][i] if results["ids"] else None,
                })
        return formatted

    def search_by_threat_level(self, threat_level: str, n_results: int = 10) -> list[dict]:
        """Search frames by threat level."""
        results = self.collection.get(
            where={"threat_level": threat_level},
            limit=n_results,
        )

        formatted = []
        if results and results["documents"]:
            for i, doc in enumerate(results["documents"]):
                formatted.append({
                    "document": doc,
                    "metadata": results["metadatas"][i] if results["metadatas"] else {},
                    "id": results["ids"][i] if results["ids"] else None,
                })
        return formatted

    def search_by_time_range(self, start_hour: int, end_hour: int, n_results: int = 10) -> list[dict]:
        """Search frames by hour range."""
        if start_hour <= end_hour:
            where_filter = {"$and": [{"hour": {"$gte": start_hour}}, {"hour": {"$lte": end_hour}}]}
        else:
            # Handle overnight ranges like 22:00 - 06:00
            where_filter = {"$or": [{"hour": {"$gte": start_hour}}, {"hour": {"$lte": end_hour}}]}

        results = self.collection.get(
            where=where_filter,
            limit=n_results,
        )

        formatted = []
        if results and results["documents"]:
            for i, doc in enumerate(results["documents"]):
                formatted.append({
                    "document": doc,
                    "metadata": results["metadatas"][i] if results["metadatas"] else {},
                    "id": results["ids"][i] if results["ids"] else None,
                })
        return formatted

    def get_all_frames(self) -> list[dict]:
        """Retrieve all indexed frames."""
        results = self.collection.get()
        formatted = []
        if results and results["documents"]:
            for i, doc in enumerate(results["documents"]):
                formatted.append({
                    "document": doc,
                    "metadata": results["metadatas"][i] if results["metadatas"] else {},
                    "id": results["ids"][i] if results["ids"] else None,
                })
        return formatted

    def get_stats(self) -> dict:
        """Get indexer statistics."""
        return {
            "total_frames_indexed": self.collection.count(),
            "collection_name": self.collection.name,
        }


if __name__ == "__main__":
    print("=== Frame Indexer Test ===\n")

    indexer = FrameIndexer(persist_directory="./test_chroma_db")

    # Index some test frames
    test_analyses = [
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
            "identifiers": ["Blue Ford F150", "XYZ-5678"],
            "requires_alert": False,
        },
        {
            "frame_id": "FRM-020",
            "timestamp": "2024-01-15T00:01:00",
            "location": "main_gate",
            "raw_description": "Person walking slowly near main gate at midnight.",
            "summary": "Suspicious person at main gate at midnight",
            "objects": ["person in dark hoodie"],
            "object_categories": ["person"],
            "activity_type": "suspicious",
            "threat_level": "high",
            "identifiers": [],
            "requires_alert": True,
        },
    ]

    count = indexer.index_batch(test_analyses)
    print(f"Indexed {count} frames.\n")

    # Test search
    print("Search: 'truck events'")
    results = indexer.search_by_query("truck events")
    for r in results:
        print(f"  Found: {r['id']} — {r['metadata'].get('location', 'N/A')}")

    print("\nSearch: 'suspicious person at night'")
    results = indexer.search_by_query("suspicious person at night")
    for r in results:
        print(f"  Found: {r['id']} — {r['metadata'].get('threat_level', 'N/A')}")

    print(f"\nStats: {indexer.get_stats()}")

    # Cleanup test db
    import shutil
    shutil.rmtree("./test_chroma_db", ignore_errors=True)
