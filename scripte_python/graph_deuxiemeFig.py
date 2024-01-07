import plotly_express as px
import pandas as pd

edf = pd.read_csv("../projet_pyhton_esiee/CSV/productions-consolidees-par-pays-du-groupe-edf.csv",delimiter=';')
edf.columns = [col.strip() for col in edf.columns]  # permet de n epas avoir d'espaces inutiles dans le dataframe "edf"
colors = {
    'background': '#111111',  # #111111 = noir
    'text': '#7FDBFF'   # #7FDBFF= blanc
}

def deuxiemeFig():
    """
        Crée et retourne une figure de type barre empilée représentant la production moyenne par filière et par pays.

        Cette fonction calcule d'abord la production moyenne pour chaque combinaison de 'Périmètre spatial' et 'Filière' dans le dataframe 'edf'.
        Elle utilise ensuite Plotly Express pour créer un graphique en barres empilées, où chaque barre représente un pays avec des segments colorés pour chaque filière.

        Returns:
            plotly.graph_objs._figure.Figure: Un objet Figure de Plotly contenant le graphique en barres empilées.
    """
    # Calcule la moyenne de la production pour chaque combinaison de 'Périmètre spatial' et 'Filière'.
    mean_counts_by_year = pd.DataFrame(edf.groupby(["Périmètre spatial", "Filière"], sort=True)['Production'].mean()).reset_index()
    
    # Création d'un graphique en barres empilées avec Plotly Express.
    fig2 = px.bar(mean_counts_by_year, x='Périmètre spatial',y='Production', color="Filière", height=800, barmode='stack')
    
    # Mise à jour du style de la figure (fond, couleur du texte) en utilisant le dictionnaire 'colors'
    fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])
    
    return fig2