## Cifrado de Matrices

Este repositorio contiene un programa de Python para cifrar y descifrar mensajes utilizando un cifrado de matrices. El programa utiliza una matriz de clave predefinida para realizar la encriptación y la matriz inversa de esta clave para la desencriptación.

Realizado para la materia `Matematica C (F0304)` de la Universidad Nacional De La Plata

### Funciones Principales

El programa consta de las siguientes funciones principales:

1. **`validar_matriz_modulo30(matriz)`**: Esta función asegura que los valores de una matriz estén en el rango [1, 30], que es el módulo utilizado en el cifrado. Esto es importante para garantizar que las operaciones de módulo sean correctas.

2. **`convertir_mensaje_a_matriz(mensaje, caracteres)`**: Convierte un mensaje de texto en una matriz numérica utilizando un conjunto de caracteres definidos. El mensaje se divide en bloques de tres caracteres para llenar la matriz.

3. **`encriptar_mensaje(matriz_mensaje, clave)`**: Encripta un mensaje utilizando la matriz de clave proporcionada. Realiza operaciones de multiplicación de matrices y módulo para generar el mensaje cifrado.

4. **`desencriptar_mensaje(encriptado, inversa)`**: Descifra un mensaje encriptado utilizando la matriz inversa de la clave. También realiza operaciones de multiplicación de matrices y módulo para obtener el mensaje original.

5. **`imprimir_mensaje_letras(mensaje, caracteres)`**: Esta funcion se utiliza para imprimir una matriz de mensaje en caracteres.

### Uso

Puedes utilizar este programa para encriptar y desencriptar mensajes. Al ejecutar el programa, se te pedirá que elijas entre encriptar (seleccionando "1") o desencriptar (seleccionando "2") un mensaje. A continuación, proporciona el mensaje y sigue las instrucciones.

### Caracteres y Clave

El programa utiliza un conjunto de caracteres definidos en la lista `caracteres`, que incluye letras minúsculas y algunos símbolos comunes. La clave de encriptación se define en la matriz `clave`, y la matriz inversa correspondiente se encuentra en la matriz `inversa`. Estas matrices determinan cómo se cifra y descifra el mensaje.

### Autores

- Autor: Mateo Romero, Ramiro Cabral
- Correo Electrónico: materomero04@gmail.com , ramirocabral04@gmail.com
---

¡Gracias por visitar este repositorio! Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con nosotros.