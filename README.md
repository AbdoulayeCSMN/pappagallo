# 🦜 Pappagallo – Interface Streamlit pour Botpress  
Interface web moderne permettant d’interagir avec un chatbot Botpress via une application Streamlit simple, fluide et sécurisée.

---

## 🌟 Présentation du projet

Pappagallo est un **assistant de motivation, productivité et culture générale** destiné au milieu professionnel.  
Ce projet combine :

- **Botpress** → pour créer, entraîner et gérer le comportement du chatbot  
- **Streamlit** → pour offrir une interface élégante, moderne, responsive et impossible à manipuler côté utilisateur

L’objectif est de permettre aux employés d’accéder facilement au bot depuis une interface type *app mobile*, sans modifier l’URL ou la configuration du bot.

---

## 🎯 Fonctionnalités principales

### ✔️ Interface utilisateur
- 🎨 **UI moderne et pleine page** (style application mobile)
- 🖼️ **Image d’arrière-plan personnalisée**
- 🤖 **Logo du bot affiché dans le header**
- 💬 **Effet typing** pour les réponses du bot
- 📱 **Parfaitement responsive**

### ✔️ Sécurité
- 🔒 **Aucune possibilité de changer l'URL du bot**
- 🔧 Configuration interne totalement verrouillée

### ✔️ Technique
- ⚡ App Streamlit ultra-légère
- 🔌 Connexion directe à l’API Botpress
- 🎚️ Custom CSS intégré pour un rendu professionnel

---

## 📁 Structure du projet
```tree
/Pappagallo
│── pappagallo.py # Application Streamlit
│── requirements.txt # Dépendances Python
│── README.md # Documentation
```

---

## 🛠️ Installation

### 1️⃣ Installer Python (si pas déjà fait)

Téléchargez Python 3.10+ depuis :  
https://www.python.org/downloads/

### 2️⃣ Installer les dépendances

Assurez-vous d’être dans le dossier du projet :

```bash
pip install -r requirements.txt
pip install streamlit requests
streamlit run pappagallo.py
```
## 👤 Auteurs & Encadrement
- **Projet réalisé par :** Abdoulaye Chaïbou Saïdou  
- **Encadré par :** Idrisse Barbara

---