import plotly_express as px
import pandas as pd

edf = pd.read_csv("../projet_python_esiee-main/CSV/productions-consolidees-par-pays-du-groupe-edf.csv",delimiter=';')

edf.columns = [col.strip() for col in edf.columns]

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def mean_counts_by_year ():
    mean_counts_by_year = (edf.groupby(["Année","Filière"], sort=True)['Production'].mean()).reset_index()
    return mean_counts_by_year

def premiereFig():
    fig1 = px.bar(mean_counts_by_year(), x='Année', y='Production',color="Filière", height=800,barmode="group")
    
    fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])
    
    return fig1

