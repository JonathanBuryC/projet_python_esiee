import plotly_express as px
import pandas as pd
import requests
import json


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def dataframe_with_api():
    resultat = requests.get("https://opendata.edf.fr/api/explore/v2.1/catalog/datasets/emissions-de-co2-consolidees-par-pays-du-groupe-edf/records?limit=60") #le 60 car il y a 60 ligne de dataframe
    data = resultat.json()['results']
    dataframe_api = pd.DataFrame([{
    'Périmètre spatial': d['perimetre_spatial'],
    "emissions_co2": d["emissions_co2"],
    "Année": d["annee"]
    } for d in data])
    return dataframe_api



def diagramme_api():
    diagr_api = px.line(dataframe_with_api(), x='Périmètre spatial', y="emissions_co2", height=800,title='Diagramme Ligne')
    
    diagr_api.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])
    
    return diagr_api
