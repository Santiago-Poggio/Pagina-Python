import streamlit as st
from PIL import Image

st.title("Hola mundo en python")

st.write("escribir hola mundo es comunmente lo primero que se hace cuando se utiliza un nuevo lenguaje de programación.")

st.subheader("Escribir Hola Mundo")

st.write("Para escribir hola mundo en python uno tiene que utilizar la función “print”, que nos permite imprimir en la consola. escribimos print y entre paréntesis y comillas al lado de la función, escribimos “Hola Mundo”. se tendría que ver de esta forma. print(“Hola Mundo”) . Al ejecutar el programa(en la pagina web seria apretando en run) veremos que en la consola se escribió hola mundo. ")

st.write("Asi se tendria que ver cuando lo ejecutemos:")

image = Image.open("hola_mundo.png")

st.image(image)