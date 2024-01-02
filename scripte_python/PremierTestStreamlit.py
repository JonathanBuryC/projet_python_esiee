
import pandas as pd
import streamlit as st
import plotly_express as px
import sweetviz as sv
import folium
import numpy as np
from folium.plugins import MarkerCluster
import pkg_resources

#######################################



st.title("Etude du maché de l'énergie d'EDF au niveau mondial")

st.write("""
Data set appartenant à edf
""")
st.markdown("[Sourceinternet](https://opendata.edf.fr/explore/dataset/productions-consolidees-par-pays-du-groupe-edf/information/?disjunctive.perimetre_spatial&disjunctive.filiere&sort=-tri&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJwcm9kdWN0aW9uIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzAwMUE3MCJ9XSwieEF4aXMiOiJhbm5lZSIsIm1heHBvaW50cyI6bnVsbCwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd25UaW1lc2NhbGUiOiIiLCJjb25maWciOnsiZGF0YXNldCI6InByb2R1Y3Rpb25zLWNvbnNvbGlkZWVzLXBhci1wYXlzLWR1LWdyb3VwZS1lZGYiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnBlcmltZXRyZV9zcGF0aWFsIjp0cnVlLCJkaXNqdW5jdGl2ZS5maWxpZXJlIjp0cnVlLCJzb3J0IjoiLXRyaSJ9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)")

#data frame de EDF
edf = pd.read_csv("../CSV/productions-consolidees-par-pays-du-groupe-edf.csv",
delimiter=';')

#data frame des pays
paysDF = pd.read_csv("../CSV/Country.csv" )

#data frame EDF + pays
edf_pays=pd.read_csv("../CSV/edf_AND_country.csv")

# problème de , à la place de point
edf_pays=edf_pays.dropna(subset=['Production'])
edf_pays['Production'] = edf_pays['Production'].astype('str').str.replace(',','').astype('float')

edf_pays.to_csv('edf_AND_country.csv', index=False)


edf_pays['Année'] = edf_pays['Année'].astype('str').str.replace(',','').astype('float')

st.dataframe(edf_pays, height=300)

# # st.dataframe(edf.style.background_gradient(axis=0))


if st.button('voir le data set "EDF"  dans son entièreté?'):
    st.write("Voici la Productions consolidées par pays du groupe EDF")
    st.dataframe(edf, height=300)

if st.button('voir le data set "pays" dans son entièreté?'):
    st.write("Voici des information sur les pays du monde")
    st.dataframe(paysDF, height=300)

if st.button('voir le data set "edf + pays"  dans son entièreté?'):
    st.write("Voici le data set complet")
    st.dataframe(edf_pays, height=300)

# #############################################################################


st.subheader("Type d'énergie vendu par edf de 2019 à 2022")

@st.cache_resource
def premièreFig():
    mean_counts_by_year = pd.DataFrame(edf.groupby(["Année",
    "Filière"], sort=True)['Production'].mean()).reset_index()
    fig1 = px.bar(mean_counts_by_year, x='Année', y='Production',
    color="Filière", height=800)
    return fig1

fig1 =premièreFig()
st.write(fig1)
# ###############################################################################
st.subheader(" Type d'énergie vendu en moyenne par EDF pour chaque pays client ")

@st.cache_resource
def deuxièmeFig():
    mean_counts_by_year = pd.DataFrame(edf.groupby(["Périmètre spatial", "Filière"], sort=True)['Production'].mean()).reset_index()
    fig2 = px.bar(mean_counts_by_year, x='Périmètre spatial',
    y='Production', color="Filière", height=800)
    return fig2

fig2 =deuxièmeFig()
st.write(fig2)

# ##############################################################################################

st.subheader("Détail de la production d'énergie d'EDF par pays")

selected_country = st.selectbox("Choisir un pays :", edf['Périmètre spatial'].unique())

filtered_df = edf[edf['Périmètre spatial'] == selected_country] #.loc , query
filtered_df['Année'] = filtered_df['Année'].astype('category')



@st.cache_resource
def selectPays():
    fig3 = px.scatter(filtered_df, x='Année', y='Production',render_mode='svg', labels={'Année': 'Année','Production': 'Production'},
                template='plotly_white',color_discrete_sequence=['blue'])  #permet de ne  pas mettre la moyenne des année en abscisse , ex : 2019,5
    # Forcer Plotly Express à traiter l'axe x comme catégorie
    fig3.update_xaxes(type='category')
    return fig3

fig3 =selectPays()
st.write(fig3)

#####################################################################

TroisD= px.line_3d(edf, x='Année', y='Sector', z='Production')
st.write(TroisD)

######################################################################



# Sélection des colonnes nécessaires
df_map = edf_pays[['country', 'Filière','Production', 'lat', 'lng','population']]

# # Création de la carte choroplèthe interactive
Carte = px.scatter_geo(df_map, locations='country', lat ='lat',lon='lng' , color='Production',
                     hover_name='country', size='Production',
                     projection='natural earth', title='Pays et leurs energies')

# # Affichage de la carte choroplèthe interactive dans Streamlit
st.plotly_chart(Carte)

##############################################################################

def trier_production(colonne):
    return pd.DataFrame(edf).sort_values(by=colonne, ascending=True)

if st.button("trier par production d'énergie"):
    laProduction = trier_production('Production')
    st.write(laProduction)


def trier_pays_alpha():
    return pd.DataFrame(edf).sort_index( ascending=True)

if st.button("trier par ordre alphabétique les pays"):
    pays_alpha=  trier_pays_alpha()
    st.write(pays_alpha)

####################################################################

m = folium.Map(location=(45.5236, -122.6750))
st.write(m)



######################################################################

# mapEDF = pd.DataFrame(edf_pays,

#     columns=['lat', 'lng'])

# st.map(mapEDF)


# data['info'] = ['San Francisco', 'Los Angeles', 'New York']

# # Créer une carte avec les données
# st.map(data)
