import pandas as pd



# Charger les deux fichiers CSV
df1 = pd.read_csv('C:/Users/jonat/Documents/projet_pyhton_esiee/scripte_python/edf_AND_country.csv')
df2 = pd.read_csv('C:/Users/jonat/Documents/projet_pyhton_esiee/scripte_python/all.csv')
# Pour df1
for col in df1.select_dtypes(include=['object']).columns:
    df1[col] = df1[col].str.strip()

# Pour df2
for col in df2.select_dtypes(include=['object']).columns:
    df2[col] = df2[col].str.strip()



# Fusionner les deux dataframes en utilisant la colonne 'country' comme clé
merged_df = pd.merge(df1, df2, on='country                    ', how='outer')

# Supprimer les doublons
merged_df = merged_df.drop_duplicates(subset='Tri   ', keep='first')


# Enregistrez le résultat dans un nouveau fichier CSV
merged_df.to_csv('edf_AND_country_AND_iso.csv', index=False)
