import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")

st.image('./images/logotransparente.png', width=230)
st.image('./images/principal.jpg')


st.markdown("### Analisis profundo de los Flujos Migratorios")

st.markdown("* Se nos consulto para poder analisar la data de los Flujos Migratorios y poder hallar insights que respondan a los siguientes objetivos ")  

st.markdown("* OBJETIVOS : ")

st.markdown("* 1. Analizar a los migrantes en Estados Unidos y Latinoamérica para identificar patrones y tendencias de migración.")
st.markdown("* 2. Identificar las principales razones por las cuales las personas migran de un país a otro.")
st.markdown("* 3. Analizar la situación económica de los migrantes para comprender como la migración afecta la economía del país de origen y destino.")
st.markdown("* 4. Comparar el índice de felicidad de los diferentes países de Latinoamérica con el índice de felicidad de Estados Unidos.")


st.title("")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### :blue[Dashboard Flujos Migratorios]")
    st.markdown("###### Es una herramienta que ayudará a su empresa  a tener datos en de indices demograficos actualizados, para poder hacer analisis con exactitud y poder tomar mejores decisiones.")

with col2:
    st.markdown("#### :blue[Modelos de Machine Learning]")
    st.markdown("* **Modelo de Prediccion de Indice de Migracion neto:** Ayuda a predecir la tasa de migracion neta en cada pais y con respecto a un año en especifico.")
    st.markdown("* **Modelo de Prediccion de Indice de Desempleo:** Ayuda a predecir la tasa de desempleo en cada pais y con respecto a un año en especifico.")



