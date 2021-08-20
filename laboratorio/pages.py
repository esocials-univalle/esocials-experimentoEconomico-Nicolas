from logging import setLoggerClass
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
# Trabajar con fechas utilizando Python haremos uso de la librería datetime
from datetime import datetime, date, timedelta
import pytz
#
import difflib
from difflib import Differ

import math


class ConsentimientoInformado(Page):

    def is_displayed(self):
        zona_horaria = datetime.now(pytz.timezone('America/Bogota'))
        fecha_actual = zona_horaria.date()
        print(fecha_actual)
        return self.round_number == 1

    def before_next_page(self):
        self.player.set_treatment()
        self.player.get_time()
        print('======================')
        print(self.player.start_date)
        print(self.player.next_date)
        print(self.player.date_after_next)
        print(self.player.date_after_after_next)
        print('======================')

    form_model = 'player'
    form_fields = ['consentimiento']


class Instrucciones(Page):

    def is_displayed(self):
        print("============================")
        print(self.player.in_round(1).treatment)
        print("============================")
        return self.round_number == 2


class Contrato_formal_fijo(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_formal_fijo and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_formal_indefinido(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_formal_indefinido and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_formal_servicios(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_formal_servicios and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_informal_fijo(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_informal_fijo and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_informal_indefinido(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_informal_indefinido and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Contrato_informal_servicios(Page):
    def is_displayed(self):
        return self.player.in_round(1).treatment == Constants.contrato_informal_servicios and self.round_number == 2

    form_model = 'player'
    form_fields = ['terminos_actividad']


class Instrucciones_actividad(Page):
    def is_displayed(self):
        return self.round_number == 3


class Identificacion(Page):
    def is_displayed(self):
        return self.round_number == 3

    form_model = 'player'
    form_fields = ['codigo', 'confirmacion_codigo']

    def error_message(self, values):
        print('values is', values)
        if values['codigo'] != values['confirmacion_codigo']:
            return 'El código y la verificación del código no coinciden'


class Ronda_1(Page):

    timeout_seconds = 180

    def is_displayed(self):
        return self.round_number > 2 and self.round_number < Constants.num_rounds

    def vars_for_template(self):

        titulo = ''
        texto_original = ""
        texto_alternativo = ""

        if self.round_number >= 3 and self.round_number <= 9:
            titulo = 'Mercados de energía'
        elif self.round_number >= 10 and self.round_number <= 16:
            titulo = 'Ecoturismo'
        elif self.round_number >= 17 and self.round_number <= 23:
            titulo = 'Espacio'

        if self.round_number == 3:
            texto_original = Constants.textoOriginal1
            texto_alternativo = Constants.textoAlternativo1
        elif self.round_number == 4:
            texto_original = Constants.textoOriginal2
            texto_alternativo = Constants.textoAlternativo2
        elif self.round_number == 5:
            texto_original = Constants.textoOriginal3
            texto_alternativo = Constants.textoAlternativo3
        elif self.round_number == 6:
            texto_original = Constants.textoOriginal4
            texto_alternativo = Constants.textoAlternativo4
        elif self.round_number == 7:
            texto_original = Constants.textoOriginal5
            texto_alternativo = Constants.textoAlternativo5
        elif self.round_number == 8:
            texto_original = Constants.textoOriginal6
            texto_alternativo = Constants.textoAlternativo6
        elif self.round_number == 9:
            texto_original = Constants.textoOriginal7
            texto_alternativo = Constants.textoAlternativo7

        elif self.round_number == 10:
            texto_original = Constants.textoOriginal8
            texto_alternativo = Constants.textoAlternativo8
        elif self.round_number == 11:
            texto_original = Constants.textoOriginal9
            texto_alternativo = Constants.textoAlternativo9
        elif self.round_number == 12:
            texto_original = Constants.textoOriginal10
            texto_alternativo = Constants.textoAlternativo10
        elif self.round_number == 13:
            texto_original = Constants.textoOriginal11
            texto_alternativo = Constants.textoAlternativo11
        elif self.round_number == 14:
            texto_original = Constants.textoOriginal12
            texto_alternativo = Constants.textoAlternativo12
        elif self.round_number == 15:
            texto_original = Constants.textoOriginal13
            texto_alternativo = Constants.textoAlternativo13
        elif self.round_number == 16:
            texto_original = Constants.textoOriginal14
            texto_alternativo = Constants.textoAlternativo14

        elif self.round_number == 17:
            texto_original = Constants.textoOriginal15
            texto_alternativo = Constants.textoAlternativo15
        elif self.round_number == 18:
            texto_original = Constants.textoOriginal16
            texto_alternativo = Constants.textoAlternativo16
        elif self.round_number == 19:
            texto_original = Constants.textoOriginal17
            texto_alternativo = Constants.textoAlternativo17
        elif self.round_number == 20:
            texto_original = Constants.textoOriginal18
            texto_alternativo = Constants.textoAlternativo18
        elif self.round_number == 21:
            texto_original = Constants.textoOriginal19
            texto_alternativo = Constants.textoAlternativo19
        elif self.round_number == 22:
            texto_original = Constants.textoOriginal20
            texto_alternativo = Constants.textoAlternativo20
        elif self.round_number == 23:
            texto_original = Constants.textoOriginal21
            texto_alternativo = Constants.textoAlternativo21

        return {
            "titulo": titulo,
            "texto_original": texto_original,
            "texto_alternativo": texto_alternativo,
            "ronda": self.round_number - 2,
        }

    def before_next_page(self):

        if self.player.in_round(1).treatment == Constants.contrato_formal_servicios or self.player.in_round(1).treatment == Constants.contrato_informal_servicios:
            print("calcular pago prestacion por servicios")

            erroresReportados = 0
            erroresReales = 0

            if self.round_number == 3:
                erroresReportados = self.player.erroresTexto1
                erroresReales = Constants.NumeroErrores1
            elif self.round_number == 4:
                erroresReportados = self.player.erroresTexto2
                erroresReales = Constants.NumeroErrores2
            elif self.round_number == 5:
                erroresReportados = self.player.erroresTexto3
                erroresReales = Constants.NumeroErrores3
            elif self.round_number == 6:
                erroresReportados = self.player.erroresTexto4
                erroresReales = Constants.NumeroErrores4
            elif self.round_number == 7:
                erroresReportados = self.player.erroresTexto5
                erroresReales = Constants.NumeroErrores5
            elif self.round_number == 8:
                erroresReportados = self.player.erroresTexto6
                erroresReales = Constants.NumeroErrores6
            elif self.round_number == 9:
                erroresReportados = self.player.erroresTexto7
                erroresReales = Constants.NumeroErrores7
            elif self.round_number == 10:
                erroresReportados = self.player.erroresTexto8
                erroresReales = Constants.NumeroErrores8
            elif self.round_number == 11:
                erroresReportados = self.player.erroresTexto9
                erroresReales = Constants.NumeroErrores9
            elif self.round_number == 12:
                erroresReportados = self.player.erroresTexto10
                erroresReales = Constants.NumeroErrores10
            elif self.round_number == 13:
                erroresReportados = self.player.erroresTexto11
                erroresReales = Constants.NumeroErrores11
            elif self.round_number == 14:
                erroresReportados = self.player.erroresTexto12
                erroresReales = Constants.NumeroErrores12
            elif self.round_number == 15:
                erroresReportados = self.player.erroresTexto13
                erroresReales = Constants.NumeroErrores13
            elif self.round_number == 16:
                erroresReportados = self.player.erroresTexto14
                erroresReales = Constants.NumeroErrores14
            elif self.round_number == 17:
                erroresReportados = self.player.erroresTexto15
                erroresReales = Constants.NumeroErrores15
            elif self.round_number == 18:
                erroresReportados = self.player.erroresTexto16
                erroresReales = Constants.NumeroErrores16
            elif self.round_number == 19:
                erroresReportados = self.player.erroresTexto17
                erroresReales = Constants.NumeroErrores17
            elif self.round_number == 20:
                erroresReportados = self.player.erroresTexto18
                erroresReales = Constants.NumeroErrores18
            elif self.round_number == 21:
                erroresReportados = self.player.erroresTexto19
                erroresReales = Constants.NumeroErrores19
            elif self.round_number == 22:
                erroresReportados = self.player.erroresTexto20
                erroresReales = Constants.NumeroErrores20
            elif self.round_number == 23:
                erroresReportados = self.player.erroresTexto21
                erroresReales = Constants.NumeroErrores21

            if erroresReportados >= erroresReales-2 and erroresReportados <= erroresReales+2:
                self.player.payoff += c(1000)

            # if porcentaje > Constants.porcentaje_similitud:
            #     self.player.payoff += c(1750)
        else:
            self.player.payoff += c(1000)
        print(self.player.payoff)

    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['erroresTexto1']
        elif self.round_number == 4:
            return ['erroresTexto2']
        elif self.round_number == 5:
            return ['erroresTexto3']
        elif self.round_number == 6:
            return ['erroresTexto4']
        elif self.round_number == 7:
            return ['erroresTexto5']
        elif self.round_number == 8:
            return ['erroresTexto6']
        elif self.round_number == 9:
            return ['erroresTexto7']
        elif self.round_number == 10:
            return ['erroresTexto8']
        elif self.round_number == 11:
            return ['erroresTexto9']
        elif self.round_number == 12:
            return ['erroresTexto10']
        elif self.round_number == 13:
            return ['erroresTexto11']
        elif self.round_number == 14:
            return ['erroresTexto12']
        elif self.round_number == 15:
            return ['erroresTexto13']
        elif self.round_number == 16:
            return ['erroresTexto14']
        elif self.round_number == 17:
            return ['erroresTexto15']
        elif self.round_number == 18:
            return ['erroresTexto16']
        elif self.round_number == 19:
            return ['erroresTexto17']
        elif self.round_number == 20:
            return ['erroresTexto18']
        elif self.round_number == 21:
            return ['erroresTexto19']
        elif self.round_number == 22:
            return ['erroresTexto20']
        elif self.round_number == 23:
            return ['erroresTexto21']


class Results(Page):
    def is_displayed(self):
        return self.round_number > 2 and self.round_number < Constants.num_rounds

    def vars_for_template(self):

        erroresReportados = 0
        erroresReales = 0

        if self.round_number == 3:
            erroresReportados = self.player.erroresTexto1
            erroresReales = Constants.NumeroErrores1
        elif self.round_number == 4:
            erroresReportados = self.player.erroresTexto2
            erroresReales = Constants.NumeroErrores2
        elif self.round_number == 5:
            erroresReportados = self.player.erroresTexto3
            erroresReales = Constants.NumeroErrores3
        elif self.round_number == 6:
            erroresReportados = self.player.erroresTexto4
            erroresReales = Constants.NumeroErrores4
        elif self.round_number == 7:
            erroresReportados = self.player.erroresTexto5
            erroresReales = Constants.NumeroErrores5
        elif self.round_number == 8:
            erroresReportados = self.player.erroresTexto6
            erroresReales = Constants.NumeroErrores6
        elif self.round_number == 9:
            erroresReportados = self.player.erroresTexto7
            erroresReales = Constants.NumeroErrores7
        elif self.round_number == 10:
            erroresReportados = self.player.erroresTexto8
            erroresReales = Constants.NumeroErrores8
        elif self.round_number == 11:
            erroresReportados = self.player.erroresTexto9
            erroresReales = Constants.NumeroErrores9
        elif self.round_number == 12:
            erroresReportados = self.player.erroresTexto10
            erroresReales = Constants.NumeroErrores10
        elif self.round_number == 13:
            erroresReportados = self.player.erroresTexto11
            erroresReales = Constants.NumeroErrores11
        elif self.round_number == 14:
            erroresReportados = self.player.erroresTexto12
            erroresReales = Constants.NumeroErrores12
        elif self.round_number == 15:
            erroresReportados = self.player.erroresTexto13
            erroresReales = Constants.NumeroErrores13
        elif self.round_number == 16:
            erroresReportados = self.player.erroresTexto14
            erroresReales = Constants.NumeroErrores14
        elif self.round_number == 17:
            erroresReportados = self.player.erroresTexto15
            erroresReales = Constants.NumeroErrores15
        elif self.round_number == 18:
            erroresReportados = self.player.erroresTexto16
            erroresReales = Constants.NumeroErrores16
        elif self.round_number == 19:
            erroresReportados = self.player.erroresTexto17
            erroresReales = Constants.NumeroErrores17
        elif self.round_number == 20:
            erroresReportados = self.player.erroresTexto18
            erroresReales = Constants.NumeroErrores18
        elif self.round_number == 21:
            erroresReportados = self.player.erroresTexto19
            erroresReales = Constants.NumeroErrores19
        elif self.round_number == 22:
            erroresReportados = self.player.erroresTexto20
            erroresReales = Constants.NumeroErrores20
        elif self.round_number == 23:
            erroresReportados = self.player.erroresTexto21
            erroresReales = Constants.NumeroErrores21



        return {
            # "por": self.player.porcentaje1,
            # "porcentaje": porcentaje,
            "erroresReportados": erroresReportados,
            "erroresReales": erroresReales,
            "ronda": self.round_number,
        }


class Pago(Page):

    def is_displayed(self):

        if self.round_number == 9:
            return True
        if self.round_number == 16:
            return True
        if self.round_number == 23:
            return True


    def vars_for_template(self):

        pagoSesion = 0

        if self.round_number == 9:
            self.player.pagoSesion1 = self.player.in_round(3).payoff + self.player.in_round(4).payoff + self.player.in_round(5).payoff + self.player.in_round(6).payoff + self.player.in_round(7).payoff + self.player.in_round(8).payoff + self.player.in_round(9).payoff
            pagoSesion = self.player.pagoSesion1
        elif self.round_number == 16:
            self.player.pagoSesion2 = self.player.in_round(10).payoff + self.player.in_round(11).payoff + self.player.in_round(12).payoff + self.player.in_round(13).payoff + self.player.in_round(14).payoff + self.player.in_round(15).payoff + self.player.in_round(16).payoff
            pagoSesion = self.player.pagoSesion2
        elif self.round_number == 23:
            self.player.pagoSesion3 = self.player.in_round(17).payoff + self.player.in_round(18).payoff + self.player.in_round(19).payoff + self.player.in_round(20).payoff + self.player.in_round(21).payoff + self.player.in_round(22).payoff + self.player.in_round(23).payoff
            pagoSesion = self.player.pagoSesion3
        return {
            "pagoSesion": pagoSesion, 
        }     


class Articulos(Page):
    def is_displayed(self):
        if self.round_number == 9:
            return True
        if self.round_number == 16:
            return True
        if self.round_number == 23:
            return True

    def js_vars(self):
        pagoSesion = 0
        if self.round_number == 9:
            pagoSesion = self.player.pagoSesion1
        elif self.round_number == 16:
            pagoSesion = self.player.pagoSesion2
        elif self.round_number == 23:
            pagoSesion = self.player.pagoSesion3
        return dict(
            payoff=pagoSesion,
        )

    def vars_for_template(self):
        pagoSesion = 0
        if self.round_number == 9:
            pagoSesion = self.player.pagoSesion1
        elif self.round_number == 16:
            pagoSesion = self.player.pagoSesion2
        elif self.round_number == 23:
            pagoSesion = self.player.pagoSesion3
        return {
            "pagoSesion": pagoSesion,
        }

    form_model = 'player'
    form_fields = [
        'productos_alimentos',
        'productos_snack',
        'productos_aseo',
        'productos_electronicos',
        'productos_servicios',
        'productos_transporte',
        'productos_diversion',
        'productos_ahorro',
        'productos_deudas',
        'total',
    ]


class DateWaitPage(Page):

    def is_displayed(self):
        if self.round_number == 9:
            return True
        if self.round_number == 16:
            return True
        if self.round_number == 23:
            return True

    # Pasando datos de Python a JavaScript
    def js_vars(self):
        fecha = ""
        if self.round_number == 9:
            fecha = self.player.in_round(1).next_date
        if self.round_number == 16:
            fecha = self.player.in_round(1).date_after_next
        if self.round_number == 23:
            fecha = self.player.in_round(1).date_after_after_next
        return dict(
            fecha_espera=fecha,
            # payoff=self.player.payoff,
        )

    def vars_for_template(self):

        # Pasar datos entre rondas
        print('======================')
        print(self.player.in_round(1).start_date)
        print(self.player.in_round(1).next_date)
        print(self.player.in_round(1).date_after_next)
        print(self.player.in_round(1).date_after_after_next)
        print('======================')

        fecha = ""
        if self.round_number == 9:
            fecha = self.player.in_round(1).next_date
            date_time_obj = datetime.strptime(fecha, '%Y-%m-%d')
        if self.round_number == 16:
            fecha = self.player.in_round(1).date_after_next
            date_time_obj = datetime.strptime(fecha, '%Y-%m-%d')
        if self.round_number == 23:
            fecha = self.player.in_round(1).date_after_after_next
            date_time_obj = datetime.strptime(fecha, '%Y-%m-%d')

        return {
            "date_time_obj": date_time_obj.date(),
        }


class ArticulosPost(Page):
    def is_displayed(self):
        if self.round_number == 9:
            return True
        if self.round_number == 16:
            return True
        if self.round_number == 23:
            return True

    def js_vars(self):
        pagoSesion = 0
        if self.round_number == 9:
            pagoSesion = self.player.pagoSesion1
        elif self.round_number == 16:
            pagoSesion = self.player.pagoSesion2
        elif self.round_number == 23:
            pagoSesion = self.player.pagoSesion3
        return dict(
            payoff=pagoSesion,
        )

    def vars_for_template(self):
        pagoSesion = 0
        if self.round_number == 9:
            pagoSesion = self.player.pagoSesion1
        elif self.round_number == 16:
            pagoSesion = self.player.pagoSesion2
        elif self.round_number == 23:
            pagoSesion = self.player.pagoSesion3
        return {
            "pagoSesion": pagoSesion,
        }

    form_model = 'player'
    form_fields = [

        'productos_post_alimentos',
        'productos_post_snack',
        'productos_post_aseo',
        'productos_post_electronicos',
        'productos_post_servicios',
        'productos_post_transporte',
        'productos_post_diversion',
        'productos_post_ahorro',
        'productos_post_deudas',
        'total_post',

    ]


class Test(Page):

    live_method = 'live_test'

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['actividad_2']


class Encuesta(Page):

    def is_displayed(self):
        return self.round_number == 9

    form_model = 'player'
    form_fields = [
        'edad',
        'ciudad',
        'sexo',
        'estrato',
        'estado_civil',
        'hijos',
        'etnia',
        'religion',
        'estudios',
        'actividad_actual',
        'esta_laborando',
        'ingreso_mensual',
        'gasto_mensual',
        'alimentos',
        'aseo',
        'electronicos',
        'transporte',
        'servicios',
        'diversion',
        'ahorro',
        'deudas',
        'offer_1',
        'Estabilidad',
        'Independencia',
        'Descanso',
        'Lucro',
        'Protección',
        'encuesta_tabla1_pregunta1',
        'encuesta_tabla1_pregunta2',
        'encuesta_tabla1_pregunta3',
        'encuesta_tabla1_pregunta4',
        'encuesta_tabla1_pregunta5',
        'encuesta_tabla1_pregunta6',
        'encuesta_tabla1_pregunta7',
        'encuesta_tabla1_pregunta8',
        'encuesta_tabla1_pregunta9',
        'encuesta_tabla1_pregunta10',

        'encuesta_tabla2_pregunta1',
        'encuesta_tabla2_pregunta2',
        'encuesta_tabla2_pregunta3',
        'encuesta_tabla2_pregunta4',
        'encuesta_tabla2_pregunta5',
        'encuesta_tabla2_pregunta6',
        'encuesta_tabla2_pregunta7',
        'encuesta_tabla2_pregunta8',
        'encuesta_tabla2_pregunta9',
        'encuesta_tabla2_pregunta10',
        'encuesta_tabla2_pregunta11',
   
        'encuesta_tabla3_pregunta1',
        'encuesta_tabla3_pregunta2',
      
        'encuesta_tabla3_pregunta4',
    
        'encuesta_tabla3_pregunta6',
  
        'encuesta_tabla3_pregunta8',
        'encuesta_tabla3_pregunta9',
     
        'encuesta_tabla3_pregunta12',
        'encuesta_tabla3_pregunta13',

        'encuesta_tabla3_pregunta15',
        'encuesta_tabla3_pregunta16',

        'encuesta_tabla3_pregunta18',
        'encuesta_tabla3_pregunta19',
  
        'encuesta_tabla3_pregunta21',
        'encuesta_tabla3_pregunta22',

    ]


class EndGame(Page):
    def is_displayed(self):
        if self.player.consentimiento == False:
            return True
        if self.player.terminos_actividad == False:
            return True
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False


class PaginaEspera(Page):
    timeout_seconds = 60

    def is_displayed(self):
        if self.round_number == 9:
            return True
        if self.round_number == 16:
            return True
        if self.round_number == 23:
            return True

    def vars_for_template(self):
        return{
            "": 2,
        }


page_sequence = [
    ConsentimientoInformado,
    Instrucciones,
    Contrato_formal_fijo,
    Contrato_formal_indefinido,
    Contrato_formal_servicios,
    Contrato_informal_fijo,
    Contrato_informal_indefinido,
    Contrato_informal_servicios,
    Instrucciones_actividad,
    Identificacion,
    Ronda_1,
    Results,
    Test,
    Pago,
    Articulos,
    Encuesta,
    #PaginaEspera,
    DateWaitPage,
    ArticulosPost,
    EndGame]
