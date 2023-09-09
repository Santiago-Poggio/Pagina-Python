import streamlit as st
from PIL import Image

st.title("variables y tipos de datos")

st.write("las variables son donde uno va a guardar los datos que utilizará en su programa, en python uno declara una variable simplemente escribiendo Nombre = Valor . en el espacio de Nombre uno elige el nombre que quiere ponerle a la variable y en Valor pones el dato que queres ponerle a la variable, pero… ¿que tipos de datos hay?")

image2 = Image.open("variable.png")
st.image(image2,caption="variables en python")

st.subheader("tipos de datos")

st.write('''existen varios tipos de datos pero los más básicos que hay son:
         
**Numeros(int,float)**:
         
**Int**: Los datos tipo int pueden almacenar cualquier número entero sin límite de tamaño.
         
**float**: Los datos tipo float pueden almacenar  números negativos o positivos con decimales, osea, números reales.
         
**texto(string)**: los datos tipo string permiten almacenar secuencia de caracteres dentro de dos comillas “”
         
**booleanos**: el dato booleano solo permite almacenar dos tipos de datos, true(verdadero) o false(falso).
''')
image = Image.open("datos.png")
st.image(image,caption="los datos en python")