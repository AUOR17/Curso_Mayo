import {useState, useEffect} from "react";
import {useNavigate} from "react-router-dom";
import api from "../api";
import type {Adventurer,Guild} from "../types";
import AdventurerCard from "../components/AventurerCard";
import AddGuild from "../components/AddGuild";
import AddAdventurer from "../components/AddAdventurer";
import Button from "../components/Button";

export default function Dashboard(){
    const [guilds, setGuilds] = useState<Guild[]>([]);
    const [adventurers, setAdventurers] = useState<Adventurer[]>([]);
    const navigate = useNavigate();

    useEffect(() => {
        cargarTablero();
    }, []);

    const cargarTablero = async () => {
        try {
            const [resAdventurers, resGuilds] = await Promise.all([
                api.get<Adventurer[]>("adventurers/"),
                api.get<Guild[]>("guilds/")
            ]);

            setAdventurers(resAdventurers.data);
            setGuilds(resGuilds.data);
        }
        catch (error: any){
            console.error("Error detectado:", error);
            if (error.response && error.response.status === 401) {
                alert("Tu sesión ha expirado. Por favor, inicia sesión nuevamente.");
                handleLogout();
            }
        }
    };

    const handleLogout = () => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        navigate("/login");
    };

    const getGuildName = (guildId: number) => {
        const guild = guilds.find(g => g.id === guildId);
        return guild ? guild.name : "Sin gremio";   
        };

    return (
        <div className="min-h-screen bg-gray-900 text-white p-8 font-sans">
            <div className="flex items-center justify-between mb-8 border-b border-gray-700 pb-4">
                <h1 className="text-3xl font-bold text-yellow-500">Tablero de Aventureros</h1>
                <Button onClick={handleLogout} variant="danger" className="!w-auto">
                    Cerrar Sesión
                </Button>
            </div>

            <div className="flex flex-col lg:flex-row gap-8 items-start">
                <div className="flex flex-col gap-8 w-80 shrink-0">
                    <AddAdventurer guild={guilds} onSuccess={cargarTablero} />
                    <AddGuild onSuccess={cargarTablero} />
                </div>

                <div className="flex-1 grid grid-cols-[repeat(auto-fill,minmax(250px,1fr))] gap-6 content-start">
                    {adventurers.length === 0 ? (
                        <p className="text-gray-500"> No hay aventureros registrados aun </p>
                    ) : (
                        adventurers.map( (adventurer) => (
                            <AdventurerCard 
                            key={adventurer.id} 
                            adventurer={adventurer}
                            guilName= {getGuildName(adventurer.guild)}
                            onActionSuccess={cargarTablero} />
                        ))
                    )}
                </div>

            </div>

        </div>
    );
}