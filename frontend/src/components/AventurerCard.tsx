import api from "../api";
import type {Adventurer} from "../types";
import Button from "./Button";

interface AdventurerCardProps {
    adventurer: Adventurer;
    guilName: string;
    onActionSuccess: () => void;
}

export default function AdventurerCard({adventurer, guilName, onActionSuccess}: AdventurerCardProps) {
    const matarAventurero = async () => {
        if (!window.confirm(`¿Estás seguro de que quieres eliminar a ${adventurer.name}?`)) return;

        try {
            await api.delete(`adventurers/${adventurer.id}`);
            onActionSuccess();
        } catch (error) {
            console.error(error);
            alert("Error al eliminar al aventurero");
        }
    };

    const subirNivel = async () => {
        try {
            await api.patch(`adventurers/${adventurer.id}/`, {level: adventurer.level + 1});
            onActionSuccess();
        }
        catch (error) {
                console.error(error);
                alert("Error al subir de nivel al aventurero");
        }
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg border border-gray-700 shadow-md flex flex-col hover:border-gray-500 transition-colors">
            <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-bold text-white">{adventurer.name}</h2>
                <span className="bg-blue-500 text-white px-3 py-1 rounded-full text-sm font-semibold">
                    Nivel {adventurer.level}
                </span>
            </div>

            <div className="flex flex-col gap-2 text-sm text-gray-300 mb-6 grow">
                <p><strong className="text-gray-400">Clase:</strong> {adventurer.class_type}</p>
                <p><strong className="text-gray-400">Estado:</strong> {adventurer.status}</p>
                <p><strong className="text-gray-400">Gremio:</strong> <span className="text-blue-400">{guilName}</span></p>
            </div>

            <div className="flex flex-col gap-2">
                <Button onClick={matarAventurero} variant="danger" className="hover:bg-red-950 hover:border-red-950 hover:text-red-200">
                    Eliminar
                </Button>
                <Button onClick={subirNivel} variant="success">
                    Subir Nivel
                </Button>
            </div>
        </div>
    );
}
