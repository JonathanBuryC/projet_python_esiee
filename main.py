import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc,  Input, Output, callback
import plotly_express as px
import plotly.graph_objects as go
import sys
from dash.dependencies import Input, Output



sys.path.append('../projet_pyhton_esiee/scripte_python') 
from graph_premiereFig import premiereFig
from graph_premiereFig import mean_counts_by_year
from graph_deuxiemeFig import deuxiemeFig
from mapChloropleth import figure_chloropleth
from API import dataframe_with_api
from API import diagramme_api



edf = pd.read_csv("../projet_pyhton_esiee/CSV/productions-consolidees-par-pays-du-groupe-edf.csv",delimiter=';')

iso=pd.read_csv("../projet_pyhton_esiee/CSV/all.csv")


edf.columns = [col.strip() for col in edf.columns]



app = dash.Dash(__name__)

app.layout = html.Div(children=[
  
    html.H1("Étude du marché de l'énergie d'EDF au niveau mondial", style={'textAlign': 'center', 'color': 'white','text-decoration': 'underline'}),

    
    html.P("Dataset et API appartenant à EDF"),
    dcc.Markdown("[Source EDF](https://opendata.edf.fr/explore/dataset/productions-consolidees-par-pays-du-groupe-edf/information/?disjunctive.perimetre_spatial&disjunctive.filiere&sort=-tri&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJwcm9kdWN0aW9uIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzAwMUE3MCJ9XSwieEF4aXMiOiJhbm5lZSIsIm1heHBvaW50cyI6bnVsbCwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd25UaW1lc2NhbGUiOiIiLCJjb25maWciOnsiZGF0YXNldCI6InByb2R1Y3Rpb25zLWNvbnNvbGlkZWVzLXBhci1wYXlzLWR1LWdyb3VwZS1lZGYiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnBlcmltZXRyZV9zcGF0aWFsIjp0cnVlLCJkaXNqdW5jdGl2ZS5maWxpZXJlIjp0cnVlLCJzb3J0IjoiLXRyaSJ9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)",style={'color': 'white'}),
    

    
    html.H3("Dataframe de EDF",style={'textAlign': 'center', 'color': 'white'}),
    html.Div([
        dash_table.DataTable(
            data=edf.to_dict('records'),
            page_size=10,
            style_data_conditional=[
                {
                    'backgroundColor': 'black',
                    'color': 'white'   
                }
            ], style_cell={'minWidth': '50px', 'width': '100px', 'maxWidth': '150px'}       
        )
    ], style={'width': '80%', 'marginLeft': '0  %', 'marginRight': '5%'}),
    
    
    html.H3("Dataframe ISO 3166-1",style={'textAlign': 'center','color': 'white'}),
    dcc.Markdown("[Source de l'API](https://gist.github.com/tadast/8827699)",style={'color': 'white'}),

    html.Div([
        dash_table.DataTable(   
            data=iso.to_dict('records'),
            page_size=10,
            style_data_conditional=[
                {
                    'backgroundColor': 'black',
                    'color': 'white'   
                }
            ],
            style_cell={'minWidth': '50px', 'width': '100px', 'maxWidth': '150px'}
        )
    ], style={'width': '80%', 'marginLeft': '5%', 'marginRight': '5%'}),
      
      
   
    html.H3("Histogramme détaillant la production d'énergie par edf de 2019 à 2022 selon la filière   ",style={'textAlign': 'center','color': 'white'}),
    dcc.Graph(figure=premiereFig()),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.H3("Histogramme détaillant la production d'énergie par pays client d'edf selon la filière ",style={'textAlign': 'center','color': 'white' }),
    dcc.Graph(figure=deuxiemeFig()),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
  
    
    html.H3("Détail de la production d'énergie d'EDF par pays sur 4 ans",style={'textAlign': 'center','color': 'white' }),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country}
        for country in edf['Périmètre spatial'].unique()],
        value=edf['Périmètre spatial'].unique()[0],  # Default value
        multi=False,
        style={'width': '50%', 'color': 'blue'},
        placeholder='Choisir un pays',
        ),  
    dcc.Graph( id='diagramme'),
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.H3("Détail de la production de CO2 par pays sur 4 ans (causé par EDF)",style={'textAlign': 'center','color': 'white' }),
    html.P("Il y a moins de pays disponibles que dans le diagramme précédent."),
    dcc.Markdown("[Source de l'API](https://opendata.edf.fr/explore/dataset/emissions-de-co2-consolidees-par-pays-du-groupe-edf/api/?disjunctive.perimetre_spatial&sort=-tri)",style={'color': 'white'}),
    dcc.Dropdown(
        id='country-dropdown2',
        options=[{'label': country, 'value': country}
        for country in dataframe_with_api()['Périmètre spatial'].unique()],
        value=dataframe_with_api()['Périmètre spatial'].unique()[0],  # Default value
        multi=False,

        style={'width': '50%', 'color': 'blue' },
        placeholder='Choisir un pays',
    ),
    dcc.Graph( id='diagramme_CO2'),  
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.H3("Carte chloropleth indiquant la production d'électricité par pays ",style={'textAlign': 'center','color': 'white' }),
    dcc.Graph(figure=figure_chloropleth()),
    
], style={'backgroundImage': 'linear-gradient(to bottom, #5e5d5d, #1f1d21)'})




@app.callback(
    Output('diagramme', 'figure'),
    Input('country-dropdown', 'value')
)
def update_diagram(selected_country):
    filtered_df = edf[edf['Périmètre spatial'] == selected_country]
    filtered_df['Année','Production'] = filtered_df['Année'].astype('category')
    # Grouper par 'Année' et calculer la somme de 'Production' pour chaque groupe
    sum_df = filtered_df.groupby('Année')['Production'].sum().reset_index()
    fig = px.line(
        sum_df,
        x='Année',
        y='Production',
        render_mode='svg',
        # style = {'backgroundColor': '#FFD700'},
        labels={'Année': 'Année', 'Production': 'Production '},
        template='plotly_white',
        color_discrete_sequence=['blue']
    )
    # Forcer Plotly Express à traiter l'axe x comme catégorie
    fig.update_xaxes(type='category')
    fig.update_layout(
        plot_bgcolor='black',  # Couleur de fond de la zone de traçage
        paper_bgcolor='black'  # Couleur de fond de l'ensemble du graphique
    )
    return fig

@app.callback(
    Output('diagramme_CO2', 'figure'),
    Input('country-dropdown2', 'value')
)

def update_diagram(selected_country):
    filtered_df = dataframe_with_api()[dataframe_with_api()['Périmètre spatial'] == selected_country]
    filtered_df['Année','emissions_co2'] = filtered_df['Année'].astype('category')
    # Grouper par 'Année' et calculer la somme de 'emissions_co2' pour chaque groupe
    sum_df = filtered_df.groupby('Année')['emissions_co2'].sum().reset_index()
    fig2 = px.line(
        sum_df,
        x='Année',
        y='emissions_co2',
        render_mode='svg',
        # style = {'backgroundColor': '#FFD700'},
        labels={'Année': 'Année', 'emissions_co2': 'emissions_co2'},
        template='plotly_white',
        color_discrete_sequence=['blue']
    )
    # Forcer Plotly Express à traiter l'axe x comme catégorie
    fig2.update_xaxes(type='category')
    fig2.update_layout(
        plot_bgcolor='black',  # Couleur de fond de la zone de traçage
        paper_bgcolor='black'  # Couleur de fond de l'ensemble du graphique
    )
    return fig2


if __name__ == '__main__':
    app.run(debug=True)