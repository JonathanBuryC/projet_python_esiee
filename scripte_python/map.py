import plotly_express as px
import pandas as pd

edf_pays=pd.read_csv("../CSV/edf_AND_country.csv")



edf_pays['lat      '] = pd.to_numeric(edf_pays['lat      '], errors='coerce')
edf_pays['lng     '] = pd.to_numeric(edf_pays['lng     '], errors='coerce')

# Convertir les colonnes 'lat' et 'lng' en entiers (si nécessaire)
edf_pays['lat      '] = edf_pays['lat      '].astype('int', errors='ignore')
edf_pays['lng     '] = edf_pays['lng     '].astype('int', errors='ignore')

edf_pays['lat      '] = edf_pays['lat      '].fillna(0)
edf_pays['lng     '] = edf_pays['lng     '].fillna(0)

# def fig_map():

fig_map = px.choropleth(edf_pays,
                        geojson= ("../mapGeojson/mapGeojson/custom.geo.json"),
                        color= "Filière        ",
                        lat='lat      ',
                        lon='lng     ',
                        size='production',
                        size_max=30,
                        zoom=2)
