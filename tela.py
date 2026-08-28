import streamlit as st
st.image("logo.png", width=200)
if "carrinho" not in st.session_state:
 st.session_state["carrinho"] = []
st.title("Sistema de Orçamento - Alumínio")
st.write("---")
estoque_perfis = {       
        "MP 357": 3.800/6,
        "MP 358": 3.600/6,
        "MP 360": 2.600/6, 
        "MP 300": 2.000/6,
        "MP 309": 2.100/6,
        "MP 321": 2.800/6, 
        "MP 302": 2.500/6, 
        "BG 202": 0.650/6, 
        "MP 352": 1.100/6,  
        "MP 332": 3.000/6,
        "25026": 3.900/6, 
        "BX 157": 3.000/6,
        "BX 158": 1.000/6,
        "BX 116": 1.200/6,
        "BX 156": 1.200/6,
        "BX 159": 1.000/6,
        "BX 850": 2.200/6,
        "BX 089": 1.250/6,
        "BX 085": 1.000/6,
        "BX 087": 1.000/6,
        "BX 090": 1.000/6,
        "PC 026": 3.400/6,
        "AD 001": 3.400/6,
        "AD 004": 2.800/6,
        "19 652": 4.100/6,
        "PU 639": 1.700/6,
        "25 617": 2.000/6,    
        "TG 074": 1.200/6, 
        "TG 004": 2.100/6,
        "PT 008": 1.000/6,    
        "TR 004": 0.600/6,
        "TR 011": 0.800/6,   
        "TR 038": 1.100/6,
        "TQ 022": 1.500/6,
        "TQ 018": 3.300/6,   
        "TR 001": 0.300/6,
        "TR 018": 0.900/6,
        "JH 073": 2.100/6,   
        "BG 035": 0.700/6,   
        "25 301": 2.05/6,
        "25 312": 1.800/6,
        "25 311": 1.700/6,
        "MM 375": 2.350/6,
        "MM 376": 3.000/6,
        "NU 990": 3.250/6,
        "P 068": 4.500/6,
        "CG 083": 7.100/6,
        "CG 077": 5.100/6,
        "CG 075": 3.100/6,
        "CG 074": 1.600/6,
        "25 504": 2.660/6,
        "25 002": 1.600/6,
        "25 508": 4.000/6,
        "BG 001": 0.650/6,
        "SU 001": 4.000/6,
        "SU 002": 3.700/6,
        "SU 003": 3.100/6,
        "SU 055": 3.100/6,
        "SU 056": 3.300/6,
        "SU 186": 3.100/6,
        "TQ 005": 1.200/6,
        "CM 063": 1.000/6,
        "30 044": 1.500/6,
        "CG 003": 3.300/6,
        "RP 610": 4.300/6,
        "AL 001": 2.700/6,
        "AL 002": 1.300/6,
        "AL 003": 1.650/6,
        "AL 027": 0.350/6,
        "AL 004": 3.300/6,
        "AL 005": 1.600/6,
        "AL 006": 1.750/6,
        "AL 007": 0.500/6,
        "AL 076": 2.200/6,
        "AL 067": 0.700/6,
        "AL 068": 0.800/6,   
        }

perfil = st.selectbox("Escolha o Perfil:", list(estoque_perfis.keys()))

peso_metro = estoque_perfis[perfil]


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

if st.button("Adicionar ao Orçamento"):
    peso_total = metros * peso_metro
    valor_final = peso_total * preco_kg
    
    item = {
        "Perfil": perfil,
        "Cor": cor,
        "Metros": metros,
        "Peso (kg)": round(peso_total, 3),
        "Valor (R$)": round(valor_final, 2)
    }
    st.session_state["carrinho"].append(item)
    st.success("Item adicionado com sucesso!")

st.write("---") 
st.write("**🛒 Itens no Orçamento:**")

if len(st.session_state["carrinho"]) > 0:
    st.table(st.session_state["carrinho"])
    
    peso_pedido = sum(linha["Peso (kg)"] for linha in st.session_state["carrinho"])
    valor_pedido = sum(linha["Valor (R$)"] for linha in st.session_state["carrinho"])
    
    st.info(f"**PESO TOTAL:** {peso_pedido:.3f} kg")
    st.success(f"**VALOR TOTAL DO PEDIDO: R$ {valor_pedido:.2f}**")
    
    if st.button("Limpar Carrinho"):
        st.session_state["carrinho"].clear()
        st.rerun()