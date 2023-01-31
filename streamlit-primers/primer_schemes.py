from typing import Type

import requests
import yaml

from pydantic import BaseModel
import streamlit as st
import streamlit_pydantic as sp

from manifest import PrimerSchemeManifest
from scheme import AmpliconScheme

def get_description(model: Type[BaseModel], property: str) -> str:
    schema = model.schema()
    if property in schema['properties']:
        if 'description' in schema['properties'][property]:
            return schema['properties'][property]['description']
    return ''


st.set_page_config(layout="wide")

@st.cache
def fetch_primer_list(schemelist_url: str = 'https://raw.githubusercontent.com/pha4ge/primer-schemes/main/index.yml') -> PrimerSchemeManifest:
    response = requests.get(schemelist_url)
    if response.status_code == 200:
        manifest_info = yaml.safe_load(response.content)
        scheme_info = PrimerSchemeManifest.parse_obj(manifest_info)
        return scheme_info

@st.cache
def fetch_primer_schemes(scheme_list: PrimerSchemeManifest) -> dict[str, AmpliconScheme]:
    scheme_info_dict = {}
    for scheme in primer_list.schemes:
        for version in scheme.versions:
            info_name = f'{scheme.name.lower()}-{version.version}'
            url = version.repository.replace('github.com', 'raw.githubusercontent.com') + f'/{info_name}.yaml'
            response = requests.get(url)
            if response.status_code == 200:
                scheme_info = yaml.safe_load(response.content)
                scheme = AmpliconScheme.parse_obj(scheme_info)
                scheme_info_dict[info_name] = scheme


def add_alias():
    st.session_state.num_aliases += 1


def remove_alias(alias_num: int):
    if alias_num in st.session_state.aliases:
        del st.session_state.aliases[alias_num]
    st.session_state.num_aliases = len(st.session_state.aliases)

(tab1, tab2) = st.tabs(['Primer Scheme Info', 'Primer Scheme Designer'])

primer_list = fetch_primer_list()
scheme_details = fetch_primer_schemes(primer_list)
organisms = list(set([ scheme.organism for scheme in primer_list.schemes ]))
if 'selected_organisms' not in st.session_state:
    st.session_state['selected_organisms'] = [organisms[0]]
if 'num_aliases' not in st.session_state:
    st.session_state['num_aliases'] = 0
    st.session_state['aliases'] = {}

tab1.header(primer_list.metadata)
tab1.write(primer_list.repository + ' / ' + primer_list.latest_doi)
tab1.write(primer_list.license)
tab1.subheader('Primer Schemes')
if len(organisms) > 1:
    tab1.multiselect('Organisms', organisms, key='selected_organisms')
    tab1.write(st.session_state.selected_organisms)
table_md = ['|Name|Organism|Latest version|Available versions', '|--|--|--|--|']
(col1, col2, col3, col4) = tab1.columns(4)
for scheme in primer_list.schemes:
    if scheme.organism in st.session_state.selected_organisms:
        bold_if = lambda v: '**' if v.version == scheme.latest_version else ''
        scheme_versions_md = ', '.join([ f'{bold_if(v)}[{v.version}]({v.repository}){bold_if(v)}' for v in scheme.versions ])
        col1.write(scheme.name)
        col2.write(scheme.organism)
        for v in scheme.versions:
            col3.markdown()
        table_md.append(f'|{scheme.name}|{scheme.organism}|{scheme.latest_version}|{scheme_versions_md}|')
tab1.markdown('\n'.join(table_md))

# with tab2.form(key='new_scheme'):
#     c1, c2 = st.columns(2)
#     with c1:
#         st.text_input(label='Name', key='new_scheme_name', help=get_description(AmpliconScheme, 'name'))
#     with c2:
#         st.button(label='Add alias', on_click=add_alias)
#     st.text_input(label='Organism', help=get_description(AmpliconScheme, 'organism'))
#     st.write('Name:' + st.session_state.new_scheme_name)
#     # st.write(AmpliconScheme.schema()['properties'])
#     st.form_submit_button()