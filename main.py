import os

def validar_matriz_modulo30(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = (matriz[i][j] % 30 + 30) % 30
    return matriz

def convertir_mensaje_a_matriz(mensaje, caracteres):
    matriz_mensaje = [[0] * (len(mensaje) // 3 + 1) for _ in range(3)]
    col = 0
    fila = 0

    for caracter in mensaje:
        encontrado = False
        for j in range(len(caracteres)):
            if caracter == caracteres[j] and caracter != '\n':
                matriz_mensaje[fila][col] = j
                fila += 1
                encontrado = True
                break
        if not encontrado:
            print("Carácter no válido en el mensaje:", caracter)
            exit(1)
        if fila == 3:
            fila = 0
            col += 1
    return matriz_mensaje

def encriptar_mensaje(matriz_mensaje, clave):
    encriptado = [[0] * len(matriz_mensaje[0]) for _ in range(3)]

    for i in range(len(encriptado[0])):
        for j in range(3):
            for k in range(3):
                encriptado[j][i] += clave[j][k] * matriz_mensaje[k][i]
            encriptado[j][i] = (encriptado[j][i] % 30 + 30) % 30
            if encriptado[j][i] == 0:
                encriptado[j][i] = 30
    return encriptado

def desencriptar_mensaje(encriptado, inversa):
    desencriptado = [[0] * len(encriptado[0]) for _ in range(3)]

    for i in range(len(desencriptado[0])):
        for j in range(3):
            for k in range(3):
                desencriptado[j][i] += inversa[j][k] * encriptado[k][i]
            desencriptado[j][i] = (desencriptado[j][i] % 30 + 30) % 30
            if desencriptado[j][i] == 0:
                desencriptado[j][i] = 30
    return desencriptado

def imprimir_mensaje(mensaje):
    print("Mensaje:")
    for i in range(len(mensaje[0])):
        row = []
        for j in range(3):
            row.append(str(mensaje[j][i]))
        print("[" + " ".join(row) + "]", end=" ")
    print()

def imprimir_mensaje_letras(mensaje, caracteres):
    print("Mensaje: ")
    for i in range(len(mensaje[0])):
        for j in range(3):
            print(caracteres[mensaje[j][i]], end="")
    print()



caracteres = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',']
clave = [
    [35, 53, 12],
    [12, 21, 5],
    [2, 4, 1]
]
inversa = [
    [1, -5, 13],
    [-2, 11, -31],
    [6, -34, 99]
]

# Asegurarse de que los valores de la matriz inversa estén en el rango [0, 29]
inversa = validar_matriz_modulo30(inversa)


os.system("cls")
while True:
    opcion=input("Desea encriptar (Seleccione 1) o desencriptar (Seleccione 2) un mensaje? (3 cancela la ejecucion) \n")

    os.system("cls")
    if opcion == "1":
        mensaje = input("Ingrese el mensaje a encriptar: ").lower()
        matriz_mensaje = convertir_mensaje_a_matriz(mensaje, caracteres)
        encriptado = encriptar_mensaje(matriz_mensaje, clave)
        imprimir_mensaje_letras(encriptado, caracteres)

    elif opcion == "2":
        mensaje = input("Ingrese el mensaje a desencriptar: ").lower()
        encriptado = convertir_mensaje_a_matriz(mensaje, caracteres)
        desencriptado = desencriptar_mensaje(encriptado, inversa)
        imprimir_mensaje_letras(desencriptado, caracteres)

    elif opcion == "3":
        break

    else:
        print("Opción no válida")

print("Gracias por usar el programa!")