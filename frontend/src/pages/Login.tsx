import {useState} from "react";
import {useNavigate} from "react-router-dom";
import api from "../api";
import type {AuthTokens} from "../types";
import Button from "../components/Button";

export default function Login(){
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const [error, setError] = useState("");

    const handleLogin = async (e: React.SyntheticEvent<HTMLFormElement>) => {
        e.preventDefault();
        setError("");
        try {
            const response = await api.post<AuthTokens>("token/", { username, password });
            localStorage.setItem("access_token", response.data.access);
            localStorage.setItem("refresh_token", response.data.refresh);
            navigate("/dashboard");
        } catch (error) {
            console.error(error);
            setError("Credenciales inválidas");
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-900 text-white p-8 font-sans">
            <div className="bg-gray-800 p-8 rounded-lg shadow-xl w-96 border border-gray-700">
                <h1 className="text-3xl font-bold text-yellow-500 mb-8">Iniciar Sesión</h1>

                {error && (
                    <div className="bg-red-900 border border-red-500 text-red-200 p-3 rounded mb-4 text-sm text-center">
                        {error}
                    </div>
                )}

                <form onSubmit={handleLogin} className="flex flex-col gap-6">
                    <div className="mb-4">
                        <label className="block text-sm text-gray-400 mb-1">Nombre de Usuario</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white focus:outline-none focus:border-blue-500 transition-colors"
                            placeholder="Ingresa tu nombre de usuario"
                            required
                        />
                    </div>
                    <div className="mb-6">
                        <label  className="block text-gray-300 mb-2">Contraseña</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-white focus:outline-none focus:border-blue-500 transition-colors"
                            placeholder="Ingresa tu contraseña"
                            required
                        />
                    </div>
                    <Button type="submit" variant="primary" className="mt-2">
                        Iniciar Sesión
                    </Button>
                </form>
            </div>
        </div>
    );
}