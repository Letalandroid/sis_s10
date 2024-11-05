import requests
import json

API_KEY = 'AIzaSyCMJH77s_6SgFxfgzUVr56ZL_rjy4hSxJ4'  # Reemplaza esto con tu clave API de AI Studio
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

def generar_respuesta(prompt):
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': prompt
                    }
                ]
            }
        ]
    }

    url_con_api_key = f"{API_URL}?key={API_KEY}"

    response = requests.post(url_con_api_key, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"Error: {response.status_code}, {response.text}"

print("Bienvenido al chatbot. Escribe 'adiós' para terminar la conversación.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == 'adiós' or user_input.lower() == 'adios':
        print("Chatbot: ¡Hasta luego!")
        break
    respuesta = generar_respuesta(user_input)
    print("Chatbot:", respuesta)