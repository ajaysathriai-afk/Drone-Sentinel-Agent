import { useEffect, useState } from "react";
import { fetchAlerts } from "../services/api";

const severityConfig: Record<
  string,
  {
    color: string;
    bg: string;
    dot: string;
  }
> = {
  CRITICAL: {
    color: "text-red-400",
    bg: "bg-red-500/10 border-red-500/20",
    dot: "bg-red-500",
  },

  HIGH: {
    color: "text-orange-400",
    bg: "bg-orange-500/10 border-orange-500/20",
    dot: "bg-orange-500",
  },

  MEDIUM: {
    color: "text-yellow-400",
    bg: "bg-yellow-500/10 border-yellow-500/20",
    dot: "bg-yellow-500",
  },

  LOW: {
    color: "text-green-400",
    bg: "bg-green-500/10 border-green-500/20",
    dot: "bg-green-500",
  },
};

export default function AlertFeed() {

  const [alerts, setAlerts] =
    useState<any[]>([]);

  useEffect(() => {

    fetchAlerts()
      .then(setAlerts)
      .catch(console.error);

  }, []);

  return (

    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

      {/* Header */}

      <div className="flex items-center justify-between mb-6">

        <div>

          <h2 className="text-xl font-semibold text-white">
            🚨 Live Alert Feed
          </h2>

          <p className="text-sm text-slate-500 mt-1">
            Active security notifications
          </p>

        </div>

        <span className="px-3 py-1 rounded-full bg-red-500/10 border border-red-500/20 text-red-400 text-xs">

          {alerts.length} Active

        </span>

      </div>

      {alerts.length === 0 ? (

        <div className="py-16 text-center">

          <div className="text-5xl mb-3">
            ✅
          </div>

          <p className="text-slate-500">
            No active alerts
          </p>

        </div>

      ) : (

        <div className="space-y-4">

          {alerts.map((alert, index) => {

            const cfg =
              severityConfig[
                alert.severity?.toUpperCase()
              ] ??
              severityConfig.LOW;

            return (

              <div
                key={index}
                className={`
                  rounded-xl
                  border
                  ${cfg.bg}
                  p-4
                  hover:scale-[1.01]
                  transition
                `}
              >

                <div className="flex justify-between items-start">

                  <div className="flex gap-3">

                    <div
                      className={`w-3 h-3 rounded-full mt-2 ${cfg.dot}`}
                    />

                    <div>

                      <div
                        className={`font-semibold ${cfg.color}`}
                      >
                        {alert.severity}
                      </div>

                      <div className="text-slate-300 mt-1">

                        {alert.message}

                      </div>

                    </div>

                  </div>

                  <span className="text-xs text-slate-500">

                    LIVE

                  </span>

                </div>

              </div>

            );

          })}

        </div>

      )}

    </div>

  );

}