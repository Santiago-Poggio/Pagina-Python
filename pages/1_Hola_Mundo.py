import streamlit as st
from PIL import Image

st.title("Hola mundo en python")

st.write("Escribir hola mundo es comúnmente lo primero que se hace cuando se utiliza un nuevo lenguaje de programación.")

st.subheader("Escribir Hola Mundo")

st.write("Para escribir hola mundo en python uno tiene que utilizar la función “print”, que nos permite imprimir en la consola. Escribimos print y entre paréntesis y comillas al lado de la función, escribimos “Hola Mundo”. se tendría que ver de esta forma. print(“Hola Mundo”) . Al ejecutar el programa(en la página web sería apretando en run) veremos que en la consola se escribió hola mundo. ")

st.write("Así se tendría que ver cuando lo ejecutemos:")

image = Image.open("hola_mundo.png")

st.image(image)
