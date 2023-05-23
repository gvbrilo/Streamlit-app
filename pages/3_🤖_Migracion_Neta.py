import os

from stqdm import stqdm

from time import sleep

import numpy as np

import streamlit as st

import pandas as pd

from pandas.tseries.offsets import DateOffset

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

import pickle

button_labels = ['argentina','chile','colombia','estados unidos','guatemala','honduras','mexico','uruguay']

current_dir = os.getcwd() 

filename1 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "argentina.csv")

filename2 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "chile.csv")

filename3 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "colombia.csv")

filename4 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "el salvador.csv")

filename5 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "estados unidos.csv")

filename6 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "guatemala.csv")

filename7 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "honduras.csv")

filename8 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "mexico.csv")

filename9 = os.path.join(current_dir, "ml_models_migracion_neta", "datasets", "uruguay.csv")

df_argentina = pd.read_csv(filename1,index_col=0,parse_dates=True)

df_chile= pd.read_csv(filename2,index_col=0,parse_dates=True)

df_colombia = pd.read_csv(filename3,index_col=0,parse_dates=True)

df_el_salvador = pd.read_csv(filename4,index_col=0,parse_dates=True)

df_estados_unidos = pd.read_csv(filename5,index_col=0,parse_dates=True)

df_guatemala = pd.read_csv(filename6,index_col=0,parse_dates=True)

df_honduras = pd.read_csv(filename7,index_col=0,parse_dates=True)

df_mexico = pd.read_csv(filename8,index_col=0,parse_dates=True)

df_uruguay = pd.read_csv(filename9,index_col=0,parse_dates=True)

df_mexico = df_mexico.rename(columns={'méxico': 'mexico'})

dict_datasets = {'argentina':df_argentina,'chile':df_chile,'colombia':df_colombia,'el salvador':df_el_salvador, 'estados unidos':df_estados_unidos,'guatemala':df_guatemala,'honduras':df_honduras,'mexico':df_mexico,'uruguay':df_uruguay}

current_dir = os.getcwd()  

filename1m = os.path.join(current_dir, "ml_models_migracion_neta", "argentina_model")

filename2m = os.path.join(current_dir, "ml_models_migracion_neta", "chile_model")

filename3m = os.path.join(current_dir, "ml_models_migracion_neta", "colombia_model")

filename4m = os.path.join(current_dir, "ml_models_migracion_neta", "el_salvador_model")

filename5m = os.path.join(current_dir, "ml_models_migracion_neta", "estados_unidos_model")

filename6m = os.path.join(current_dir, "ml_models_migracion_neta", "guatemala_model")

filename7m = os.path.join(current_dir, "ml_models_migracion_neta", "honduras_model")

filename8m = os.path.join(current_dir, "ml_models_migracion_neta", "mexico_model")

filename9m = os.path.join(current_dir, "ml_models_migracion_neta", "uruguay_model")

argentina_model = pickle.load(open(filename1m, 'rb'))

chile_models = pickle.load(open(filename2m, 'rb'))

colombia_models = pickle.load(open(filename3m, 'rb'))

el_salvador_models = pickle.load(open(filename4m, 'rb'))

estados_unidos_models = pickle.load(open(filename5m, 'rb'))

guatemala_models = pickle.load(open(filename6m, 'rb'))

honduras_models =  pickle.load(open(filename7m, 'rb'))

mexico_models = pickle.load(open(filename8m, 'rb'))

uruguay_models = pickle.load(open(filename9m, 'rb'))

dict_model = {'argentina': argentina_model,'chile': chile_models,'colombia': colombia_models,'el salvador': el_salvador_models,'estados unidos': estados_unidos_models,'guatemala': guatemala_models,'honduras': honduras_models,'mexico': mexico_models,'uruguay': uruguay_models}

st.set_page_config(layout="centered")

active = None 

st.title(f"Prediccion de Migracion Neta en Pais")

st.markdown("## **Modelos de Machine Learning**")

country_selected = False

country = None

option = st.selectbox("Select a country",["Argentina", "Chile", "Colombia", "El Salvador", "Estados Unidos", "Guatemala", "Honduras", "Mexico", "Uruguay"])

if option :

    country_selected = True

    country = option.lower()

    st.write(f"Seleccionaste {country}")

    año_predecir = st.slider("Migracion Neta - Predicion", min_value=2022, max_value=2030, value=2025)

    df_selected = dict_datasets[f'{country}']

    train = df_selected.iloc[:46]

    test = df_selected.iloc[46:] 

    start=len(train)

    end = len(train)+len(test)-1

    if año_predecir:

        modelo = dict_model[f'{country}']

        modelo1 = dict_model[f'{country}']

        if st.button("Realizar Predicción"):

            pred = modelo.predict(start=len(df_selected),end=len(df_selected)+(año_predecir-2022)-1,typ='levels').rename('ARIMA Predictions')

            st.write(pred)

            pred1=modelo1.predict(start=start,end=end,typ='levels').rename('ARIMA Predictions')

            st.write(f'Predicciones para los proximos {año_predecir} años: ',pred)

            figure1 = plt.figure(figsize=(12,5), dpi=100)

            plt.plot(train, label='training')

            plt.plot(test, label='actual')

            plt.plot(pred, label='forecast')

            plt.title(f"Prediccion de Migracion Neta en {country} Comp - Test")

            plt.legend(loc='upper left', fontsize=8)

            plt.show()

            st.write(figure1)

            figure2 = plt.figure(figsize=(12,5), dpi=100)

            plt.plot(df_selected, label='actual')

            plt.plot(pred, label='forecast')

            plt.title(f"Prediccion de Migracion Neta en {country} Final")

            plt.legend(loc='upper left', fontsize=8)

            plt.show()

            st.write(figure2)

            st.write(f"La migración neta para el año {año_predecir} es de {pred[-1]}")

        else:
            st.write("Model is not trained. Please Press the 'Predict Button'.")

    else:
        st.write("Model is not trained. Please select a Year and train the model first.")
        
else:
        st.write("Model is not trained. Please select a country and train the model first.")


# cd PI_Grupal_09_main\PF-Migracion\Github\Streamlit

# streamlit run 🗨️_Principal.py




















































# Deploy app : https://www.youtube.com/watch?v=HKoOBiAaHGg