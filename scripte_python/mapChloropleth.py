import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc,  Input, Output, callback
import plotly_express as px
import numpy as np


add_iso_to_edf_pays=pd.read_csv("../projet_python_esiee/CSV/edf_AND_country_AND_iso.csv")

add_iso_to_edf_pays.columns = [col.strip() for col in add_iso_to_edf_pays.columns]
add_iso_to_edf_pays.dropna()

choropleth_data = add_iso_to_edf_pays.groupby(['country', 'alpha-3'])['Production'].sum().reset_index()
codes_pays = [code.strip() for code in choropleth_data["alpha-3"]]




def figure_chloropleth():
    fig_choropleth = px.choropleth(
        choropleth_data,
        locations=codes_pays,
        color="Production",
        hover_name="country",
        title='Fait à partir du dataframe "ISO 3166-1"',
        color_continuous_scale='Rainbow',
        range_color=[0, 100000]
    )




    fig_choropleth.update_layout(
        geo=dict(
            showframe=True,
            showland=True,
            landcolor="rgb(243, 243, 243)",
            showcoastlines=True,
            projection_type='natural earth'
        )
    )

    fig_choropleth.update_geos(
        showcountries=True,
        showcoastlines=False,
        coastlinecolor="black",
        showland=False,
    )
    
    return fig_choropleth


