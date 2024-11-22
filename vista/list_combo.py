class Lista_combobox:
    def __init__(self):
        
        self.opciones = {
            "Sim": 1,
            "Não": 0
        }
     #   
        self.deficiencia = {
            "Não tem": 1,
            "Visual": 2,
            "Auditiva": 3,
            "Vocal": 4,
            "Mental": 5,
            "Física": 6,            
            "Múltipla": 7,
            "Outra": 8
        }
        
        self.ninos_menor={
            "0":1,
            "1":2,
            "2":3,
            "3 ou mais":4
        }
        
        self.estado_civil={
            "Solteiro":1,
            "Casado ou União Estável":2,
            "Viúvo":3,
            "Divorciado ou Separado":4
        }
        
        self.situa_laboral={
            "Aposentado":1,
            "Desempregado":2,
            "Trabalhando Formalmente":3,
            "Trabalhando Informalmente":4,
            "Empreendedor Formalizado (MEI ou Empresa)":5,
            "Empreendedor Informal":6

        }
        
        self.actividad_econo = {
    "Administração pública, defesa e seguridade social": 1,
    "Agricultura, pecuária, produção florestal, pesca e aqüicultura": 2,
    "Água, esgoto, atividades de gestão de resíduos e descontaminação": 3,
    "Alojamento e alimentação": 4,
    "Artes, cultura, esporte e recreação": 5,
    "Atividades administrativas e serviços complementares": 6,
    "Atividades financeiras, de seguros e serviços relacionados": 7,
    "Atividades imobiliárias": 8,
    "Atividades profissionais, científicas e técnicas": 9,
    "Comércio; reparação de veículos automotores e motocicletas": 10,
    "Construção": 11,
    "Economia Verde": 12,
    "Educação": 13,
    "Eletricidade e gás": 14,
    "Indústrias de transformação": 15,
    "Indústrias extrativas": 16,
    "Informação e comunicação": 17,
    "Organismos internacionais e outras instituições extraterritoriais": 18,
    "Outras atividades de serviços": 19,
    "Saúde humana e serviços sociais": 20,
    "Serviços domésticos": 21,
    "Transporte, armazenagem e correio": 22,
    "NO TIENE":23
}
        
        self.status_migr = {
    "Indocumentado":1,
    "Visto de Turismo":2,
    "Solicitação de Residência":3,
    "Residência Temporária":4,
    "Residência Permanente":5,
    "Solicitação de Refúgio":6,
    "Refugiado":7,
    "Outro":8
}
        
        
        self.renta_mes = {
    "Não quis informar":1,
"De R$ 0,01 a R$ 710,50":2,
"De R$ 711,00 a R$ 1.421,00":3,
"De 1.422,00 a R$ 2.842,00":4,
"Acima de R$ 2.842,00":5

}
        
        self.etnia={
            "Warao":1,
            "Pemón":2,
            "Ka'riña":3,
            "E'ñepá":4,
            "Outra não nacional":5,
            "Outra etnia brasileira":6            
        }
        
        self.uf_residen={
            "PR":1
                      
        }
        
        
    def retorn_opcion(self,selct_opcion):
        if selct_opcion==True:
            return "Sim"
        else:
            return "Não"
        
    def format_fecha(self,cargar_fecha):
        return cargar_fecha.strftime('%d/%m/%Y')
    
    