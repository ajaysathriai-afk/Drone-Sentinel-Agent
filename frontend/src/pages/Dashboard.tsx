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

  const handleAnalysisComplete = (result: any) => {
    setAnalysisResult(result);

    // Force dashboard widgets to reload
    setRefreshKey((prev) => prev + 1);
  };

  return (

    <div className="space-y-8">

      {/* Header */}

      <div>

        <h1 className="text-4xl font-bold text-white">
          🚁 DroneSentinel Command Center
        </h1>

        <p className="text-slate-400 mt-2">
          AI-powered surveillance, incident monitoring and threat investigation.
        </p>

      </div>

      {/* Stats */}

      <StatsCards key={`stats-${refreshKey}`} />

      {/* Workspace */}

      <div className="grid xl:grid-cols-2 gap-6">

        {/* LEFT */}

        <div className="space-y-6">

          <ImageUpload
            onAnalysisComplete={handleAnalysisComplete}
          />

          <AIInvestigator />

        </div>

        {/* RIGHT */}

        <div className="space-y-6">

          <AnalysisResult
            result={analysisResult}
          />

          <AlertFeed key={`alerts-${refreshKey}`} />

        </div>

      </div>

      {/* Timeline */}

      <IncidentTimeline key={`timeline-${refreshKey}`} />

      {/* Analytics */}

      <ZoneAnalytics key={`analytics-${refreshKey}`} />

    </div>

  );

}