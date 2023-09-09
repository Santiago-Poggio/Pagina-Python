import streamlit as st
from PIL import Image

st.title("operadores aritméticos")

st.write("Los operadores aritméticos son los operadores más comunes que nos podemos encontrar y son los que nos permiten hacer las operaciones aritméticas como sumar, restar, dividir,etc.")

st.write("los operadores aritméticos son:")

st.write('''
+: suma los valores.
         
-: resta los valores.
         
*: multiplica los valores.
         
/: divide los valores.
         
% : devuelve el resto de la división entera.
         
** : realiza la potencia entre los valores
         
// : devuelve el cociente de la división.
''')

image = Image.open("operadores.png")
st.image(image,caption="los diferentes operadores en funcionamiento")