import { useEffect, useState } from "react";
import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Tooltip,
} from "recharts";

import { fetchZoneAnalytics } from "../services/api";

type Props = {
  refreshKey: number;
};

type Zone = {
  zone: string;
  count: number;
};

const COLORS = [
  "#3b82f6",
  "#ef4444",
  "#22c55e",
  "#eab308",
  "#8b5cf6",
  "#06b6d4",
];

export default function ZoneAnalytics({
  refreshKey,
}: Props) {

  const [data, setData] = useState<Zone[]>([]);

  useEffect(() => {

    fetchZoneAnalytics()
      .then((result) => {

        if (Array.isArray(result)) {
          setData(result);
        } else {
          setData([]);
        }

      })
      .catch(console.error);

  }, [refreshKey]);

  const total = data.reduce(
    (sum, item) => sum + item.count,
    0
  );

  return (

    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">

      <div className="flex items-center justify-between mb-6">

        <div>

          <h2 className="text-xl font-semibold text-white">
            🛰️ Zone Analytics
          </h2>

          <p className="text-sm text-slate-400">
            Incident distribution by surveillance zone
          </p>

        </div>

        <span className="text-xs uppercase text-slate-500">
          {total} Total
        </span>

      </div>

      {data.length === 0 ? (

        <div className="h-[320px] flex flex-col items-center justify-center text-slate-500">

          <div className="text-5xl mb-4">
            📡
          </div>

          <p>
            No analytics available yet
          </p>

        </div>

      ) : (

        <div className="grid lg:grid-cols-2 gap-6">

          <div className="h-[320px]">

            <ResponsiveContainer>

              <PieChart>

                <Pie
                  data={data}
                  dataKey="count"
                  nameKey="zone"
                  outerRadius={110}
                  label
                >

                  {data.map((_, index) => (

                    <Cell
                      key={index}
                      fill={
                        COLORS[
                          index % COLORS.length
                        ]
                      }
                    />

                  ))}

                </Pie>

                <Tooltip />

              </PieChart>

            </ResponsiveContainer>

          </div>

          <div className="space-y-3">

            {data.map((zone, index) => (

              <div
                key={zone.zone}
                className="
                  flex
                  justify-between
                  items-center
                  bg-slate-800
                  rounded-lg
                  p-4
                "
              >

                <div className="flex items-center gap-3">

                  <div
                    className="w-4 h-4 rounded-full"
                    style={{
                      background:
                        COLORS[
                          index %
                          COLORS.length
                        ],
                    }}
                  />

                  <span className="text-white">

                    {zone.zone}

                  </span>

                </div>

                <span className="font-bold text-cyan-400">

                  {zone.count}

                </span>

              </div>

            ))}

          </div>

        </div>

      )}

    </div>

  );

}