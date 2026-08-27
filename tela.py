import streamlit as st
st.title("Sistema de Orçamento - Alumínio")
st.write("---")
perfil = st.selectbox("Escolha o Perfil:", ["25504", "Bg001", "25002", "25508", "25510", "25001", "25016", "Ad004"])
preco_kg = 0
if perfil == "25504":
    peso_metro = 0.425
elif perfil == "Bg001":
    peso_metro = 0.100
elif perfil == "25002":
    peso_metro = 0.500
elif perfil == "25508":
    peso_metro = 0.650  
elif perfil == "25510":
    peso_metro = 0.166  
elif perfil == "25001":
    peso_metro = 0.283
elif perfil == "25016":
    peso_metro = 0.240
elif perfil == "Ad004":
    peso_metro = 0.483

cor = st.selectbox("Escolha a Cor:", ["Branco", "Fosco", "Preto", "Bronze"]) 
preco_kg = 0   

if cor == "Branco":
        preco_kg = 45
elif cor == "Fosco":
    preco_kg = 45
elif cor == "Preto":
    preco_kg = 50
elif cor == "Bronze":
    preco_kg = 50   
metros = st.number_input("quantos metros o cliente vai querer?", min_value=0.0)

if st.button("Gerar Orçamento"):
    peso_total = metros * peso_metro
    valor_final = peso_total * preco_kg
    st.success(f"Peso total: {peso_total} kg")
    st.success(f"Valor desta peça: R$ {valor_final}")
