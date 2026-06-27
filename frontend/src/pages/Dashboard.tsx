import { useState } from "react";

import StatsCards from "../components/StatsCards";
import ImageUpload from "../components/ImageUpload";
import AnalysisResult from "../components/AnalysisResult";
import AIInvestigator from "../components/AIInvestigator";
import AlertFeed from "../components/AlertFeed";
import IncidentTimeline from "../components/IncidentTimeline";
import ZoneAnalytics from "../components/ZoneAnalytics";

export default function Dashboard() {
  const [analysisResult, setAnalysisResult] = useState<any>(null);
  const [refreshKey, setRefreshKey] = useState(0);

  return (
    <div className="space-y-8">
      {/* Header */}

      <div>
        <h1 className="text-4xl font-bold text-white">
          🚁 DroneSentinel Command Center
        </h1>

        <p className="text-slate-400 mt-2">
          AI-powered surveillance, incident monitoring and threat
          investigation.
        </p>
      </div>

      {/* Stats */}

      <StatsCards
        key={`stats-${refreshKey}`}
        refreshKey={refreshKey}
      />

      {/* Workspace */}

      <div className="grid xl:grid-cols-2 gap-6">

        <div className="space-y-6">

          <ImageUpload
            onAnalysisComplete={(result) => {
              setAnalysisResult(result);
              setRefreshKey((prev) => prev + 1);
            }}
          />

          <AIInvestigator />

        </div>

        <div className="space-y-6">

          <AnalysisResult
            result={analysisResult}
          />

          <AlertFeed
            key={`alerts-${refreshKey}`}
            refreshKey={refreshKey}
          />

        </div>

      </div>

      <IncidentTimeline
        key={`timeline-${refreshKey}`}
        refreshKey={refreshKey}
      />

      <ZoneAnalytics
        key={`analytics-${refreshKey}`}
        refreshKey={refreshKey}
      />

    </div>
  );
}