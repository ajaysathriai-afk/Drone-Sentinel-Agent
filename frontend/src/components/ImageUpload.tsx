import { useDropzone } from "react-dropzone";
import { useState } from "react";
import { analyzeImage } from "../services/api";

type Props = {
  onAnalysisComplete: (result: any) => void;
};

export default function ImageUpload({
  onAnalysisComplete,
}: Props) {
  const [fileName, setFileName] = useState("");
  const [loading, setLoading] = useState(false);

  const { getRootProps, getInputProps } = useDropzone({
    accept: {
      "image/*": [],
    },

    onDrop: async (acceptedFiles) => {
      if (!acceptedFiles.length) return;

      const file = acceptedFiles[0];

      setFileName(file.name);
      setLoading(true);

      try {
        const result = await analyzeImage(file);
        onAnalysisComplete(result);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    },
  });

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-5">

      <div className="mb-4">
        <h2 className="text-lg font-semibold text-white">
          Drone Image Analysis
        </h2>

        <p className="text-sm text-slate-400">
          Upload a surveillance image for AI analysis
        </p>
      </div>

      <div
        {...getRootProps()}
        className="
          border-2
          border-dashed
          border-slate-700
          rounded-xl
          p-8
          cursor-pointer
          hover:border-blue-500
          hover:bg-slate-800/30
          transition
          text-center
        "
      >
        <input {...getInputProps()} />

        <div className="text-4xl mb-3">
          📡
        </div>

        <h3 className="font-medium text-white">
          Upload Drone Image
        </h3>

        <p className="text-sm text-slate-400 mt-2">
          Drag & Drop or Click
        </p>

        <p className="text-xs text-slate-500 mt-1">
          PNG • JPG • JPEG
        </p>
      </div>

      {fileName && (
        <div className="mt-4 flex items-center justify-between bg-slate-800 rounded-lg px-4 py-3 border border-slate-700">
          <span className="text-sm text-slate-300 truncate">
            📄 {fileName}
          </span>

          <span className="text-xs text-green-400">
            Ready
          </span>
        </div>
      )}

      {loading && (
        <div className="mt-4 rounded-lg bg-blue-500/10 border border-blue-500/30 px-4 py-3">

          <div className="flex items-center gap-3">

            <div className="animate-spin text-lg">
              🤖
            </div>

            <div>

              <p className="text-blue-400 font-medium">
                AI Processing...
              </p>

              <p className="text-xs text-slate-400">
                Detecting objects and generating threat assessment
              </p>

            </div>

          </div>

        </div>
      )}

    </div>
  );
}