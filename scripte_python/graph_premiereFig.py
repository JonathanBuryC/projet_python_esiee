import plotly_express as px
import pandas as pd

edf = pd.read_csv("../projet_pyhton_esiee/CSV/productions-consolidees-par-pays-du-groupe-edf.csv",delimiter=';')

edf.columns = [col.strip() for col in edf.columns]  # permet de n epas avoir d'espaces inutiles dans le dataframe "edf"

colors = {
    'background': '#111111', # #111111 = noir
    'text': '#7FDBFF'   # #7FDBFF= blanc
}

def mean_counts_by_year ():
    """
        Calcule et retourne la production moyenne par année et par filière.

        Cette fonction groupe le dataframe 'edf' par 'Année' et 'Filière', calcule la moyenne de la production pour chaque groupe,
        et renvoie ces informations sous forme de dataframe.

        Returns:
            pandas.DataFrame: Un dataframe avec les colonnes 'Année', 'Filière' et la production moyenne pour chaque combinaison de ces deux.
    """
    # Groupe le dataframe par 'Année' et 'Filière', et calcule la moyenne de 'Production' pour chaque groupe.
    mean_counts_by_year = (edf.groupby(["Année","Filière"], sort=True)['Production'].mean()).reset_index()
    return mean_counts_by_year

def premiereFig():
    """
        Crée et retourne une figure de type barre groupée pour la production moyenne par année et filière.

        Cette fonction utilise le dataframe généré par la fonction mean_counts_by_year() pour créer un graphique en barres groupées,
        où chaque groupe de barres représente une année et chaque barre au sein d'un groupe représente une filière.

        Returns:
            plotly.graph_objs._figure.Figure: Un objet Figure de Plotly contenant le graphique en barres groupées.
    """
    
    # Création d'un graphique en barres groupées avec Plotly Express.
    fig1 = px.bar(mean_counts_by_year(), x='Année', y='Production',color="Filière", height=800,barmode="group")
    
    # Mise à jour du style de la figure (fond, couleur du texte) en utilisant le dictionnaire 'colors'.
    fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])
    
    return fig1

