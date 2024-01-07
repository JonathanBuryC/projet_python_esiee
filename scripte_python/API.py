import plotly_express as px
import pandas as pd
import requests
import json


colors = {
    'background': '#111111',  # #111111 = noir
    'text': '#7FDBFF' # #7FDBFF= blanc
}

def dataframe_with_api():
    """
        Récupère des données depuis une API EDF et les convertit en dataframe Pandas.

        Cette fonction fait une requête GET à l'API EDF pour obtenir les données sur les émissions de CO2 consolidées par pays.
        Elle traite ensuite ces données pour les transformer en un dataframe Pandas, facilitant ainsi leur manipulation et analyse.

        Returns:
            pandas.DataFrame: Un dataframe contenant les données récupérées, avec les colonnes 'Périmètre spatial', 
                            'emissions_co2' et 'Année'.
    """
    resultat = requests.get("https://opendata.edf.fr/api/explore/v2.1/catalog/datasets/emissions-de-co2-consolidees-par-pays-du-groupe-edf/records?limit=60") #le 60 car il y a 60 ligne de dataframe
    data = resultat.json()['results']
    dataframe_api = pd.DataFrame([{
    'Périmètre spatial': d['perimetre_spatial'],
    "emissions_co2": d["emissions_co2"],
    "Année": d["annee"]
    } for d in data])
    return dataframe_api



