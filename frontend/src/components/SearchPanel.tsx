import { useState } from "react";
import { searchIncidents } from "../services/api";

export default function SearchPanel() {

  const [query, setQuery] =
    useState("");

  const [results, setResults] =
    useState<any>(null);

  const [loading, setLoading] =
    useState(false);

  const handleSearch =
    async () => {

      if (!query.trim()) return;

      setLoading(true);

      try {

        const data =
          await searchIncidents(
            query
          );

        setResults(data);

      } finally {

        setLoading(false);

      }
    };

  return (
    <div className="bg-slate-900 border border-slate-700 rounded-xl p-6 shadow-lg">

      <div className="mb-4">
        <h2 className="text-xl font-semibold">
          Semantic Search
        </h2>

        <p className="text-sm text-slate-400 mt-1">
          Search historical incidents using AI-powered retrieval
        </p>
      </div>

      <div className="flex gap-2">

        <input
          value={query}
          onChange={(e) =>
            setQuery(
              e.target.value
            )
          }
          placeholder="e.g. vehicle, person, threat..."
          className="flex-1 bg-slate-800 border border-slate-700 p-3 rounded-lg"
        />

        <button
          onClick={handleSearch}
          className="bg-blue-600 hover:bg-blue-500 px-5 py-3 rounded-lg transition"
        >
          {loading
            ? "Searching..."
            : "Search"}
        </button>

      </div>

      {results?.documents?.[0] && (

        <div className="mt-6">

          <h3 className="font-semibold mb-4">
            Search Results
          </h3>

          <div className="space-y-3">

            {results.documents[0].map(
              (
                doc: string,
                index: number
              ) => (

                <div
                  key={index}
                  className="bg-slate-800 border border-slate-700 rounded-xl p-4 hover:border-blue-500 transition"
                >

                  <div className="flex items-center gap-2 mb-2">

                    <span>
                      📍
                    </span>

                    <span className="text-sm text-slate-400">
                      Incident
                    </span>

                  </div>

                  <p className="text-slate-300 leading-relaxed">
                    {doc}
                  </p>

                </div>

              )
            )}

          </div>

        </div>

      )}

    </div>
  );
}