from sqlalchemy import desc
from modelo.model_persona import Persona
from modelo.model_registro import Registro
from modelo.model_tipo_solicitud import Tipo_Solicitud
from modelo.model_profec_ofic import Profec_Ofici
from modelo.model_pais_ciudad import Pais_Ciudad
from modelo.model_hijos_menor import Hijo

from model import session
from datetime import datetime



class Controller_Perona:
    def __init__(self):
        self.session = session    
        #self.fecha_creacion=datetime.now()
    def agregar_persona(self, nombre_apellido,ni,pais_id,fecha_nacim,nivel_escol_id,direccion,
                        email,telefono,genero_id,raza_id,benf_gob,lgbt,deficiencia,nino_menor,
                        estado_civil,situa_laboral,activ_econo,status_migrat,tipo_solicitud,
                        renta_mens,etnia,fecha_llega_brasil,ciudad_resid_brasil,profec_oficio,observacion,
                        uf_residen,pais_ciudad,fecha_creacion,datos_h, cadastrante,cartera_trabajo):
        self.fecha_creacion=fecha_creacion
        #fecha_creacion=datetime.now()
        # Verificar si la persona ya existe
        cadastrante=cadastrante.upper()
        tipo_solicitud=tipo_solicitud.upper()
        profec_oficio=profec_oficio.upper()
        pais_ciudad=pais_ciudad.strip().upper()
        
        persona_existente = self.session.query(Persona).filter(
            Persona.nombre_apellido == nombre_apellido.title(),
            Persona.pais_id == pais_id,
            Persona.fecha_nacimiento == fecha_nacim,
            Persona.ciudad_person == pais_ciudad
        ).first()
        
       
        existing_tiposolicitud = self.session.query(Tipo_Solicitud).filter_by(nombre=tipo_solicitud).first()
        if not existing_tiposolicitud:
            nuevo_tiposolicitud = Tipo_Solicitud(nombre=tipo_solicitud)
            self.session.add(nuevo_tiposolicitud)
            self.session.commit()
            
        existing_profeoficio = self.session.query(Profec_Ofici).filter_by(nombre=profec_oficio).first()
        if not existing_profeoficio:
            nuevo_tiposolicitud = Profec_Ofici(nombre=profec_oficio)
            self.session.add(nuevo_tiposolicitud)
            self.session.commit()
        
        existing_paisciudad = self.session.query(Pais_Ciudad).filter_by(nombre=pais_ciudad,pais_id=pais_id).first()
        if not existing_paisciudad:
            nuevo_paisciudad = Pais_Ciudad(nombre=pais_ciudad,pais_id=pais_id)
            
            self.session.add(nuevo_paisciudad)
            self.session.commit()
        
        
        
        if persona_existente:
        # Si la persona existe, agregar el nuevo registro
            nuevo_registro = Registro(
            direccion=direccion,
            num_ident=ni,
            fecha_creacion=self.fecha_creacion,
            telefono=telefono,
            email=email,
            beneficio_gobierno=benf_gob,
            lgbtqiapn=lgbt,
            deficiencia=deficiencia,
            nino_menor=nino_menor,
            estado_civil=estado_civil,
            situa_laboral=situa_laboral,
            activ_econo=activ_econo,
            status_migrat=status_migrat,
            tipo_solicitud=tipo_solicitud,
            renta_mens=renta_mens,
            etnia=etnia,
            ciudad_resid_brasil=ciudad_resid_brasil,
            profec_oficio=profec_oficio,
            observacion=observacion,
            uf_residen=uf_residen,
            cadastrante=cadastrante,
            cartera_trabajo=cartera_trabajo
        
        )
            
            persona_existente.registros.append(nuevo_registro)
        else:
        # Si no existe, crear una nueva persona
            nueva_persona = Persona(
            nombre_apellido=nombre_apellido.title(),
            pais_id=pais_id,
            fecha_creacion=self.fecha_creacion,
            fecha_nacimiento=fecha_nacim,
            fecha_llegada=fecha_llega_brasil,
            nivel_escol_id=nivel_escol_id,
            genero_id=genero_id,
            raza_id=raza_id,
            ciudad_person=pais_ciudad
        )
        
            nuevo_registro = Registro(
            direccion=direccion,
            num_ident=ni,
            fecha_creacion=self.fecha_creacion,
            telefono=telefono,
            email=email,
            beneficio_gobierno=benf_gob,
            lgbtqiapn=lgbt,
            deficiencia=deficiencia,
            nino_menor=nino_menor,
            estado_civil=estado_civil,
            situa_laboral=situa_laboral,
            activ_econo=activ_econo,
            status_migrat=status_migrat,
            tipo_solicitud=tipo_solicitud,
            renta_mens=renta_mens,
            etnia=etnia,
            ciudad_resid_brasil=ciudad_resid_brasil,
            profec_oficio=profec_oficio,
            observacion=observacion,
            uf_residen=uf_residen,
            cadastrante=cadastrante,
            cartera_trabajo=cartera_trabajo
            
            
        )
            for list_hijos in datos_h:   
                fecha_nacimiento=list_hijos[1]
                #fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y').date()          
                nuevo_hijos=Hijo( genero=list_hijos[0], fecha_nacimiento=fecha_nacimiento)
                nueva_persona.hijos.append(nuevo_hijos)
                
            nueva_persona.registros.append(nuevo_registro)
        
            self.session.add(nueva_persona)
        self.session.commit()
        
        
    def listar(self):
        return self.session.query(Persona).order_by(desc(Persona.id)).all()
    
    
    def listar_person_id(self,id_person):
        return self.session.query(Persona).filter(Persona.id==id_person).order_by(desc(Persona.id)).all()


    def listar_fecha(self):
        fecha_creacion=datetime.now()
        start_of_day = datetime(fecha_creacion.year, fecha_creacion.month, fecha_creacion.day)
        return self.session.query(Persona).filter(Persona.fecha_creacion>=start_of_day).order_by(desc(Persona.id)).all()
    
    def actualizar_pers_regist(self,id_persona,nuevo_nombre,nueva_observa,cadastrante,email,numro_identi,
                               genero_id,telefono,tipo_solicitud,raza_id,benef_gob,pais_ciudad,
                               ciudad_brasil,deficiencia,activ_econo,estado_civil,profec_oficio,
                               uf_residen,renta_mensual,etnia,situacion_laboral,status_migrato,
                               lgbt,nino_menores,pais_id,nivel_escolar_id,fecha_nacimiento,
                               fecha_llega_brasil,direccion,cartera_trabajo):
        personas= self.session.query(Persona).filter_by(id=id_persona).first()
        registro=self.session.query(Registro).filter_by(persona_id=id_persona).order_by(desc(Registro.id)).first()
        
        personas.nombre_apellido=nuevo_nombre.title()
        personas.genero_id=genero_id
        personas.raza_id=raza_id
        personas.ciudad_person=pais_ciudad.strip().upper()
        personas.pais_id=pais_id
        personas.nivel_escol_id=nivel_escolar_id
        personas.fecha_nacimiento=fecha_nacimiento
        personas.fecha_llegada=fecha_llega_brasil
        
        registro.observacion=nueva_observa
        registro.cadastrante=cadastrante
        registro.email=email
        registro.num_ident=numro_identi
        registro.telefono=telefono
        registro.tipo_solicitud=tipo_solicitud
        registro.beneficio_gobierno=benef_gob
        registro.ciudad_resid_brasil=ciudad_brasil
        registro.deficiencia=deficiencia
        registro.activ_econo=activ_econo
        registro.estado_civil=estado_civil
        registro.profec_oficio=profec_oficio
        registro.uf_residen=uf_residen
        registro.renta_mens=renta_mensual
        registro.etnia=etnia
        registro.situa_laboral=situacion_laboral
        registro.status_migrat=status_migrato
        registro.lgbtqiapn=lgbt
        registro.nino_menor=nino_menores
        registro.direccion=direccion
        registro.cartera_trabajo=cartera_trabajo
        
        self.session.commit()