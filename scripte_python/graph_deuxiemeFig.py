import plotly_express as px
import pandas as pd

edf = pd.read_csv("../projet_python_esiee-main/CSV/productions-consolidees-par-pays-du-groupe-edf.csv",delimiter=';')
edf.columns = [col.strip() for col in edf.columns]
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def deuxiemeFig():
    mean_counts_by_year = pd.DataFrame(edf.groupby(["Périmètre spatial", "Filière"], sort=True)['Production'].mean()).reset_index()
    fig2 = px.bar(mean_counts_by_year, x='Périmètre spatial',y='Production', color="Filière", height=800, barmode='stack')
    
    fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])
    
    return fig2