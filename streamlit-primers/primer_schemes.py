import asyncio

import time

import aiohttp

import requests
import streamlit as st
import yaml

from manifest import PrimerSchemeManifest

@st.cache
def fetch_primer_list(schemelist_url: str = 'https://raw.githubusercontent.com/pha4ge/primer-schemes/main/index.yml') -> PrimerSchemeManifest:
    response = requests.get(schemelist_url)
    if response.status_code == 200:
        manifest_info = yaml.safe_load(response.content)
        scheme_info = PrimerSchemeManifest.parse_obj(manifest_info)
        return scheme_info

(tab1, tab2) = st.tabs(['Primer Scheme Info', 'Primer Scheme Designer'])

primer_list = fetch_primer_list()
organisms = list(set([ scheme.organism for scheme in primer_list.schemes ]))
if 'selected_organisms' not in st.session_state:
    st.session_state['selected_organisms'] = [organisms[0]]

tab1.header(primer_list.metadata)
tab1.write(primer_list.repository + ' / ' + primer_list.latest_doi)
tab1.write(primer_list.license)
tab1.subheader('Primer Schemes')
if len(organisms) > 1:
    tab1.multiselect('Organisms', organisms, key='selected_organisms')
    tab1.write(st.session_state.selected_organisms)
table_md = ['|Name|Latest version|Available versions', '|--|--|--|']
for scheme in primer_list.schemes:
    if scheme.organism in st.session_state.selected_organisms:
        bold_if = lambda v: '**' if v.version == scheme.latest_version else ''
        scheme_versions_md = ', '.join([ f'{bold_if(v)}[{v.version}]({v.repository}){bold_if(v)}' for v in scheme.versions ])
        table_md.append(f'|{scheme.name}|{scheme.latest_version}|{scheme_versions_md}|')
tab1.markdown('\n'.join(table_md))

