import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import folium

app = dash.Dash(__name__)

#######################################
def premièreFig():
    mean_counts_by_year = pd.DataFrame(edf.groupby(["Année",
    "Filière"], sort=True)['Production'].mean()).reset_index()
    fig1 = px.bar(mean_counts_by_year, x='Année', y='Production',
    color="Filière", height=800)
    return fig1

app.layout = html.Div([
    html.H1("Étude du marché de l'énergie d'EDF au niveau mondial"),

    html.Div([
        html.P("Data set appartenant à EDF"),
        dcc.Markdown("[Source Internet](https://opendata.edf.fr/explore/dataset/productions-consolidees-par-pays-du-groupe-edf/information/?disjunctive.perimetre_spatial&disjunctive.filiere&sort=-tri&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJwcm9kdWN0aW9uIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzAwMUE3MCJ9XSwieEF4aXMiOiJhbm5lZSIsIm1heHBvaW50cyI6bnVsbCwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd25UaW1lc2NhbGUiOiIiLCJjb25maWciOnsiZGF0YXNldCI6InByb2R1Y3Rpb25zLWNvbnNvbGlkZWVzLXBhci1wYXlzLWR1LWdyb3VwZS1lZGYiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnBlcmltZXRyZV9zcGF0aWFsIjp0cnVlLCJkaXNqdW5jdGl2ZS5maWxpZXJlIjp0cnVlLCJzb3J0IjoiLXRyaSJ9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)")
    ]),

    html.Div([
        html.H2("Data frame de EDF"),
        dcc.Graph(figure=premièreFig)
    ]),

    # html.Div([
    #     html.H2("Data frame des pays"),
    #     dcc.Graph(figure=fig2)
    # ]),

    # html.Div([
    #     html.H2("Data frame EDF + pays"),
    #     dcc.Graph(figure=fig3)
    # ]),

    # html.Div([
    #     html.H2("Type d'énergie vendu par EDF de 2019 à 2022"),
    #     dcc.Graph(figure=px.line_3d(edf, x='Année', y='Sector', z='Production'))
    # ]),

    # html.Div([
    #     html.H2("Carte choroplèthe interactive"),
    #     dcc.Graph(figure=Carte)
    # ]),

    # html.Div([
    #     html.H2("Trier par production d'énergie"),
    #     html.Button("Trier", id="button_production"),
    #     dcc.Graph(id="graph_production")
    # ]),

    # html.Div([
    #     html.H2("Trier par ordre alphabétique les pays"),
    #     html.Button("Trier", id="button_alpha"),
    #     dcc.Graph(id="graph_alpha")
    # ]),

    # html.Div([
    #     html.H2("Carte avec folium"),
    #     html.Iframe(id='map', style={'width': '100%', 'height': '500px'})
    # ]),

])

# @app.callback(
#     dash.dependencies.Output('graph_production', 'figure'),
#     [dash.dependencies.Input('button_production', 'n_clicks')]
# )
# def update_production(n_clicks):
#     if n_clicks is None:
#         raise dash.exceptions.PreventUpdate

#     return px.bar(laProduction, x='Production', y='Année', color='Filière', height=800)

# @app.callback(
#     dash.dependencies.Output('graph_alpha', 'figure'),
#     [dash.dependencies.Input('button_alpha', 'n_clicks')]
# )
# def update_alpha(n_clicks):
#     if n_clicks is None:
#         raise dash.exceptions.PreventUpdate

#     return px.bar(pays_alpha, x='Production', y='Année', color='Filière', height=800)

if __name__ == '__main__':
    app.run_server(debug=True)



# import pandas as pd
# import dash
# from dash import dcc, html
# import plotly.express as px

# #data frame de EDF
# edf = pd.read_csv("../CSV/productions-consolidees-par-pays-du-groupe-edf.csv",
# delimiter=';')

# app = dash.Dash(__name__)

# def premièreFig():
#     mean_counts_by_year = pd.DataFrame(edf.groupby(["Année", "Filière"], sort=True)['Production'].mean()).reset_index()
#     fig1 = px.bar(mean_counts_by_year, x='Année', y='Production', color="Filière", height=800)
#     return fig1

# app.layout = html.Div([
#     html.H1("Étude du marché de l'énergie d'EDF au niveau mondial"),

#     html.Div([
#         html.P("Data set appartenant à EDF"),
#         dcc.Markdown("[Source Internet](https://opendata.edf.fr/explore/dataset/productions-consolidees-par-pays-du-groupe-edf/information/?disjunctive.perimetre_spatial&disjunctive.filiere&sort=-tri&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJwcm9kdWN0aW9uIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzAwMUE3MCJ9XSwieEF4aXMiOiJhbm5lZSIsIm1heHBvaW50cyI6bnVsbCwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd25UaW1lc2NhbGUiOiIiLCJjb25maWciOnsiZGF0YXNldCI6InByb2R1Y3Rpb25zLWNvbnNvbGlkZWVzLXBhci1wYXlzLWR1LWdyb3VwZS1lZGYiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnBlcmltZXRyZV9zcGF0aWFsIjp0cnVlLCJkaXNqdW5jdGl2ZS5maWxpZXJlIjp0cnVlLCJzb3J0IjoiLXRyaSJ9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)")
#     ]),

#     html.Div([
#         html.H2("Data frame de EDF"),
#         dcc.Graph(figure=premièreFig())
#     ]),
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
