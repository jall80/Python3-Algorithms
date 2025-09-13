from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "EleutherAI/gpt-neo-125M"  # Más ligero, rápido en CPU

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

print("Modelo cargado correctamente.\n")  # <- Esto confirma que ya puedes chatear

def chat(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Bucle de conversación
print("Escribe 'salir' para terminar el chat.\n")
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        break
    response = chat(user_input)
    print("Bot:", response)


    # NO SMART CHATBOT XD
