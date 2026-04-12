import requests
import streamlit as st

def generar_aritculo(topic):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer TU_API_KEY",
            "Content-Type": "application/json"
        },
        json={
            "model": "openchat/openchat-7b",
            "messages": [
                {"role": "user", "content": f"Escribe un artículo sobre {topic}"}
            ]
        }
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return None