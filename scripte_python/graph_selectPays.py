import plotly_express as px
import pandas as pd
from dash import Dash, html, dash_table, dcc,  Input, Output, callback

edf = pd.read_csv("../projet_pyhton_esiee/CSV/productions-consolidees-par-pays-du-groupe-edf.csv",delimiter=';')

edf.columns = [col.strip() for col in edf.columns]



def button_select_country():
    options = [{'label': country, 'value': country} for country in edf['Périmètre spatial'].unique()]
    selected_country = dcc.Dropdown(options=options, placeholder='Choisir un pays')
    return selected_country
    
    
    


       

def selectPays(selected_country):
    filtered_df = edf[edf['Périmètre spatial'] == selected_country]
    filtered_df['Année'] = filtered_df['Année'].astype('category')
    fig = px.scatter(
        filtered_df,
        x='Année',
        y='Production',
        render_mode='svg',
        labels={'Année': 'Année', 'Production': 'Production'},
        template='plotly_white',
        color_discrete_sequence=['blue']
    )
    fig.update_xaxes(type='category')
    return fig

