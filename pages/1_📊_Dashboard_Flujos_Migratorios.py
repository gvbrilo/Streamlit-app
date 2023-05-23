# Librerías
import streamlit as st
import streamlit.components.v1 as components


# Hace más ancha la página
st.set_page_config(layout="wide")

# Encabezado
components.html("""
<div>
    <style>
        .box {
            width: 1250px;
            font-family: Arial, Helvetica, sans-serif;
        }
        .heading{
            background-color:blueviolet;
            color:lightyellow;
            border-radius: 20px;
            text-align:center;
        }
    </style>
    <div class="box">
    <h1>
        Dashboard Flujos Migratorios
    </h1>
    <p>
        Contar con un herramienta tecnológica como un dashboard de flujos migratorios, es muy útil, ya que en tiempo real estamos recibiendo miles de datos limpios y filtrados que serán muy importantes para poder tomar decisiones informadas, asertivas y con mayor rapidez, en un ámbito hospitalario el tiempo es vital.
    </p>
    </div>
</div>
""")

#Embeber dashboard
components.iframe("https://app.powerbi.com/reportEmbed?reportId=3e87ef0a-e7af-4820-834b-3ae6f985da8f&autoAuth=true&ctid=c9553b71-e9f5-4264-9080-f30bc2ddf506 ", 
                  width=1300, height=2850, scrolling=False)

