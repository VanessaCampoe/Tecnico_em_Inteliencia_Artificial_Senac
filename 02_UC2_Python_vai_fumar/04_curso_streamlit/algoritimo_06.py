# importando a biblioteca do streamlit
import streamlit as st
# importando a biblioteca matemática
import math

# inserindo um título do aplicativo
st.title("Calculadora de Raiz Quadrada")

# Entrada do número
numero = st.number_input("Digite um número:", min_value=0.0, step=0.1)

# Botão para calcular
if st.button("Calcular Raiz Quadrada"):
    if numero >= 0:
        resultado = math.sqrt(numero)
        st.success(f"A raiz quadrada de {numero} é {resultado:.4f}")
    else:
        st.error("Por favor, insira um número não negativo.")
