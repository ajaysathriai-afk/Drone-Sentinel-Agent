import { useEffect, useState } from "react";
import { fetchIncidents } from "../services/api";

type Props = {
  refreshKey: number;
};

type Incident = {
  id: number;
  timestamp: string;
  event: string;
};

export default function IncidentTimeline({
  refreshKey,
}: Props) {

  const [incidents, setIncidents] = useState<Incident[]>([]);

  useEffect(() => {

    fetchIncidents()
      .then((data) => {

        if (Array.isArray(data)) {

          setIncidents(
            data
              .slice()
              .reverse()
          );

        } else {

          setIncidents([]);

        }

      })
      .catch(console.error);

  }, [refreshKey]);

  return (

    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">

      <div className="flex items-center justify-between mb-6">

        <h2 className="text-xl font-semibold text-white">
          📜 Incident Timeline
        </h2>

        <span className="text-xs uppercase text-slate-500">
          {incidents.length} Records
        </span>

      </div>

      {incidents.length === 0 ? (

        <div className="text-center py-10 text-slate-500">

          <div className="text-5xl mb-4">
            📭
          </div>

          <p>
            No incidents recorded yet.
          </p>

        </div>

      ) : (

        <div className="space-y-4">

          {incidents.map((incident) => (

            <div
              key={incident.id}
              className="
                border-l-4
                border-blue-500
                pl-5
                py-2
              "
            >

              <div className="flex items-center justify-between">

                <h3 className="text-white font-medium">

                  {incident.event}

                </h3>

                <span className="text-xs text-slate-500">

                  #{incident.id}

                </span>

              </div>

              <p className="text-sm text-slate-400 mt-2">

                {incident.timestamp}

              </p>

            </div>

          ))}

        </div>

      )}

    </div>

  );

}