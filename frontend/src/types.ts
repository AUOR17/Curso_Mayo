export type Gremio = {
    id: number;
    nombre: string;
    fundacion: string;
};

export type Aventurero = {
    id: number;
    nombre: string;
    clase_rpg: string;
    nivel: number;
    estado: string;
    gremio: number;
};

export type Columnas = {
    [key: string]: Aventurero[];
};