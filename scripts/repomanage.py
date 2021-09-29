#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import argparse
import requests
from requests.structures import CaseInsensitiveDict

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="Listar los repositorios", action="store_true")
parser.add_argument("-c", "--create", help="Crear repositorio", action="store_true")
args = parser.parse_args()

# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.list:
        response = requests.get('http://192.168.99.106:32000/service/rest/v1/repositories', auth=('admin', 'admin123'))
        print (response.text)

if args.create:

        url = "http://192.168.99.106:32000/service/rest/v1/repositories/docker/hosted"

        headers = CaseInsensitiveDict()
        headers ["Content-Type"] = "application/json"

        data = open('template.json')
        resp = requests.post(url, headers=headers, data=data, auth=('admin','admin123'))
        print(resp.status_code)