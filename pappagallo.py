import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(
    page_title="Pappagallo - Assistant Intelligent",
    page_icon="🦜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour l'arrière-plan et le style
st.markdown("""
    <style>
    /* Arrière-plan avec image de perroquet */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Overlay semi-transparent pour améliorer la lisibilité */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.7), rgba(147, 51, 234, 0.7));
        z-index: 0;
    }
    
    /* Assurer que le contenu est au-dessus de l'overlay */
    .main > div {
        position: relative;
        z-index: 1;
    }
    
    /* Style de la sidebar */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(15px);
        border-right: 2px solid rgba(79, 70, 229, 0.3);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Style du titre */
    .title-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Container pour le bot */
    .bot-container {
        background: rgba(255, 255, 255, 0.98);
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.4);
    }
    
    /* Cacher le footer Streamlit */
    footer {
        visibility: hidden;
    }
    
    /* Style du header */
    header {
        background: transparent !important;
    }
    
    /* Animation du titre */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .title-container {
        animation: fadeIn 0.8s ease-out;
    }
    
    /* Style des éléments de la sidebar */
    .sidebar-content {
        padding: 1rem;
        background: rgba(79, 70, 229, 0.1);
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🦜 À propos de Pappagallo")
    
    st.markdown("""
    <div class="sidebar-content">
        <h4 style="color: #4f46e5; margin-top: 0;">👋 Qui suis-je ?</h4>
        <p style="font-size: 0.9rem; line-height: 1.6;">
        Je suis <strong>Pappagallo</strong>, votre assistant de motivation et de productivité !
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mes capacités")
    
    st.markdown("""
    <div style="background: rgba(79, 70, 229, 0.05); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;">
        <strong>💪 Motivation & Productivité</strong><br>
        <small>Je vous aide à rester motivé et productif au travail</small>
    </div>
    
    <div style="background: rgba(147, 51, 234, 0.05); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;">
        <strong>💬 Discussion Amicale</strong><br>
        <small>On peut parler de tout et de rien ensemble</small>
    </div>
    
    <div style="background: rgba(79, 70, 229, 0.05); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;">
        <strong>🌍 Géographie & Culture</strong><br>
        <small>Je partage des connaissances sur le monde</small>
    </div>
    
    <div style="background: rgba(147, 51, 234, 0.05); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;">
        <strong>🎲 Quiz Interactifs</strong><br>
        <small>Testez vos connaissances avec mes quiz</small>
    </div>
    
    <div style="background: rgba(79, 70, 229, 0.05); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;">
        <strong>🤝 Personnalisation</strong><br>
        <small>Je m'adapte à vous pour une meilleure expérience</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### ✨ Conseils d'utilisation")
    
    st.info("""
    **💡 Pour bien commencer :**
    - Présentez-vous pour que je puisse personnaliser nos échanges
    - Posez-moi des questions sur la productivité
    - Demandez-moi un quiz pour tester vos connaissances
    - Partagez vos défis, je suis là pour vous encourager !
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Limitations")
    
    st.warning("""
    **Note importante :**
    Je ne peux pas fournir de conseils médicaux ou psychologiques professionnels. Pour ces questions, consultez un professionnel qualifié.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #4f46e5, #9333ea); 
                border-radius: 10px; color: white; margin-top: 1rem;">
        <p style="margin: 0; font-weight: 600;">🦜 Pappagallo</p>
        <p style="margin: 0.3rem 0 0 0; font-size: 0.85rem;">Propulsé par Botpress</p>
    </div>
    """, unsafe_allow_html=True)

# En-tête avec le nom du bot
st.markdown("""
    <div class="title-container">
        <h1 style="text-align: center; color: #4f46e5; margin-bottom: 0.5rem; font-size: 3rem;">
            🦜 Pappagallo
        </h1>
        <p style="text-align: center; color: #6b7280; font-size: 1.2rem; margin-bottom: 0;">
            Votre assistant de motivation et de productivité
        </p>
        <p style="text-align: center; color: #9ca3af; font-size: 0.95rem; margin-top: 0.5rem;">
            💪 Motivation • 📈 Productivité • 🌍 Culture • 🎲 Quiz
        </p>
    </div>
""", unsafe_allow_html=True)

# Container principal pour le bot
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown('<div class="bot-container">', unsafe_allow_html=True)
    
    # Intégration du bot Botpress Pappagallo
    botpress_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            #webchat-container {
                width: 100%;
                height: 650px;
                border-radius: 15px;
                overflow: hidden;
            }
            iframe {
                border: none;
                border-radius: 15px;
            }
        </style>
    </head>
    <body>
        <div id="webchat-container">
            <iframe 
                src="https://cdn.botpress.cloud/webchat/v3.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/12/04/08/20251204082457-PV379E8F.json"
                width="100%"
                height="100%"
                frameborder="0">
            </iframe>
        </div>
    </body>
    </html>
    """
    
    components.html(botpress_html, height=650)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Informations supplémentaires
st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <div style="display: inline-block; background: rgba(255, 255, 255, 0.95); 
                    padding: 1.5rem 3rem; border-radius: 15px; 
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
                    backdrop-filter: blur(10px);">
            <p style="margin: 0; color: #4f46e5; font-weight: 600; font-size: 1.1rem;">
                🦜 Commencez la conversation et boostez votre productivité !
            </p>
            <p style="margin: 0.5rem 0 0 0; color: #6b7280; font-size: 0.9rem;">
                Disponible 24/7 pour vous accompagner
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
