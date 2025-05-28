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
st.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Logo_%2BUACH.svg")
