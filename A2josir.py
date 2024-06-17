import streamlit as st
import pandas as pd
from PIL import Image
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
        
        if canais_diferentes == "Sim":
            st.subheader("Que ótimo! Mesmo que você já assista a diferentes canais, esse programa pode ajudar você a descobrir ainda mais opções interessantes. Você terá acesso aos canais de maior popularidades por nicho e a um gráfico de popularidade por nicho. É uma oportunidade perfeita para expandir ainda mais sua lista de favoritos!😍")
            if st.button("Next"):  # Verifica se o botão "Next" foi pressionado
                st.session_state["page"] = 2
        else:
            st.subheader("Se você gosta de assistir os mesmos conteúdos, esse programa é uma ótima oportunidade para conhecer novos canais de podcast de diferentes nichos! 🥰")
            if st.button("Next"):  # Verifica se o botão "Next" foi pressionado
                st.session_state["page"] = 2
                
# Função para gerar e exibir o gráfico
def mostrar_grafico(df, nicho):
    st.header(f"Comparação de Inscritos nos Canais de {nicho}")
    df = df.nlargest(10, 'Número de Inscritos')  # Filtra apenas os 10 canais com mais inscritos
    fig = px.bar(df, x='Canal', y='Número de Inscritos', title=f'Número de Inscritos nos Canais de {nicho}')
    st.plotly_chart(fig)

# Página 2: Perguntar sobre o nicho de interesse
if page == 2:
    with st.container():
        st.title("Nicho de Podcast")
        st.header("Qual nicho de podcast você gosta de assistir? 🎤")
        nicho = st.selectbox("Escolha um nicho", ["Conversas", "Empreendedorismo", "Educacao", "Esporte", "Jogos", "Tecnologia", "Noticias"])
        nome_arquivo = "podcast_" + nicho.lower() + ".csv"

        try:
            # Mostrar canais de podcast relacionados ao nicho escolhido
            df = pd.read_csv(nome_arquivo)
            df = df.rename(columns={"channel_title": "Canal", "channel_url": "Link", "subscriber_count": "Número de Inscritos"})
            st.header(f"Canais relacionados sobre {nicho}")
            st.write(df)

            # Mostrar o gráfico
            mostrar_grafico(df, nicho)

        except FileNotFoundError:
            st.error(f"Arquivo {nome_arquivo} não encontrado. Por favor, verifique se o arquivo existe.")

