import { useEffect, useState } from "react";
import { fetchAlerts } from "../services/api";

type Props = {
  refreshKey: number;
};

type Alert = {
  id: number;
  severity: string;
  message: string;
};

export default function AlertFeed({
  refreshKey,
}: Props) {

  const [alerts, setAlerts] = useState<Alert[]>([]);

  useEffect(() => {

    fetchAlerts()
      .then((data) => {

        if (Array.isArray(data)) {
          setAlerts(data);
        } else {
          setAlerts([]);
        }

      })
      .catch(console.error);

  }, [refreshKey]);

  const badgeColor = (severity: string) => {

    switch (severity) {

      case "HIGH":
        return "bg-red-500/20 text-red-400 border-red-500/40";

      case "MEDIUM":
        return "bg-yellow-500/20 text-yellow-400 border-yellow-500/40";

      default:
        return "bg-green-500/20 text-green-400 border-green-500/40";

    }

  };

  return (

    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">

      <div className="flex items-center justify-between mb-6">

        <h2 className="text-xl font-semibold text-white">
          🚨 Live Alerts
        </h2>

        <span className="text-xs text-slate-500 uppercase">
          {alerts.length} Active
        </span>

      </div>

      {alerts.length === 0 ? (

        <div className="text-center py-10 text-slate-500">

          <div className="text-5xl mb-4">
            📭
          </div>

          <p>
            No alerts generated yet
          </p>

        </div>

      ) : (

        <div className="space-y-4">

          {alerts
            .slice()
            .reverse()
            .map((alert) => (

              <div
                key={alert.id}
                className="
                  bg-slate-800
                  rounded-lg
                  border
                  border-slate-700
                  p-4
                "
              >

                <div className="flex justify-between items-start">

                  <span
                    className={`
                      px-3
                      py-1
                      rounded-full
                      text-xs
                      border
                      ${badgeColor(alert.severity)}
                    `}
                  >
                    {alert.severity}
                  </span>

                  <span className="text-xs text-slate-500">
                    Alert #{alert.id}
                  </span>

                </div>

                <p className="mt-3 text-slate-300">

                  {alert.message}

                </p>

              </div>

            ))}

        </div>

      )}

    </div>

  );

}