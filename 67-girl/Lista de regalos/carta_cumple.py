# Paquetes de recursos
import sys
import tkinter as tk

# Configuración general del programa
VELOCIDAD_MS = 38
PAUSA_PUNTUACION_MS = 220
PAUSA_SALTO_MS = 350
ESPERA_BOTON_MS = 5000

BG = "#1b1033"
FG = "#f4ecff"
ORO = "#ffd166"
ROSA = "#ff8fcf"
CIAN = "#6fe7ff"
ROJO = "#ff2d2d"

# Textito todo cursi con indicaciones de toqueteado
TEXTO = """{t}¡Hola! Parece ser que ya es tu {r}día especial{/r}, jeje.{/t}

A la fecha que escribo esto, es el 23/11/2026, a las 23:30PM, exáctamente. ¿Un poco temprano verdad? Supongo que para ese entonces no tuve nada mejor que hacer. Lo conveniente de igual modo, es que leas esto el {r}05/12/2026{/r}, ya que es para tu {r}cumpleaños{/r}. No sé si seré capaz de poder entregártelo a las 0:00AM en tu país, ya que para mí serían las 05:00AM, ¿pero al menos lo habré intentado, no?

A veces me pregunto si realmente debería invertir tanta dedicación en una persona que no suelo conocer de hace tanto. Quizás, es hasta una pregunta que te pueda llegar a surgir. Nos conocemos desde hace como un mes apenas, y aquí me ves, dedicándote tiempo y alma porque a la pequeña le falta un año menos para morirse. Yo sinceramente tampoco me entiendo, estas cosas siempre me pasan factura; ya lo hemos hablado varias veces. Mi pasado está marchito de "personajes" y de malas decisiones. No fueron las peores, eso es de reconocer, pero tampoco fueron las mejores.

A veces me pregunto:

{p}   - "¿Y si solo me quiere para algo en concreto y después me ignorará?"
   - "¿Quizás solo esté intentando sonsacarme cosas para poder funarme de algún modo?"
   - "¿Realmente soy de relevancia para esta persona?"
   - "¿Tan siquiera le importo?"
   -  . . .{/p}

Lo sé, son preguntas que quizás sean exageradas, o estúpidas, pero así mismo eso creí en otras ocasiones, y bueno, no hace falta explicarte qué ocurrió. Me temo que soy demasiado apasionado por naturaleza, y por consecuente, soy un poco mi propio veneno, JAJAJA.

A veces me gustaría conocerte en profundidad, me causas bastante interés como persona en general, aunque temo que mi curiosidad se vuelva tu agobio. Lo que le falta a una abogada es que ahora tenga a un idiota como yo atrás, ¿Me equivoco? De no ser así, aspiro a que algún día, quizás hasta después de leer esto (si lo lees), puedas abrir tu caparazón más. Te haces la dura, pero por lo que he presenciado, eres una persona {r}hermosa de corazón y alma{/r}.

Hay muchas cosas de las que me gustaría hablar y hasta realizar contigo, pero creo que esta carta no está hecha para esos asuntos. ¡Es tu cumpleaños! Eres toda una anciana dormilona para mí ahora. Una cosita tan estúpida para su edad, que me provoca ternura total... Tan solo espero que disfrutes de este día, y siempre que lo necesites, voy a estar dispuesto a dialogar contigo, quieras informar, o quieras simplemente hacerlo porque quieres hablar conmigo; sea por amistad, por necesidad, por lo que sea. Eso a mí me haría bastante feliz :).

No creo tener que comentarte mucho más, he hecho lo mejor que he podido para ti. Me dejaba bastante mal sabor de boca solo darte un dibujo, por lo que hice lo mejor que pude. Probablemente no me acerque a ser el mejor regalo que tuviste, habrá cientos de cosas que quieras y que tendrás por tus familiares y cercanos, pero al menos quiero dar de mí para estar, aunque no suponga algo significativo.

Con todo esto dicho, {t}{r}¡Feliz cumpleaños!{/r}{/t} {r}Se te quiere.{/r}

Con dedicación;

{s}- att: ༺ 𖤐 𖤓C̶α̷ɓ̽͡a Vσ̶l̽͜d (o Caballero3 -> Tu mafioso de confianza ;) ){/s}"""

ETIQUETAS_VALIDAS = {"r", "t", "p", "s"}

# El absoluto INFIERNO :(. De aquí para abajo serán definiciones que el sistema tiene que usar para poder personalizar y darle color a la página emergente
def parsear(texto):
    resultado = []
    activas = []
    i = 0
    while i < len(texto):
        if texto[i] == "{":
            fin = texto.find("}", i)
            nombre = texto[i + 1:fin]
            if nombre.startswith("/") and nombre[1:] in ETIQUETAS_VALIDAS:
                if nombre[1:] in activas:
                    activas.remove(nombre[1:])
                i = fin + 1
                continue
            if nombre in ETIQUETAS_VALIDAS:
                activas.append(nombre)
                i = fin + 1
                continue
        resultado.append((texto[i], tuple(activas)))
        i += 1
    return resultado


class Carta: # Para la configuración de la ventana, concretamente
    def __init__(self, root):
        self.root = root
        root.title("🎂 ¡Feliz cumpleaños! 🎉")
        root.configure(bg=BG)
        root.geometry("900x720")
        root.minsize(600, 450)
        root.protocol("WM_DELETE_WINDOW", self.cerrar)

        marco = tk.Frame(root, bg=BG)
        marco.pack(fill="both", expand=True, padx=30, pady=(25, 10))

        self.texto = tk.Text(
            marco, wrap="word", bg=BG, fg=FG, bd=0, highlightthickness=0,
            font=("Georgia", 14), spacing1=2, spacing3=4, padx=10, pady=5,
            cursor="arrow", insertwidth=0, state="disabled",
        )
        self.texto.pack(fill="both", expand=True)

        self.texto.tag_configure("r", foreground=ROJO, underline=True,
                                 font=("Georgia", 14, "bold"))
        self.texto.tag_configure("t", foreground=ORO, font=("Georgia", 18, "bold"))
        self.texto.tag_configure("p", foreground=ROSA, font=("Georgia", 14, "italic"))
        self.texto.tag_configure("s", foreground=CIAN, font=("Georgia", 13, "italic"))

        self.texto.tag_raise("r")

        self.pie = tk.Frame(root, bg=BG, height=70)
        self.pie.pack(fill="x", pady=(0, 15))
        self.pie.pack_propagate(False)

        self.caracteres = parsear(TEXTO)
        self.indice = 0
        self.root.after(600, self.escribir)


    def escribir(self):
        if self.indice >= len(self.caracteres):
            self.root.after(ESPERA_BOTON_MS, self.mostrar_boton)
            return

        caracter, etiquetas = self.caracteres[self.indice]
        self.indice += 1

        self.texto.configure(state="normal")
        try:
            self.texto.insert("end", caracter, etiquetas)
        except tk.TclError:
            pass
        self.texto.configure(state="disabled")
        self.texto.see("end")

        espera = VELOCIDAD_MS
        if caracter in ".,!?;:":
            espera += PAUSA_PUNTUACION_MS
        elif caracter == "\n":
            espera += PAUSA_SALTO_MS
        self.root.after(espera, self.escribir)


    def mostrar_boton(self):
        self.boton = tk.Button(
            self.pie, text="", width=20, font=("Georgia", 13, "bold"),
            bg=ROJO, fg="white", activebackground="#ff5c5c",
            activeforeground="white", relief="flat", bd=0, pady=8,
            cursor="hand2", command=self.cerrar,
        )
        self.boton.pack(pady=8)
        self.etiqueta = "Cerrar esta ventana"
        self.pos_etiqueta = 0
        self.escribir_boton()

    def escribir_boton(self):
        if self.pos_etiqueta > len(self.etiqueta):
            return
        self.boton.configure(text=self.etiqueta[:self.pos_etiqueta])
        self.pos_etiqueta += 1
        self.root.after(VELOCIDAD_MS + 30, self.escribir_boton)

    def cerrar(self):
        self.root.destroy()
        sys.exit(0)


if __name__ == "__main__":
    ventana = tk.Tk()
    Carta(ventana)
    ventana.mainloop()

# Eres muy traviesa mirando por aquí ;)
# Espero que te haya gustado todo lo que he hecho, ahora mismo esto lo escribo cerca de las 2:00AM, día 25/11/2026. Estuviste inactiva hoy, lo cual es una pena
# pero aproveché para poder trabajar en ti. En caso de que no pueda recibir de ti respuesta en ese día, espero que esté todo bien por allí.

# ¡Gracias por ser tal y como eres! :]