from pathlib import Path
import streamlit as st

# -------------------------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------------------------
st.set_page_config(
    page_title="Zona Suroccidente – Barranquilla",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent
IMG_CARTO = BASE_DIR / "Cartografia_1988"
IMG_FOTOS = BASE_DIR / "Fotografia_1988"

def show_image(path, caption=None):
    img_path = Path(path)
    if not img_path.is_absolute():
        img_path = BASE_DIR / path
    if img_path.exists():
        st.image(str(img_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"No se encontró la imagen: {img_path}")

def get_images_from_folder(folder: Path):
    extensiones = {".jpg", ".jpeg", ".png", ".webp"}
    if not folder.exists():
        return []
    return sorted([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in extensiones])

# -------------------------------------------------
# ESTILOS
# -------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: "Arial", sans-serif;
}
.main {
    background-color: #f7f7f7;
}
.block-container {
    padding-top: 1.6rem;
    padding-bottom: 2rem;
    max-width: 1180px;
}
.hero {
    background: linear-gradient(135deg, #1f3b73 0%, #2c5aa0 100%);
    color: white;
    padding: 2rem 2.2rem;
    border-radius: 18px;
    margin-bottom: 1.4rem;
}
.slide-card {
    background: white;
    padding: 1.5rem 1.6rem;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 1rem;
}
.metric-box {
    background: #eef3fb;
    border-left: 6px solid #2c5aa0;
    padding: 1rem 1.1rem;
    border-radius: 12px;
    margin-bottom: 0.8rem;
}
.risk-box {
    background: #fff4f4;
    border-left: 6px solid #c62828;
    padding: 1rem 1.1rem;
    border-radius: 12px;
    margin-bottom: 0.9rem;
}
.loss-box {
    background: #fff8e8;
    border-left: 6px solid #ef6c00;
    padding: 1rem 1.1rem;
    border-radius: 12px;
    margin-bottom: 0.8rem;
}
.info-box {
    background: #f6f7fb;
    border-left: 6px solid #5b6b8c;
    padding: 1rem 1.1rem;
    border-radius: 12px;
    margin-bottom: 0.8rem;
}
.big-number {
    font-size: 2rem;
    font-weight: 700;
    color: #1f3b73;
    line-height: 1.1;
}
.small-note {
    font-size: 0.95rem;
    color: #4a5568;
}
.centered {
    text-align: center;
}
ul {
    margin-top: 0.35rem;
    margin-bottom: 0.35rem;
}
h1, h2, h3, h4 {
    margin-top: 0;
}
.album-wrap {
    background: linear-gradient(180deg, #efe5d0 0%, #e7dbc1 100%);
    border-radius: 20px;
    padding: 1.2rem;
    box-shadow: inset 0 0 0 1px rgba(90,70,40,.12), 0 6px 22px rgba(0,0,0,.08);
    margin-bottom: 1.2rem;
}
.album-title {
    text-align: center;
    font-size: 1.35rem;
    font-weight: 700;
    color: #5b4325;
    margin-bottom: .35rem;
}
.album-subtitle {
    text-align: center;
    color: #6a5840;
    font-size: .98rem;
    margin-bottom: 1rem;
}
.polaroid {
    background: #fffdf8;
    padding: .7rem .7rem 1rem .7rem;
    border-radius: 8px;
    box-shadow: 0 8px 20px rgba(0,0,0,.16);
    transform: rotate(-1deg);
    margin-bottom: 1rem;
    border: 1px solid #ece3d1;
}
.polaroid:nth-child(2n) {
    transform: rotate(1.2deg);
}
.photo-note {
    text-align: center;
    font-size: .92rem;
    color: #5d4c33;
    margin-top: .45rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# NAVEGACIÓN
# -------------------------------------------------
slides = ["Portada", "Slide 1", "Slide 2", "Slide 4", "Slide 5", "Slide 6"]

if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

nav1, nav2, nav3 = st.columns([1, 2.8, 1])

with nav1:
    if st.button("◀ Anterior", use_container_width=True):
        st.session_state.slide_idx = max(0, st.session_state.slide_idx - 1)

with nav2:
    selected = st.radio(
        "Navegación",
        slides,
        index=st.session_state.slide_idx,
        horizontal=True,
        label_visibility="collapsed"
    )
    st.session_state.slide_idx = slides.index(selected)

with nav3:
    if st.button("Siguiente ▶", use_container_width=True):
        st.session_state.slide_idx = min(len(slides) - 1, st.session_state.slide_idx + 1)

slide = slides[st.session_state.slide_idx]

# -------------------------------------------------
# PORTADA
# -------------------------------------------------
if slide == "Portada":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.35rem;">Zona Suroccidente – Barranquilla</h1>
        <h3 style="margin-top:0; font-weight:400; opacity:0.96;">Factores estructurales y dinámicas territoriales</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="slide-card">
        <h3>Presentación ejecutiva</h3>
        <p>Esta presentación sintetiza el problema histórico de erosión en la zona suroccidental de Barranquilla, su impacto poblacional y económico, y la evidencia cartográfica utilizada para interpretar la dinámica territorial del riesgo en 1988.</p>
        <p>Use la navegación superior para recorrer las diapositivas.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# SLIDE 1
# -------------------------------------------------
elif slide == "Slide 1":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.35rem;">Slide 1</h1>
        <h2 style="margin-top:0; font-weight:600;">EL PROBLEMA DE LA EROSIÓN EN LA ZONA SUR-OCC.</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <div class="slide-card">
            <h3>Generadores del problema</h3>
            <p><strong>Falta de planeación</strong><br>
            ↓<br>
            <strong>Urbanizaciones piratas en zonas no aptas</strong></p>

            <p><strong>Servicios incompletos</strong><br>
            a) Fugas de agua<br>
            b) Pozas sépticas<br>
            c) Basuras</p>

            <p><strong>Descobertura vegetal</strong></p>

            <p><strong>Arroyos</strong><br>
            <em>(Nacimientos de agua – invierno)</em></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="risk-box">
            <h3>Lectura sintética</h3>
            <p>La erosión aparece como resultado de la interacción entre ocupación informal del suelo, déficit de servicios básicos, pérdida de cobertura vegetal y presión hídrica estacional.</p>
        </div>
        <div class="metric-box">
            <h3>Cadena causal</h3>
            <p>Falta de planeación → Urbanización en zonas no aptas → Servicios incompletos → Erosión</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------
# SLIDE 2
# -------------------------------------------------
elif slide == "Slide 2":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.35rem;">Slide 2</h1>
        <h2 style="margin-top:0; font-weight:600;">Impacto poblacional, zonas críticas y pérdidas</h2>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="slide-card"><h3>Impacto poblacional total</h3>', unsafe_allow_html=True)
        st.markdown('<div class="metric-box"><div class="big-number">231.000</div><div>Habitantes en zonas afectadas por erosión y arroyos</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-box"><div class="big-number">54.200</div><div>Habitantes afectados directamente por erosión</div><div><strong>Equivalente a 10.800 familias</strong></div></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="risk-box">
            <h3>Evento crítico (Invierno 1988)</h3>
            <p>
            Familias censadas: <strong>1.250</strong><br>
            Familias en alto riesgo: <strong>750</strong><br>
            Total afectadas: <strong>2.000 familias</strong><br>
            Equivalente aproximado: <strong>10.000 habitantes</strong>
            </p>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="slide-card">
            <h3>Zonas de alto riesgo</h3>
            <ul>
                <li>Me Quejo – (Base del) Silencio</li>
                <li>Carlos Meisel I y II</li>
                <li>Florida – Mercedes Sur</li>
                <li>Bajas de San Felipe</li>
                <li>Villate</li>
                <li>Bajo Valle</li>
                <li>La Libertad – Nueva Colombia</li>
                <li>Terrazas – Villa Rosario</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="slide-card">
        <h3>Pérdidas aproximadas por erosión (1987–1988)</h3>
    </div>
    """, unsafe_allow_html=True)

    l1, l2, l3 = st.columns(3)

    with l1:
        st.markdown("""
        <div class="loss-box">
            <h4>Vivienda</h4>
            <div class="big-number">$700.000.000</div>
            <div>Setecientos millones de pesos</div>
        </div>
        """, unsafe_allow_html=True)

    with l2:
        st.markdown("""
        <div class="loss-box">
            <h4>Infraestructura</h4>
            <div class="big-number">$200.000.000</div>
            <div>Pavimento, energía, redes, etc.</div>
        </div>
        """, unsafe_allow_html=True)

    with l3:
        st.markdown("""
        <div class="loss-box">
            <h4>Total</h4>
            <div class="big-number">$900.000.000</div>
            <div>Periodo 1987–1988</div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------
# SLIDE 4
# -------------------------------------------------
elif slide == "Slide 4":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.35rem;">Slide 4</h1>
        <h2 style="margin-top:0; font-weight:600;">Aproximación de ubicación de barrios en la ladera sur-occ (1988)</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="slide-card">
        <h3>Modelo 3D conceptual</h3>
        <p>Representación aproximada de la secuencia territorial de barrios sobre la ladera occidental, con énfasis en gradiente de altura y exposición al riesgo.</p>
    </div>
    """, unsafe_allow_html=True)

    col_img1, col_img2 = st.columns(2)

    with col_img1:
        show_image(BASE_DIR / "newplot (2).png", "Perfil longitudinal de la ladera (vista lateral)")

    with col_img2:
        show_image(BASE_DIR / "newplot (3).png", "Vista 3D de la ladera y ubicación de barrios")

    st.markdown("""
    <div class="risk-box">
        <h3>Lectura territorial</h3>
        <p>La distribución de barrios a lo largo de la pendiente evidencia una relación directa entre altura, ocupación informal y exposición al riesgo de erosión.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# SLIDE 5
# -------------------------------------------------
elif slide == "Slide 5":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.35rem;">Slide 5</h1>
        <h2 style="margin-top:0; font-weight:600;">Análisis cartográfico de deslizamientos (1988)</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="slide-card">
        <h3>Lectura espacial de eventos de remoción en masa</h3>
        <p>Cartografía histórica intervenida que evidencia zonas críticas de deslizamientos, trazas de escorrentía y ocupación en ladera.</p>
        <p class="small-note">Las imágenes se cargan desde la carpeta <strong>Cartografia_1988</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h4>Secuencia cartográfica</h4>
        <p>Croquis general del sistema de ladera y detalle de sectores críticos: Villate, La Libertad, Bajo Valle y dos piezas de análisis sobre La Manga / zona crítica.</p>
    </div>
    """, unsafe_allow_html=True)

    row1 = st.columns(3)
    row2 = st.columns(3)

    with row1[0]:
        show_image(IMG_CARTO / "Croquis_general.jpeg", "Croquis general de Barranquilla (1988)")
    with row1[1]:
        show_image(IMG_CARTO / "Villate.jpeg", "Zona crítica – Villate")
    with row1[2]:
        show_image(IMG_CARTO / "La_Manga.jpeg", "Barrio La Manga")

    with row2[0]:
        show_image(IMG_CARTO / "Manga_Zona_Critica.jpeg", "Zona crítica en La Manga")
    with row2[1]:
        show_image(IMG_CARTO / "La_Libertad.jpeg", "Zona crítica – La Libertad")
    with row2[2]:
        show_image(IMG_CARTO / "Bajo_Valle.jpeg", "Zona crítica – Bajo Valle")

    st.markdown("""
    <div class="risk-box">
        <h3>Interpretación técnica</h3>
        <p>Las intervenciones manuales indican zonas de inestabilidad, direcciones probables de escorrentía y sectores con alta susceptibilidad a deslizamientos, permitiendo reconstruir la lógica territorial del riesgo identificada en 1988.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# SLIDE 6 - ÁLBUM FOTOGRÁFICO
# -------------------------------------------------
elif slide == "Slide 6":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.35rem;">Slide 6</h1>
        <h2 style="margin-top:0; font-weight:600;">Álbum fotográfico histórico (1988)</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="album-wrap">
        <div class="album-title">Registro fotográfico de campo</div>
        <div class="album-subtitle">Zona Suroccidente – Barranquilla · archivo visual histórico</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="slide-card">
        <h3>Lectura visual del archivo</h3>
        <p>Las imágenes corresponden a un registro histórico de campo asociado a la ladera occidental y a los procesos de erosión, escorrentía, ocupación en pendiente y afectación territorial observados en 1988.</p>
        <p class="small-note">La galería se carga automáticamente desde la carpeta <strong>Fotografia_1988</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

    fotos = get_images_from_folder(IMG_FOTOS)

    if not fotos:
        st.warning(f"No se encontraron imágenes en: {IMG_FOTOS}")
    else:
        st.markdown("""
        <div class="info-box">
            <h4>Álbum</h4>
            <p>Visualización automática de las fotografías disponibles en el repositorio. La disposición busca simular un álbum histórico con piezas seriadas de observación de terreno.</p>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(3)
        for i, foto in enumerate(fotos):
            with cols[i % 3]:
                st.markdown('<div class="polaroid">', unsafe_allow_html=True)
                st.image(str(foto), use_container_width=True)
                st.markdown(
                    f'<div class="photo-note">{foto.stem}</div>',
                    unsafe_allow_html=True
                )
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="risk-box">
            <h3>Valor analítico</h3>
            <p>Este registro fotográfico complementa la cartografía de 1988 al aportar evidencia visual sobre morfología de ladera, ocupación del suelo, trazas de agua y sectores potencialmente expuestos a remoción en masa.</p>
        </div>
        """, unsafe_allow_html=True)

st.caption("Presentación en Streamlit basada en la sistematización histórica del riesgo por erosión en la zona suroccidental de Barranquilla.")
