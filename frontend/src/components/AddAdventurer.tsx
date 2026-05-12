import {useState} from "react";
import api from "../api";
import type {Guild} from "../types";
import Button from "../components/Button";

interface AddAdventurerProps {
    guild: Guild[];
    onSuccess: () => void;
}

export default function AddAdventurer({guild, onSuccess}: AddAdventurerProps) {
    const [newName, setNewName] = useState("");
    const [newClass, setNewClass] = useState<'MAGE' | 'WARRIOR' | 'ROGUE' | 'CLERIC'>('WARRIOR');
    const [newGuild, setNewGuild] = useState<number | ''>('');

    
    const crearAventurero = async (e: React.SyntheticEvent<HTMLFormElement>) => {
        e.preventDefault();

        if (newGuild === ''){
            alert("El aventurero debe pertenecer a un gremio");
            return;
        }

        try {
            await api.post("adventurers/", {
                name: newName,
                class: newClass,
                guild: newGuild, 
                level: 1,
                status: "ACTIVE"
            });

            setNewName("");
            setNewClass("WARRIOR");
            setNewGuild('');
            onSuccess();
        }
        catch (error){
            console.error(error);
            alert("Error al crear el aventurero");
        }
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg border border-gray-700 shadow-md" >
            <h2 className="text-xl font-bold text-blue-400 mb-4"> Reclutar Aventurero</h2>
            <form onSubmit={crearAventurero} noValidate className="flex flex-col gap-4">

                <div>
                    <label className="block text-sm text-gray-400 mb-2">Nombre</label>
                    <input
                        type="text"
                        value={newName}
                        onChange={(e) => setNewName(e.target.value)}
                        className="bg-gray-700 text-gray-300 placeholder:text-gray-500 border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Nombre del aventurero"
                    />
                </div>

                <div>
                    <label className="block text-sm text-gray-400 mb-2">Clase</label>
                    <select
                        value={newClass}
                        onChange={(e) => setNewClass(e.target.value as 'MAGE' | 'WARRIOR' | 'ROGUE' | 'CLERIC')}
                        className="bg-gray-700 text-gray-300 border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        <option value="MAGE">Mago</option>
                        <option value="WARRIOR">Guerrero</option>
                        <option value="ROGUE">Pícaro</option>
                        <option value="CLERIC">Clérigo</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm text-gray-400 mb-2">Gremio</label>
                    <select
                        value={newGuild}
                        onChange={(e) => setNewGuild(Number(e.target.value))}
                        className="bg-gray-700 text-gray-300 border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        <option value="">Seleccionar gremio</option>
                        {guild.map((g) => (
                            <option key={g.id} value={g.id}>
                                {g.name}
                            </option>
                        ))}
                    </select>
                </div>

                <Button type="submit" variant="success" className="mt-2">Reclutar</Button>

            </form>

        </div>
    );
}