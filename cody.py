import streamlit as st
import pandas as pd
import subprocess
# Titre centré de la page avec balise HTML
st.markdown("<h1 style='text-align: center;'>CODY+</h1>", unsafe_allow_html=True)

# Fonction pour obtenir le top 5 des départements en fonction du critère choisi
def top5_departements(choix_critere):
    if choix_critere == "Je veux me sentir en sécurité":
        # Charger les données du premier CSV (remplacez ce chemin par le vôtre)
        df = pd.read_csv('Crime21.csv', sep=';')
        # Sélectionner les 5 départements avec le taux de crime le plus faible
        top5 = df.nsmallest(5, 'taux crime/1000')[['Dep', 'nom']]
        # Centrer le tableau
        st.write("Top 5 des départements correspondant au critère choisi :")
        st.table(top5)
        # Afficher l'histogramme pour les données de crime
        st.bar_chart(df.nsmallest(5, 'taux crime/1000').set_index('nom')['taux crime/1000'])
    elif choix_critere == "Je veux pouvoir me balader dans diverses zones vertes":
        # Charger les données du deuxième CSV (remplacez ce chemin par le vôtre)
        df = pd.read_csv('data_com-2.csv', sep=';', encoding="ISO-8859-1")
        # Sélectionner les 5 départements avec la densité de forêt la plus élevée
        top5 = df.nlargest(5, 'forêt')[['com_code', 'Nom']]
        # Centrer le tableau
        st.write("Top 5 des départements correspondant au critère choisi :")
        st.table(top5)
        # Afficher l'histogramme pour les données de forêt
        st.bar_chart(df.nlargest(5, 'forêt').set_index('Nom')['forêt'])
    elif choix_critere == "Je veux vivre dans une ville dense":
        # Charger les données du deuxième CSV (remplacez ce chemin par le vôtre)
        df = pd.read_csv('data_com-2.csv', sep=';', encoding="ISO-8859-1")
        # Sélectionner les 5 départements avec la densité de population la plus élevée
        top5 = df.nlargest(5, 'densité population')[['com_code', 'Nom']]
        # Centrer le tableau
        st.write("Top 5 des départements correspondant au critère choisi :")
        st.table(top5)
        # Afficher l'histogramme pour les données de densité de population
        st.bar_chart(df.nlargest(5, 'densité population').set_index('Nom')['densité population'])
    elif choix_critere == "Je veux vivre dans une ville peu dense":
        # Charger les données du deuxième CSV (remplacez ce chemin par le vôtre)
        df = pd.read_csv('data_com-2.csv', sep=';',encoding="ISO-8859-1")
        # Sélectionner les 5 départements avec la densité de population la plus faible
        top5 = df.nsmallest(5, 'densité population')[['com_code', 'Nom']]
        # Centrer le tableau
        st.write("Top 5 des départements correspondant au critère choisi :")
        st.table(top5)
        # Afficher l'histogramme pour les données de densité de population
        st.bar_chart(df.nsmallest(5, 'densité population').set_index('Nom')['densité population'])
    elif choix_critere == "Je veux vivre dans une ville avec beaucoup d'habitants":
        # Charger les données du deuxième CSV (remplacez ce chemin par le vôtre)
        df = pd.read_csv('data_com-2.csv', sep=';', encoding="ISO-8859-1")
        # Sélectionner les 5 départements avec la population la plus élevée
        top5 = df.nlargest(5, 'population')[['com_code', 'Nom']]
        # Centrer le tableau
        st.write("Top 5 des départements correspondant au critère choisi :")
        st.table(top5)
        # Afficher l'histogramme pour les données de population
        st.bar_chart(df.nlargest(5, 'population').set_index('Nom')['population'])
    elif choix_critere == "Je veux vivre dans une ville avec peu d'habitants":
        # Charger les données du deuxième CSV (remplacez ce chemin par le vôtre)
        df = pd.read_csv('data_com-2.csv', sep=';',encoding="ISO-8859-1")
        # Sélectionner les 5 départements avec la population la plus faible
        top5 = df.nsmallest(5, 'population')[['com_code', 'Nom']]
        # Centrer le tableau
        st.write("Top 5 des départements correspondant au critère choisi :")
        st.table(top5)
        # Afficher l'histogramme pour les données de population
        st.bar_chart(df.nsmallest(5, 'population').set_index('Nom')['population'])
    elif choix_critere == "Je veux vivre dans un endroit chaud":
        # Charger les données du CSV contenant les informations sur la température
        df_temp = pd.read_csv('data_com-2.csv', sep=';',encoding="ISO-8859-1")
        # Convertir la colonne de température en numérique
        df_temp['temperature'] = pd.to_numeric(df_temp['temperature'], errors='coerce')
        # Sélectionner les 5 départements avec les températures les plus élevées
        top5 = df_temp.nlargest(5, 'temperature')[['com_code', 'Nom']]
        # Centrer le tableau
        st.write("Top 5 des départements correspondant au critère choisi :")
        st.table(top5)
        # Afficher l'histogramme pour les données de température
        st.bar_chart(df_temp.nlargest(5, 'temperature').set_index('Nom')['temperature'])
    # Ajoutez d'autres conditions pour les autres critères
    return top5

# Liste déroulante pour choisir un critère
choix_critere = st.selectbox('Choisissez un critère :', ["Je veux me sentir en sécurité", 
                                                        "Je veux pouvoir me balader dans diverses zones vertes",
                                                        "Je veux vivre dans une ville dense",
                                                        "Je veux vivre dans une ville peu dense",
                                                        "Je veux vivre dans une ville avec beaucoup d'habitants",
                                                        "Je veux vivre dans une ville avec peu d'habitants",
                                                        "Je veux vivre dans un endroit chaud"])

# Afficher le top 5 des départements correspondant au critère choisi
top5_departements(choix_critere)

if st.button("Partie visuel"):
    st.markdown("[Lien vers l'application visuelle](https://3f1ranalyse.streamlit.app)")
