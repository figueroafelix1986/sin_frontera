import customtkinter as ctk
from datetime import datetime
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox




class Tooltip:
    """Clase para crear un tooltip simple."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None

        # Bind mouse events       

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
        self.widget.bind("<Button-1>", self.hide_tooltip_on_click)  # Agregar este binding


    def show_tooltip(self, event=None):
        """Muestra el tooltip."""
        if not self.tooltip_window:  # Solo mostrar si no está visible
            x = self.widget.winfo_rootx() + 20
            y = self.widget.winfo_rooty() + 20
            self.tooltip_window = ctk.CTkToplevel(self.widget)
            self.tooltip_window.wm_overrideredirect(True)  # Sin bordes
            self.tooltip_window.wm_geometry(f"+{x}+{y}")
            label = ctk.CTkLabel(self.tooltip_window, text=self.text)
            label.pack()

    def hide_tooltip(self, event=None):
        """Oculta el tooltip."""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

    def hide_tooltip_on_click(self, event=None):
        """Oculta el tooltip al hacer clic en el widget."""
        self.hide_tooltip()