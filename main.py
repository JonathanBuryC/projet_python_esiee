import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc,  Input, Output, callback
import plotly_express as px
import plotly.graph_objects as go
import sys
from dash.dependencies import Input, Output
import os




script_path = os.path.join(os.path.dirname(__file__), 'scripte_python')
sys.path.append(script_path) 
from graph_premiereFig import premiereFig               #appel de la fonction qui produit le premier histogramme
from graph_deuxiemeFig import deuxiemeFig               #appel de la fonction qui produit le second histogramme
from mapChloropleth import figure_chloropleth           #appel de la fonction qui produit la carte chloropleth
from API import dataframe_with_api                      #appel de la fonction qui transforme l'API en dataframe



CSV_path = os.path.join(os.path.dirname(__file__), 'CSV')
csv_name_one = 'productions-consolidees-par-pays-du-groupe-edf.csv'
csv_file_path_one = os.path.join(CSV_path, csv_name_one)
edf = pd.read_csv(csv_file_path_one,delimiter=';') #dataframe utilisé pour les deux histogrammes


csv_name_two= 'all.csv'
csv_file_path_two = os.path.join(CSV_path, csv_name_two)
iso=pd.read_csv(csv_file_path_two) #dataframe utilisé pour la map chloropleth


edf.columns = [col.strip() for col in edf.columns]   # permet de n epas avoir d'espaces inutiles dans le dataframe "edf"



app = dash.Dash(__name__)         #initialisation de dash

app.layout = html.Div(children=[
  
    html.H1("Étude du marché de l'énergie d'EDF au niveau mondial", style={'textAlign': 'center', 'color': 'white','text-decoration': 'underline'}),

    
    html.P("Dataset et API appartenant à EDF"),
    dcc.Markdown("[Source EDF](https://opendata.edf.fr/explore/dataset/productions-consolidees-par-pays-du-groupe-edf/information/?disjunctive.perimetre_spatial&disjunctive.filiere&sort=-tri&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJwcm9kdWN0aW9uIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzAwMUE3MCJ9XSwieEF4aXMiOiJhbm5lZSIsIm1heHBvaW50cyI6bnVsbCwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd25UaW1lc2NhbGUiOiIiLCJjb25maWciOnsiZGF0YXNldCI6InByb2R1Y3Rpb25zLWNvbnNvbGlkZWVzLXBhci1wYXlzLWR1LWdyb3VwZS1lZGYiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnBlcmltZXRyZV9zcGF0aWFsIjp0cnVlLCJkaXNqdW5jdGl2ZS5maWxpZXJlIjp0cnVlLCJzb3J0IjoiLXRyaSJ9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)",style={'color': 'white'}),
    

    
    html.H3("Dataframe de EDF",style={'textAlign': 'center', 'color': 'white'}),
    html.Div([                                                               # affichage du datraframe "edf" avec un style adéquat
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

    html.Div([                                                          # affichage du datraframe "iso" avec un style adéquat
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
      
      
   
    html.H3("Histogramme détaillant la production d'énergie par edf de 2019 à 2022 selon la filière en GWh  ",style={'textAlign': 'center','color': 'white'}),
    dcc.Graph(figure=premiereFig()),   #pour comprendre , allez voir "scripte_python/graph_premiereFig.py"
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.H3("Histogramme détaillant la production d'énergie (GWh) par pays client d'edf selon la filière ",style={'textAlign': 'center','color': 'white' }),
    dcc.Graph(figure=deuxiemeFig()),   #pour comprendre , allez voir "scripte_python/graph_deuxiemeFig.py"
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
  
    
    html.H3("Détail de la production d'énergie d'EDF par pays sur 4 ans",style={'textAlign': 'center','color': 'white' }),
    dcc.Dropdown(
        id='country-dropdown',   # Identifiant unique pour le menu déroulant pour  le second diagramme ( fait avec le dataframe "edf")
        options=[{'label': country, 'value': country}
        for country in edf['Périmètre spatial'].unique()],   # Crée une liste d'options pour le menu déroulant. Chaque option est un pays unique trouvé dans la colonne 'Périmètre spatial' du dataframe 'edf'.
        value=edf['Périmètre spatial'].unique()[0],  # Définit la valeur par défaut du menu déroulant comme étant le premier pays dans la liste unique des pays.
        multi=False,    # Indique que l'utilisateur ne peut sélectionner qu'une seule option (pays) à la fois.
        style={'width': '50%', 'color': 'blue'},    # Définit le style CSS pour le menu déroulant, ajustant sa largeur et la couleur du texte
        placeholder='Choisir un pays',          # Texte affiché dans le menu déroulant quand aucune option n'est sélectionnée.
        ),  
    dcc.Graph( id='diagramme'),   # allez en bas pour comprendre avec l utilisation de @app.callback .
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.H3("Détail de la production de CO2 par pays sur 4 ans (causé par EDF)",style={'textAlign': 'center','color': 'white' }),
    html.P("Il y a moins de pays disponibles que dans le diagramme précédent."),
    dcc.Markdown("[Source de l'API](https://opendata.edf.fr/explore/dataset/emissions-de-co2-consolidees-par-pays-du-groupe-edf/api/?disjunctive.perimetre_spatial&sort=-tri)",style={'color': 'white'}),
    dcc.Dropdown(
        id='country-dropdown2',    # Identifiant unique pour le menu déroulant pour  le second diagramme ( fait avec l'API)
        options=[{'label': country, 'value': country}
        for country in dataframe_with_api()['Périmètre spatial'].unique()],  # Crée une liste d'options pour le menu déroulant où chaque option est un pays unique trouvé dans la colonne 'Périmètre spatial' du dataframe retourné par dataframe_with_api().
        value=dataframe_with_api()['Périmètre spatial'].unique()[0],  # Valeur par défaut du menu déroulant, qui est le premier pays dans la liste unique des pays.
        multi=False,    # Spécifie que l'utilisateur ne peut sélectionner qu'une seule option (pays) à la fois.

        style={'width': '50%', 'color': 'blue' }, # Style CSS pour le menu déroulant, définissant sa largeur et la couleur du texte.
        placeholder='Choisir un pays',  # Texte affiché dans le menu déroulant lorsqu'aucune option n'est sélectionnée
    ),
    dcc.Graph( id='diagramme_CO2'),   # allez en bas pour comprendre avec l utilisation de @app.callback .
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.H3("Carte chloropleth indiquant la production d'électricité par pays en GWh",style={'textAlign': 'center','color': 'white' }),
    dcc.Graph(figure=figure_chloropleth()),   #pour comprendre , allez voir "scripte_python/mapChloropleth.py"
    
], style={'backgroundImage': 'linear-gradient(to bottom, #5e5d5d, #1f1d21)'})  # produit en fond écran , unn dégradé de couleur du gris vers le noir




@app.callback(
    Output('diagramme', 'figure'),    # Déclare que la sortie de ce callback est la figure du composant Graph identifié par 'diagramme'.
    Input('country-dropdown', 'value')  # Déclare que l'entrée de ce callback est la valeur sélectionnée du menu déroulant identifié par 'country-dropdown'.
)
def update_diagram(selected_country):
    """
     Met à jour et retourne un graphique linéaire représentant la production d'énergie pour un pays sélectionné.
    
     Cette fonction filtre le dataframe 'edf' pour un pays spécifique, calcule la somme annuelle de la production d'énergie,
     et utilise Plotly Express pour créer un graphique linéaire de cette somme annuelle de production par année.

     Args:
        selected_country (str): Le pays sélectionné par l'utilisateur dans le menu déroulant.

     Returns:
        plotly.graph_objs._figure.Figure: Un objet Figure de Plotly contenant le graphique linéaire mis à jour.
    """
    filtered_df = edf[edf['Périmètre spatial'] == selected_country]    # Filtre le dataframe 'edf' pour ne conserver que les données correspondant au pays sélectionné (en parametre de la fonction)
    filtered_df['Année','Production'] = filtered_df['Année'].astype('category')  # Convertit la colonne 'Année' en catégorie, sinon i y a  des probleme au niveau du graph
    sum_df = filtered_df.groupby('Année')['Production'].sum().reset_index() # Grouper par 'Année' et calculer la somme de 'Production' pour chaque groupe
    fig = px.line(              # Création d'un graphique linéaire avec Plotly Express.
        sum_df,
        x='Année',
        y='Production',
        render_mode='svg',
        # style = {'backgroundColor': '#FFD700'},
        labels={'Année': 'Année', 'Production': 'Production en GWh '},
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
    Output('diagramme_CO2', 'figure'),     # Sortie pour un second graphique, identifié par 'diagramme_CO2'.
    Input('country-dropdown2', 'value')    # Entrée liée à un second menu déroulant, 'country-dropdown2'.
)

def update_diagram(selected_country):
    """
        Met à jour et retourne un graphique linéaire représentant les émissions de CO2 pour un pays sélectionné.
        
        Cette fonction filtre un dataframe obtenu via une fonction externe pour un pays spécifique, convertit la colonne 'Année' en catégorie,
        calcule la somme annuelle des émissions de CO2, et crée un graphique linéaire de ces sommes annuelles par année.

        Args:
            selected_country (str): Le pays sélectionné par l'utilisateur dans un autre menu déroulant.

        Returns:
        plotly.graph_objs._figure.Figure: Un objet Figure de Plotly contenant le graphique linéaire des émissions de CO2 mis à jour.
    """
    
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
        labels={'Année': 'Année', 'emissions_co2': 'emissions_co2 en ktonnes'},
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