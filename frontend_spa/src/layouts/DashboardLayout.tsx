import { Link, useLocation, Outlet } from 'react-router-dom';
import { Map, ScrollText, Users, ShieldAlert, Tent } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import BotonSalida from '../components/botones/BotonSalida';

export default function DashboardLayout() {
  const location = useLocation();
  const { user } = useAuth();

  const baseMenuItems = [
    { name: 'Tablero de Misiones', path: '/tablero', icon: Map },
    { name: 'Códice (Leads)', path: '/leads', icon: ScrollText },
  ];

  let menuItems = [...baseMenuItems];
  if (user?.role !== 'GRAN_MAESTRO') {
    menuItems.push({ name: 'Mi Gremio', path: '/mi-gremio', icon: ShieldAlert });
  }

  if (user?.role === 'MAESTRO' || user?.role === 'GRAN_MAESTRO') {
    menuItems.push({ name: 'Directorio Global', path: '/gremio', icon: Users });
  }

  if (user?.role === 'GRAN_MAESTRO') {
    menuItems.push({ name: 'Sedes y Alianzas', path: '/sedes', icon: Tent });
  }
  
  const iniciales = user?.username ? user.username.substring(0, 2).toUpperCase() : 'TR';

  return (
    <div className="flex h-screen bg-rpg-dark text-rpg-parchment font-sans">
      <aside className="w-64 bg-[#141614] border-r border-rpg-blood/30 flex flex-col">
        <div className="p-6">
          <h1 className="text-2xl font-bold text-rpg-gold font-serif flex items-center gap-2">
            <ShieldAlert className="w-8 h-8 text-rpg-blood" />
            Gremio RPG
          </h1>
        </div>

        <nav className="flex-1 px-4 space-y-2 mt-4">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            
            return (
              <Link
                key={item.name}
                to={item.path}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive 
                    ? 'bg-rpg-blood/20 text-rpg-gold border border-rpg-blood/50 shadow-[0_0_10px_rgba(130,23,21,0.2)]' 
                    : 'hover:bg-rpg-dark/50 text-rpg-silver hover:text-rpg-bone'
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="font-medium">{item.name}</span>
              </Link>
            );
          })}
        </nav>

        <div className="p-4 border-t border-rpg-blood/30">
          <div className="flex items-center gap-3 mb-3">
            <div className="w-10 h-10 rounded-full bg-rpg-dark border-2 border-rpg-gold flex items-center justify-center font-bold text-rpg-gold">
              {iniciales}
            </div>
            <div className="overflow-hidden">
              <p className="truncate font-bold text-rpg-bone">{user?.username || 'Fantasma'}</p>
              <p className="text-xs text-rpg-silver truncate">Nivel {user?.level || '?'} - {user?.role || 'Desconocido'}</p>
            </div>
          </div>
          
          <div className="flex justify-center border-t border-rpg-blood/10 pt-3">
            <BotonSalida />
          </div>
        </div>
      </aside>

      <main className="flex-1 overflow-x-hidden overflow-y-auto bg-rpg-dark p-8">
        <Outlet />
      </main>
    </div>
  );
}