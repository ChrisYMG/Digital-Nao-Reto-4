import random

# Lista de palabras
palabras = ['python', 'programacion', 'ahorcado', 'computadora', 'teclado']

# Seleccionar una palabra al azar
palabra = random.choice(palabras)

# Estado del juego
estado = ['_'] * len(palabra)

# Número de intentos
intentos = 6

# Letras ya intentadas
letras_intentadas = set()

while intentos > 0 and '_' in estado:
    print(f"\nEstado actual: {' '.join(estado)}")
    print(f"Intentos restantes: {intentos}")
    print(f"Letras intentadas: {', '.join(sorted(letras_intentadas))}")
    
    # Leer la entrada del usuario
    letra = input("Ingresa una letra: ").lower()
    
    # Verificar si la letra ya fue intentada
    if letra in letras_intentadas:
        print("Ya intentaste con esa letra. Elige otra.")
        continue
    else:
        letras_intentadas.add(letra)
    
    # Verificar si la letra está en la palabra
    if letra in palabra:
        print("¡Bien! La letra está en la palabra.")
        for i, l in enumerate(palabra):
            if l == letra:
                estado[i] = letra
    else:
        print("La letra no está en la palabra.")
        intentos -= 1

# Verificar si el juego terminó
if '_' not in estado:
    print(f"\n¡Felicidades! Adivinaste la palabra: {palabra}")
else:
    print(f"\nLo siento, te quedaste sin intentos. La palabra era: {palabra}")