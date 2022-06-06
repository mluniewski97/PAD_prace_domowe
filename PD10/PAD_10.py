import streamlit as st
import plotly.express as px
import pandas as pd
import time

#strona glowna, 2 zakladki
st.header("PAD 10")
page = st.selectbox("'Wybierz stronę:", ["Ankieta", "Staty"]) 

#ankieta
if page == 'Ankieta':
    st.title("Ankieta")
    name = st.text_input('Imię: ')
    surname = st.text_input('Nazwisko: ')

    if st.button('OK'):
        if name.isalpha() and surname.isalpha():
            with open('ankieta.csv', 'a') as file:
                file.write(','.join([name, surname]))
                file.write('\n')
                file.close()
            st.success('Dane zostaly zapisane')
        else:
            st.error('Niepoprawne dane, prosze sprawdz je')

#staty
if page == 'Staty':
    st.title("Staty")
    csv_file = st.file_uploader('Wczytaj dane', type=['csv'])

    if csv_file is not None:
        with st.spinner('Przetwarzanie'):
            time.sleep(2)
            df = pd.read_csv(csv_file, sep=',')
        st.dataframe(df)

        type = st.selectbox('Wybierz rodzaj wykresu: ', ('Punktowy', 'Kolowy'))
        vars = tuple(x for x in df.columns if df[x].dtype in ['str', 'object'])

        if type == 'Punktowy':
            variable = st.selectbox('Zmienna: ', vars)
            df_counts = df[variable].value_counts().reset_index()
            scatter = px.scatter(df_counts, x='index', y=variable)
            st.plotly_chart(scatter)

        elif type == 'Kolowy':
            variable = st.selectbox('Zmienna: ', vars)
            df_counts = df[variable].value_counts().reset_index()
            pie = px.pie(df_counts, values=variable, names=variable)
            st.plotly_chart(pie)