import streamlit as st

# Configuración de la página (opcional)
st.set_page_config(
    page_title="Conversor Numérico",
    page_icon="🔢"
)

# Título
st.title("Conversor de Sistemas Numéricos")

# Inputs del usuario
number = st.text_input("Ingresa el número:")
from_base = st.selectbox("De base:", [2, 8, 10, 16])
to_base   = st.selectbox("A base:",   [2, 8, 10, 16])

# Botón de conversión
if st.button("Convertir"):
    if not number.strip():
        st.error("Por favor introduce un número.")
    else:
        try:
            # Convertimos el número de la base origen a decimal
            decimal = int(number, from_base)

            # Mostramos el resultado según la base destino
            if to_base == 2:
                resultado = bin(decimal)[2:]
            elif to_base == 8:
                resultado = oct(decimal)[2:]
            elif to_base == 10:
                resultado = str(decimal)
            elif to_base == 16:
                resultado = hex(decimal)[2:].upper()
            else:
                resultado = str(decimal)  # fallback

            st.success(f"Resultado: **{resultado}**")
        except ValueError:
            st.error(
                f"El valor '{number}' no es válido para la base {from_base}."
            )