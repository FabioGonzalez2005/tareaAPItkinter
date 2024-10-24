from dataclasses import dataclass

@dataclass
class Empresa:
    nombre: str
    titular: str
    cif: str
    direccion: str
    email: str