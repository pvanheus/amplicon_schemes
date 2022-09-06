#!/usr/bin/env python3

from models import *

import json
from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from yaml import safe_load, safe_dump

app = FastAPI()

origins = [
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
SCHEMES_PATH='../schemes.yml'
SCHEMES_OUTPUT_PATH="schemes.yml"
scheme_list = safe_load(open(SCHEMES_PATH))
scheme_dict = {}
for scheme_obj in scheme_list:
    s = Scheme.parse_obj(scheme_obj)
    scheme_dict[s.name] = s

@app.get('/schema')
def list_schemes():
    return list(scheme_dict.keys())

@app.get('/schema/{name}')
def read_scheme(name: str):
    if name in scheme_dict:
        return scheme_dict[name].dict()

@app.put('/schema/{name}')
def add_scheme(scheme: Scheme):
    scheme_dict[scheme.name] = scheme
    yamlified = {}
    for name in scheme_dict:
        yamlified[name] = scheme_dict[name].dict()
    safe_dump(yamlified, open(SCHEMES_OUTPUT_PATH, "w"))