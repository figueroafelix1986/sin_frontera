import customtkinter as ctk
from datetime import datetime
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox
from .tool_coment import Tooltip
from .list_combo import Lista_combobox


class PersonaView(ctk.CTkToplevel):
    def __init__(self, controller_person,controller_pais,controller_nivelescolar,
                 controller_registro,controller_genero,controller_raza,controller_tiposolicitud,
                 controller_ciudadbrasil,controller_profeoficio,controller_paisciudad,
                 controller_hijosmenores,ciudadbrasil_list,country_list):
        super().__init__()
        self.controller_person = controller_person
        self.controller_pais = controller_pais   
        self.controller_nivelescolar= controller_nivelescolar  
        self.controller_registro=controller_registro
        self.controller_genero=controller_genero 
        self.controller_raza=controller_raza
        self.controller_ciudadbrasil=controller_ciudadbrasil
        self.controller_tiposolicitud=controller_tiposolicitud
        self.controller_profeoficio=controller_profeoficio
        self.controller_paisciudad=controller_paisciudad
        self.controller_hijosmenores=controller_hijosmenores
        self.country_list=country_list
        self.ciudadbrasil_list=ciudadbrasil_list
        self.contr_list_comb = Lista_combobox()
        self.datos_hijos = []
        self.cantidad_regi=0 
        self.cantidadpersonas=""
        self.title("Agregar Persona")  
        #self.attributes('-fullscreen', True) 
        # Para salir del modo de pantalla completa, puedes usar la tecla Esc
    
    
       # Obtener la lista de países
        country_list = self.country_list
        
        #obtener la lista de nivel escolar
        nivelescolar_list=self.controller_nivelescolar.listar_nivelescolar()
        
        #ontener genero
        genero_list=self.controller_genero.listar_genero()
        
        self.genero_hijos_list=genero_list
        
        tiposoli_list=self.controller_tiposolicitud.listar_tiposolicitud()    
        
        profec_ofici_list=self.controller_profeoficio.listar_profeoficio() 
        
        raza_list=self.controller_raza.listar_raza()
        
        ciudadbrasil_list=self.ciudadbrasil_list
        
        pais_ciudad_list=self.controller_paisciudad.listar_paisciudad()
          
        # Maximizar la ventana
        #self.state('zoomed')
         # Configurar la grid para que la columna 1 tenga peso
        #self.grid_columnconfigure(1, weight=1)
        
       
        self.label_frame_supe = ctk.CTkFrame(self, corner_radius=10, border_width=5)
        self.label_frame_supe.pack(side="top",expand=False,fill="x")
        
        self.label_frame_bajo = ctk.CTkFrame(self, corner_radius=10, border_width=10)
        self.label_frame_bajo.pack(side="top",expand=False,fill="x")
        
        self.entry_nombre = ctk.CTkEntry(self.label_frame_supe,placeholder_text="Nombre y Apellido")#width=300)
        self.entry_nombre.grid(row=0, column=1,
                             padx=20,
                            pady=20, sticky="ew")   
        
        self.entry_ni = ctk.CTkEntry(self.label_frame_supe,placeholder_text="CPF")
        self.entry_ni.grid(row=0, column=2,
                             padx=20,
                            pady=20, sticky="ew")       
            
        self.entry_telefono = ctk.CTkEntry(self.label_frame_supe,placeholder_text="Telefono")
        self.entry_telefono.grid(row=0, column=3,
                             padx=20,
                            pady=20, sticky="ew")
               
        self.email = ctk.CTkEntry(self.label_frame_supe,placeholder_text="Email")
        self.email.grid(row=0, column=4,  padx=20, pady=10, sticky="ew")
        
        
        self.genero_combobox = ctk.CTkComboBox(self.label_frame_supe,values=[genero.nombre for genero in genero_list], 
                                                command=self.on_combobox_genero,state="readonly")
       
        self.genero_combobox.grid(row=0, column=5,
                            padx=20,
                            pady=20, sticky="ew")   
        
        
        self.raza_combobox = ctk.CTkComboBox(self.label_frame_supe,values=[raza.nombre for raza in raza_list], 
                                                command=self.on_combobox_raza,state="readonly")
       
        self.raza_combobox.grid(row=0, column=6,
                             padx=20,
                            pady=20, sticky="ew")
               
        
        self.lgbt_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.opciones.keys()),
            command=self.on_combobox_lgbt, 
            state="readonly"
        )
               
        # Establecemos el valor por defecto
        default_value_lgbt = list(self.contr_list_comb.opciones.keys())[1]  # "No"
        self.lgbt_combobox.set(default_value_lgbt)

        # Guardamos el ID correspondiente en la variable
        self.selected_lgbt_id = self.contr_list_comb.opciones[default_value_lgbt]
        
        
        self.lgbt_combobox.grid(row=1, column=1,padx=20,pady=20, sticky="ew")
        
                           
        
        self.deficiencia_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.deficiencia.keys()),
            command=self.on_combobox_deficiencia, 
            state="readonly"
        )
        
       
         # Establecemos el valor por defectoopciones
        self.selected_deficiencia_nomb = list(self.contr_list_comb.deficiencia.keys())[0] 
        self.deficiencia_combobox.set(self.selected_deficiencia_nomb)
  
        self.deficiencia_combobox.grid(row=1, column=2,
                             padx=20,
                            pady=20, sticky="ew")
        
        self.estado_civil_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.estado_civil.keys()),
            command=self.on_combobox_estado_civil, 
            state="readonly"
        )
        
    
        self.selected_estcivil_nomb = list(self.contr_list_comb.estado_civil.keys())[0] 
        self.estado_civil_combobox.set(self.selected_estcivil_nomb)
  
        self.estado_civil_combobox.grid(row=1, column=6,
                             padx=20,
                            pady=20, sticky="ew")
        
        self.entry_fecha_brasil = DateEntry(self.label_frame_supe, date_pattern='dd/mm/yyyy')
        self.entry_fecha_brasil.grid(row=2, column=1,
                             padx=20,
                            pady=20, sticky="ew")
        
        
        self.nombre_ciudad_brasil = [ciudadbrasil.nombre for ciudadbrasil in ciudadbrasil_list]
        
        nuevo_ciudad_brasil=self.nombre_ciudad_brasil[:10]

        self.ciudad_brasil_combobox = ctk.CTkComboBox(self.label_frame_supe,values=nuevo_ciudad_brasil ,
                                                      command=self.on_combobox_ciudadbrasil)
        
        self.ciudad_brasil_combobox.grid(row=3, column=1,  padx=20, pady=10)
        
        self.ciudad_brasil_combobox.bind('<KeyRelease>', self.autocompletar)  
        
        self.ciudad_brasil_combobox._entry.bind('<FocusIn>', self.select_combobox_txt)
        
        
        self.entry_direccion = ctk.CTkEntry(self.label_frame_supe,placeholder_text="Direccion",width=120)
        self.entry_direccion.grid(row=3, column=2,
                            padx=20,
                            pady=20, sticky="ew")  
        
        self.ninos_menor_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.ninos_menor.keys()),
            command=self.on_combobox_nino_menores, 
            state="readonly"
        )            
        self.selected_ninomenor_nomb = list(self.contr_list_comb.ninos_menor.keys())[0] 
        self.ninos_menor_combobox.set(self.selected_ninomenor_nomb)
  
        self.ninos_menor_combobox.grid(row=1, column=4,
                             padx=20,
                            pady=20, sticky="ew")   
        
        
        # Crear un combobox con los nombres de los países
        self.nivel_esco_combobox = ctk.CTkComboBox(self.label_frame_supe,values=[nivelescolar.nombre for nivelescolar in nivelescolar_list], 
                                                command=self.on_combobox_nivelescolar,state="readonly")
       
        self.nivel_esco_combobox.grid(row=1, column=7,
                             padx=20,
                            pady=20, sticky="ew")      
               
        
        
             
        self.status_migra_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.status_migr.keys()),
            command=self.on_combobox_statumigra_laboral, 
            state="readonly"
        )
        
             
        self.selected_statumigra_nomb = list(self.contr_list_comb.status_migr.keys())[0] 
        self.status_migra_combobox.set(self.selected_statumigra_nomb)
  
        self.status_migra_combobox.grid(row=2, column=2,
                             padx=20,
                            pady=20, sticky="ew")
        
       
        
        
        self.acti_econo_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.actividad_econo.keys()),
            command=self.on_combobox_actiecono_laboral, 
            state="readonly"
        )
        
             
        self.selected_actiecono_nomb = list(self.contr_list_comb.actividad_econo.keys())[22] 
        self.acti_econo_combobox.set(self.selected_actiecono_nomb)
  
        self.acti_econo_combobox.grid(row=2, column=4,
                             padx=20,
                            pady=20, sticky="ew")
        
        self.situa_laboral_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.situa_laboral.keys()),
            command=self.on_combobox_situacion_laboral, 
            state="readonly"
        )
        
             
        self.selected_situlaboral_nomb = list(self.contr_list_comb.situa_laboral.keys())[0] 
        self.situa_laboral_combobox.set(self.selected_situlaboral_nomb)
  
        self.situa_laboral_combobox.grid(row=2, column=3,
                             padx=20,
                            pady=20, sticky="ew")
        
                
 
        if tiposoli_list:
            self.tiposolicitud_combobox = ctk.CTkComboBox(self.label_frame_supe,values=[tiposolicitud.nombre for tiposolicitud in tiposoli_list], 
                                                command=self.on_combobox_tiposolicitud)
        else:
            self.tiposolicitud_combobox = ctk.CTkComboBox(self.label_frame_supe,values=["No hay datos"], 
                                                command=self.on_combobox_tiposolicitud)
            
       
        self.tiposolicitud_combobox.grid(row=3, column=7,
                             padx=20,
                            pady=20, sticky="ew")
        
        
        
        self.cartera_trab_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.opciones.keys()),
            command=self.on_combobox_cartera, 
            state="readonly"
        )
        
        # Establecemos el valor por defecto
        default_value_cartera = list(self.contr_list_comb.opciones.keys())[1]  # "No"
        self.cartera_trab_combobox.set(default_value_cartera)

        # Guardamos el ID correspondiente en la variable
        self.selected_cartera_id = self.contr_list_comb.opciones[default_value_cartera]

        self.cartera_trab_combobox.grid(row=2, column=5,
                            padx=20,
                            pady=20, sticky="ew")
        
        
        self.ayuda_gob_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.opciones.keys()),
            command=self.on_combobox_ayuda_gob, 
            state="readonly"
        )
        
        # Establecemos el valor por defecto
        default_value_ayuda = list(self.contr_list_comb.opciones.keys())[1]  # "No"
        self.ayuda_gob_combobox.set(default_value_ayuda)

        # Guardamos el ID correspondiente en la variable
        self.selected_ayugob_id = self.contr_list_comb.opciones[default_value_ayuda]

        self.ayuda_gob_combobox.grid(row=2, column=6,
                             padx=20,
                            pady=20, sticky="ew")
        
               
        
        
        self.uf_reside_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.uf_residen.keys()),
            command=self.on_combobox_uf_resid, 
            state="readonly"
        )
        
        # Establecemos el valor por defecto
        default_value_uf_reside = list(self.contr_list_comb.uf_residen.keys())[0]  
        self.uf_reside_combobox.set(default_value_uf_reside)

        # Guardamos el ID correspondiente en la variable
        self.selected_ufresid_id = self.contr_list_comb.uf_residen[default_value_uf_reside]

        self.uf_reside_combobox.grid(row=2, column=7,
                             padx=20,
                            pady=20, sticky="ew")
                
               
              
        
        if profec_ofici_list:
        
            self.profecion_ofic_combobox = ctk.CTkComboBox(self.label_frame_supe,values=[profecoficio.nombre for profecoficio in profec_ofici_list], 
                                                command=self.on_combobox_profeoficio)
        else:
            self.profecion_ofic_combobox = ctk.CTkComboBox(self.label_frame_supe,values=["No hay datos"], 
                                                command=self.on_combobox_profeoficio)
       
        self.profecion_ofic_combobox.grid(row=3, column=4,
                             padx=20,
                            pady=20, sticky="ew")
        
        self.profecion_ofic_combobox._entry.bind('<FocusIn>', self.select_combobox_txt)
        
        
        
        self.renta_mensual_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.renta_mes.keys()),
            command=self.on_combobox_rentames_laboral, 
            state="readonly"
        )
        
             
        self.selected_rentames_nomb = list(self.contr_list_comb.renta_mes.keys())[0] 
        self.renta_mensual_combobox.set(self.selected_rentames_nomb)
  
        self.renta_mensual_combobox.grid(row=3, column=3,
                            padx=20,
                            pady=20, sticky="ew")
        
               
        self.pais_ciudad_combobox = ctk.CTkComboBox(self.label_frame_supe,values=[pasisciudad.nombre for pasisciudad in pais_ciudad_list], 
                                                command=self.on_combobox_paisciudad)
        
            
            
        self.pais_ciudad_combobox.grid(row=3, column=5,
                            padx=20,
                            pady=20, sticky="ew")
        
        
        # Crear un botón para guardar
        self.button_agregar_nino = ctk.CTkButton(
            self.label_frame_supe, 
            fg_color="white", 
            hover_color="grey",
            text_color="black", 
            text="Cantidad de hijos",
            command=self.abrir_vent_hijos
        )
        self.button_agregar_nino.grid(row=3, column=6,
                            padx=20,
                            pady=20, sticky="w")             
        
      
        
        
        self.entry_observacion = ctk.CTkEntry(self.label_frame_supe,placeholder_text="Observacion")
        self.entry_observacion.grid(row=4, column=1,columnspan=3,
                             padx=20,
                            pady=20, sticky="ew") 
        
        
        self.entry_cadastrante = ctk.CTkEntry(self.label_frame_supe,placeholder_text="Cadastrante")
        self.entry_cadastrante.grid(row=5, column=1,columnspan=2,
                             padx=20,
                            pady=20, sticky="ew") 
        
        
        
        self.entry_fecha = DateEntry(self.label_frame_supe, date_pattern='dd/mm/yyyy')
        self.entry_fecha.grid(row=1, column=3,
                             padx=20,
                            pady=20, sticky="ew")

       

        
        self.nombre_pais_naci =[country.nombre for country in country_list]
        
        nuevo_pais_naci=self.nombre_pais_naci[:10]
        

# Crear un combobox con los nombres de los países
        self.country_combobox = ctk.CTkComboBox(self.label_frame_supe,values=nuevo_pais_naci, 
                                                command=self.on_combobox_select,state="normal")
       
        self.country_combobox.grid(row=1, column=5,
                             padx=20,
                            pady=20, sticky="ew")
        
        self.country_combobox.bind('<KeyRelease>', self.autocompletar_pais)
        # Vincular el evento de clic al Combobox
        self.country_combobox._entry.bind('<FocusIn>', self.select_combobox_txt)
       
       
       
        self.etnia_combobox = ctk.CTkComboBox(
            self.label_frame_supe,
            values= list(self.contr_list_comb.etnia.keys()),
            command=self.on_combobox_etnia_laboral, 
            state="readonly"
        )
        
             
        self.selected_etnia_nomb = list(self.contr_list_comb.etnia.keys())[4] 
        self.etnia_combobox.set(self.selected_etnia_nomb)
  
        self.etnia_combobox.grid(row=0, column=7,
                             padx=20,
                            pady=20, sticky="ew")      
              
        
        
        if country_list:  # Asegúrate de que la lista country_comboboxno esté vacía
            default_country = country_list[223].nombre  # Establece el primer país como seleccionado
            self.country_combobox.set(default_country)  # Establece el valor en el combobox
            self.selected_value_id = default_country 
            
        self.opcion_ciudad_pais(default_country)

        if nivelescolar_list:
            defaul_nivelescolar=nivelescolar_list[0].nombre
            self.nivel_esco_combobox.set(defaul_nivelescolar)
            self.selcted_nivel_id=defaul_nivelescolar
        
        if genero_list:
            defaul_genero=genero_list[0].nombre
            self.genero_combobox.set(defaul_genero)
            self.selcted_genero_id=defaul_genero
        
        if raza_list:
            defaul_raza=raza_list[0].nombre
            self.raza_combobox.set(defaul_raza)
            self.selcted_raza_id=defaul_raza
            
            
        if (len(tiposoli_list))>0:
            defaul_tiposoliciud=tiposoli_list[0].nombre
            self.tiposolicitud_combobox.set(defaul_tiposoliciud)
            #self.selcted_tiposoli_id=defaul_raza
        
        if  profec_ofici_list:
            defaul_profocficio=profec_ofici_list[0].nombre
            self.profecion_ofic_combobox.set(defaul_profocficio) 
            
            
            
        if ciudadbrasil_list:
            defaul_ciudad_brasil=ciudadbrasil_list[1].nombre
            self.ciudad_brasil_combobox.set(defaul_ciudad_brasil)
            #self.selcted_ciudadbrasi_id=defaul_raza
        
        
        row_botones=5
        # Crear un botón para guardar
        self.button_guardar = ctk.CTkButton(
            self.label_frame_supe, 
            text="Guardar", 
            text_color="white", 
            command=self.guardar_persona
        )
        self.button_guardar.grid(row=row_botones, column=6,
                            padx=20,
                            pady=20, sticky="w")
        
        # Crear un botón para guardar
        self.button_editar = ctk.CTkButton(
            self.label_frame_supe, 
            fg_color="green", 
            hover_color="grey",
            text_color="white", 
            text="Editar",
            command=self.actualizar_pers_regist
        )
        self.button_editar.grid(row=row_botones, column=7,
                            padx=20,
                            pady=20, sticky="w")
        
        self.button_editar.configure(state='disabled')
        
        self.cantidadpersonas=ctk.CTkLabel(self.label_frame_bajo,text="Cantidad de personas "+str(self.cantidad_regi))
        self.cantidadpersonas.pack()
        
        # Crear el Treeview
        self.tree = ttk.Treeview(self.label_frame_bajo, columns=("ID", "Nombre", "CPF", "Pais", 
                                                                 "Fech_Nacimiento", "Telefono","ENDEREÇO","Email",
                                                                 "Genero","Color de Piel","Etnia",
                                                                 "LGBTQIAPN+","Deficiência","Filhos Menores",
                                                                 "País de Nacionalidade","Estado Civil",
                                                                 "Escolaridade","Data de Chegada ao Brasil",
                                                                 "Status Migratório","Situação Laboral",
                                                                 "Atividade econômica","Benefício do governo?",
                                                                 "Cidade de Residência do Migrante",
                                                                 "Renda Familiar Mensal","Profesión y oficio",
                                                                 "Tipo de Solicitud","Observaciones",
                                                                 "Cadastrante","Cartera de trab","Ciudad Nacimiento"), show='headings')


        self.tree.column("ID", width=0)  # Ocultar la columna ID
        self.tree.heading("ID", text="")

        # Crear las barras de desplazamiento
        self.scrollbar_y = ttk.Scrollbar(self.label_frame_bajo, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = ttk.Scrollbar(self.label_frame_bajo, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scrollbar_x.set)

        # Empaquetar las barras de desplazamiento
        self.scrollbar_y.pack(side="right", fill='y')
        self.scrollbar_x.pack(side="bottom", fill='x')

        # Empaquetar el Treeview
        self.tree.pack(side="left", expand=True, fill='both')

        # Configuración de encabezados y columnas
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            #self.tree.column(col, width=100)  # Ajusta el ancho según sea necesario

             
       
        # Cargar datos seleccionados        
        self.tree.bind("<<TreeviewSelect>>", self.cargar_datseleccionados)
        
        
         # Cargar datos
        self.cargar_personas()
        self.descrip_combo_entry()  
    
        
    def cargar_personas(self):
        # Limpiar el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener las personas del controlador
        self.personas = self.controller_person.listar_fecha()
        self.registros=self.controller_registro.listar_fecha()
        self.cantidad_regi=len(self.registros)
        self.cantidadpersonas.configure(text="Cantidad de personas "+str(self.cantidad_regi))
        
      

        # Insertar los datos en el Treeview
        for registro in self.registros:
            persona_ids=self.controller_person.listar_person_id(registro.persona_id)
            for persona in persona_ids:
                    pais=self.controller_pais.get_id_pais(persona.pais_id)
                    genero=self.controller_genero.get_id_genero(persona.genero_id)
                    raza=self.controller_raza.get_id_raza(persona.raza_id)
                    nivel_escolar=self.controller_nivelescolar.get_id_nivelescolar(persona.nivel_escol_id)
                  
                                            
                    self.tree.insert("", "end", values=(persona.id, persona.nombre_apellido, registro.num_ident,
                                                        pais.nombre, 
                                                        self.contr_list_comb.format_fecha(persona.fecha_nacimiento),
                                                        registro.telefono,
                                                        registro.direccion,registro.email,genero.nombre,                                                        
                                                        raza.nombre,registro.etnia,
                                                        self.contr_list_comb.retorn_opcion(registro.lgbtqiapn),
                                                        registro.deficiencia,
                                                        registro.nino_menor,pais.nombre,registro.estado_civil,
                                                        nivel_escolar.nombre,
                                                        self.contr_list_comb.format_fecha(persona.fecha_llegada),
                                                        registro.status_migrat,registro.situa_laboral,
                                                        registro.activ_econo,
                                                        self.contr_list_comb.retorn_opcion(registro.beneficio_gobierno),
                                                        registro.ciudad_resid_brasil,registro.renta_mens,
                                                        registro.profec_oficio,registro.tipo_solicitud,registro.observacion,
                                                        registro.cadastrante,
                                                        self.contr_list_comb.retorn_opcion(registro.cartera_trabajo),persona.ciudad_person))

        #self.actualizar_cantregistro()
    
    def on_combobox_select(self,selected_value):
     # Obtener el valor seleccionado
     
        id_paises=self.controller_pais.get_pais(selected_value)
        
        select_porid = self.controller_paisciudad.get_id_pais(id_paises.id)
        
        # Configurar los valores del Combobox
        pais_ciudad_nombres = [paisciudad.nombre for paisciudad in select_porid]
        if pais_ciudad_nombres:
            self.pais_ciudad_combobox.configure(values=pais_ciudad_nombres)
            self.pais_ciudad_combobox.set(pais_ciudad_nombres[0])     
        else:
            self.pais_ciudad_combobox.configure(values=["No hay registros"])
            self.pais_ciudad_combobox.set("No hay registros")

        
        self.selected_value_id = selected_value  # Obtener el valor seleccionado
        return self.selected_value_id
    
    def on_combobox_nivelescolar(self,selected_value):
    # Obtener el valor seleccionado
        self.selcted_nivel_id = selected_value  # Obtener el valor seleccionado
        return (self.selcted_nivel_id)
    
    def on_combobox_genero(self,selected_value):
    # Obtener el valor seleccionado
        self.selcted_genero_id = selected_value  # Obtener el valor seleccionado
        return (self.selcted_genero_id)
    
    def on_combobox_ciudadbrasil(self,selected_value):
    # Obtener el valor seleccionado       
        self.selcted_ciudadbrasil_nom = selected_value  # Obtener el valor seleccionado
        return (self.selcted_ciudadbrasil_nom)
    
    def on_combobox_profeoficio(self,selected_value):
    # Obtener el valor seleccionado       
        self.selcted_profecoficio = selected_value  # Obtener el valor seleccionado
        return (self.selcted_profecoficio)
    
    
    def on_combobox_tiposolicitud(self,selected_value):
    # Obtener el valor seleccionado
        self.selcted_tiposolicitud_nom = selected_value  # Obtener el valor seleccionado
        return (self.selcted_tiposolicitud_nom)
    
    def on_combobox_paisciudad(self,selected_value):
    # Obtener el valor seleccionado
        self.selcted_paisciudad_nom = selected_value  # Obtener el valor seleccionado
        return (self.selcted_paisciudad_nom)
    
    
    
    
    def on_combobox_raza(self,selected_value):
    # Obtener el valor seleccionado
        self.selcted_raza_id = selected_value  # Obtener el valor seleccionado
        return (self.selcted_raza_id)
    
    
    def on_combobox_cartera(self,selected_value):
    # Obtener el valor seleccionado
        self.selected_cartera_id = self.contr_list_comb.opciones[selected_value]  # Obtener el valor seleccionado
        return (self.selected_cartera_id)
    
    def on_combobox_ayuda_gob(self, seleccion):
        if seleccion == "Ayuda del gobierno":
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción válida.")            
        else:
            # Obtenemos el valor asociado a la opción seleccionada
            self.selected_ayugob_id = self.contr_list_comb.opciones[seleccion]
        return (self.selected_ayugob_id)
        #print(f"Seleccionaste: {seleccion}, Valor asociado: {valor}")
        
        
    def on_combobox_uf_resid(self, seleccion):
        return self.contr_list_comb.uf_residen[seleccion]
        
    def on_combobox_lgbt(self, seleccion):
        if seleccion == "LBGT+":
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción válida.")            
        else:
            # Obtenemos el valor asociado a la opción seleccionada
            self.selected_lgbt_id = self.contr_list_comb.opciones[seleccion]
        return (self.selected_lgbt_id)

    def on_combobox_deficiencia(self, seleccion):
        if seleccion == "Deficiencia":
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción válida.")            
        else:
            # Obtenemos el valor asociado a la opción seleccionada
            self.selected_deficiencia_id = self.contr_list_comb.deficiencia[seleccion]
            self.selected_deficiencia_nomb=seleccion
        return (self.selected_deficiencia_id,self.selected_deficiencia_nomb)
    
    def on_combobox_nino_menores(self, seleccion):
            self.selected_nino_menor_id = self.contr_list_comb.ninos_menor[seleccion]
            self.selected_ninomenor_nomb=seleccion
            return (self.selected_nino_menor_id,self.selected_ninomenor_nomb)
    
    def on_combobox_estado_civil(self, seleccion):
            self.selected_estcivil_id = self.contr_list_comb.estado_civil[seleccion]
            self.selected_estcivil_nomb=seleccion
            return (self.selected_estcivil_id,self.selected_estcivil_nomb)    
        
        
    def on_combobox_situacion_laboral(self, seleccion):
            self.selected_situa_laboral_id = self.contr_list_comb.situa_laboral[seleccion]
            self.selected_situlaboral_nomb=seleccion
            return (self.selected_situa_laboral_id,self.selected_situlaboral_nomb)
        
        
    def on_combobox_actiecono_laboral(self, seleccion):
            self.selected_actiecono_id = self.contr_list_comb.actividad_econo[seleccion]
            self.selected_actiecono_nomb=seleccion
            return (self.selected_actiecono_id,self.selected_actiecono_nomb)
        
    def on_combobox_statumigra_laboral(self, seleccion):
            #self.selected_actiecono_id = self.contr_list_comb.actividad_econo[seleccion]
            self.selected_statumigra_nomb=seleccion
            return (self.selected_statumigra_nomb)
        
        
    def on_combobox_rentames_laboral(self, seleccion):
            #self.selected_actiecono_id = self.contr_list_comb.actividad_econo[seleccion]
            self.selected_rentames_nomb=seleccion
            return (self.selected_rentames_nomb)
        
    def on_combobox_etnia_laboral(self, seleccion):
            #self.selected_actiecono_id = self.contr_list_comb.actividad_econo[seleccion]
            self.selected_etnia_nomb=seleccion
            return (self.selected_etnia_nomb)
        
    def abrir_vent_hijos(self):
        # Crear una nueva ventana
        nueva_ventana = ctk.CTkToplevel(self)
        nueva_ventana.title("Agregar Hijo")

        # Frame superior para ingresar datos
        label_frame_supe = ctk.CTkFrame(nueva_ventana, corner_radius=10, border_width=5)
        label_frame_supe.pack(side="top", expand=False, fill="x", padx=10, pady=10)

        # ComboBox para seleccionar el género
        self.genero_hijos_combobox = ctk.CTkComboBox(label_frame_supe, 
            values=[genero.nombre for genero in self.genero_hijos_list], 
            command=self.on_combobox_genero, state="readonly")
        self.genero_hijos_combobox.grid(row=0, column=0, padx=20, pady=20)

        if self.genero_hijos_list:
            defaul_genero = self.genero_hijos_list[0].nombre
            self.genero_hijos_combobox.set(defaul_genero)
            self.selcted_genero_id = defaul_genero

        # DateEntry para seleccionar la fecha de nacimiento
        self.fecha_nacimiento_entry = DateEntry(label_frame_supe, date_pattern='dd/mm/yyyy')
        self.fecha_nacimiento_entry.grid(row=0, column=1, padx=20, pady=20)

        # Botón para agregar
        boton_guardar = ctk.CTkButton(label_frame_supe, text="Agregar", command=lambda: self.guardar_hijos(nueva_ventana))
        boton_guardar.grid(row=0, column=2, padx=20, pady=20)

        # Frame inferior para el Treeview
        self.tree_frame = ctk.CTkFrame(nueva_ventana)
        self.tree_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        # Treeview para mostrar los datos
        self.tree_hijo = ttk.Treeview(self.tree_frame, columns=("Género", "Fecha de Nacimiento","Edad"), show='headings')
        self.tree_hijo.heading("Género", text="Género")
        self.tree_hijo.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
        self.tree_hijo.heading("Edad", text="Edad")
        self.tree_hijo.pack(fill="both", expand=True)
        
        self.cargar_datos_en_treeview()



    def mostrar_ventana_principal(self, ventana):
        ventana.destroy()  # Cerrar la nueva ventana
        self.deiconify()   # Mostrar la ventana principal
        
        
    def guardar_hijos(self, nueva_ventana):
        # Obtener los valores del ComboBox y DateEntry
        genero = self.genero_hijos_combobox.get()
        fecha_nacimiento_str = self.fecha_nacimiento_entry.get()
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y').date() 
        fecha_actual = datetime.now().date() 
        edad = (fecha_actual - fecha_nacimiento).days//365
        # Guardar los datos en la lista
        self.datos_hijos.append((genero, fecha_nacimiento,edad))

        # Verificar si la ventana sigue abierta antes de intentar insertar datos
        if nueva_ventana.winfo_exists():
            # Insertar los datos en el Treeview
            self.tree_hijo.insert("", "end", values=(genero, fecha_nacimiento,edad))
        else:
            print("La ventana ya ha sido cerrada. No se pueden agregar datos.")

 
        
    def cargar_datos_en_treeview(self):
        # Limpiar el Treeview antes de cargar los datos
        for item in self.tree_hijo.get_children():
            self.tree_hijo.delete(item)

        # Cargar los datos guardados en el Treeview
        for dato in self.datos_hijos:
            self.tree_hijo.insert("", "end", values=dato)
    
    def actualizar_pers_regist(self):
        nombre = self.entry_nombre.get()
        observacion = self.entry_observacion.get()
        cadastrante=self.entry_cadastrante.get()
        email = self.email.get()
        datos_h = self.datos_hijos  # Datos de los hijos
        numro_identi = self.entry_ni.get()
        valor_genero=self.genero_combobox.get()
        genero = self.controller_genero.get_genero(valor_genero)
        telefono = self.entry_telefono.get()
        tipo_solicitud = self.tiposolicitud_combobox.get()
        valor_raza=self.raza_combobox.get()
        raza = self.controller_raza.get_raza(valor_raza)
        valor_benf_gob=self.ayuda_gob_combobox.get()
        benef_gob = self.contr_list_comb.opciones[valor_benf_gob]
        
        pais_ciudad = self.pais_ciudad_combobox.get()
        ciudad_brasil = self.ciudad_brasil_combobox.get()
        deficiencia = self.deficiencia_combobox.get()
        activ_econo = self.acti_econo_combobox.get()
        estado_civil = self.estado_civil_combobox.get()
        profec_oficio = self.profecion_ofic_combobox.get()
        uf_residen = self.uf_reside_combobox.get()
        renta_mensual = self.renta_mensual_combobox.get()
        etnia = self.etnia_combobox.get()
        situacion_laboral = self.situa_laboral_combobox.get()
        status_migrato = self.status_migra_combobox.get()
        valor_lgbt=self.lgbt_combobox.get()
        lgbt =self.contr_list_comb.opciones[valor_lgbt]
        nino_menores = self.ninos_menor_combobox.get()
        valor_cartera=self.cartera_trab_combobox.get()
        cartera_trabajo=self.contr_list_comb.opciones[valor_cartera]
        valor_pais=self.country_combobox.get()
        pais = self.controller_pais.get_pais(valor_pais)
        valor_nivelescolar=self.nivel_esco_combobox.get()
        nivelescolar = self.controller_nivelescolar.get_nivelescolar(valor_nivelescolar)
            
            # Procesar fechas
        fnacimiento = self.entry_fecha.get()
        fecha_nacimiento = datetime.strptime(fnacimiento, '%d/%m/%Y')
            
        fentrada_brasil = self.entry_fecha_brasil.get()
        fecha_llega_brasil = datetime.strptime(fentrada_brasil, '%d/%m/%Y')
        fecha_creacion = datetime.now()
          
        direccion = self.entry_direccion.get()
        
                
        
        self.controller_person.actualizar_pers_regist(self.id_person_global,
                nombre,observacion,cadastrante,email,numro_identi,genero.id,telefono,tipo_solicitud,
                raza.id,benef_gob,pais_ciudad,ciudad_brasil,deficiencia,activ_econo,estado_civil,
                profec_oficio,uf_residen,renta_mensual,etnia,situacion_laboral,status_migrato,lgbt,
                nino_menores,pais.id,nivelescolar.id,fecha_nacimiento,fecha_llega_brasil,direccion,
                cartera_trabajo
            )
        
        self.button_editar.configure(state='disabled')
        self.button_guardar.configure(state='normal')
        self.cargar_personas()
        self.limpiar_datos(pais)
         

    def guardar_persona(self):
        try:
            # Obtener datos de los campos de entrada
            nombre = self.entry_nombre.get()
            observacion = self.entry_observacion.get()
            cadastrante=self.entry_cadastrante.get()
            email = self.email.get()
            datos_h = self.datos_hijos  # Datos de los hijos
            numro_identi = self.entry_ni.get()
            genero = self.controller_genero.get_genero(self.selcted_genero_id)
            telefono = self.entry_telefono.get()
            tipo_solicitud = self.tiposolicitud_combobox.get()
            raza = self.controller_raza.get_raza(self.selcted_raza_id)
            benef_gob = self.selected_ayugob_id
            pais_ciudad = self.pais_ciudad_combobox.get()
            ciudad_brasil = self.ciudad_brasil_combobox.get()
            deficiencia = self.selected_deficiencia_nomb
            activ_econo = self.selected_actiecono_nomb
            estado_civil = self.selected_estcivil_nomb
            profec_oficio = self.profecion_ofic_combobox.get()
            uf_residen = self.uf_reside_combobox.get()
            renta_mensual = self.selected_rentames_nomb
            etnia = self.selected_etnia_nomb
            situacion_laboral = self.selected_situlaboral_nomb
            status_migrato = self.selected_statumigra_nomb
            lgbt = self.selected_lgbt_id
            cartera_trabajo=self.selected_cartera_id
            nino_menores = self.selected_ninomenor_nomb
            pais = self.controller_pais.get_pais(self.selected_value_id)
            nivelescolar = self.controller_nivelescolar.get_nivelescolar(self.selcted_nivel_id)
            
            
            
            # Procesar fechas
            fnacimiento = self.entry_fecha.get()
            fecha_nacimiento = datetime.strptime(fnacimiento, '%d/%m/%Y')
            
            fentrada_brasil = self.entry_fecha_brasil.get()
            fecha_llega_brasil = datetime.strptime(fentrada_brasil, '%d/%m/%Y')
            fecha_creacion = datetime.now()
            
            direccion = self.entry_direccion.get()
            if not (nombre and cadastrante and numro_identi):  # Verificar si el campo está vacío
                messagebox.showwarning("Advertencia", "Existen campos vacios")
                return  # Salir de la función si está vacío
            
            if pais_ciudad=="No hay registros":
                messagebox.showwarning("Advertencia", "Debe de escribir la ciudad")
                return  # Salir de la función si está vacío
                
            
            # Llamar al controlador para agregar la persona
            self.controller_person.agregar_persona(
                nombre, numro_identi, pais.id, fecha_nacimiento.date(),
                nivelescolar.id, direccion, email, telefono, genero.id,
                raza.id, benef_gob, lgbt, deficiencia, nino_menores, estado_civil,
                situacion_laboral, activ_econo, status_migrato, tipo_solicitud,
                renta_mensual, etnia, fecha_llega_brasil, ciudad_brasil,
                profec_oficio, observacion, uf_residen, pais_ciudad, fecha_creacion,
                datos_h,cadastrante,cartera_trabajo
            )

            self.limpiar_datos(pais)
            

            # Cargar personas en el Treeview, asegurándose de que la ventana y el Treeview existan
            if self.tree.winfo_exists():
                self.cargar_personas()
            else:
                print("La ventana que contiene el Treeview ha sido cerrada.")

        except Exception as e:
            print(f"Ocurrió un error al guardar la persona: {e}")
        
    def cargar_datseleccionados(self,event):        
        selected_item = self.tree.selection()  
        if selected_item: 
            selected_item = self.tree.selection()[0]
            valores = self.tree.item(selected_item, "values")
            self.datos_hijos=[]
            self.id_person_global=int (valores[0])
            self.entry_nombre.delete(0, ctk.END)
            self.entry_nombre.insert(0, valores[1])
            
            self.button_editar.configure(state='normal')
            self.button_guardar.configure(state='disabled')
            
            self.entry_telefono.delete(0, ctk.END)
            self.entry_telefono.insert(0, valores[5])
            
            self.entry_fecha.delete(0, ctk.END)
            self.entry_fecha.insert(0, valores[4])        
            
            self.entry_ni.delete(0, ctk.END)
            self.entry_ni.insert(0, valores[2]) 
            
            self.entry_direccion.delete(0, ctk.END)
            self.entry_direccion.insert(0, valores[6])
            
            self.genero_combobox.set(valores [8])
            
            self.raza_combobox.set(valores [9])
            self.etnia_combobox.set(valores [10])
            self.lgbt_combobox.set(valores [11])
            self.deficiencia_combobox.set(valores [12])
            self.ninos_menor_combobox.set(valores [13])
            self.estado_civil_combobox.set(valores [15])
            self.nivel_esco_combobox.set(valores [16])
            self.entry_fecha_brasil.delete(0, ctk.END)
            self.entry_fecha_brasil.insert(0, valores[17])         
            self.status_migra_combobox.set(valores [18])
            self.situa_laboral_combobox.set(valores [19])
            self.acti_econo_combobox.set(valores [20])
            self.ayuda_gob_combobox.set(valores [21])
            self.renta_mensual_combobox.set(valores [23])
            self.profecion_ofic_combobox.set(valores [24])
            self.tiposolicitud_combobox.set(valores [25])
            
            self.entry_observacion.delete(0, ctk.END)
            self.entry_observacion.insert(0, valores[26])
            
            self.entry_cadastrante.delete(0, ctk.END)
            self.entry_cadastrante.insert(0, valores[27])
            
            self.cartera_trab_combobox.set(valores[28])
            
            self.pais_ciudad_combobox.set(valores[29])
            
            
            self.email.delete(0, ctk.END)
            self.email.insert(0, valores[7])  
            
            ciudad_resid=valores[22]
            
            # Filtrar las opciones que coinciden con el texto
            opciones_filtradas = [opcion for opcion in self.nombre_ciudad_brasil if ciudad_resid.lower() in opcion.lower()]
        
            self.ciudad_brasil_combobox.configure(values=opciones_filtradas)    

            # Mantener el texto actual del ComboBoxopcion
            self.ciudad_brasil_combobox.set(ciudad_resid)
            
            #self.country_combobox.delete(0, tk.END)
            self.country_combobox.set(valores[3])
            country=valores[3]
            # Filtrar las opciones que coinciden con el textotexto
            opciones_filtradas = [opcion_count for opcion_count in self.nombre_pais_naci if country.lower() in opcion_count.lower()]
        
            self.country_combobox.configure(values=opciones_filtradas)    

            # Mantener el texto actual del ComboBox
            self.country_combobox.set(country)
            
            # Obtener la fecha actual
            fecha_actual = datetime.now().date() 
            lista_hijos=self.controller_hijosmenores.listar_hijosmenores(self.id_person_global)
            for tiposolicitud in lista_hijos:
                # Convertir la fecha de nacimiento a un objeto datetime
                fecha_nacimiento = tiposolicitud.fecha_nacimiento
                
                # Calcular la edad
                edad = (fecha_actual - fecha_nacimiento).days // 365
                
                # Agregar los datos a la lista
                self.datos_hijos.append((tiposolicitud.genero, tiposolicitud.fecha_nacimiento, edad))
        
       
    def autocompletar(self, event):
        # Obtener el texto actual del ComboBox
        texto = self.ciudad_brasil_combobox.get()
        #print(f"Texto actual: {texto}")
        
        # Solo proceder si el texto tiene 5 o más caracteres
        if len(texto) < 3:
            self.ciudad_brasil_combobox['values'] = self.nombre_ciudad_brasil  # Restablecer a la lista completa
            #print("Restableciendo la lista completa")
            return

        # Filtrar las opciones que coinciden con el texto
        opciones_filtradas = [opcion for opcion in self.nombre_ciudad_brasil if texto.lower() in opcion.lower()]
       
        self.ciudad_brasil_combobox.configure(values=opciones_filtradas)    

        # Mantener el texto actual del ComboBox
        self.ciudad_brasil_combobox.set(texto)

        # Mostrar el menú desplegable si hay opciones filtradas
        if opciones_filtradas:
            self.ciudad_brasil_combobox.focus_set()
            self.ciudad_brasil_combobox.event_generate('<Down>')  # Abre el menú desplegable
            #print("Desplegando las opciones")
            
            
    def autocompletar_pais(self, event):
        # Obtener el texto actual del ComboBox
        texto = self.country_combobox.get()
        #print(f"Texto actual: {texto}")

        # Solo proceder si el texto tiene 5 o más caracteres
        if len(texto) < 3:
            self.country_combobox['values'] = self.nombre_pais_naci  # Restablecer a la lista completa
            #print("Restableciendo la lista completa")
            return

        # Filtrar las opciones que coinciden con el texto
        opciones_filtradas = [opcion for opcion in self.nombre_pais_naci if texto.lower() in opcion.lower()]
       
        self.country_combobox.configure(values=opciones_filtradas)    

        # Mantener el texto actual del ComboBox
        self.country_combobox.set(texto)

        # Mostrar el menú desplegable si hay opciones filtradas
        if opciones_filtradas:
            self.country_combobox.focus_set()
            self.country_combobox.event_generate('<Down>')  # Abre el menú desplegable

    def descrip_combo_entry(self):
    
        # Creamos un tooltip para el ComboBox
        Tooltip(self.ayuda_gob_combobox, "Ayuda del gobierno")              
        Tooltip(self.entry_fecha, "Fecha de nacimiento")        
        Tooltip(self.lgbt_combobox, "LGBTQIAPN+")        
        Tooltip(self.entry_fecha_brasil,"Fecha de llegada a Brasil")        
        Tooltip(self.country_combobox,"Pais")        
        Tooltip(self.profecion_ofic_combobox,"Profecion u oficio")        
        Tooltip(self.tiposolicitud_combobox, "Tipo de solicitud")        
        Tooltip(self.pais_ciudad_combobox,"Ciudad de nacimiento")        
        Tooltip(self.nivel_esco_combobox,"Escolaridade")        
        Tooltip(self.raza_combobox,"Color de Piel")        
        Tooltip(self.deficiencia_combobox,"Deficiencia")        
        Tooltip(self.ninos_menor_combobox,"Hijos menores de edad")
        Tooltip(self.estado_civil_combobox,"Estado Civil")
        Tooltip(self.situa_laboral_combobox,"Situaicion Laboral")
        Tooltip(self.acti_econo_combobox,"Actividad economica")
        Tooltip(self.status_migra_combobox,"Status Migratorio")
        Tooltip(self.cartera_trab_combobox,"Carteira de Trabalho")
        Tooltip(self.ciudad_brasil_combobox,"Cidade de Residência do Migrante")
        Tooltip(self.renta_mensual_combobox,"Renda Familiar Mensal")
        Tooltip(self.entry_nombre,"Nombre y Apellidos")
        Tooltip(self.entry_ni,"CPF o numero identificativo")
        Tooltip(self.entry_telefono,"Numero de telefono")
        Tooltip(self.email,"Correo o Email")
        
        
        
    
    def limpiar_datos(self,pais):
        # Limpiar los campos de entrada
            self.entry_nombre.delete(0, ctk.END)
            self.entry_telefono.delete(0, ctk.END)
            #self.entry_direccion.delete(0, ctk.END)
            self.entry_observacion.delete(0, ctk.END)
            self.email.delete(0, ctk.END)
            self.entry_ni.delete(0, ctk.END)

            # Reiniciar la lista de datos de hijos
            self.datos_hijos = []            
            
            # Actualizar los ComboBoxes
            nueva_lista_soli = self.controller_tiposolicitud.listar_tiposolicitud()
            nueva_lista_prof = self.controller_profeoficio.listar_profeoficio()
            nueva_lista_ciupas=self.controller_paisciudad.get_id_pais(pais.id)
            self.tiposolicitud_combobox.configure(values=[tiposolicitud.nombre for tiposolicitud in nueva_lista_soli])
            self.profecion_ofic_combobox.configure(values=[profecoficio.nombre for profecoficio in nueva_lista_prof])
            self.pais_ciudad_combobox.configure(values=[ciudad.nombre for ciudad in nueva_lista_ciupas])

    
    def select_combobox_txt(self, event):
        """Selecciona todo el texto cuando el combobox recibe el foco"""
        combo_widget = event.widget
    
        # Selecciona todo el texto
        combo_widget.select_range(0, 'end')
        return "break"
    
    
    def opcion_ciudad_pais(self,nomb_pais):
        id_paises=self.controller_pais.get_pais(nomb_pais)
        
        select_porid = self.controller_paisciudad.get_id_pais(id_paises.id)
        
        # Configurar los valores del Combobox
        pais_ciudad_nombres = [paisciudad.nombre for paisciudad in select_porid]
        if pais_ciudad_nombres:
            self.pais_ciudad_combobox.configure(values=pais_ciudad_nombres)
            self.pais_ciudad_combobox.set(pais_ciudad_nombres[0])     
        else:
            self.pais_ciudad_combobox.configure(values=["No hay registros"])
            self.pais_ciudad_combobox.set("No hay registros")