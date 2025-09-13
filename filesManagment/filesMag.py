import os

filename = "ejemplo.txt"

# 1. Crear y escribir en el archivo
with open(filename, "w") as file:
    file.write("Hola, este es un archivo de ejemplo.\n")
    file.write("Línea 2: Python es genial.\n")
    file.write("Línea 3: Trabajando con archivos.\n")
print("✅ Archivo creado y escrito.")

# 2. Leer todo el contenido
with open(filename, "r") as file:
    contenido = file.read()
print("\n📖 Contenido completo del archivo:")
print(contenido)

# 3. Añadir más líneas (modo append)
with open(filename, "a") as file:
    file.write("Línea 4: Añadiendo más información.\n")
    file.write("Línea 5: Última línea.\n")
print("➕ Nuevas líneas añadidas.")

# 4. Leer línea por línea
print("\n📄 Lectura línea por línea:")
with open(filename, "r") as file:
    for i, linea in enumerate(file, start=1):
        print(f"Línea {i}: {linea.strip()}")

# 5. Manejo de errores (archivo inexistente)
archivo_inexistente = "no_existe.txt"
try:
    with open(archivo_inexistente, "r") as file:
        contenido = file.read()
except FileNotFoundError:
    print(f"\n🚫 Error: El archivo '{archivo_inexistente}' no existe.")

# 6. Eliminar el archivo (descomentar si deseas eliminarlo)
if os.path.exists(filename):
    os.remove(filename)
    print(f"\n🗑️ El archivo '{filename}' ha sido eliminado.")
else:
    print(f"\n⚠️ El archivo '{filename}' no existe para eliminar.")
