# -*- coding: utf-8 -*-
"""lagnchain

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CKenWUB5LyMcJ6Q6AXcMvcGzJGVxQzao
"""

import os
import pandas as pd
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Função para analisar o relatório
class RelatorioFinanceiroAnalyzer:
    def __init__(self):
        # Passe a chave da API diretamente aqui
        self.llm = OpenAI(api_key="org-ycOurawIUBUyn1iUMfHp64Sd", model="text-davinci-003")

        self.prompt = PromptTemplate(
            input_variables=["documento"],
            template="Por favor, analise o seguinte relatório financeiro e forneça um resumo detalhado:\n\n{documento}",
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def analisar_relatorio(self, documento):
        try:
            # Analisar o relatório usando a cadeia de análise
            resultado = self.chain.run(documento=documento)
            return resultado

        except Exception as e:
            st.error(f"Erro ao processar o documento: {e}")

# Configuração do Streamlit
st.title("Analisador de Relatório Financeiro")
st.write("Faça upload de um arquivo CSV contendo o relatório financeiro para análise.")

uploaded_file = st.file_uploader("Escolha o arquivo CSV", type="csv")

if uploaded_file is not None:
    try:
        # Carregar o relatório financeiro CSV
        df = pd.read_csv(uploaded_file)

        # Converter o dataframe em uma string para análise
        documentos = df.to_string()

        # Analisar o relatório financeiro
        analyzer = RelatorioFinanceiroAnalyzer()
        resultado_analise = analyzer.analisar_relatorio(documentos)

        if resultado_analise:
            st.subheader("Resultado da Análise")
            st.write(resultado_analise)
    except pd.errors.EmptyDataError:
        st.error("O arquivo CSV está vazio.")
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")