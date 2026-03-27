import streamlit as st

st.set_page_config(page_title="Zona Suroccidente – Barranquilla", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #f7f7f7;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}
.hero {
    background: linear-gradient(135deg, #1f3b73 0%, #2c5aa0 100%);
    color: white;
    padding: 2rem 2.2rem;
    border-radius: 18px;
    margin-bottom: 1.5rem;
}
.slide-card {
    background: white;
    padding: 1.5rem 1.7rem;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 1.2rem;
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
    margin-bottom: 1rem;
}
.loss-box {
    background: #fff8e8;
    border-left: 6px solid #ef6c00;
    padding: 1rem 1.1rem;
    border-radius: 12px;
    margin-bottom: 0.8rem;
}
.big-number {
    font-size: 2rem;
    font-weight: 700;
    color: #1f3b73;
}
ul {
    margin-top: 0.4rem;
}
</style>
""", unsafe_allow_html=True)

slides = ["Portada", "Slide 1", "Slide 2"]
if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
with col_nav1:
    if st.button("◀ Anterior", use_container_width=True):
        st.session_state.slide_idx = max(0, st.session_state.slide_idx - 1)
with col_nav2:
    selected = st.radio(
        "Navegación",
        slides,
        index=st.session_state.slide_idx,
        horizontal=True,
        label_visibility="collapsed"
    )
    st.session_state.slide_idx = slides.index(selected)
with col_nav3:
    if st.button("Siguiente ▶", use_container_width=True):
        st.session_state.slide_idx = min(len(slides) - 1, st.session_state.slide_idx + 1)

slide = slides[st.session_state.slide_idx]

if slide == "Portada":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.4rem;">Zona Suroccidente – Barranquilla</h1>
        <h3 style="margin-top:0; font-weight:400; opacity:0.95;">Factores estructurales y dinámicas territoriales</h3>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="slide-card">
        <h3>Presentación ejecutiva</h3>
        <p>Esta presentación resume el problema histórico de erosión en la zona suroccidental de Barranquilla, su impacto poblacional y económico, y la localización de las principales zonas de alto riesgo identificadas para el periodo 1987–1988.</p>
        <p>Usa la navegación superior para avanzar entre diapositivas.</p>
    </div>
    """, unsafe_allow_html=True)

elif slide == "Slide 1":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.4rem;">Slide 1</h1>
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

elif slide == "Slide 2":
    st.markdown("""
    <div class="hero">
        <h1 style="margin-bottom:0.4rem;">Slide 2</h1>
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
            <p>Familias censadas: <strong>1.250</strong><br>
            Familias en alto riesgo: <strong>750</strong><br>
            Total afectadas: <strong>2.000 familias</strong><br>
            Equivalente aproximado: <strong>10.000 habitantes</strong></p>
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
        st.markdown('<div class="loss-box"><h4>Vivienda</h4><div class="big-number">$700.000.000</div><div>Setecientos millones de pesos</div></div>', unsafe_allow_html=True)
    with l2:
        st.markdown('<div class="loss-box"><h4>Infraestructura</h4><div class="big-number">$200.000.000</div><div>Pavimento, energía, redes, etc.</div></div>', unsafe_allow_html=True)
    with l3:
        st.markdown('<div class="loss-box"><h4>Total</h4><div class="big-number">$900.000.000</div><div>Periodo 1987–1988</div></div>', unsafe_allow_html=True)

st.caption("Presentación en Streamlit basada en la sistematización histórica del riesgo por erosión en la zona suroccidental de Barranquilla.")
