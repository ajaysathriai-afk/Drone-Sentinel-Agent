import { Link, useLocation } from "react-router-dom";

const navItems = [
  { path: "/", label: "Dashboard", icon: "⬛" },
  { path: "/incidents", label: "Incidents", icon: "🔴" },
  { path: "/investigator", label: "Investigator", icon: "🔵" },
];

export default function Sidebar() {
  const location = useLocation();

  return (
    <div className="w-64 h-screen bg-slate-950 border-r border-slate-800/60 flex flex-col">

      {/* Logo */}
      <div className="p-6 border-b border-slate-800/60">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-lg bg-blue-600 flex items-center justify-center text-lg">
            🚁
          </div>
          <div>
            <h1 className="font-bold text-white text-base leading-tight">
              DroneSentinel
            </h1>
            <p className="text-xs text-slate-500">
              Threat Intelligence
            </p>
          </div>
        </div>
      </div>

      {/* Nav */}
      <nav className="flex-1 p-4 space-y-1">
        <p className="text-xs text-slate-600 font-medium uppercase tracking-widest px-3 mb-3">
          Navigation
        </p>
        {navItems.map((item) => {
          const active = location.pathname === item.path;
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all ${
                active
                  ? "bg-blue-600/15 text-blue-400 border border-blue-500/20"
                  : "text-slate-400 hover:text-white hover:bg-slate-800/60"
              }`}
            >
              <span className="text-base">{item.icon}</span>
              {item.label}
              {active && (
                <div className="ml-auto w-1.5 h-1.5 rounded-full bg-blue-400" />
              )}
            </Link>
          );
        })}
      </nav>

      {/* Status */}
      <div className="p-4 border-t border-slate-800/60">
        <div className="bg-slate-900 rounded-xl p-4">
          <div className="flex items-center gap-2 mb-2">
            <div className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
            <span className="text-sm font-medium text-white">System Active</span>
          </div>
          <p className="text-xs text-slate-500">
            AI Surveillance Online
          </p>
          <div className="mt-3 h-1 bg-slate-800 rounded-full">
            <div className="h-1 bg-green-400 rounded-full w-4/5" />
          </div>
          <p className="text-xs text-slate-600 mt-1">CPU 23% · Healthy</p>
        </div>
      </div>

    </div>
  );
}
