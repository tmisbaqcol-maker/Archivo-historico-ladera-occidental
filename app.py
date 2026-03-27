from pathlib import Path
import streamlit as st

# CONFIG
st.set_page_config(page_title="Zona Suroccidente – Barranquilla", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
IMG_CARTO = BASE_DIR / "cartografia_1988"

def show_image(path, caption=None):
    if Path(path).exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"No se encontró la imagen: {path}")

# ESTILOS
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #1f3b73 0%, #2c5aa0 100%);
    color: white;
    padding: 2rem;
    border-radius: 18px;
    margin-bottom: 1.5rem;
}
.slide-card {
    background: white;
    padding: 1.5rem;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 1rem;
}
.metric-box {
    background: #eef3fb;
    border-left: 6px solid #2c5aa0;
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 0.8rem;
}
.risk-box {
    background: #fff4f4;
    border-left: 6px solid #c62828;
    padding: 1rem;
    border-radius: 12px;
}
.loss-box {
    background: #fff8e8;
    border-left: 6px solid #ef6c00;
    padding: 1rem;
    border-radius: 12px;
}
.big-number {
    font-size: 2rem;
    font-weight: bold;
    color: #1f3b73;
}
</style>
""", unsafe_allow_html=True)

# NAVEGACIÓN
slides = ["Portada", "Slide 1", "Slide 2", "Slide 4", "Slide 5"]

if "slide" not in st.session_state:
    st.session_state.slide = slides[0]

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("◀"):
        i = slides.index(st.session_state.slide)
        st.session_state.slide = slides[max(0, i-1)]

with col2:
    st.session_state.slide = st.radio("", slides, index=slides.index(st.session_state.slide), horizontal=True)

with col3:
    if st.button("▶"):
        i = slides.index(st.session_state.slide)
        st.session_state.slide = slides[min(len(slides)-1, i+1)]

slide = st.session_state.slide

# PORTADA
if slide == "Portada":
    st.markdown("""
    <div class="hero">
        <h1>Zona Suroccidente – Barranquilla</h1>
        <h3>Factores estructurales y dinámicas territoriales</h3>
    </div>
    """, unsafe_allow_html=True)

# SLIDE 1
elif slide == "Slide 1":
    st.markdown("""
    <div class="hero"><h2>EL PROBLEMA DE LA EROSIÓN</h2></div>
    <div class="slide-card">
    Falta de planeación → Urbanizaciones piratas<br><br>
    Servicios incompletos:
    <ul>
    <li>Fugas de agua</li>
    <li>Pozas sépticas</li>
    <li>Basuras</li>
    </ul>
    Descobertura vegetal<br>
    Arroyos (invierno)
    </div>
    """, unsafe_allow_html=True)

# SLIDE 2
elif slide == "Slide 2":
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="metric-box"><div class="big-number">231.000</div>Afectados</div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-box"><div class="big-number">54.200</div>Directos</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="risk-box">
        Zonas:
        <ul>
        <li>Villate</li>
        <li>Bajo Valle</li>
        <li>La Libertad</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# SLIDE 4
elif slide == "Slide 4":
    col1, col2 = st.columns(2)
    with col1:
        show_image(BASE_DIR / "newplot (2).png", "Perfil")
    with col2:
        show_image(BASE_DIR / "newplot (3).png", "3D")

# SLIDE 5 (CARTOGRAFÍA)
elif slide == "Slide 5":

    st.markdown("### Zonas críticas identificadas en cartografía histórica (1988)")

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    with col1:
        show_image(IMG_CARTO / "Croquis_general.jpeg", "Croquis general")

    with col2:
        show_image(IMG_CARTO / "Villate.jpeg", "Villate")

    with col3:
        show_image(IMG_CARTO / "La_Manga.jpeg", "La Manga")

    with col4:
        show_image(IMG_CARTO / "Manga_Zona_Critica.jpeg", "Zona crítica")

    with col5:
        show_image(IMG_CARTO / "La_Libertad.jpeg", "La Libertad")

    with col6:
        show_image(IMG_CARTO / "Bajo_Valle.jpeg", "Bajo Valle")

st.caption("Cartografía histórica 1988 – análisis territorial")
