"""
Proyectil. Bala que disparan las torres.
==========================================
Fase: 6 - Combate.

Viaja hacia un enemigo objetivo y le aplica daño al impactar.
"""

from model.mapa import TAM_CELDA
CENTRO_CELDA = TAM_CELDA // 2  

class Proyectil:
    """
    Un proyectil que viaja hacia un enemigo objetivo.
    
    Atributos:
        col (int): Columna de origen.
        fila (int): Fila de origen.
        x (float): Posición x actual en píxeles.
        y (float): Posición y actual en píxeles.
        enemigo: Referencia al enemigo objetivo.
        dano (int): Daño que aplica al impactar.
        velocidad (float): Velocidad de avance.
        activo (bool): True si sigue en vuelo.
    """

    def __init__(self, col: int, fila: int, enemigo, dano: int = 15, velocidad: float = 8):
        """
        Inicializa un proyectil apuntando a un enemigo.
        
        Args:
            col: Columna de la torre que dispara.
            fila: Fila de la torre que dispara.
            enemigo: Enemigo objetivo.
            dano: Daño a aplicar al impactar (default 15).
            velocidad: Velocidad de avance (default 8).
        """
        self.col = col
        self.fila = fila
        self.x = col * TAM_CELDA + CENTRO_CELDA
        self.y = fila * TAM_CELDA + CENTRO_CELDA
        self.enemigo = enemigo
        self.dano = dano
        self.velocidad = velocidad
        self.activo = True

    def mover(self, dt: float) -> None:
        """
        Avanza el proyectil hacia su objetivo.
        Si el objetivo murió, se desactiva.
        Si llega al objetivo, aplica daño y se desactiva.
        
        Args:
            dt: Delta time desde el último frame.
        """
        if not self.enemigo.esta_vivo():
            self.activo = False
            return

        # Pitagoras - Distancia
        dx = self.enemigo.x + CENTRO_CELDA - self.x
        dy = self.enemigo.y + CENTRO_CELDA - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia < 5:
            self.enemigo.recibir_dano(self.dano)
            self.activo = False
            return

        self.x += (dx / distancia) * self.velocidad * dt * 60
        self.y += (dy / distancia) * self.velocidad * dt * 60

    def fuera_de_pantalla(self) -> bool:
        """
        Verifica si el proyectil salió de los límites de la pantalla.
        
        Returns:
            bool: True si está fuera de la pantalla.
        """
        return self.x < 0 or self.x > 800 or self.y < 0 or self.y > 670