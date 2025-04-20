def check_vowels():
    nombre = input(" > ")  # Mismo formato que el ejemplo
    nombre_minuscula = nombre.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        print(f"Contiene {vocal}: {vocal in nombre_minuscula}")
