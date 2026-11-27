
"""Los mensajes tras "#" son comentarios realizados por el programador (yo). Quizás encuentres algún detalle interesante."""

# Un segundo, ¿Qué haces mirando aquí? ¡No hay nada que ver!

# Importe de recursos para la página.
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import pygame

NOMBRES_VALIDOS: list = {"arya", "sauth", "sauthland", "shut", "arya.exe", "cosita"} # -> Aquí los nombres de la consentida, creo que no me dejo ninguno :/
EDAD_VALIDA = 20 # -> 20 añitos ya, toda una anciana estás hecha.

# Pide datos del usuario para continuar con el programa.
def pedir_datos(raiz):
    while True:
        nombre = simpledialog.askstring(
            "Cumpleaños", "¿Cómo te llamas?", parent=raiz
        )
        if nombre is None:
            return None

        if nombre.strip().lower() not in NOMBRES_VALIDOS:
            messagebox.showerror(
                "Error",
                "Ambos sabemos que ese no es un nombre con el que yo te reconozca",
                parent=raiz,
            )
            continue

        edad = simpledialog.askstring(
            "Cumpleaños", "¿Qué edad vas a cumplir?", parent=raiz
        )
        if edad is None:
            return None

        if edad.strip() != str(EDAD_VALIDA):
            messagebox.showerror("Error", "¿A quién intentas engañar?", parent=raiz)
            continue

        return nombre.strip()

# ¡¡Te estoy diciendo que aquí no hay nada!!!!

# Forma y color del pastel de cumpleaños.
def dibujar_tarta(c, cx, base_y):
    c.create_rectangle(cx - 190, base_y, cx + 190, base_y + 16,
                       fill="#c0c0c0", outline="#808080", width=2)

    c.create_rectangle(cx - 160, base_y - 90, cx + 160, base_y,
                       fill="#f4a6c0", outline="#b5566f", width=3)
    c.create_rectangle(cx - 115, base_y - 170, cx + 115, base_y - 90,
                       fill="#ffd3a5", outline="#b57a3f", width=3)
    c.create_rectangle(cx - 70, base_y - 235, cx + 70, base_y - 170,
                       fill="#f4a6c0", outline="#b5566f", width=3)

    for (izq, der, y) in [(cx - 160, cx + 160, base_y - 90),
                          (cx - 115, cx + 115, base_y - 170),
                          (cx - 70, cx + 70, base_y - 235)]:
        x = izq
        while x < der:
            fin = min(x + 28, der)
            c.create_oval(x, y - 10, fin, y + 14, fill="white", outline="#dddddd")
            x += 28

    colores = ["#e63946", "#2a9d8f", "#f4d35e", "#457b9d"]
    for i, x in enumerate(range(cx - 140, cx + 141, 40)):
        c.create_oval(x - 7, base_y - 45, x + 7, base_y - 31,
                      fill=colores[i % 4], outline="")

    for y in (base_y - 130, base_y - 115):
        c.create_line(cx - 105, y, cx - 55, y + 8, cx, y, cx + 55, y + 8, cx + 105, y,
                      smooth=True, fill="#b57a3f", width=2)

    cima = base_y - 235 # -> Mucha mierda muy tediosa...
    for x in range(cx - 50, cx + 51, 25):
        c.create_rectangle(x - 5, cima - 45, x + 5, cima - 5,
                           fill="#4cc9f0", outline="#1d6f8c", width=2)
        c.create_line(x - 5, cima - 33, x + 5, cima - 25, fill="white", width=2)
        c.create_line(x - 5, cima - 20, x + 5, cima - 12, fill="white", width=2)
        c.create_line(x, cima - 45, x, cima - 52, fill="black", width=2)
        c.create_oval(x - 7, cima - 78, x + 7, cima - 52,
                      fill="#ffb703", outline="#fb8500", width=2)
        c.create_oval(x - 3, cima - 68, x + 3, cima - 56,
                      fill="#ffe66d", outline="")

# Hace sonar la música de fondo, ¡yupi!
def reproducir_audio():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arya_cumple.mp3")
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(-1)
    except (pygame.error, FileNotFoundError):
        pass

# Forma de la ventana final.
def mostrar_ventana(raiz, nombre):
    raiz.title("¡Feliz cumpleaños!")
    raiz.resizable(False, False)

    ancho, alto = 760, 700
    c = tk.Canvas(raiz, width=ancho, height=alto, bg="#fff8e7", highlightthickness=0)
    c.pack()
    cx = ancho // 2

    c.create_text(cx, 45, text=f"FELIZ CUMPLEAÑOS {nombre.upper()}",
                  font=("Arial", 30, "bold"), fill="#d62828")

    dibujar_tarta(c, cx, base_y=470)

    c.create_text(cx, 545, text="TQM", font=("Arial", 52, "bold"), fill="#e63946")

    c.create_text(cx, 625, text="Con mucho cariño y aprecio;",
                  font=("Georgia", 12, "italic"), fill="#555555")
    c.create_text(cx, 650, text="- Tu querido 'pequeño' mafioso calabacín de Whisky",
                  font=("Georgia", 12, "italic"), fill="#555555")
    
    raiz.deiconify()
    reproducir_audio()


# Ventana de datos.
def main():
    raiz = tk.Tk()
    raiz.withdraw()

    nombre = pedir_datos(raiz)
    if nombre is None:
        raiz.destroy()
        return

    mostrar_ventana(raiz, nombre)
    raiz.mainloop()


if __name__ == "__main__":
    main()


# Bueno, pues parece ser que la curioisdad te puede a ti... Eres de lo que no hay. 
# Por si no entiendes mucho, este es el código que hace el programa funcional; 
# ¡desde las acciones hasta el propio dibujito de la tarta! Soy bastante amateur, jeje. 
# Espero que te llegue a gustar, Arya".exe". Hice lo mejor de mí para ti, pero prometo mejorar a futuro :]