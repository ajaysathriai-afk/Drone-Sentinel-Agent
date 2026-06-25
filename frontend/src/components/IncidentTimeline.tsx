import { useEffect, useState } from "react";
import { fetchIncidents } from "../services/api";

export default function IncidentTimeline() {
  const [incidents, setIncidents] = useState<any[]>([]);

  useEffect(() => {
    fetchIncidents()
      .then((data) => setIncidents(data.slice(-6).reverse()))
      .catch(console.error);
  }, []);

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

      {/* Header */}

      <div className="flex items-center justify-between mb-6">

        <div>
          <h2 className="text-xl font-semibold text-white">
            Activity Timeline
          </h2>

          <p className="text-sm text-slate-500 mt-1">
            Latest surveillance events
          </p>
        </div>

        <span className="px-3 py-1 rounded-full bg-blue-500/10 text-blue-400 text-xs border border-blue-500/20">
          {incidents.length} Events
        </span>

      </div>

      {/* Timeline */}

      {incidents.length === 0 ? (

        <div className="text-center py-16">

          <div className="text-5xl mb-4">
            📭
          </div>

          <p className="text-slate-500">
            No incidents recorded
          </p>

        </div>

      ) : (

        <div className="space-y-5 max-h-[520px] overflow-y-auto pr-2">

          {incidents.map((incident, index) => {

            const event =
              incident.event || "";

            const color =
              event.toLowerCase().includes("unauthorized")
                ? "bg-red-500"

                : event.toLowerCase().includes("vehicle")
                ? "bg-orange-500"

                : event.toLowerCase().includes("person")
                ? "bg-blue-500"

                : "bg-green-500";

            return (

              <div
                key={index}
                className="flex gap-4"
              >

                {/* Timeline */}

                <div className="flex flex-col items-center">

                  <div
                    className={`w-3 h-3 rounded-full ${color}`}
                  />

                  {index !== incidents.length - 1 && (

                    <div className="w-px flex-1 bg-slate-700 mt-2" />

                  )}

                </div>

                {/* Card */}

                <div className="flex-1 bg-slate-800 rounded-xl p-4 hover:bg-slate-700 transition">

                  <div className="flex justify-between items-center mb-2">

                    <span className="text-xs text-slate-500">
                      {incident.timestamp}
                    </span>

                    <span className="text-[10px] uppercase tracking-wider text-slate-400">
                      EVENT
                    </span>

                  </div>

                  <p className="text-sm text-white leading-relaxed">
                    {incident.event}
                  </p>

                </div>

              </div>

            );

          })}

        </div>

      )}

    </div>
  );
}