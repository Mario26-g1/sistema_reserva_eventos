import tkinter as tk
from tkinter import messagebox


# Colecciones de datos

servicios = {
    "Catering": 1200,
    "Decoración": 800,
    "Música": 500,
    "Fotografía": 900
}
reservas = []  



# Funciones de negocio

def iniciar_sesion(usuario, contraseña):
    if usuario == "admin" and contraseña == "123":
        return True
    elif usuario == "cliente" and contraseña == "456":
        return True
    else:
        return False


def mostrar_catalogo():
    texto = "Catálogo de Servicios:\n\n"
    for nombre, precio in servicios.items():
        texto += f" {nombre}: ${precio}\n"
    return texto


def reservar_servicio(servicio, fecha):
    try:
        if servicio not in servicios:
            raise ValueError("Servicio no disponible")
        reservas.append({"servicio": servicio, "fecha": fecha})
        return f"Reserva confirmada: {servicio} para el {fecha}"
    except ValueError as e:
        return f"! Error: {e}"


def mostrar_reservas():
    if not reservas:
        return "No tienes reservas registradas."
    texto = "📌 Mis Reservas:\n\n"
    for idx, r in enumerate(reservas, start=1):
        texto += f"{idx}. {r['servicio']} - {r['fecha']}\n"
    return texto



# Interfaz gráfica (GUI)

def interfaz():
    ventana = tk.Tk()
    ventana.title("Sistema de Reservas de Eventos")
    ventana.geometry("450x400")

    # LOGIN 
    def login():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()
        if iniciar_sesion(usuario, contraseña):
            marco_login.pack_forget()
            marco_menu.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    marco_login = tk.Frame(ventana)
    marco_login.pack(fill="both", expand=True)

    tk.Label(marco_login, text="Iniciar Sesión", font=("Arial", 14)).pack(pady=10)
    tk.Label(marco_login, text="Usuario:").pack()
    entry_usuario = tk.Entry(marco_login)
    entry_usuario.pack()

    tk.Label(marco_login, text="Contraseña:").pack()
    entry_contraseña = tk.Entry(marco_login, show="*")
    entry_contraseña.pack()

    tk.Button(marco_login, text="Ingresar", command=login).pack(pady=10)

    # MENÚ PRINCIPAL 
    marco_menu = tk.Frame(ventana)

    tk.Label(marco_menu, text="Bienvenido al Sistema de Reservas", font=("Arial", 14)).pack(pady=10)

    resultado = tk.Label(marco_menu, text="", justify="left")
    resultado.pack(pady=10)

    # Funciones de botones
    def ver_catalogo():
        resultado.config(text=mostrar_catalogo())

    def ver_reservas():
        resultado.config(text=mostrar_reservas())

    def abrir_reservar():
        marco_menu.pack_forget()
        marco_reserva.pack(fill="both", expand=True)

    def cerrar_sesion():
        reservas.clear()
        marco_menu.pack_forget()
        marco_login.pack(fill="both", expand=True)

    # Botones menú
    tk.Button(marco_menu, text="Ver Catálogo", command=ver_catalogo, width=20).pack(pady=5)
    tk.Button(marco_menu, text="Reservar Servicio", command=abrir_reservar, width=20).pack(pady=5)
    tk.Button(marco_menu, text="Mis Reservas", command=ver_reservas, width=20).pack(pady=5)
    tk.Button(marco_menu, text="Cerrar Sesión", command=cerrar_sesion, width=20).pack(pady=5)

    # FORMULARIO DE RESERVA 
    marco_reserva = tk.Frame(ventana)

    tk.Label(marco_reserva, text="Reservar Servicio", font=("Arial", 14)).pack(pady=10)

    tk.Label(marco_reserva, text="Seleccione un servicio:").pack()
    servicio_var = tk.StringVar()
    servicio_var.set(list(servicios.keys())[0])  
    drop_servicios = tk.OptionMenu(marco_reserva, servicio_var, *servicios.keys())
    drop_servicios.pack()

    tk.Label(marco_reserva, text="Ingrese fecha (dd/mm/aaaa):").pack()
    entry_fecha = tk.Entry(marco_reserva)
    entry_fecha.pack()

    def confirmar_reserva():
        servicio = servicio_var.get()
        fecha = entry_fecha.get()
        if fecha.strip() == "":
            messagebox.showwarning("Atención", "Debe ingresar una fecha")
            return
        mensaje = reservar_servicio(servicio, fecha)
        messagebox.showinfo("Reserva", mensaje)
        entry_fecha.delete(0, tk.END)

    def volver_menu():
        marco_reserva.pack_forget()
        marco_menu.pack(fill="both", expand=True)

    tk.Button(marco_reserva, text="Confirmar Reserva", command=confirmar_reserva).pack(pady=5)
    tk.Button(marco_reserva, text="Volver al Menú", command=volver_menu).pack(pady=5)

    ventana.mainloop()



if __name__ == "__main__":
    interfaz()
