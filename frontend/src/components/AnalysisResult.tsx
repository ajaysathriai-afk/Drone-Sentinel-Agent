type Props = {
  result: any;
};

const threatConfig: Record<
  string,
  {
    color: string;
    bg: string;
  }
> = {
  CRITICAL: {
    color: "text-red-400",
    bg: "bg-red-500/10 border-red-500/20",
  },

  HIGH: {
    color: "text-orange-400",
    bg: "bg-orange-500/10 border-orange-500/20",
  },

  MEDIUM: {
    color: "text-yellow-400",
    bg: "bg-yellow-500/10 border-yellow-500/20",
  },

  LOW: {
    color: "text-green-400",
    bg: "bg-green-500/10 border-green-500/20",
  },
};

export default function AnalysisResult({
  result,
}: Props) {

  if (!result) return null;

  const threat =
    result.analysis?.threat_level?.toUpperCase() ??
    "LOW";

  const cfg =
    threatConfig[threat] ??
    threatConfig.LOW;

  return (

    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

      {/* Header */}

      <div className="flex justify-between items-center mb-6">

        <div>

          <h2 className="text-xl font-semibold">
            🧠 AI Intelligence Report
          </h2>

          <p className="text-sm text-slate-500 mt-1">
            Automated surveillance analysis
          </p>

        </div>

        <div
          className={`
            px-4
            py-2
            rounded-full
            border
            ${cfg.bg}
            ${cfg.color}
            font-semibold
          `}
        >
          {threat}
        </div>

      </div>

      {/* Objects */}

      <div className="bg-slate-800 rounded-xl p-4 mb-4">

        <h3 className="text-sm uppercase tracking-wide text-slate-400 mb-3">

          📦 Objects Detected

        </h3>

        <div className="space-y-2">

          {result.object_counts &&
            Object.entries(
              result.object_counts
            ).map(
              ([label, count]) => (

                <div
                  key={label}
                  className="flex justify-between"
                >

                  <span className="capitalize">

                    {label}

                  </span>

                  <span className="font-semibold text-cyan-400">

                    × {count as number}

                  </span>

                </div>

              )
            )}

        </div>

      </div>

      {/* AI Findings */}

      <div className="bg-slate-800 rounded-xl p-4 mb-4">

        <h3 className="text-sm uppercase tracking-wide text-slate-400 mb-3">

          🧠 AI Findings

        </h3>

        <p className="text-slate-300 leading-7">

          {result.analysis?.short_summary}

        </p>

      </div>

      {/* Recommendation */}

      <div className="bg-blue-500/10 border border-blue-500/20 rounded-xl p-4">

        <h3 className="text-sm uppercase tracking-wide text-blue-300 mb-3">

          ✅ Recommendation

        </h3>

        <p className="text-slate-300">

          {threat === "LOW"
            ? "Continue monitoring. No immediate action required."

            : threat === "MEDIUM"
            ? "Increase surveillance and monitor the area."

            : threat === "HIGH"
            ? "Dispatch a security team for verification."

            : "Immediate response required. Notify authorities."}

        </p>

      </div>

    </div>

  );

}