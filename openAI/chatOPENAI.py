from openai import OpenAI

client = OpenAI()  # Detecta automáticamente la API Key de la variable de entorno OPENAI_API_KEY

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Hola, ¿cómo estás?"}
    ]
)

mensaje = response.choices[0].message.content
print(mensaje)

####  It needs to be paid for using
