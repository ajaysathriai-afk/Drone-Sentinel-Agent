import { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Cell } from "recharts";
import { fetchZoneAnalytics } from "../services/api";

const COLORS = ["#3b82f6", "#6366f1", "#8b5cf6", "#a855f7", "#ec4899"];

export default function ZoneAnalytics() {
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    fetchZoneAnalytics().then(setData).catch(console.error);
  }, []);

  const total = data.reduce((s, z) => s + z.count, 0);
  const highest = data.length > 0 ? [...data].sort((a, b) => b.count - a.count)[0].zone : "—";

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-5">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h2 className="text-base font-semibold text-white">Zone Analytics</h2>
          <p className="text-xs text-slate-500 mt-0.5">Incident distribution across monitored zones</p>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-3 mb-5">
        {[
          { label: "Active Zones", value: data.length },
          { label: "Total Incidents", value: total },
          { label: "Highest Activity", value: highest },
        ].map((s) => (
          <div key={s.label} className="bg-slate-800/50 rounded-lg p-3 text-center">
            <p className="text-xs text-slate-500 mb-1">{s.label}</p>
            <p className="text-xl font-bold text-white">{s.value}</p>
          </div>
        ))}
      </div>

      {data.length === 0 ? (
        <div className="h-48 flex items-center justify-center text-slate-600 text-sm">
          No zone data yet — analyze images to populate
        </div>
      ) : (
        <div className="h-52">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data} margin={{ top: 4, right: 4, left: -20, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
              <XAxis dataKey="zone" tick={{ fill: "#64748b", fontSize: 12 }} axisLine={false} tickLine={false} />
              <YAxis tick={{ fill: "#64748b", fontSize: 12 }} axisLine={false} tickLine={false} />
              <Tooltip
                contentStyle={{ backgroundColor: "#0f172a", border: "1px solid #1e293b", borderRadius: 8 }}
                labelStyle={{ color: "#94a3b8" }}
                itemStyle={{ color: "#e2e8f0" }}
              />
              <Bar dataKey="count" radius={[6, 6, 0, 0]}>
                {data.map((_, i) => (
                  <Cell key={i} fill={COLORS[i % COLORS.length]} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}
