import streamlit as st


maladies_db = {
    "paludisme": (
        "Le paludisme est une maladie transmise par les moustiques. Ses"
        " symptômes incluent la fièvre et des frissons."
    ),
    "diabete": "Le diabète est caractérisé par un taux élevé de sucre dans le sang.",
    "diabète": "Le diabète est caractérisé par un taux élevé de sucre dans le sang.",
    "hypertension": (
        "L'hypertension correspond à une pression artérielle trop élevée dans"
        " les artères."
    ),
}

symptomes_db = {
    "fievre": (
        "Une fièvre indique souvent que le corps lutte contre une infection."
    ),
    "fièvre": (
        "Une fièvre indique souvent que le corps lutte contre une infection."
    ),
    "toux": (
        "La toux peut être causée par une irritation, un rhume ou une allergie."
    ),
    "fatigue": (
        "La fatigue chronique peut venir d'un manque de sommeil ou d'une"
        " carence."
    ),
}

prevention_db = {
    "hygiene": (
        "Lavez-vous régulièrement les mains avec du savon et utilisez du gel"
        " hydroalcoolique."
    ),
    "eau": (
        "Buvez au moins 1,5 litre d'eau potable par jour pour rester bien"
        " hydraté."
    ),
    "moustique": (
        "Utilisez des moustiquaires imprégnées et des répulsifs pour vous"
        " protéger du paludisme."
    ),
}

st.title("Hénorisbot 🩺")
st.write(
    "Bienvenue sur Hénorisbot, votre assistant d'information médicale."
)

menu = st.radio(
    "Choisissez une catégorie :",
    [
        "Accueil",
        "1. Informations sur les maladies",
        "2. Comprendre les symptômes",
        "3. Conseils de prévention",
    ],
)

if menu == "1. Informations sur les maladies":
  choix = st.text_input(
      "Sur quelle maladie ? (ex: paludisme, diabete, hypertension)"
  ).lower()
  if choix in maladies_db:
    st.success(maladies_db[choix])
elif  menu == "2. Comprendre les symptômes":
  choix = st.text_input(
      "Quel symptôme ? (ex: fievre, toux, fatigue)"
  ).lower()
  if choix in  symptomes_db:
    st.success(symptomes_db[choix])
elif  menu == "3. Conseils de prévention":
  choix = st.text_input(
      "Quel sujet de prévention ? (ex: hygiene, eau, moustique)"
  ).lower()
  if  choix in prevention_db:
    st.success(prevention_db[choix])
