#!/usr/bin/env python3

import argparse
from typing import Union
from pydantic import BaseModel, conlist, HttpUrl
from pydantic_yaml import YamlModel
from yaml import safe_load

class PersonOrOrg(BaseModel):
    name: str
    url: Union[HttpUrl, str] = None

class Scheme(BaseModel):
    name: str
    organism: str
    organism_aliases: list[str]
    aliases: conlist(str, unique_items=True)
    developers: conlist(PersonOrOrg, min_items=1)
    vendors: list[PersonOrOrg]
    amplicon_size: int
    bed_url: HttpUrl
    bed_checksum: str
    reference_sequence: Union[str, HttpUrl]
    reference_checksum: str
    citation: Union[HttpUrl, str] = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('schemas_file', type=argparse.FileType())
    args = parser.parse_args()

    scheme_objects = safe_load(args.schemas_file)
    s = Scheme.parse_obj(scheme_objects[0])
    print(s)


    