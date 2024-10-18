import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar os dados
df = pd.read_csv('Producao_de_mel_2023_limpo.csv')
df = df.drop(0)  # Remove a linha extra de cabeçalho

# Ajustar os tipos de dados
df['Produção 2023 L'] = pd.to_numeric(df['Produção 2023 L'], errors='coerce')
df['Produção 2023 Kg'] = pd.to_numeric(df['Produção 2023 Kg'], errors='coerce')

# Título do App
st.title("Dashboard de Produção de Mel - 2023")

# Filtro de Produtor
produtor_selecionado = st.selectbox('Selecione o Produtor', df['PRODUTOR'].unique())

# Filtrar dados para o produtor selecionado
filtered_df = df[df['PRODUTOR'] == produtor_selecionado]

# Gráfico de barras - Produção total do produtor selecionado
st.subheader(f'Produção Total de {produtor_selecionado}')
fig_bar = px.bar(filtered_df, x='PRODUTOR', y=['Produção 2023 L', 'Produção 2023 Kg'])
st.plotly_chart(fig_bar)

# Gráfico de linha - Produção ao longo das colheitas
st.subheader(f'Produção ao longo das colheitas - {produtor_selecionado}')
colheitas = ['1ª Colheita', '2ª  Colheita', '3ª  Colheita', '4ª  Colheita', '5ª  Colheita', '6ª Colheita']
fig_line = px.line(filtered_df, x=colheitas, y=filtered_df[colheitas].values[0])
st.plotly_chart(fig_line)
