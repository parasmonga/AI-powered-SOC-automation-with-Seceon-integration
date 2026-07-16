
import { useState } from "react";
import api from "../services/api";

export default function AlertForm({ onResult }) {

    const [loading, setLoading] = useState(false);

    const [alertData, setAlertData] = useState({

        alert_id: "ALT-1001",

        alert_name: "PowerShell Execution",

        severity: "High",

        timestamp: new Date().toISOString(),

        source_ip: "192.168.10.5",

        destination_ip: "8.8.8.8",

        protocol: "TCP",

        username: "administrator",

        hostname: "SERVER-01",

        description: "Suspicious PowerShell command"

    });

    const handleChange = (e) => {

        setAlertData({

            ...alertData,

            [e.target.name]: e.target.value

        });

    };

    const analyzeAlert = async () => {

        setLoading(true);

        try {

            const payload = {

                ...alertData,

                timestamp: new Date().toISOString()

            };

            const response = await api.post(
                "/alerts",
                payload
            );

            console.log("Backend Response:", response.data);

            onResult(response.data);

        }

        catch (error) {

            console.error(error);

            onResult({

                status: "error",

                message:
                    error.response?.data?.message ||
                    error.message

            });

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div className="space-y-5">

            <div>

                <label className="block text-sm text-slate-400 mb-2">

                    Alert Name

                </label>

                <input

                    className="w-full rounded-lg bg-slate-800 border border-slate-700 px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-cyan-500"

                    name="alert_name"

                    value={alertData.alert_name}

                    onChange={handleChange}

                />

            </div>

            <div>

                <label className="block text-sm text-slate-400 mb-2">

                    Severity

                </label>

                <select

                    className="w-full rounded-lg bg-slate-800 border border-slate-700 px-4 py-3 text-white"

                    name="severity"

                    value={alertData.severity}

                    onChange={handleChange}

                >

                    <option>Low</option>

                    <option>Medium</option>

                    <option>High</option>

                    <option>Critical</option>

                </select>

            </div>

            <div>

                <label className="block text-sm text-slate-400 mb-2">

                    Source IP

                </label>

                <input

                    className="w-full rounded-lg bg-slate-800 border border-slate-700 px-4 py-3 text-white"

                    name="source_ip"

                    value={alertData.source_ip}

                    onChange={handleChange}

                />

            </div>

            <div>

                <label className="block text-sm text-slate-400 mb-2">

                    Destination IP

                </label>

                <input

                    className="w-full rounded-lg bg-slate-800 border border-slate-700 px-4 py-3 text-white"

                    name="destination_ip"

                    value={alertData.destination_ip}

                    onChange={handleChange}

                />

            </div>

            <button

                onClick={analyzeAlert}

                disabled={loading}

                className="w-full bg-cyan-600 hover:bg-cyan-500 transition duration-300 rounded-lg py-3 font-bold text-white"

            >

                {

                    loading

                        ? "Analyzing..."

                        : "🛡 Analyze Threat"

                }

            </button>

        </div>

    );

}