import customtkinter as ctk
import tkinter as tk
from model import engine, Base
from controller.cont_persona import Controller_Perona
from controller.cont_pais import Controller_Pais
from controller.contr_nivescol import Controller_Nivelescolar
from controller.contr_registro import Controller_Registro
from controller.cont_genero import Controller_Genero
from controller.cont_raza import Controller_Raza
from controller.contr_tipo_solicitud import Controller_TipoSolicitud
from controller.cont_ciudad_brasil import Controller_Ciudad_Brasil
from controller.contr_prof_oficio import Controller_ProfOficio
from controller.contr_pais_ciudad import Controller_PaisCiudad
from controller.contr_hijos import Controller_HijosMenor



from vista.vie_persona import PersonaView
from vista.vie_pais import PaisView
from vista.report_fecha import ReporteFecha

Base.metadata.create_all(engine)

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Personas y Países")
        self.geometry("400x300")
        

        # Inicializar el controlador
        self.controller_personas = Controller_Perona()
        self.controller_pais = Controller_Pais()
        self.controller_nivelescol=Controller_Nivelescolar()
        self.controller_registro=Controller_Registro()
        self.controller_genero=Controller_Genero()
        self.controller_raza=Controller_Raza()
        self.controller_tiposolicitud=Controller_TipoSolicitud()
        self.controller_ciudadbrasil=Controller_Ciudad_Brasil()
        self.controller_profeoficio=Controller_ProfOficio()
        self.controller_paisciudad=Controller_PaisCiudad()
        self.controller_hijosmenores=Controller_HijosMenor()

        # Crear el menú
        self.create_menu()
        
        self.ciudadbrasil_list=self.controller_ciudadbrasil.listar_ciudadbrasil()
        self.country_list=self.controller_pais.listar_paises()
        
        # Centrar la ventana
        self.center_window()

    def create_menu(self):
        menu_bar = tk.Menu(self)
        
        # Nomencladores
        #nomencladores_menu = tk.Menu(menu_bar, tearoff=0)
        #nomencladores_menu.add_command(label="País", command=self.open_pais_view)
        #menu_bar.add_cascade(label="Nomencladores", menu=nomencladores_menu)

        # Gestión
        gestion_menu = tk.Menu(menu_bar, tearoff=0)
        gestion_menu.add_command(label="Personas", command=self.open_persona_view)
        #gestion_menu.add_command(label="Reporte", command=self.open_report_fecha)
        menu_bar.add_cascade(label="Gestión", menu=gestion_menu)
        
        
        reportes_menu = tk.Menu(menu_bar, tearoff=0)
        reportes_menu.add_command(label="Rango fecha", command=self.open_report_fecha)
        menu_bar.add_cascade(label="Reportes", menu=reportes_menu)

        self.config(menu=menu_bar)

    
    def open_report_fecha(self):
        report_fecha = ReporteFecha(self.controller_registro,self.controller_hijosmenores)
    
    def open_pais_view(self):
        pais_view = PaisView(self.controller_pais)

    def open_persona_view(self):
        persona_view = PersonaView(self.controller_personas,self.controller_pais,
                                   self.controller_nivelescol,self.controller_registro,
                                   self.controller_genero,self.controller_raza,self.controller_tiposolicitud,
                                   self.controller_ciudadbrasil,self.controller_profeoficio,
                                   self.controller_paisciudad,self.controller_hijosmenores,
                                   self.ciudadbrasil_list,self.country_list)
    def center_window(self):
        # Obtener el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Obtener el tamaño de la ventana
        window_width = 400
        window_height = 300

        # Calcular la posición x e y
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Establecer la posición de la ventana
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modo de apariencia: "light", "dark", "system"
    ctk.set_default_color_theme("blue")  # Tema de color
    app = MainApp()
    app.mainloop()