import tkinter as tk
from tkinter import ttk, Menu, messagebox
from punto_de_funcion import mostrar_punto_de_funcion
from caso import AplicacionCasosUsos  # Importar la clase AplicacionCasosUsos

def mostrar_mensaje(metric):
    message = f"Seleccionaste {metric}"
    messagebox.showinfo("Información", message)

def mostrar_aplicacion_casos_usos():
    # Crear una nueva ventana para la aplicación de casos de uso
    new_window = tk.Toplevel(root)
    app = AplicacionCasosUsos(new_window)

def crear_menu(root):
    barra_menu = Menu(root, background='#3e4149', foreground='white', activebackground='#2d2f33', activeforeground='white')
    root.config(menu=barra_menu)

def estilo_personalizado():
    style = ttk.Style()
    style.theme_use('clam')

    # Estilos para botones
    style.configure('TButton', font=('Arial', 12), padding=10, background='#90a4ae')  # Cambia el color de fondo de los botones
    
    # Estilos para etiquetas
    style.configure('TLabel', font=('Arial', 12))

    # Estilos para el marco
    style.configure('TFrame', background='#f0f0f0')

def main():
    global root  # Hacer root global para mantener la referencia
    root = tk.Tk()
    root.title("Software de Métricas de Software")
    root.geometry("1200x700")
    root.configure(bg='#3e4149')  # Establecer el fondo de color del root

    # Aplicar estilos personalizados
    estilo_personalizado()

    # Crear y configurar el menú
    crear_menu(root)

    # Crear un marco principal
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)
    main_frame.configure(style='TFrame', relief='sunken')  # Establecer el fondo de color del main_frame

    # Agregar un título en el centro de la ventana
    titulo = ttk.Label(main_frame, text="Bienvenido al Software de Métricas de Software", font=("Arial", 24), background='#257485', foreground='white')
    titulo.pack(pady=20)

    # Marco para los botones
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=20)
    button_frame.configure(style='TFrame', relief='sunken')  # Establecer el fondo de color del button_frame

    # Botón de Punto de Función
    punto_funcion_button = ttk.Button(button_frame, text="Punto de Función", command=mostrar_punto_de_funcion)
    punto_funcion_button.grid(row=0, column=0, padx=10, pady=10)

    # Botón de Punto de Casos de Uso
    punto_casos_uso_button = ttk.Button(button_frame, text="Punto de Casos de Uso", command=mostrar_aplicacion_casos_usos)
    punto_casos_uso_button.grid(row=0, column=1, padx=10, pady=10)

    # Botón de Punto Objeto
    punto_objeto_button = ttk.Button(button_frame, text="Punto Objeto", command=lambda: mostrar_mensaje("Punto Objeto"))
    punto_objeto_button.grid(row=1, column=0, padx=10, pady=10)

    # Botón de McCall
    mccall_button = ttk.Button(button_frame, text="McCall", command=lambda: mostrar_mensaje("McCall"))
    mccall_button.grid(row=1, column=1, padx=10, pady=10)

    # Botón de Métricas
    metricas_button = ttk.Button(button_frame, text="Métricas", command=lambda: mostrar_mensaje("Métricas"))
    metricas_button.grid(row=2, column=0, padx=10, pady=10)

    # Botón de salida
    exit_button = ttk.Button(button_frame, text="Salir", command=root.quit)
    exit_button.grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
