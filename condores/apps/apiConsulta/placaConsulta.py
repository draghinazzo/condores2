from django.http import JsonResponse
from django.shortcuts import render, resolve_url
import requests
import json
class placaConsulta():
    def consulta(self, placa):
        url = "http://admin.sap.ssc.cdmx.gob.mx/api/v1/empleado/busqueda/numeroempleado?numero_empleado="+str(placa)
        payload={}
        headers = {
        'Authorization': 'Token e8dcf47186f14f70826a1a849e4976d5765a7bce'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = [
                {
                    'error' : 1,
                    'data' : 'nada'
                }
            ]
        if response: 
            data = [
                {
                    'error' : 0,
                    'data' : json.loads(response.text)
                }
            ]
            return JsonResponse({'data': data})
        else:
            return JsonResponse({'data': data})

class imagenConsulta():
    def consulta(self, placa):
        url = "http://admin.sap.ssc.cdmx.gob.mx/api/v1/empleado/"+str(placa)+"/picture"
        payload={}
        headers = {
        'Authorization': 'Token a9a5a809f5370633c92806565f43e4c92cf5bfde'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = [
                {
                    'error' : 1,
                    'data' : 'nada'
                }
            ]
        if response: 
            data = [
                {
                    'error' : 0,
                    'data' : json.loads(response.text)
                }
            ]
            return JsonResponse({'data': data})
        else:
            return JsonResponse({'data': data})