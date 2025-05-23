import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu

with st.sidebar:
    selection = option_menu(
        menu_title="Accueil",  # Tu peux mettre None si tu ne veux pas de titre
        options=["Accueil", "Photos"]
    )

# Afficher le contenu dans la zone principale selon la sélection
if selection == "Accueil":
    st.title("Bienvenue sur la page d'accueil !")
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.title("Bienvenue sur mon album photo")
    st.write("Bienvenue sur mon album photo")


# Création de 3 colonnes 
col1, col2, col3 = st.columns(3)

# Création de deux colonnes où col2 est deux fois plus large que col1 :
col1, col2 = st.columns([1, 2])

# Contenu de la première colonne : 
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

# Contenu de la deuxième colonne :
with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

# Contenu de la troisième colonne : 
with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")


  import streamlit as st

# On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
# L'utilisateur peut choisir son moyen de contact préféré parmi trois options
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", # Question affichée
    ("Email", "Home phone", "Mobile phone") # Options proposées
)

# Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
with st.sidebar:
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
    add_radio = st.radio(
        "Choose a shipping method",  # Titre de la question
        ("Standard (5-15 days)", "Express (2-5 days)")  # Choix proposés
    )

import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)  