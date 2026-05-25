import { useEffect, useState, useCallback } from 'react';
import { apiDjango } from '../api/client';
import { Users, Shield, Sword, Wand2, Crosshair, Coins, UserPlus, Crown, Tent } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useModal } from '../context/ModalContext';
import ModalReclutarCazador from '../components/modales/ModalReclutarCazador';
import ModalNombrarMaestro from '../components/modales/ModalNombrarMaestro';
import ModalAsignarGremio from '../components/modales/ModalAsignarGremio';
import ModalLiquidar from '../components/modales/ModalLiquidar';
import { Cazador } from '../types'; 

export default function Gremio() {
  const [cazadores, setCazadores] = useState<Cazador[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { user } = useAuth();
  const { openModal, closeModal } = useModal();
  const [activeTab, setActiveTab] = useState<'CANDIDATOS' | 'MAESTROS'>('CANDIDATOS');
  

  const fetchGremio = useCallback(async () => {
    try {
      const response = await apiDjango.get('/gremio/');
      setCazadores(response.data);
    } catch (err) {
      console.error("Fallo al contactar al maestro:", err);
      setError("No se pudo cargar el registro de cazadores.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchGremio();
  }, [fetchGremio]);

  const getRoleIcon = (role: string) => {
    switch (role) {
      case 'GRAN_MAESTRO': return <Crown className="w-4 h-4 text-purple-400" />;
      case 'MAESTRO': return <Shield className="w-4 h-4 text-rpg-gold" />;
      case 'GUERRERO': return <Sword className="w-4 h-4 text-rpg-silver" />;
      case 'MAGO': return <Wand2 className="w-4 h-4 text-blue-400" />;
      case 'PICARO': return <Crosshair className="w-4 h-4 text-green-400" />;
      default: return <Users className="w-4 h-4 text-gray-400" />;
    }
  };

  const cazadoresFiltrados = cazadores.filter(cazador => {
    if (activeTab === 'CANDIDATOS') {
      return cazador.role !== 'MAESTRO' && cazador.role !== 'GRAN_MAESTRO';
    } else {
      return cazador.role === 'MAESTRO' || cazador.role === 'GRAN_MAESTRO';
    }
  });

  if (activeTab === 'MAESTROS') {
    cazadoresFiltrados.sort((a, b) => {
      if (a.role === 'GRAN_MAESTRO' && b.role !== 'GRAN_MAESTRO') return -1;
      if (a.role !== 'GRAN_MAESTRO' && b.role === 'GRAN_MAESTRO') return 1;
      return 0;
    });
  }

  if (loading) return <div className="text-xl text-rpg-blood animate-pulse font-serif p-8">Desplegando el pergamino...</div>;
  if (error) return <div className="bg-rpg-blood/20 border border-rpg-blood text-rpg-parchment p-4 rounded-lg m-8">{error}</div>;

 return (
    <div className="flex flex-col h-full relative">
      <div className="flex justify-between items-start mb-6 pb-4">
        <div>
          <h2 className="text-3xl font-bold text-rpg-gold font-serif flex items-center gap-3 mb-2">
            <Users className="w-8 h-8 text-rpg-blood" />
            Salón del Gremio
          </h2>
          <p className="text-rpg-silver">Registro oficial de cazadores, rangos y botín acumulado.</p>
        </div>
        
        <div className="flex items-center gap-4">
          {user?.role === 'GRAN_MAESTRO' && (
            <button 
              onClick={() => openModal(
                <ModalNombrarMaestro 
                  isOpen={true} 
                  onClose={closeModal} 
                  onSuccess={() => { fetchGremio(); closeModal(); }} 
                />
              )}
              className="bg-rpg-blood text-white px-4 py-2 rounded-md hover:bg-red-700 transition-colors shadow-lg font-serif border border-rpg-gold/30 flex items-center gap-2 text-sm"
            >
              <Crown className="w-4 h-4" />
              Nombrar Maestro
            </button>
          )}

          {user?.role === 'MAESTRO' && (
            <button 
              onClick={() => openModal(
                <ModalReclutarCazador 
                  isOpen={true} 
                  onClose={closeModal} 
                  onSuccess={() => { fetchGremio(); closeModal(); }} 
                />
              )}
              className="bg-rpg-blood text-white px-4 py-2 rounded-md hover:bg-red-700 transition-colors shadow-lg font-serif border border-rpg-gold/30 flex items-center gap-2 text-sm"
            >
              <UserPlus className="w-4 h-4" />
              Reclutar Cazador
            </button>
          )}

          <div className="bg-[#141614] border border-rpg-blood/30 px-4 py-2 rounded-lg text-center ml-2">
            <p className="text-xs text-rpg-parchment">Miembros</p>
            <p className="text-xl font-bold text-rpg-gold">{cazadoresFiltrados.length}</p>
          </div>
        </div>
      </div>

      <div className="flex gap-4 mb-4 border-b border-rpg-blood/20 pb-2">
        <button
          onClick={() => setActiveTab('CANDIDATOS')}
          className={`px-4 py-2 font-serif transition-colors rounded-t-lg ${
            activeTab === 'CANDIDATOS'
              ? 'bg-rpg-blood/20 text-rpg-gold border-b-2 border-rpg-gold'
              : 'text-rpg-silver hover:text-rpg-bone hover:bg-rpg-dark/50'
          }`}
        >
          Candidatos (Mortales)
        </button>
        <button
          onClick={() => setActiveTab('MAESTROS')}
          className={`px-4 py-2 font-serif transition-colors rounded-t-lg ${
            activeTab === 'MAESTROS'
              ? 'bg-rpg-blood/20 text-rpg-gold border-b-2 border-rpg-gold'
              : 'text-rpg-silver hover:text-rpg-bone hover:bg-rpg-dark/50'
          }`}
        >
          Maestros y Deidades
        </button>
      </div>
      
      <div className="bg-[#141614] border border-rpg-blood/30 rounded-lg overflow-hidden shadow-[0_0_15px_rgba(130,23,21,0.1)]">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-rpg-dark border-b border-rpg-blood/50">
              <th className="p-4 text-rpg-gold font-serif">Héroe</th>
              <th className="p-4 text-rpg-gold font-serif">Clase</th>
              <th className="p-4 text-rpg-gold font-serif text-center">Nivel</th>
              {activeTab === 'MAESTROS' && (
                <th className="p-4 text-rpg-gold font-serif text-center">Sede / Gremio</th>
              )}
              <th className="p-4 text-rpg-gold font-serif text-right">Oro Acumulado</th>
            </tr>
          </thead>
          <tbody>
            {cazadoresFiltrados.map((cazador) => (
              <tr key={cazador.id} className="border-b border-rpg-blood/10 hover:bg-rpg-blood/5 transition-colors">
                <td className="p-4 flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-rpg-dark border border-rpg-blood flex items-center justify-center font-bold text-rpg-bone text-xs">
                    {cazador.username.substring(0, 2).toUpperCase()}
                  </div>
                  <span className={`font-bold ${cazador.role === 'GRAN_MAESTRO' ? 'text-purple-400' : cazador.role === 'MAESTRO' ? 'text-rpg-gold' : 'text-rpg-bone'}`}>
                    {cazador.username}
                  </span>
                </td>
                <td className="p-4">
                  <div className="flex items-center gap-2 text-sm text-rpg-silver">
                    {getRoleIcon(cazador.role)}
                    {cazador.role}
                  </div>
                </td>
                <td className="p-4 text-center">
                  <span className="bg-rpg-dark border border-rpg-silver/30 px-2 py-1 rounded text-xs text-rpg-bone">Lvl {cazador.level}</span>
                </td>
                
                {activeTab === 'MAESTROS' && (
                  <td className="p-4 text-center">
                    {cazador.role === 'GRAN_MAESTRO' ? (
                      <span className="text-purple-400/50 text-xs italic">Omnipresente</span>
                    ) : cazador.gremio_nombre ? (
                      <span className="flex items-center justify-center gap-1 text-purple-300 text-sm">
                        <Tent className="w-4 h-4" /> {cazador.gremio_nombre}
                      </span>
                    ) : (
                      <button 
                        onClick={() => openModal(
                          <ModalAsignarGremio 
                            isOpen={true} 
                            onClose={closeModal} 
                            onSuccess={() => { fetchGremio(); closeModal(); }}
                            maestroId={cazador.id}
                            maestroNombre={cazador.username}
                          />
                        )}
                        className="bg-purple-900/40 hover:bg-purple-800 text-purple-200 px-3 py-1 rounded border border-purple-500/30 text-xs transition-colors"
                      >
                        Asignar Gremio
                      </button>
                    )}
                  </td>
                )}

                <td className="p-4 text-right">
                  <div className="flex items-center justify-end gap-3 text-rpg-gold font-bold">
                    <span className="flex items-center gap-1">{cazador.gold} <Coins className="w-4 h-4" /></span>
                    {user?.role === 'GRAN_MAESTRO' && (
                      <button 
                        onClick={() => openModal(
                          <ModalLiquidar 
                            isOpen={true} 
                            onClose={closeModal} 
                            onSuccess={() => { fetchGremio(); closeModal(); }}
                            cazador={cazador}
                          />
                        )}
                        className="bg-green-900/40 hover:bg-green-700 text-green-300 px-2 py-1 rounded text-xs border border-green-500/30 transition-colors"
                      >
                        Liquidar
                      </button>
                    )}
                  </div>
                </td>
              </tr>
            ))}
            {cazadoresFiltrados.length === 0 && (
              <tr>
                <td colSpan={activeTab === 'MAESTROS' ? 5 : 4} className="p-8 text-center text-rpg-silver/50 font-serif italic border-none">
                  El salón está vacío...
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}