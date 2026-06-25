import { useState } from "react";
import { chatWithInvestigator } from "../services/api";

export default function AIInvestigator() {

  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const suggestions = [
    "Latest incident",
    "Show recent incidents",
    "How many incidents?",
    "Any high threat events?"
  ];

  const handleAsk = async (question?: string) => {

    const finalQuery = question || query;

    if (!finalQuery.trim()) return;

    setLoading(true);
    setAnswer("");

    try {

      const data =
        await chatWithInvestigator(finalQuery);

      setAnswer(data.answer);

      if (question) {
        setQuery(question);
      }

    } catch (error) {

      console.error(error);

      setAnswer(
        "Unable to contact investigator."
      );

    } finally {

      setLoading(false);

    }

  };

  return (

    <div className="bg-slate-900 border border-slate-700 rounded-xl p-6">

      <div className="flex items-center gap-3 mb-2">

        <div className="text-3xl">
          🤖
        </div>

        <div>

          <h2 className="text-xl font-semibold">
            AI Security Investigator
          </h2>

          <p className="text-sm text-slate-400">
            Ask natural language questions about incidents and threats.
          </p>

        </div>

      </div>

      {/* Suggested Questions */}

      <div className="flex flex-wrap gap-2 mt-5 mb-5">

        {suggestions.map((item) => (

          <button
            key={item}
            onClick={() => handleAsk(item)}
            className="
              bg-slate-800
              hover:bg-blue-600
              border
              border-slate-700
              rounded-full
              px-4
              py-2
              text-sm
              transition
            "
          >
            {item}
          </button>

        ))}

      </div>

      {/* Input */}

      <div className="flex gap-3">

        <input
          value={query}
          onChange={(e) =>
            setQuery(e.target.value)
          }
          placeholder="Ask anything about incidents..."
          className="
            flex-1
            bg-slate-800
            border
            border-slate-700
            rounded-xl
            px-4
            py-3
            outline-none
            focus:border-blue-500
          "
        />

        <button
          onClick={() => handleAsk()}
          disabled={loading}
          className="
            bg-blue-600
            hover:bg-blue-500
            rounded-xl
            px-6
            font-medium
            disabled:opacity-50
          "
        >
          {loading
            ? "Thinking..."
            : "Ask AI"}
        </button>

      </div>

      {/* Response */}

      {(loading || answer) && (

        <div className="mt-6 bg-slate-800 rounded-xl border border-slate-700 p-5">

          <div className="flex items-center gap-2 mb-4">

            <span className="text-xl">
              🤖
            </span>

            <span className="font-semibold">
              Investigation Result
            </span>

          </div>

          {loading ? (

            <div className="text-slate-400">
              AI is analyzing incident history...
            </div>

          ) : (

            <div className="whitespace-pre-wrap leading-7 text-slate-300">
              {answer}
            </div>

          )}

        </div>

      )}

    </div>

  );

}