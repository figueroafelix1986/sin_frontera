import customtkinter as ctk
from tkinter import ttk


class PaisView(ctk.CTkToplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Agregar País")
        
        self.label_nombre = ctk.CTkLabel(self, text="Nombre del País:")
        self.label_nombre.pack(pady=10)
        
        self.entry_nombre = ctk.CTkEntry(self)
        self.entry_nombre.pack(pady=10)
        
        self.button_guardar = ctk.CTkButton(self, text="Guardar", command=self.guardar_pais)
        self.button_guardar.pack(pady=10)

    def guardar_pais(self):
        nombre = self.entry_nombre.get()
        self.controller.agregar_pais(nombre)
        self.destroy()