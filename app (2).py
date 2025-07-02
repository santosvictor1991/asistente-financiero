
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import json

st.title("📋 Formulario de Contacto - Asesoría Financiera")

st.write("Por favor completa este formulario y nos pondremos en contacto contigo lo antes posible.")

# Campos del formulario
nombre = st.text_input("👤 Nombre completo")
contacto = st.text_input("📱 Correo electrónico o WhatsApp")
plan = st.selectbox("📌 Plan de interés", ["Asesoría Express", "Asesoría Esencial", "Asesoría Integral"])
consulta = st.text_area("💬 Describe brevemente tu situación o consulta")

# Verifica si se completaron todos los campos
if st.button("Enviar formulario"):
    if not nombre or not contacto or not consulta:
        st.warning("Por favor completa todos los campos antes de enviar.")
    else:
        try:
            # Obtener credenciales desde st.secrets
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            credentials_dict = st.secrets["google"]
            creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
            client = gspread.authorize(creds)

            # Abrir la hoja de cálculo por nombre
            sheet = client.open("Formulario Asesoría Financiera").sheet1

            # Guardar datos
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.append_row([now, nombre, contacto, plan, consulta])

            st.success("✅ Tu información ha sido enviada correctamente. ¡Gracias!")
        except Exception as e:
            st.error(f"❌ Ocurrió un error al enviar el formulario: {e}")
