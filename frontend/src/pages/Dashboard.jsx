import { useState } from "react";

import Navbar from "../components/Navbar";
import AlertForm from "../components/AlertForm";
import AlertHistory from "../components/AlertHistory";

export default function Dashboard() {

    const [result, setResult] = useState(null);
    const [history, setHistory] = useState([]);

    const handleResult = (response) => {
        setResult(response);
        setHistory((prev) => [response, ...prev]);
    };

    return (

        <div className="min-h-screen bg-slate-950 text-white">

            <div className="max-w-7xl mx-auto p-8">

                <Navbar />

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

                    {/* Alert Form */}

                    <div className="bg-slate-900 rounded-2xl border border-slate-800 p-6">

                        <h2 className="text-2xl font-bold text-cyan-400 mb-6">
                            🚨 Alert Input
                        </h2>

                        <AlertForm onResult={handleResult} />

                    </div>

                    {/* Risk Summary */}

                    <div className="bg-slate-900 rounded-2xl border border-red-900 p-6">

                        <h2 className="text-2xl font-bold text-red-400 mb-6">
                            🔥 Risk Summary
                        </h2>

                        {result ? (

                            <div className="flex flex-col items-center justify-center h-72">

                                <h1 className="text-8xl font-extrabold text-red-500">
                                    {result.decision?.risk_score}
                                </h1>

                                <h2 className="text-3xl font-bold mt-4">
                                    {result.decision?.decision}
                                </h2>

                                <p className="text-slate-400 mt-3">
                                    Confidence
                                </p>

                                <p className="text-xl text-cyan-400 font-semibold">
                                    {(result.decision?.probability * 100).toFixed(2)}%
                                </p>

                            </div>

                        ) : (

                            <div className="flex flex-col items-center justify-center h-72">

                                <h1 className="text-8xl text-red-500">
                                    --
                                </h1>

                                <p className="text-2xl mt-4">
                                    Waiting...
                                </p>

                                <p className="text-slate-400">
                                    Analyze an alert
                                </p>

                            </div>

                        )}

                    </div>

                    {/* Threat Intelligence */}

                    <div className="bg-slate-900 rounded-2xl border border-green-900 p-6">

                        <h2 className="text-2xl font-bold text-green-400 mb-6">
                            🌍 Threat Intelligence
                        </h2>

                        {result ? (

                            <div className="space-y-5">

                                <div>
                                    <p className="text-slate-400">Reputation</p>
                                    <h3 className="text-2xl font-bold">
                                        {result.threat?.reputation}
                                    </h3>
                                </div>

                                <div>
                                    <p className="text-slate-400">Blacklisted</p>
                                    <h3 className="text-2xl font-bold">
                                        {result.threat?.blacklisted ? "Yes" : "No"}
                                    </h3>
                                </div>

                                <div>
                                    <p className="text-slate-400">Source IP</p>
                                    <h3 className="text-xl">
                                        {result.threat?.ip}
                                    </h3>
                                </div>

                            </div>

                        ) : (

                            <p className="text-slate-400">
                                Waiting for analysis...
                            </p>

                        )}

                    </div>

                    {/* MITRE */}

                    <div className="bg-slate-900 rounded-2xl border border-yellow-900 p-6">

                        <h2 className="text-2xl font-bold text-yellow-400 mb-6">
                            🎯 MITRE ATT&CK
                        </h2>

                        {result ? (

                            <div className="space-y-5">

                                <div>
                                    <p className="text-slate-400">Technique</p>
                                    <h3 className="text-2xl font-bold">
                                        {result.mitre?.technique}
                                    </h3>
                                </div>

                                <div>
                                    <p className="text-slate-400">Technique ID</p>
                                    <h3 className="text-2xl font-bold">
                                        {result.mitre?.technique_id}
                                    </h3>
                                </div>

                                <div>
                                    <p className="text-slate-400">Tactic</p>
                                    <h3 className="text-2xl font-bold">
                                        {result.mitre?.tactic}
                                    </h3>
                                </div>

                            </div>

                        ) : (

                            <p className="text-slate-400">
                                Waiting for analysis...
                            </p>

                        )}

                    </div>

                </div>

                {/* AI Explanation */}

                <div className="bg-slate-900 rounded-2xl border border-purple-900 p-6 mt-6">

                    <h2 className="text-2xl font-bold text-purple-400 mb-6">
                        🤖 AI Explanation
                    </h2>

                    {result ? (

                        <ul className="space-y-4">

                            {result.explanation?.map((line, index) => (

                                <li
                                    key={index}
                                    className="bg-slate-800 rounded-lg p-4 border-l-4 border-purple-500"
                                >
                                    ✅ {line}
                                </li>

                            ))}

                        </ul>

                    ) : (

                        <p className="text-slate-400">
                            Waiting for analysis...
                        </p>

                    )}

                </div>

                {/* Alert History */}

                <AlertHistory history={history} />

            </div>

        </div>

    );

}