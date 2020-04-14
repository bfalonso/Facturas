#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
import datetime as dt

class MainHandler(webapp2.RequestHandler):
    def post(self):
        cif_emisor = str(self.request.get("cif_emisor"))
        nombre_emisor = str(self.request.get("nombre_emisor"))
        direccion_emisor = str(self.request.get("direccion_emisor"))
        poblacion_emisor = str(self.request.get("poblacion_emisor"))
        provincia_emisor = str(self.request.get("provincia_emisor"))
        cp_emisor = str(self.request.get("cp_emisor"))
        pais_emisor = str(self.request.get("pais_emisor"))
        contacto_emisor = str(self.request.get("contacto_emisor"))
        email_emisor = str(self.request.get("email_emisor"))
        telefono_emisor = str(self.request.get("telefono_emisor"))

        cif_cliente = str(self.request.get("cif_cliente"))
        nombre_cliente = str(self.request.get("nombre_cliente"))
        direccion_cliente = str(self.request.get("direccion_cliente"))
        poblacion_cliente = str(self.request.get("poblacion_cliente"))
        provincia_cliente = str(self.request.get("provincia_cliente"))
        cp_cliente = str(self.request.get("cp_cliente"))
        pais_cliente = str(self.request.get("pais_cliente"))
        contacto_cliente = str(self.request.get("contacto_cliente"))
        email_cliente = str(self.request.get("email_cliente"))
        telefono_cliente = str(self.request.get("telefono_cliente"))

        concepto = str(self.request.get("concepto"))
        pu = str(self.request.get("pu"))
        uds = str(self.request.get("uds"))
        importe_bruto = str(self.request.get("importe_bruto"))
        iva = str(self.request.get("iva"))
        importe_total = str(self.request.get("importe_total"))

        today = dt.datetime.today()

        jinja = jinja2.get_jinja2(app=self.app)
        valores = {
            "cif_emisor": cif_emisor,
            "nombre_emisor": nombre_emisor,
            "direccion_emisor": direccion_emisor,
            "poblacion_emisor": poblacion_emisor,
            "provincia_emisor": provincia_emisor,
            "cp_emisor": cp_emisor,
            "pais_emisor": pais_emisor,
            "contacto_emisor": contacto_emisor,
            "email_emisor": email_emisor,
            "telefono_emisor": telefono_emisor,
            "cif_cliente": cif_cliente,
            "nombre_cliente": nombre_cliente,
            "direccion_cliente": direccion_cliente,
            "poblacion_cliente": poblacion_cliente,
            "provincia_cliente": provincia_cliente,
            "cp_cliente": cp_cliente,
            "pais_cliente": pais_cliente,
            "contacto_cliente": contacto_cliente,
            "email_cliente": email_cliente,
            "telefono_cliente": telefono_cliente,
            "concepto": concepto,
            "pu": pu,
            "uds": uds,
            "importe_bruto": importe_bruto,
            "iva": iva,
            "importe_total": importe_total,
            "fecha": today
        }

        self.response.write(jinja.render_template("factura.html", **valores))



app = webapp2.WSGIApplication([
    ('/facturar', MainHandler)
], debug=True)
