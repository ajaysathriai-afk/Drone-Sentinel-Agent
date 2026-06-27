import { useEffect, useState } from "react";
import { fetchStats } from "../services/api";

type Props = {
  refreshKey: number;
};

export default function StatsCards({
  refreshKey,
}: Props) {

  const [stats, setStats] = useState({
    incidents: 0,
    alerts: 0,
    threat_level: "LOW",
  });

  useEffect(() => {
    fetchStats()
      .then(setStats)
      .catch(console.error);
  }, [refreshKey]);

  const cards = [
    {
      title: "Total Incidents",
      value: stats.incidents,
      icon: "📍",
      border: "border-blue-500/30",
      valueColor: "text-blue-400",
    },
    {
      title: "Active Alerts",
      value: stats.alerts,
      icon: "🚨",
      border: "border-red-500/30",
      valueColor: "text-red-400",
    },
    {
      title: "Threat Level",
      value: stats.threat_level,
      icon: "🛡️",
      border: "border-yellow-500/30",
      valueColor:
        stats.threat_level === "CRITICAL"
          ? "text-red-500"
          : stats.threat_level === "HIGH"
          ? "text-orange-400"
          : stats.threat_level === "MEDIUM"
          ? "text-yellow-400"
          : "text-green-400",
    },
  ];

  return (
    <div className="grid md:grid-cols-3 gap-5">

      {cards.map((card) => (

        <div
          key={card.title}
          className={`
            bg-slate-900
            border
            ${card.border}
            rounded-xl
            p-6
            transition
            hover:border-blue-500
          `}
        >

          <div className="flex items-center justify-between mb-5">

            <div className="text-3xl">
              {card.icon}
            </div>

            <span className="text-xs uppercase tracking-wider text-slate-500">
              LIVE
            </span>

          </div>

          <p className="text-slate-400 text-sm">
            {card.title}
          </p>

          <h2 className={`text-4xl font-bold mt-2 ${card.valueColor}`}>
            {card.value}
          </h2>

        </div>

      ))}

    </div>
  );
}