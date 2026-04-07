import json
import os


class ConjuntoPersistente:
    """
    Implementación de un Conjunto matemático persistente.

    Cumple con el axioma de extensionalidad: no permite
    elementos duplicados. Su estado se guarda automáticamente
    en un archivo JSON y puede recuperarse entre ejecuciones.
    """

    def __init__(self, nombre_archivo, elementos_iniciales=None):
        """
        Inicializa el conjunto persistente.

        Si el archivo ya existe, carga los datos guardados.
        Si no existe, crea un conjunto nuevo y lo guarda.

        Parametros:
            nombre_archivo (str): Nombre del archivo JSON
                sin extensión.
            elementos_iniciales (iterable, optional): Elementos
                con los que se construye el conjunto si el archivo
                no existe aún. Los duplicados son ignorados.

        Raises:
            TypeError: Si nombre_archivo no es una cadena válida.
        """
        if not isinstance(nombre_archivo, str) or not nombre_archivo.strip():
            raise TypeError(
                "El nombre de archivo debe ser una cadena no vacía."
            )

        self.nombre_archivo = f"{nombre_archivo}.json"
        self.elementos = []

        if os.path.exists(self.nombre_archivo):
            self._cargar()
            print(f"[INFO] Conjunto cargado desde '{self.nombre_archivo}'.")
        else:
            if elementos_iniciales is not None:
                for elemento in elementos_iniciales:
                    self.agregar(elemento)
            self._guardar()
            print(f"[INFO] Conjunto nuevo guardado en '{self.nombre_archivo}'.")

    def agregar(self, elemento):
        """
        Añade un elemento y guarda automáticamente en disco.

        Parametros:
            elemento (int): El elemento a agregar.

        Raises:
            TypeError: Si el elemento no es un entero.
        """
        if not isinstance(elemento, int):
            raise TypeError(
                f"Solo se permiten enteros. "
                f"Se recibió '{type(elemento).__name__}': {elemento!r}."
            )
        if elemento not in self.elementos:
            self.elementos.append(elemento)
            self._guardar()

    def eliminar(self, elemento):
        """
        Elimina un elemento y guarda automáticamente en disco.

        Parametros:
            elemento (int): El elemento a eliminar.

        Raises:
            KeyError: Si el elemento no existe en el conjunto.
        """
        if elemento not in self.elementos:
            raise KeyError(
                f"El elemento {elemento!r} no existe en el conjunto."
            )
        self.elementos.remove(elemento)
        self._guardar()

    def _guardar(self):
        """
        Guarda el estado actual en el archivo JSON.

        Retorna:
            None
        """
        with open(self.nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump({"elementos": self.elementos}, archivo, indent=4)

    def _cargar(self):
        """
        Carga el estado desde el archivo JSON.

        Retorna:
            None
        """
        with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            self.elementos = datos.get("elementos", [])

    def eliminar_archivo(self):
        """
        Borra el archivo JSON del disco.

        Retorna:
            None
        """
        if os.path.exists(self.nombre_archivo):
            os.remove(self.nombre_archivo)
            print(f"[INFO] Archivo '{self.nombre_archivo}' eliminado.")

    def esta_vacio(self):
        """
        Verifica si el conjunto no tiene elementos.

        Retorna:
            bool: True si está vacío, False si no.
        """
        return len(self.elementos) == 0

    def __len__(self):
        """
        Retorna la cardinalidad del conjunto.

        Retorna:
            int: Número de elementos en el conjunto.
        """
        return len(self.elementos)

    def __contains__(self, elemento):
        """
        Permite usar el operador 'in' directamente.

        Parametros:
            elemento (int): El elemento a buscar.

        Retorna:
            bool: True si el elemento pertenece al conjunto.
        """
        return elemento in self.elementos

    def __eq__(self, otro):
        """
        Permite usar el operador '==' directamente.

        Parametros:
            otro (ConjuntoPersistente): El conjunto a comparar.

        Retorna:
            bool: True si ambos conjuntos tienen los mismos elementos.
        """
        if not isinstance(otro, ConjuntoPersistente):
            return False
        return sorted(self.elementos) == sorted(otro.elementos)

    def __str__(self):
        """
        Representación en cadena con notación matemática.

        Retorna:
            str: El conjunto con formato {a, b, c}
                 o '∅' si está vacío.
        """
        if self.esta_vacio():
            return "∅"
        elementos_str = ", ".join(str(e) for e in self.elementos)
        return f"{{{elementos_str}}}"