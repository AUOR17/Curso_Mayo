import { useEffect, useState, useCallback } from 'react';
import { apiDjango } from '../api/client';
import { useAuth } from '../context/AuthContext';
import { Shield, Coins, Swords, Edit2, Send } from 'lucide-react';
import { useModal } from '../context/ModalContext';
import ModalForjarMision from '../components/modales/ModalForjarMision';
import ModalEditarMision from '../components/modales/ModalEditarMision';
import ModalAsignarMision from '../components/modales/ModalAsignarMision';
import { Quest } from '../types'; 

export default function Tablero() {
  const [quests, setQuests] = useState<Quest[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { user } = useAuth();
  const { openModal, closeModal } = useModal();
  
  const fetchQuests = useCallback(async () => {
    try {
      const response = await apiDjango.get('/quests/tablero/');
      setQuests(Array.isArray(response.data) ? response.data : []); 
    } catch (err) {
      console.error("Fallo al traer las misiones", err);
      setError("Los exploradores del Gremio no pudieron contactar a la bóveda central.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchQuests();
  }, [fetchQuests]);

  const aceptarMision = async (questId: number) => {
    if (!user) return;
    try {
      await apiDjango.patch(`/quests/tablero/${questId}/`, {
        status: 'EXPLORACION',
        assigned_to: user.id
      });
      fetchQuests();
    } catch (err) {
      console.error("Error al aceptar la misión:", err);
      alert("Alguien más ya tomó este encargo.");
    }
  };

  if (loading) return <div className="text-xl text-rpg-blood animate-pulse font-serif p-8 flex justify-center h-full items-center">Invocando pergaminos...</div>;
  if (error) return <div className="bg-rpg-blood/20 border border-rpg-blood text-rpg-parchment p-4 rounded-lg m-8">{error}</div>;

  const handleDragStart = (e: React.DragEvent, questId: number) => {
    e.dataTransfer.setData('questId', questId.toString());
  };

  const reclamarRecompensa = async (questId: number) => {
    try {
      await apiDjango.post(`/quests/tablero/${questId}/reclamar_recompensa/`);
      fetchQuests(); 
    } catch (err) {
      console.error("Error al reclamar la recompensa:", err);
      alert("Los duendes del banco rechazaron la transacción.");
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
  };

  const handleDrop = async (e: React.DragEvent, newStatus: string) => {
    e.preventDefault();
    const questId = e.dataTransfer.getData('questId');
    if (!questId) return;

    try {
      await apiDjango.patch(`/quests/tablero/${questId}/`, {
        status: newStatus
      });
      fetchQuests(); 
    } catch (err) {
      console.error("Error al mover la misión", err);
    }
  };

  const handleAbrirForja = () => {
    openModal(
      <ModalForjarMision 
        isOpen={true} 
        onClose={closeModal} 
        onSuccess={() => {
          fetchQuests();
          closeModal();
        }} 
      />
    );
  };

  return (
    <div className="flex flex-col h-full overflow-hidden relative"> 
      
      <div className="flex justify-between items-center mb-6 border-b border-rpg-blood/30 pb-4 shrink-0">
        <div>
          <h2 className="text-3xl font-bold text-rpg-gold font-serif mb-1">
            Misiones Activas
          </h2>
          <p className="text-rpg-silver">Tablero de contratos y encargos del Gremio.</p>
        </div>

        {(user?.role === 'MAESTRO' || user?.role === 'GRAN_MAESTRO') && (
          <button 
            onClick={() => openModal(
              <ModalForjarMision 
                isOpen={true} 
                onClose={closeModal} 
                onSuccess={() => { fetchQuests(); closeModal(); }} 
              />
            )}
            className="bg-rpg-blood text-white px-6 py-2 rounded-md hover:bg-red-700 transition-colors shadow-lg font-serif border border-rpg-gold/30"
          >
            + Forjar Misión
          </button>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 h-[calc(100vh-200px)] min-h-0"> 
        
        <div 
          onDragOver={handleDragOver} 
          onDrop={(e) => handleDrop(e, 'TABERNA')}
          className="bg-[#141614]/50 border border-rpg-blood/20 p-4 rounded-lg flex flex-col min-h-0 overflow-hidden"
        >
          <h4 className="text-rpg-blood font-serif text-xl border-b border-rpg-blood/30 mb-4 pb-2 flex items-center gap-2 shrink-0">
            <span>📜</span> Taberna
          </h4>
          <div className="flex-1 overflow-y-auto pr-2 space-y-4 custom-scrollbar">
            {quests?.filter(q => q.status === 'TABERNA').map(quest => (
              <div 
                key={quest.id} 
                draggable 
                onDragStart={(e) => handleDragStart(e, quest.id)}
                className="bg-[#1a1c1a] p-4 border-l-4 border-rpg-blood rounded shadow-[0_0_10px_rgba(130,23,21,0.2)] hover:border-rpg-gold transition-all group flex flex-col cursor-grab active:cursor-grabbing"
              >
                <div className="flex justify-between items-start mb-1 gap-2">
                  <h5 className="text-rpg-bone font-bold leading-tight flex-1">{quest.title}</h5>
                  
                  {(user?.role === 'GRAN_MAESTRO' || user?.role === 'MAESTRO') && (
                    <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                      <button 
                        onClick={() => openModal(
                          <ModalEditarMision 
                            isOpen={true} 
                            onClose={closeModal} 
                            onSuccess={() => { fetchQuests(); closeModal(); }} 
                            quest={quest} 
                          />
                        )}
                        className="text-rpg-silver hover:text-rpg-gold p-1" title="Editar Misión"
                      >
                        <Edit2 className="w-4 h-4" />
                      </button>
                      {user?.role === 'GRAN_MAESTRO' && (
                        <button 
                          onClick={() => openModal(
                            <ModalAsignarMision 
                              isOpen={true} 
                              onClose={closeModal} 
                              onSuccess={() => { fetchQuests(); closeModal(); }} 
                              quest={quest} 
                            />
                          )}
                          className="text-rpg-silver hover:text-purple-400 p-1" title="Delegar a Gremio"
                        >
                          <Send className="w-4 h-4" />
                        </button>
                      )}
                    </div>
                  )}
                </div>

                <div className="mb-2">
                  {quest.gremio_nombre ? (
                    <span className="bg-purple-900/40 text-purple-300 text-[10px] px-2 py-0.5 rounded border border-purple-500/30">
                      ⛺ {quest.gremio_nombre}
                    </span>
                  ) : (
                    <span className="bg-blue-900/40 text-blue-300 text-[10px] px-2 py-0.5 rounded border border-blue-500/30">
                      🌍 Global
                    </span>
                  )}
                </div>

                <p className="text-xs text-rpg-silver mb-3 line-clamp-2">{quest.description}</p>
                
                <div className="flex justify-between items-center mt-auto border-t border-rpg-blood/20 pt-2">
                  <span className="text-xs font-bold text-rpg-gold flex items-center gap-1"><Coins className="w-3 h-3"/> {quest.potential_reward}</span>
                  <button 
                    onClick={() => aceptarMision(quest.id)}
                    className="bg-rpg-blood/80 hover:bg-rpg-blood text-xs text-white px-3 py-1 rounded transition-colors"
                  >
                    Aceptar
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div 
          onDragOver={handleDragOver} 
          onDrop={(e) => handleDrop(e, 'EXPLORACION')}
          className="bg-rpg-dark/50 border border-rpg-blood/20 p-4 rounded-lg flex flex-col min-h-0 overflow-hidden"
        >
          <h4 className="text-rpg-silver font-serif text-xl border-b border-rpg-silver/30 mb-4 pb-2 flex items-center gap-2 shrink-0">
            ⚔️ En Combate
          </h4>
          <div className="flex-1 overflow-y-auto pr-2 space-y-4 custom-scrollbar">
            {quests?.filter(q => q.status === 'EXPLORACION' || q.status === 'COMBATE').map(quest => (
              <div 
                key={quest.id} 
                draggable 
                onDragStart={(e) => handleDragStart(e, quest.id)}
                className="bg-[#1a1c1a] p-4 border-l-4 border-rpg-silver rounded shadow-lg group flex flex-col relative overflow-hidden cursor-grab active:cursor-grabbing"
              >
                <div className="absolute top-0 right-0 bg-rpg-dark px-2 py-1 text-[10px] text-rpg-silver border-b border-l border-rpg-silver/20 rounded-bl">
                  {quest.status}
                </div>
                <h5 className="text-rpg-silver font-bold group-hover:text-rpg-bone pr-12">{quest.title}</h5>
                
                <div className="my-1">
                  {quest.gremio_nombre ? (
                    <span className="text-purple-400 text-[10px]">⛺ {quest.gremio_nombre}</span>
                  ) : (
                    <span className="text-blue-400 text-[10px]">🌍 Global</span>
                  )}
                </div>

                <div className="mt-2 flex items-center gap-2 text-xs text-rpg-parchment">
                  <Shield className="w-3 h-3"/> {quest.assigned_to_details?.username}
                </div>
              </div>
            ))}
          </div>
        </div>

        <div 
          onDragOver={handleDragOver} 
          onDrop={(e) => handleDrop(e, 'TESORO')}
          className="bg-rpg-dark/50 border border-rpg-gold/20 p-4 rounded-lg flex flex-col min-h-0 overflow-hidden"
        >
          <h4 className="text-rpg-gold font-serif text-xl border-b border-rpg-gold/30 mb-4 pb-2 flex items-center gap-2 shrink-0">
            🏆 Tesoro (Victoria)
          </h4>
          <div className="flex-1 overflow-y-auto pr-2 space-y-4 custom-scrollbar">
            {quests?.filter(q => q.status === 'TESORO').map(quest => (
              <div 
                key={quest.id} 
                draggable 
                onDragStart={(e) => handleDragStart(e, quest.id)}
                className="bg-rpg-gold/10 p-4 border-l-4 border-rpg-gold rounded shadow-[0_0_10px_rgba(255,215,0,0.1)] group flex flex-col cursor-grab active:cursor-grabbing"
              >
                <h5 className="text-rpg-gold font-bold">{quest.title}</h5>
                <div className="flex justify-between items-center mt-3 border-t border-rpg-gold/20 pt-2">
                  <span className="text-xs text-rpg-bone flex items-center gap-1"><Swords className="w-3 h-3"/> {quest.assigned_to_details?.username}</span>
                  <span className="text-sm font-bold text-rpg-gold">+{quest.potential_reward}</span>
                </div>
                {(user?.role === 'GRAN_MAESTRO' || user?.role === 'MAESTRO') && (
                  <button 
                    onClick={() => reclamarRecompensa(quest.id)}
                    className="mt-4 w-full bg-rpg-gold/20 hover:bg-rpg-gold/40 text-rpg-gold border border-rpg-gold/50 text-xs font-bold py-2 rounded transition-colors flex justify-center items-center"
                  >
                    💰 Liquidar Recompensa
                  </button>
                )}
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  );
}