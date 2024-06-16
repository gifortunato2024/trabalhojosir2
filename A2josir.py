import streamlit as st
import pandas as pd
from PIL import Image
pip install plotly
import plotly.express as px

st.sidebar.title("Já conhece o nosso site?")
st.sidebar.info("Nosso site é para os amantes de podcast que estão em busca de novos canais. Aqui você pode escolher a categoria que você gosta e descobrir novas experiências. Aproveite!")

# Página 1: Perguntas sobre hábitos de assistir podcasts
page = st.session_state.get("page", 1)
    
if page == 1:
    with st.container():
        st.title("Amantes de Podcast ❤️")
        foto = Image.open('Foto site .JPG')
        st.image(foto, width=500)
        st.header("Vamos conhecer seus hábitos de assistir podcasts!")
        assiste_podcast = st.radio("Você costuma assistir podcast?", ("Sim, amo!", "Não"))
        frequencia = st.selectbox("Com qual frequência você assiste?", ["Diariamente", "Semanalmente", "Mensalmente", "Raramente", "Nunca"])
        canais_diferentes = st.radio("Você costuma assistir canais diferentes?", ("Sim", "Não, gosto de assistir o mesmo sempre "))

        if assiste_podcast == "Sim, amo!":
            st.header("Se sim, que bom! Vou te mostrar outros para você experimentar. Se você só assiste os mesmos, essa é uma ótima oportunidade para conhecer novos canais.🤩")
            if st.button("Next"):  # Verifica se o botão "Next" foi pressionado
                st.session_state["page"] = 2

# Página 2: Perguntar sobre o nicho de interesse
if page == 2:
    with st.container():
        st.title("Nicho de Podcast 🎤")
        st.header("Qual nicho de podcast você gosta de assistir? ")
        nicho = st.selectbox("Escolha um nicho", ["Conversas", "Empreendedorismo", "Educacao", "Esporte", "Jogos", "Tecnologia", "Noticias"])
        nome_arquivo = "podcast_" + nicho.lower() + ".csv"
        # Mostrar  canais de podcast relacionados ao nicho escolhido
        df = pd.read_csv(nome_arquivo)
        st.header(f"Canais relacionados sobre {nicho}")
        st.write(df)
        def mostrar_grafico(df, nicho):
    st.header(f"Comparação de Inscritos nos Canais de {nicho}")
    fig = px.bar(df, x='Nome do Canal', y='Número de Inscritos', title=f'Número de Inscritos nos Canais de {nicho}')
    st.plotly_chart(fig)
        

        # Adiciona a imagem no topo da primeira página
        st.image("https://tecnoblog.net/noticias/youtube-teste-problema-desmonetizacao/", use_column_width=True)
