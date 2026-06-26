import { useEffect, useState } from "react";
import { fetchStats } from "../services/api";

export default function StatsCards() {

  const [stats, setStats] = useState({
    incidents: 0,
    alerts: 0,
    high: 0,
    medium: 0,
    low: 0,
    zones: 0,
    threat_level: "LOW",
  });

  useEffect(() => {
    fetchStats()
      .then(setStats)
      .catch(console.error);
  }, []);

  const cards = [
    {
      title: "Total Incidents",
      value: stats.incidents,
      icon: "📍",
      color: "text-blue-400",
      border: "border-blue-500/30",
    },
    {
      title: "Active Alerts",
      value: stats.alerts,
      icon: "🚨",
      color: "text-red-400",
      border: "border-red-500/30",
    },
    {
      title: "High Threats",
      value: stats.high,
      icon: "🔥",
      color: "text-orange-400",
      border: "border-orange-500/30",
    },
    {
      title: "Medium Threats",
      value: stats.medium,
      icon: "🟡",
      color: "text-yellow-400",
      border: "border-yellow-500/30",
    },
    {
      title: "Low Threats",
      value: stats.low,
      icon: "🟢",
      color: "text-green-400",
      border: "border-green-500/30",
    },
    {
      title: "Zones Monitored",
      value: stats.zones,
      icon: "📡",
      color: "text-cyan-400",
      border: "border-cyan-500/30",
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
      {cards.map((card) => (
        <div
          key={card.title}
          className={`bg-slate-900 border ${card.border} rounded-xl p-6 hover:border-blue-500 transition`}
        >
          <div className="flex justify-between items-center mb-4">
            <div className="text-3xl">{card.icon}</div>
            <span className="text-xs text-slate-500 uppercase">
              LIVE
            </span>
          </div>

          <p className="text-slate-400 text-sm">
            {card.title}
          </p>

          <h2 className={`text-4xl font-bold mt-2 ${card.color}`}>
            {card.value}
          </h2>
        </div>
      ))}
    </div>
  );
}