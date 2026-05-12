import {useState} from "react";
import api from "../api";
import Button from "./Button";

interface AddGuildProps {
    onSuccess: () => void;
}

export default function AddGuild({onSuccess}: AddGuildProps) {
   
    const [newGuildName, setNewGuildName] = useState("");
    const [newGuildKingdom, setNewGuildKingdom] = useState("");
    const [newGuildCapacity, setNewGuildCapacity] = useState(50);

    
    const crearGremio = async (e: React.SyntheticEvent<HTMLFormElement>) => {
        e.preventDefault();

        try {
            await api.post("guilds/", {
                name: newGuildName,
                kingdom: newGuildKingdom,
                capacity: newGuildCapacity
            });

            setNewGuildName("");
            setNewGuildKingdom("");
            setNewGuildCapacity(50);
            onSuccess();
        }
        catch (error){
            console.error(error);
            alert("Error al crear el gremio");
        }
        };


    return (
        <div className="bg-gray-800 p-6 rounded-lg border border-gray-700 shadow-md" >
            <h2 className="text-xl font-bold text-yellow-500 mb-4"> Fundar Gremio</h2>
            <form onSubmit={crearGremio} noValidate className="flex flex-col gap-4">

                <div>
                    <label className="block text-sm text-gray-400 mb-2">Nombre</label>
                    <input
                        type="text"
                        value={newGuildName}
                        onChange={(e) => setNewGuildName(e.target.value)}
                        required
                        className="bg-gray-700 text-gray-300 placeholder:text-gray-500 border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Nombre del gremio"
                    />
                </div>

                <div>
                    <label className="block text-sm text-gray-400 mb-2">Reino</label>
                    <input
                        type="text"
                        value={newGuildKingdom}
                        onChange={(e) => setNewGuildKingdom(e.target.value)}
                        required
                        className="bg-gray-700 text-gray-300 border border-gray-500 focus:outline-none focus:ring-2 focus:ring-yellow-500"
                    />
                </div>

                <div>
                    <label className="block text-sm text-gray-400 mb-2">Capacidad maxima</label>
                    <input
                        type="text"
                        value={newGuildCapacity}
                        onChange={(e) => setNewGuildCapacity(Number(e.target.value))}
                        required
                        className="bg-gray-700 text-gray-300 border border-gray-500 focus:outline-none focus:ring-2 focus:ring-yellow-500"
                    />
                </div>

                <Button type="submit" variant="warning" className="mt-2">Construir Gremio</Button>

            </form>

        </div>
    );
}