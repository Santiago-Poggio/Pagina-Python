import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = 'Pagina Principal',
    page_icon = None
)

st.title("Prototipo pagina de python")

st.title("¡bienvenido a mi pagina!")

st.subheader("¿De qué trata esta página?")

st.write("En esta pagina se hablara sobre qué es python, para qué sirve, algunos conceptos basicos y porqué es importante que los chicos de tercero sepan sobre python, ¡pero incluso si no sos de tercero esta pagina te podría interesar!")

image = Image.open("python.png")
st.image(image)

st.subheader("¿Por qué es importante que los de terceros aprendan python?")

image2 = Image.open("codeando.png")
st.image(image2)

st.write("Es importante debido a que en tercer año, uno tiene que elegir la orientación que va a seguir, programación o redes, pero hay veces que los alumnos no saben que se hace en programación y eligen sin que se hace en esa orientación. Además, hay muchas mujeres que no eligen programación, ya que está visto comúnmente como algo que es solo para hombres.")

st.subheader("¿Por qué usar python?")

image3 = Image.open("dibujo_python.jpg")
st.image(image3)

st.write("Bueno,¿Porque Python? Elegí Python porque es un lenguaje de programación de código abierto muy versátil que puede ser utilizado para muchas cosas como por ejemplo, aplicaciones, páginas web(De hecho,¡Esta página web fue hecha con python!), ciencia de datos y el machine learning. Además es un lenguaje muy fácil de entender y de escribir para alguien que nunca tuvo programación y es un lenguaje muy utilizado en el mundo laboral.")

st.subheader("Como usar python ")

st.write("uno puede usar python instalandolo a través de la página oficial de [Python](https://www.python.org/downloads/) , pero también se puede usar a través de esta [página web](https://www.programiz.com/python-programming/online-compiler/.) llamada programiz y sin tener que instalar nada.")

st.subheader("conocimientos basicos en python")

st.write("En el menú de la izquierda podran acceder a unos conocimientos basicos de la programacion en python, ademas de algunos video tutoriales si quieren seguir aprendiendo")
