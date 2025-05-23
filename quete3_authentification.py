import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


lesDonneesDesComptes = {
    'usernames': {
        'djami': {
            'name': 'djami',
            'password': 'djami',
            'email': 'djamiss3@yahoo.fr',
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


authenticator.login()

def accueil():
    st.title("DJAMI")

if st.session_state["authentication_status"]:
    accueil()

    # Menu latéral
    with st.sidebar:
        selection = option_menu(
            menu_title="Home",  # Tu peux mettre None si tu ne veux pas de titre
            options=["Accueil", "Photos"]
        )

    # Affichage selon la sélection
    if selection == "Home":
        st.title("Bienvenue")

    elif selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
        st.image("eva_longoria-taille640_68239b9de5052.jpg")

    elif selection == "Photos":
        st.title("Bienvenue sur l'album photo de Shaïnez")
        st.write("Voici quelques images :")

        # Création de 3 colonnes 
        col1, col2, col3 = st.columns(3)


        # Contenu de la première colonne : 
        with col1:
            st.header("Selena")
            st.image("selena.webp")

        # Contenu de la deuxième colonne :
        with col2:
            st.header("Ariana")
            st.image("ariana.webp")

        # Contenu de la troisième colonne : 
        with col3:
            st.header("TINI")
            st.image("tini.jfif")

    # Le bouton de déconnexion
        authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


