
import streamlit as st
import openai

# Campo para ingresar tu API Key
api_key = st.text_input("🔐 Ingresa tu API Key de OpenAI:", type="password")

# Crear cliente solo si se ha ingresado la clave
if api_key:
    client = openai.OpenAI(api_key=api_key)

    st.title("🤖 Asistente Financiero Virtual")
    st.write("Consulta los planes y servicios de asesoría financiera personalizados que ofrecemos.")

    pregunta = st.text_input("💬 Escribe tu pregunta:")

    if st.button("Preguntar"):
        if not pregunta:
            st.warning("Por favor escribe una pregunta.")
        else:
            with st.spinner("Generando respuesta..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "system",
                                "content": """Eres un asistente virtual de una empresa de asesoría financiera. 
Debes ayudar a los usuarios a entender y elegir entre los siguientes planes de servicios:

1. Asesoría Express ($150-$250): sesión única de 60-90 minutos para resolver dudas puntuales y entregar recomendaciones rápidas.

2. Asesoría Esencial ($500-$800 o $200-$300/mes): 3 meses de acompañamiento con diagnóstico, presupuesto, ahorro y primeras inversiones.

3. Asesoría Integral ($1,200-$2,500): planificación completa para largo plazo, retiro, seguros, inversiones y seguimiento constante.

También ofreces servicios extra como análisis de portafolios, educación financiera, asesoría a pequeñas empresas y seguimiento anual.

Tu objetivo es orientar al cliente con base en sus necesidades y presupuesto. Siempre responde de forma profesional y clara.
                                """
                            },
                            {
                                "role": "user",
                                "content": pregunta
                            }
                        ]
                    )
                    respuesta = response.choices[0].message.content
                    st.success("✅ Respuesta:")
                    st.write(respuesta)
                except Exception as e:
                    st.error(f"❌ Ocurrió un error: {e}")
