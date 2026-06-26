import { useEffect, useState } from "react";
import { fetchStats } from "../services/api";

type Props = {
  refreshKey: number;
};

type Stats = {
  incidents: number;
  alerts: number;
  threat_level: string;
  high: number;
  medium: number;
  low: number;
  zones: number;
};

export default function StatsCards({
  refreshKey,
}: Props) {

  const [stats, setStats] = useState<Stats>({
    incidents: 0,
    alerts: 0,
    threat_level: "LOW",
    high: 0,
    medium: 0,
    low: 0,
    zones: 0,
  });

  useEffect(() => {

    fetchStats()
      .then((data) => {

        setStats({
          incidents: data.incidents ?? 0,
          alerts: data.alerts ?? 0,
          threat_level: data.threat_level ?? "LOW",
          high: data.high ?? 0,
          medium: data.medium ?? 0,
          low: data.low ?? 0,
          zones: data.zones ?? 0,
        });

      })
      .catch(console.error);

  }, [refreshKey]);

  const threatColor =
    stats.threat_level === "CRITICAL"
      ? "text-red-400"
      : stats.threat_level === "HIGH"
      ? "text-orange-400"
      : stats.threat_level === "MEDIUM"
      ? "text-yellow-400"
      : "text-green-400";

  const cards = [

    {
      title: "Incidents",
      value: stats.incidents,
      icon: "📍",
      border: "border-blue-500/30",
      valueColor: "text-blue-400",
    },

    {
      title: "Alerts",
      value: stats.alerts,
      icon: "🚨",
      border: "border-red-500/30",
      valueColor: "text-red-400",
    },

    {
      title: "High",
      value: stats.high,
      icon: "🔴",
      border: "border-red-500/30",
      valueColor: "text-red-400",
    },

    {
      title: "Medium",
      value: stats.medium,
      icon: "🟠",
      border: "border-yellow-500/30",
      valueColor: "text-yellow-400",
    },

    {
      title: "Low",
      value: stats.low,
      icon: "🟢",
      border: "border-green-500/30",
      valueColor: "text-green-400",
    },

    {
      title: "Zones",
      value: stats.zones,
      icon: "🛰️",
      border: "border-cyan-500/30",
      valueColor: "text-cyan-400",
    },

  ];

  return (

    <div className="grid grid-cols-2 xl:grid-cols-6 gap-5">

      {cards.map((card) => (

        <div
          key={card.title}
          className={`
            bg-slate-900
            border
            ${card.border}
            rounded-xl
            p-5
            transition
            hover:border-blue-500
          `}
        >

          <div className="flex items-center justify-between">

            <div className="text-3xl">
              {card.icon}
            </div>

            <span className="text-xs text-slate-500 uppercase">
              LIVE
            </span>

          </div>

          <p className="mt-5 text-slate-400 text-sm">
            {card.title}
          </p>

          <h2 className={`text-3xl font-bold mt-2 ${card.valueColor}`}>
            {card.value}
          </h2>

        </div>

      ))}

    </div>

  );

}