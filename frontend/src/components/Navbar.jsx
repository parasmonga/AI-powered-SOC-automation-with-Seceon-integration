import { ShieldCheck, Activity } from "lucide-react";

export default function Navbar() {
    return (
        <div className="bg-slate-900 text-white px-8 py-5 rounded-xl shadow-xl flex justify-between items-center">

            <div className="flex items-center gap-3">

                <ShieldCheck className="text-cyan-400" size={34} />

                <div>

                    <h1 className="text-3xl font-bold">
                        AI SOC Decision Engine
                    </h1>

                    <p className="text-slate-400 text-sm">
                        Intelligent Alert Triage Platform
                    </p>

                </div>

            </div>

            <div className="flex items-center gap-2">

                <Activity
                    className="text-green-400 animate-pulse"
                    size={18}
                />

                <span className="text-green-400 font-semibold">
                    SYSTEM ONLINE
                </span>

            </div>

        </div>
    );
}