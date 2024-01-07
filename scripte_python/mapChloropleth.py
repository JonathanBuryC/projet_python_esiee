import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc,  Input, Output, callback
import plotly_express as px
import numpy as np


add_iso_to_edf_pays=pd.read_csv("../projet_pyhton_esiee/CSV/edf_AND_country_AND_iso.csv")

add_iso_to_edf_pays.columns = [col.strip() for col in add_iso_to_edf_pays.columns]  # permet de n epas avoir d'espaces inutiles dans le dataframe "add_iso_to_edf_pays"
add_iso_to_edf_pays.dropna()

choropleth_data = add_iso_to_edf_pays.groupby(['country', 'alpha-3'])['Production'].sum().reset_index()
codes_pays = [code.strip() for code in choropleth_data["alpha-3"]]




def figure_chloropleth():
    """
        Crée et retourne une carte choroplèthe représentant la production totale par pays.

        Cette fonction utilise un dataframe agrégé pour afficher la somme de la production par pays sur une carte mondiale.
        Les données sont visualisées à l'aide d'une échelle de couleurs, avec chaque pays coloré en fonction de sa production totale.

        Returns:
            plotly.graph_objs._figure.Figure: Un objet Figure de Plotly contenant la carte choroplèthe.
    """
    
    # Création d'une carte choroplèthe avec Plotly Express.
    fig_choropleth = px.choropleth(
        choropleth_data,      # Données agrégées par pays et code ISO.
        locations=codes_pays,      # Utilise les codes ISO des pays pour les positions sur la carte.
        color="Production",       # Colore les pays en fonction de leur production.
        hover_name="country",       # Affiche le nom du pays au survol.
        title='Fait à partir du dataframe "ISO 3166-1"',     # Titre de la carte.
        color_continuous_scale='Rainbow',         # Utilise l'échelle de couleur 'Rainbow'.
        range_color=[0, 100000]        # Définit l'échelle de couleur pour la production.
    )



    # Mise à jour des paramètres de la carte.
    fig_choropleth.update_layout(
        geo=dict(
            showframe=True,
            showland=True,
            landcolor="rgb(243, 243, 243)",
            showcoastlines=True,
            projection_type='natural earth'   # Type de projection de la carte plus jolie
        )
    )

    fig_choropleth.update_geos(
        showcountries=True,
        showcoastlines=False,
        coastlinecolor="black",
        showland=False,
    )
    
    return fig_choropleth


