import streamlit as st
import urllib.parse
st.image("logo.png", width=200)
if "carrinho" not in st.session_state:
 st.session_state["carrinho"] = []
st.title("Sistema de Orçamento - Alumínio")
st.write("---")
estoque_cantoneiras = {
    "CT 002 L.1/2": 25.00,
    "CT 008 L.3/4": 35.00,
    "CT 017 L.1'": 45.00,
   
}

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
        "25 026": 3.900/6,
        "AL 019": 1.800/6,
        "JH 072": 9.000/6,
        "LB 050": 2.900/6,
        "SU 302": 1.350/6,
        "AL 032": 0.800/6,
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

col1, col2 = st.columns([1, 1.5])

with col1:
    tipo_venda = st.radio("Tipo de Produto:", ["Perfis (Por Peso)", "Cantoneiras (Por Peça)"], horizontal=True)
    if tipo_venda == "Perfis (Por Peso)":
        perfil = st.selectbox("Escolha o Perfil:", list(estoque_perfis.keys()))
        cor = st.selectbox("Escolha a Cor:", ["Branco", "Fosco", "Preto", "Bronze"])
        metros = st.number_input("Quantos metros o cliente vai querer?", min_value=0.0)
        
        if st.button("Adicionar ao Orçamento"):
            peso_metro = estoque_perfis[perfil]
            preco_kg = 50 if cor == "Bronze" else 45
            peso_total = metros * peso_metro
            
            item = {
                "Perfil": perfil,
                "Cor": cor,
                "Metros": metros,
                "Peso (kg)": round(peso_total, 3),
                "Valor (R$)": round(peso_total * preco_kg, 2)
            }
            st.session_state["carrinho"].append(item)
            st.rerun()
    elif tipo_venda == "Cantoneiras (Por Peça)":
        cantoneira = st.selectbox("Escolha a Cantoneira:", list(estoque_cantoneiras.keys()))
        cor_cant = st.selectbox("Escolha a Cor:", ["Branco", "Fosco", "Preto", "Bronze"], key="cor_cantoneira")
        tamanho_corte = st.selectbox("Tamanho da peça (metros):", [6, 4, 3, 2])
        if tamanho_corte == 6:
            qtd_pecas = st.number_input("Quantidade de barras (6m):", min_value=1, step=1)
        else:
            qtd_pecas = 1
            st.info(f"Venda de 1 unidade do corte de {tamanho_corte}m.")
            if st.button("Adicionar Cantoneira"):
               preco_6m = estoque_cantoneiras[cantoneira]
               preco_proporcional = (preco_6m / 6) * tamanho_corte
               texto_medida = f"{qtd_pecas} barra(s) de 6m" if tamanho_corte == 6 else f"1 pedaço de {tamanho_corte}m"
            
            item = {
                "Perfil": cantoneira,
                "Cor": cor_cant,
                "Metros": texto_medida, 
                "Peso (kg)": 0.0, 
                "Valor (R$)": round(qtd_pecas * preco_proporcional, 2)
            }
            st.session_state["carrinho"].append(item)
            st.rerun()



        
        if st.button("Adicionar Cantoneira"):
            preco_6m = estoque_cantoneiras[cantoneira]
            preco_proporcional = (preco_6m / 6) * tamanho_corte
        if st.button("Adicionar Cantoneira"):
            preco_6m = estoque_cantoneiras[cantoneira]
            preco_proporcional = (preco_6m / 6) * tamanho_corte
            
            item = {
                "Perfil": cantoneira,
                "Cor": cor_cant,"Metros": f"{qtd_pecas} un de {tamanho_corte}m", 
                "Peso (kg)": 0.0, 
                "Valor (R$)": round(qtd_pecas * preco_proporcional, 2)
            }
            st.session_state["carrinho"].append(item)
            st.rerun()


with col2:
    st.write("### 🛒 Itens no Orçamento")
    
    if len(st.session_state["carrinho"]) > 0:
        c_header1, c_header2, c_header3, c_header4 = st.columns([3, 2, 2, 1])
        with c_header1: st.write("**Produto**")
        with c_header2: st.write("**Medida**")
        with c_header3: st.write("**Valor**")
        with c_header4: st.write("**Ação**")
        st.write("---")
        for i, item in enumerate(st.session_state["carrinho"]):
            c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
            
            nome = item.get("Item", item.get("Perfil", "Produto"))
            
            with c1: 
                st.write(f"{nome} ({item.get('Cor', '-')})")
            with c2: 
                medida = item.get("Metros", item.get("Qtd/Medida", ""))
                st.write(f"{medida} m")
            with c3: 
                st.write(f"R$ {item.get('Valor (R$)', 0):.2f}")
            with c4:
                if st.button("❌", key=f"remover_{i}"):
                    st.session_state["carrinho"].pop(i)
                    st.rerun()

                    st.write("---") 
                             

        
    peso_pedido = sum(linha["Peso (kg)"] for linha in st.session_state["carrinho"])
    valor_pedido = sum(linha["Valor (R$)"] for linha in st.session_state["carrinho"])
        
    st.info(f"**PESO TOTAL:** {peso_pedido:.3f} kg")
    st.success(f"**VALOR TOTAL DO PEDIDO: R$ {valor_pedido:.2f}**")
    texto_whatsapp = "*Orçamento - AF Alumínio* 🛒\n\n"
        
    for item in st.session_state["carrinho"]:
       texto_whatsapp += f"▪️ {item['Perfil']} ({item['Cor']}) - {item['Metros']}m\n"
            
    texto_whatsapp += f"\n*Valor Total: R$ {valor_pedido:.2f}*"
    texto_codificado = urllib.parse.quote(texto_whatsapp)
    link = f"https://wa.me/?text={texto_codificado}"
    st.markdown(f"**[📱 Enviar Orçamento pelo WhatsApp]({link})**")
        
    if st.button("Limpar Carrinho"):
        st.session_state["carrinho"].clear()
        st.rerun()
