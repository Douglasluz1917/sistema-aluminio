import streamlit as st
import urllib.parse
from fpdf import FPDF
from datetime import datetime
import os

st.set_page_config(page_title="Orçamento AF Alumínio", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
        .block-container { padding-top: 1rem; padding-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)
def criar_pdf(carrinho, valor_total):
    pdf = FPDF()
    pdf.add_page()
    if os.path.exists("logo.png"):
        pdf.image("logo.png", x=10, y=8, w=35)
        
    pdf.set_font("Arial", 'B', 18)
    pdf.cell(40) 
    pdf.cell(0, 10, "ORÇAMENTO - AF ALUMÍNIO", ln=True, align='L')
    
    data_atual = datetime.now().strftime("%d/%m/%Y")
    pdf.set_font("Arial", 'I', 11)
    pdf.cell(40)
    pdf.cell(0, 5, f"Data do Pedido: {data_atual}", ln=True, align='L')
    pdf.ln(15)
    
    pdf.set_draw_color(180, 180, 180)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(8)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(140, 8, "Descrição do Produto")
    pdf.cell(50, 8, "Subtotal", ln=True, align='R')
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 11)
    for i, item in enumerate(carrinho, 1):
        descricao = f"{i}. {item.get('Perfil', '')} ({item.get('Cor', '')}) | {item.get('Metros', '')}"
        pdf.cell(140, 8, descricao, border=0)
        pdf.cell(50, 8, f"R$ {item.get('Valor (R$)', 0):.2f}", border=0, ln=True, align='R')
        
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(8)
    
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(140, 10, "VALOR TOTAL DO PEDIDO:", border=0)
    pdf.cell(50, 10, f"R$ {valor_total:.2f}", border=0, ln=True, align='R')
    
    pdf.ln(20)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, "Obrigado pela preferência! Orçamento válido por 7 dias.", ln=True, align='C')
    return pdf.output(dest="S").encode("latin-1")

estoque_acessorios = {
   "335": 16.00,
   "510": 55.00,
   "511": 32.00,
   "PARAFUSO ALTO BROCANTE 1'": 0.80,
   "038 IGREJINHA": 3.00,
   "511 A": 10.00,
   "570 V/V": 26.00,
   "571 V/A": 18.00,
   "APLICADOR DE SILICIONE": 35.00,
   "BAGUETE BOX": 6.00,
   "BASTÃO 8 E 10": 17.00,
   "BATEDOR BOX NOVO": 0.50,
   "BRAÇO MAX AR 25": 13.00,
   "BRAÇO MAX AR 35": 17.00,
   "BRAÇO MAX AR 55": 23.00,
   "BRAÇO TOLDO 1,50M": 90.00,
   "BRAÇO TOLDO 1M": 60.00,
   "BROCA 1/2": 18.00,
   "BROCA 1/8": 4.00,
   "BROCA 11/64": 6.00,
   "BROCA 5/32": 5.00,
   "BROCA 9/64": 4.50,
   "BUCHA 6": 15.00,
   "BUCHA 8": 30.00,
   "CANOPLA": 4.00,
   "CAVALETE BOX": 1.00,
   "CHAPA ACRÍLICA CRISTAL": 130.00,
   "CHAPA ACRÍLICA FUME": 110.00,
   "CHAPA ACRILICA LEITOSA": 130.00,
   "CONTROLE MOTOR": 35.00,
   "CREMALHEIRA": 55.00,
   "CUNHA PARA VIDRO": 0.50,
   "DISCO DE CORTE 4,5": 3.00,
   "DOBRADIÇA PARA BOX": 3.00,
   "DOBRADIÇA BÚZIO": 8.00,
   "DOBRADIÇA PORTA": 5.00,
   "FECHADURA CORRER BÚZIO": 75.00,
   "FECHADURA DE PORTA CORRER": 55.00,
   "FECHADURA DE PORTA GIRO": 75.00,
   "FECHADURA PORTA GIRO 401": 68.00,
   "FECHADURA BÚZIO 1/2": 92.00,
   "FECHADURA BÚZIO COMPLETA": 98.00,
   "FECHADURA ROLETE BÚZIO": 85.00,
   "FECHADURA ROLETE PORTA": 65.00,
   "FECHO AVIÃO CROMADO": 6.00,
   "FECHO AVIÃO NYLON": 5.00,
   "FECHO CONCHA C/ GATILHO": 14.00,
   "FECHO CONCHA S/ GATILHO": 8.00,
   "FERROLHO 1' 1/2": 5.00,
   "FERROLHO 2'": 8.00,
   "FERROLHO 3'": 9.00,
   "FERROLHO 4'": 10.00,
   "FERROLHO BÚZIO GRANDE 40CM": 18.00,
   "FERROLHO BÚZIO PEQUENO 20CM": 14.00,
   "FITA DE ENCOSTO": 10.00,
   "FITA DUPLA FACE": 50.00,
   "FIXA ESPELHO": 22.00,
   "GUIA BOX VELHO": 0.50,
   "GUIA BÚZIO": 5.00,
   "GUIA DE BOX NOVO": 1.00,
   "GUIA MB": 0.50,
   "GUIA MP": 0.50,
   "H PANORAMICO": 4.00,
   "H POLICARBONATO": 120.00,
   "JOGO L E CUNHA": 45.00,
   "L DE CONTRA MARCO": 1.00,
   "L PARA BOX": 1.00,
   "L PERFIL DE TELA": 2.00,
   "MOTOR": 450.00,
   "ORELHA DE RATO L 25": 7.00,
   "ORELHA DE RATO MB": 7.00,
   "ORELHA RATO MP": 7.00,
   "PARAFUSO 1' X 8": 0.25,
   "PARAFUSO 2' X 10": 0.50,
   "PARAFUSO 2' X 8": 0.50,
   "PARAFUSO COM PORCA INOX": 1.50,
   "PARAFUSO PONTA LISA GRANDE": 0.70,
   "PARAFUSO PONTA LISA PEQUENO": 0.40,
   "POLICARBONATO": 480.00,
   "PONTALETE": 25.00,
   "PORTA TOALHA": 2.00,
   "PUXADOR BOX": 1.00,
   "PUXADOR BOX DUPLO": 2.00,
   "PUXADOR INOX": 55.00,
   "PUXADOR JANELA VIDRO": 7.00,
   "PUXADOR PORTÃO BÚZIO": 14.00,
   "ROLDANA BOX": 1.00,
   "ROLDANA BOX S/ CAIXA": 1.00,
   "ROLDANA BÚZIO": 22.00,
   "ROLDANA BUZIO NYLON": 19.00,
   "ROLDANA EXCENTRICA": 7.00,
   "ROLDANA JANELA SUPREMA": 6.50,
   "ROLDANA MB": 1.00,
   "ROLDANA MP": 1.50,
   "ROLDANA MP C/ ROLAMENTO": 5.50,
   "ROLDANA PORTA MP": 7.50,
   "ROLDANA SIMPLES": 3.00,
   "ROLDANA TRILHO STANLEY PAR": 23.00,
   "SILICONE INCOLOR": 18.00,
   "SILICONE BC E PT E BZ": 20.00,
   "SILICONE BRONZE WURTH": 25.00,
   "SPRAY PRETO": 25.00,
   "SUPORTE PARA CORRIMÃO": 7.50,
   "TAMPA CORRIMÃO BOLEADO":3.00,
   "TAMPA CORRIMÃO REDONDO": 5.00,
   "TAMPA PARA PARAFUSO": 0.50,
   "TAPA FURO PT E BC": 8.00,
   "TRANQUETA MAX AR": 9.00,
   "U POLICARBONATO": 65.00,
   "VEDA CALHA": 18.00,
   "Z PANORAMICO": 4.00

}

estoque_borrachas = {
   "BORRACHA 051": 2.30,
   "SEREGEL 5X5": 1.00,
   "SEREGEL 7X5": 1.20,
}

estoque_rebites = {
   "REBITE 325": 15.00,
   "REBITE 412 FOSCO": 11.00,
   "REBITE 412 PT E BC": 13.00,
   "REBITE 425": 17.00,
   "REBITE 512": 15.00,
   "REBITE 525": 20.00,
}

   
estoque_pecas= {
    "CT 002 L.1/2": 25.00,
    "CT 008 L.3/4": 35.00,
    "CT 017 L.1'": 45.00,
    "VZ 280": 72.00,
   
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
        "JH 072": 7.400/6,
        "LB 050": 3.100/6,
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
        "CT 026": 4.100/6,
        "CT 031": 5.200/6,
        "CT 050": 2.100/6,
        "CT 019": 2.500/6,
        "BC 002": 0.800/6,
        "BC 015": 1.000/6,
        "BC 025": 1.350/6,
        "LB 012": 3.700/6,
        "VZ 024": 1.500/6,
        "NPC 006": 4.100/6,
        "NPC 005": 4.400/6,
        "NL 008": 1.200/6,
        "25 001": 1.650/6,

        
         }
if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = []

with st.sidebar:
    st.header("🛒 Orçamento Atual")
    valor_pedido = sum(item.get("Valor (R$)", 0.0) for item in st.session_state["carrinho"])
    st.markdown(f"<h3 style='color: #2e7d32; margin-top: 0;'>Total: R$ {valor_pedido:.2f}</h3>", unsafe_allow_html=True)
    
    caixa_carrinho = st.container(height=380)
    with caixa_carrinho:
        if len(st.session_state["carrinho"]) == 0:
            st.info("Nenhum item adicionado.")
        else:
            for i, item in enumerate(st.session_state["carrinho"]):
                col_info, col_del = st.columns([5, 1])
                with col_info:
                    st.markdown(f"**{item.get('Perfil', '')}** ({item.get('Cor', '')})")
                    st.markdown(f"{item.get('Metros', '')} | **R$ {item.get('Valor (R$)', 0.0):.2f}**")
                with col_del:
                    if st.button("❌", key=f"del_{i}"):
                        st.session_state["carrinho"].pop(i)
                        st.rerun()
                st.divider()

    st.write("")
    
    
    texto_whatsapp = f"*ORÇAMENTO - AF ALUMÍNIO*\n\n"
    for item in st.session_state["carrinho"]:
        texto_whatsapp += f"▪️ {item.get('Perfil', '')} ({item.get('Cor', '')}) - {item.get('Metros', '')}\n"
    texto_whatsapp += f"\n*TOTAL: R$ {valor_pedido:.2f}*"
    link_whats = f"https://wa.me/?text={urllib.parse.quote(texto_whatsapp)}"
    
    
    st.markdown(f"""
        <a href="{link_whats}" target="_blank" style="display: block; text-align: center; background-color: #25D366; color: white; padding: 10px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-bottom: 12px;">
            📱 Enviar por WhatsApp
        </a>
    """, unsafe_allow_html=True)
    
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("🗑️ Limpar", use_container_width=True):
            st.session_state["carrinho"] = []
            st.rerun()
    with col_b2:
        pdf_pronto = criar_pdf(st.session_state["carrinho"], valor_pedido)
        st.download_button("🖨️ Imprimir PDF", data=pdf_pronto, file_name="Orcamento.pdf", mime="application/pdf", use_container_width=True)
col_logo, col_titulo = st.columns([1, 6])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=130)
        
with col_titulo:
    st.title("Sistema de Orçamentos")
st.divider()

st.subheader("📝 Lançar Produto")
tipo_venda = st.radio(
    "Selecione a Categoria:", 
    ["Perfis (Por Peso)", "Produtos por Peça", "Acessórios (Unidade)", "Borrachas (Metro)", "Rebites (Cento)"], 
    horizontal=True
)
st.write("") 

if tipo_venda == "Perfis (Por Peso)":
    c1, c2, c3 = st.columns(3)
    with c1: perfil = st.selectbox("Escolha o Perfil:", list(estoque_perfis.keys()))
    with c2: cor = st.selectbox("Escolha a Cor:", ["Branco", "Fosco", "Preto", "Bronze"], key="cor_perfil")
    with c3: metros = st.number_input("Metragem (m):", min_value=0.0, step=0.5)
    
    if st.button("Adicionar Perfil", type="primary"):
        peso_metro = estoque_perfis[perfil]
        preco_kg = 50.00 if cor in ["Preto", "Bronze"] else 45.00
        peso_total = metros * peso_metro
        st.session_state["carrinho"].append({"Perfil": perfil, "Cor": cor, "Metros": f"{metros} m", "Peso (kg)": round(peso_total, 3), "Valor (R$)": round(peso_total * preco_kg, 2)})
        st.rerun()

elif tipo_venda == "Produtos por Peça":
    c1, c2, c3, c4 = st.columns(4)
    with c1: produto_peca = st.selectbox("Escolha o Produto:", list(estoque_pecas.keys()))
    with c2: cor_peca = st.selectbox("Escolha a Cor:", ["Branco", "Fosco", "Preto", "Bronze"], key="cor_peca")
    with c3: tamanho_corte = st.selectbox("Tamanho (m):", [6, 4, 3, 2])
    with c4: qtd_pecas = st.number_input("Quantidade:", min_value=1, step=1) if tamanho_corte == 6 else 1
    
    if tamanho_corte != 6:
        st.info(f"Venda de 1 unidade do corte de {tamanho_corte}m.")
        
    if st.button("Adicionar Peça", type="primary"):
        preco_proporcional = (estoque_pecas[produto_peca] / 6) * tamanho_corte
        medida = f"{qtd_pecas} barra(s) de 6m" if tamanho_corte == 6 else f"1 pedaço de {tamanho_corte}m"
        st.session_state["carrinho"].append({"Perfil": produto_peca, "Cor": cor_peca, "Metros": medida, "Valor (R$)": round(qtd_pecas * preco_proporcional, 2)})
        st.rerun()

elif tipo_venda == "Acessórios (Unidade)":
    c1, c2, c3 = st.columns(3)
    with c1: acessorio = st.selectbox("Escolha o Acessório:", list(estoque_acessorios.keys()))
    with c2: cor_acessorio = st.selectbox("Cor/Acabamento:", ["Padrão", "Branco", "Fosco", "Preto", "Bronze"], key="cor_acess")
    with c3: qtd_acessorio = st.number_input("Quantidade (Unidades):", min_value=1, step=1)
    
    if st.button("Adicionar Acessório", type="primary"):
        st.session_state["carrinho"].append({"Perfil": acessorio, "Cor": cor_acessorio, "Metros": f"{qtd_acessorio} un", "Valor (R$)": round(qtd_acessorio * estoque_acessorios[acessorio], 2)})
        st.rerun()

elif tipo_venda == "Borrachas (Metro)":
    c1, c2, c3 = st.columns(3)
    with c1: borracha = st.selectbox("Escolha a Borracha:", list(estoque_borrachas.keys()))
    with c2: cor_borracha = st.selectbox("Cor:", ["Preto", "Branco", "Cinza", "Transparente"], key="cor_borracha")
    with c3: metros_borracha = st.number_input("Metros:", min_value=0.5, step=0.5)
    
    if st.button("Adicionar Borracha", type="primary"):
        st.session_state["carrinho"].append({"Perfil": borracha, "Cor": cor_borracha, "Metros": f"{metros_borracha} m", "Valor (R$)": round(metros_borracha * estoque_borrachas[borracha], 2)})
        st.rerun()

elif tipo_venda == "Rebites (Cento)":
    c1, c2, c3 = st.columns(3)
    with c1: rebite = st.selectbox("Escolha o Rebite:", list(estoque_rebites.keys()))
    with c2: cor_rebite = st.selectbox("Cor:", ["Padrão", "Preto", "Branco", "Fosco", "Bronze"], key="cor_rebite")
    with c3: qtd_rebites = st.number_input("Qtd (Múltiplos 100):", min_value=100, step=100)
    
    if st.button("Adicionar Rebites", type="primary"):
        st.session_state["carrinho"].append({"Perfil": rebite, "Cor": cor_rebite, "Metros": f"{qtd_rebites} un", "Valor (R$)": round((qtd_rebites / 100) * estoque_rebites[rebite], 2)})
        st.rerun()