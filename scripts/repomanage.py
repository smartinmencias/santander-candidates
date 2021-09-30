#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import requests
import fileinput
import subprocess
from requests.structures import CaseInsensitiveDict

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="Listar los repositorios", action="store_true")
parser.add_argument("-c", "--create", help="Crear repositorio")
args = parser.parse_args()

if args.list:

        response = requests.get('http://192.168.99.106:32000/service/rest/v1/repositories', auth=('admin', 'admin123'))
        open('repos.json', 'wb').write(response.content)
        with open('repos.json') as file:
                db = json.load(file)
                items = []
                for item in db:
                        items.append(item["name"])
                print(items)


if args.create:
        print ("El nombre del repo a crear es:", args.create)

        with open('template.json', 'r') as file :
                filedata = file.read()

        filedata = filedata.replace('NAME_REPO', args.create)

        with open('template.json', 'w') as file:
                file.write(filedata)

        url = "http://192.168.99.106:32000/service/rest/v1/repositories/apt/hosted"
        headers = CaseInsensitiveDict()
        headers ["Content-Type"] = "application/json"
        data = open('template.json')
        resp = requests.post(url, headers=headers, data=data, auth=('admin','admin123'))
        print(resp.status_code)