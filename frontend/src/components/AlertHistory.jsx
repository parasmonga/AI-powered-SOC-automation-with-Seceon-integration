export default function AlertHistory({ history }) {
    return (
        <div className="bg-slate-900 rounded-2xl shadow-2xl border border-slate-800 p-6 mt-6">

            <h2 className="text-2xl font-bold text-cyan-400 mb-6">
                📜 Recent Alerts
            </h2>

            {!history || history.length === 0 ? (

                <p className="text-slate-400">
                    No alerts analyzed yet.
                </p>

            ) : (

                <div className="space-y-4">

                    {history.map((item, index) => {

                        // Ignore invalid/error responses
                        if (
                            !item ||
                            item.status !== "success" ||
                            !item.alert ||
                            !item.alert.metadata ||
                            !item.decision
                        ) {
                            return null;
                        }

                        return (

                            <div
                                key={index}
                                className="bg-slate-800 rounded-xl p-4 border border-slate-700 hover:border-cyan-500 transition-all"
                            >

                                <div className="flex justify-between items-center">

                                    <div>

                                        <h3 className="text-lg font-bold">
                                            {item.alert.metadata.alert_name ?? "Unknown Alert"}
                                        </h3>

                                        <p className="text-slate-400 text-sm">
                                            {item.alert.metadata.alert_id ?? "-"}
                                        </p>

                                    </div>

                                    <span
                                        className={`px-3 py-1 rounded-full text-sm font-bold ${
                                            item.decision.decision === "Escalate"
                                                ? "bg-red-600"
                                                : item.decision.decision === "Investigate"
                                                ? "bg-yellow-500 text-black"
                                                : "bg-green-600"
                                        }`}
                                    >
                                        {item.decision.decision ?? "Unknown"}
                                    </span>

                                </div>

                                <div className="mt-4 flex justify-between text-sm text-slate-400">

                                    <span>
                                        Severity: {item.alert.metadata.severity ?? "-"}
                                    </span>

                                    <span>
                                        Risk: {item.decision.risk_score ?? "-"}
                                    </span>

                                </div>

                            </div>

                        );

                    })}

                </div>

            )}

        </div>
    );
}