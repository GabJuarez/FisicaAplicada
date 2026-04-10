import tkinter as tk
from tkinter import messagebox
from math import sqrt

# Constante de Coulomb
k = 9 * 10**9


class Carga:
    def __init__(self, q, x, y):
        self.q = q
        self.x = x
        self.y = y


def calcular_fuerza(cargas):
    objetivo = cargas[-1]
    fx_total = 0
    fy_total = 0

    for carga in cargas[:-1]:
        dx = objetivo.x - carga.x
        dy = objetivo.y - carga.y
        r = sqrt(dx**2 + dy**2)

        if r == 0:
            continue

        ux = dx / r
        uy = dy / r

        F = k * carga.q * objetivo.q / (r**2)

        fx = F * ux
        fy = F * uy

        fx_total += fx
        fy_total += fy

    magnitud = sqrt(fx_total**2 + fy_total**2)

    return fx_total, fy_total, magnitud


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Fuerza Neta ⚡")
        self.root.geometry("520x650")
        self.root.config(bg="#f4f6f7")

        self.cargas = []
        self.inputs = []

        # Título
        tk.Label(root, text="Calculadora de Fuerza Neta",
                 font=("Arial", 16, "bold"),
                 bg="#f4f6f7").pack(pady=10)

        # Entrada de número de cargas
        tk.Label(root, text="Número de cargas:",
                 bg="#f4f6f7").pack()

        self.entry_n = tk.Entry(root)
        self.entry_n.pack(pady=5)

        tk.Button(root, text="Generar campos",
                  command=self.generar_campos,
                  bg="#5dade2", fg="white").pack(pady=10)

        # Frame donde se crean los campos dinámicos
        self.frame_campos = tk.Frame(root, bg="#f4f6f7")
        self.frame_campos.pack()

        # Botón calcular
        tk.Button(root, text="Calcular Fuerza",
                  command=self.calcular,
                  bg="#58d68d", fg="white").pack(pady=20)

        # Resultado
        self.resultado = tk.Label(root, text="",
                                  bg="#f4f6f7",
                                  font=("Arial", 12))
        self.resultado.pack()

    def generar_campos(self):
        for widget in self.frame_campos.winfo_children():
            widget.destroy()

        self.inputs.clear()

        try:
            n = int(self.entry_n.get())
            if n < 2:
                raise ValueError
        except:
            messagebox.showerror("Error", "Ingrese un número válido (mínimo 2)")
            return

        for i in range(n):
            contenedor = tk.Frame(self.frame_campos, bg="#f4f6f7")
            contenedor.pack(pady=5)

            titulo = f"Carga {i+1}"
            if i == n - 1:
                titulo += " (Objetivo)"

            tk.Label(contenedor, text=titulo,
                     bg="#f4f6f7",
                     font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=6)

            tk.Label(contenedor, text="x:", bg="#f4f6f7").grid(row=1, column=0)
            x = tk.Entry(contenedor, width=8)
            x.grid(row=1, column=1)

            tk.Label(contenedor, text="y:", bg="#f4f6f7").grid(row=1, column=2)
            y = tk.Entry(contenedor, width=8)
            y.grid(row=1, column=3)

            tk.Label(contenedor, text="q:", bg="#f4f6f7").grid(row=1, column=4)
            q = tk.Entry(contenedor, width=10)
            q.grid(row=1, column=5)

            self.inputs.append((x, y, q))

    def calcular(self):
        self.cargas.clear()

        try:
            for x, y, q in self.inputs:
                carga = Carga(float(q.get()), float(x.get()), float(y.get()))
                self.cargas.append(carga)

            fx, fy, mag = calcular_fuerza(self.cargas)

            self.resultado.config(
                text=f"Fuerza Neta:\nFx = {round(fx,2)} N\nFy = {round(fy,2)} N\nMagnitud = {round(mag,2)} N"
            )

        except ValueError:
            messagebox.showerror("Error", "Ingrese solo números válidos")
        except:
            messagebox.showerror("Error", "Ocurrió un error en el cálculo")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()