import streamlit as st

st.title("¡Hola, Bienvenido!")
st.write("¡Comencemos!")

# Texto y emoji
st.write("🚀 Bienvenido a tu primera aplicación interactiva con **Streamlit**.")

# Entrada de texto
nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"¡Hola, {nombre}! 👋 Qué bueno tenerte aquí.")

# Selector de opciones
opcion = st.selectbox("¿Qué tema te interesa aprender?", ["Python", "Machine Learning", "Visualización", "Streamlit"])
st.write(f"Elegiste aprender sobre: **{opcion}**.")

# Checkbox
if st.checkbox("¿Te gusta Streamlit?"):
    st.balloons()

# Imagen de prueba (requiere que subas una o pongas una URL)
st.image("https://www.bing.com/images/search?q=log%20uach%20png&view=detailv2&FORM=IQFRBA&id=6EDE5AD2B1A0FF3ECD7808E3E22E264E6E89CD58&selectedindex=0&&expw=900&exph=900&ccid=o8RPFiIT&ck=98668311C94862F3E212D3D4CD6B0A7E&simid=608045775415755198&thid=OIP.o8RPFiITz0fEQ5swYisj1gHaHa&idpp=serp&idpbck=1", width=300)

