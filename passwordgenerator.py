import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import secrets
import string
import threading

class MatrixAnimation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg='black', width=400, height=400)  # Duplicar la altura
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.characters = string.ascii_letters + string.digits + string.punctuation + ' '
        self.letter_objs = []

    def start_animation(self):
        self.animate_letters()

    def animate_letters(self):
        letter = secrets.choice(self.characters)
        x_pos = secrets.randbelow(400)  # Posición horizontal aleatoria
        y_pos = 0  # Comienza desde la parte superior
        letter_obj = self.canvas.create_text(x_pos, y_pos, text=letter, fill='green', font=('Courier', 18))

        self.letter_objs.append(letter_obj)
        self.move_letters()
        self.root.after(50, self.animate_letters)  # Llamada recursiva después de 50 milisegundos

    def move_letters(self):
        for obj in self.letter_objs:
            self.canvas.move(obj, 0, 10)  # Mueve cada letra hacia abajo

def stop_animation(matrix_animation):
    matrix_animation.root.destroy()

def generar_contrasena(matrix_animation):
    longitud = 60
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    entrada_contrasena.delete(0, tk.END)
    entrada_contrasena.insert(0, contrasena)

def copiar_contrasena():
    contrasena = entrada_contrasena.get()
    if contrasena:
        root.clipboard_clear()
        root.clipboard_append(contrasena)
        root.update()
        messagebox.showinfo('Copiado', 'Contraseña copiada al portapapeles')
    else:
        messagebox.showwarning('Error', 'Genera una contraseña primero')

# Crear la interfaz gráfica
root = tk.Tk()
root.title('Generador de Contraseñas - Estilo Matrix')

# Cambiar el fondo para dar un aspecto estilo Matrix
root.configure(bg='black')
root.geometry('400x400')  # Duplicar la altura

# Usar ttk.Style para configurar el estilo
estilo = ttk.Style()

# Configurar el estilo 3D para la etiqueta
estilo.configure('EstiloMatrix.TLabel', foreground='green', background='black', font=('Courier', 18), relief=tk.RAISED, padding=(5, 5))

# Configurar el tema clam para los botones
estilo.theme_use('clam')
estilo.configure('EstiloMatrix.TButton', foreground='green', background='black', font=('Courier', 12), relief=tk.RAISED)

# Entrada para mostrar la contraseña generada
entrada_contrasena = ttk.Entry(root, width=60, font=('Courier', 18), style='EstiloMatrix.TLabel', justify='center')
entrada_contrasena.pack(pady=10)

# Botones para generar y copiar contraseñas
boton_generar = ttk.Button(root, text='Generar Nueva Contraseña', command=lambda: generar_contrasena(matrix_animation), style='EstiloMatrix.TButton')
boton_generar.pack(pady=10)

boton_copiar = ttk.Button(root, text='Copiar Contraseña', command=copiar_contrasena, style='EstiloMatrix.TButton')
boton_copiar.pack(pady=10)

# Configurar y empezar la animación estilo Matrix en un hilo separado
matrix_animation = MatrixAnimation(root)
matrix_thread = threading.Thread(target=matrix_animation.start_animation)
matrix_thread.start()

# Detener la animación cuando se cierre la aplicación
root.protocol("WM_DELETE_WINDOW", lambda: stop_animation(matrix_animation))

# Ejecutar la aplicación
root.mainloop()
