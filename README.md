Simulación de Máquina de Galton
Este programa simula una máquina de Galton, también conocida como la "máquina de canicas", y muestra la distribución de canicas en contenedores finales después de pasar por varios niveles de obstáculos. La máquina de Galton ilustra cómo, a través de decisiones binarias aleatorias (izquierda o derecha en cada nivel), las canicas tienden a distribuirse en una distribución aproximada de campana.

Características
Simulación de la trayectoria de un conjunto de canicas a través de múltiples niveles de obstáculos.
Generación de un histograma para visualizar la distribución final de las canicas en los contenedores.
Permite ajustar el número de canicas, niveles, tamaño y color del gráfico.
Incluye manejo de errores y validación de entradas para una mayor robustez.
Opción de usar una semilla para generar resultados reproducibles.
Requisitos
Python 3.6 o superior
Bibliotecas:
matplotlib para la generación de gráficos
Instala matplotlib si aún no lo tienes:

bash
Copy code
pip install matplotlib
Estructura del Código
El código consta de tres funciones principales:

simular_canicas(num_canicas, niveles)
Simula la trayectoria de las canicas a través de la máquina de Galton. Cada canica tiene una probabilidad del 50% de moverse a la izquierda o a la derecha en cada nivel.

Parámetros:
num_canicas (int): Número de canicas a simular (debe ser un entero positivo).
niveles (int): Número de niveles de obstáculos (debe ser un entero positivo).
Devuelve: Una lista con la cantidad de canicas en cada contenedor.
graficar_histograma(contenedores, color='skyblue', figure_size=(10, 6))
Genera un histograma que muestra la distribución final de las canicas en los contenedores.

Parámetros:
contenedores (list): Lista con la cantidad de canicas en cada contenedor.
color (str): Color de las barras del histograma (por defecto es skyblue).
figure_size (tuple): Tamaño del gráfico (por defecto es (10, 6)).
simular_maquina_galton(num_canicas=3000, niveles=12, color='skyblue', figure_size=(10, 6), semilla=None)
Función principal que combina las dos funciones anteriores. Realiza la simulación y genera el gráfico con los resultados. También maneja posibles errores de entrada.

Parámetros:
num_canicas (int): Número de canicas a simular.
niveles (int): Número de niveles de la máquina de Galton.
color (str): Color de las barras del histograma.
figure_size (tuple): Tamaño de la figura del histograma.
semilla (int, opcional): Semilla para la generación aleatoria (para reproducibilidad).
Uso
Para ejecutar la simulación, puedes simplemente llamar a la función simular_maquina_galton() con los parámetros deseados.

Ejemplo:

python
Copy code
simular_maquina_galton(num_canicas=3000, niveles=12, color='steelblue', figure_size=(12, 7), semilla=42)
Este ejemplo ejecuta la simulación con 3000 canicas, 12 niveles de obstáculos, barras en color steelblue, un tamaño de figura de (12, 7), y una semilla 42 para obtener resultados reproducibles.

Manejo de Errores
El programa incluye validación de entradas y manejo de errores para asegurar que se utilicen valores válidos en los parámetros. Los errores posibles incluyen:

Error de valor: Si algún parámetro numérico no es positivo o si figure_size no es una tupla de dos números positivos.
Error de tipo: Si el tipo de dato de algún parámetro no es el esperado.
Error inesperado: Captura cualquier otro error y muestra un mensaje al usuario.
Ejemplo de Salida
Al ejecutar la simulación, se mostrará un histograma que representa la distribución final de las canicas en cada contenedor.

Contribuciones
Las contribuciones para mejorar este programa son bienvenidas. Puedes hacer un fork de este repositorio y enviar un pull request con tus mejoras.

Licencia
Este proyecto está bajo la licencia MIT.

Este archivo README.md proporciona toda la información necesaria para comprender el funcionamiento, configuración, y uso del programa de simulación de la máquina de Galton.






You said:
hazlo mas humano y con ligeros errores ortograficos 
ChatGPT said:
ChatGPT
Aquí tienes una versión del README.md con un tono más informal y algunos errores tipográficos:

Simulacion de la Maquina de Galton
Este programa simula una máquina de Galton, también conocida como la "máquina de canicas", y muestra cómo las canicas se distribuyen en diferentes contenedores al caer a través de varios niveles de obstaculos. La máquina de Galton es un ejemplo sencillo de cómo, tras decisiones aleatorias (movimiento hacia la izquierda o derecha), las canicas tienden a formar una distribución parecida a la campana.

Caracteristicas
Simula el trayecto de un grupo de canicas a traves de varios niveles de la máquina de Galton.
Muestra la distribucion final de las canicas en un histograma.
Permite cambiar el número de canicas, niveles, el color del grafico y el tamaño de la figura.
Incluye validaciones y manejo de errores para un uso más seguro.
Opcion para usar una "semilla" que hace que los resultados sean reproducibles.
Requisitos
Python 3.6 o mayor
Librerias:
matplotlib para los gráficos
Para instalar matplotlib, puedes usar:

bash
Copy code
pip install matplotlib
Estructura del Programa
El programa tiene tres funciones principales:

simular_canicas(num_canicas, niveles)
Simula el movimiento de cada canica a traves de la máquina de Galton. En cada nivel, cada canica tiene un 50% de probabilidad de moverse hacia la derecha o hacia la izquierda.

Parametros:
num_canicas (int): Número de canicas a simular (debe ser un entero positivo).
niveles (int): Número de niveles de la máquina (debe ser un entero positivo).
Retorna: Una lista con la cantidad de canicas en cada contenedor final.
graficar_histograma(contenedores, color='skyblue', figure_size=(10, 6))
Dibuja un histograma que muestra la distribucion final de las canicas.

Parametros:
contenedores (list): Lista con la cantidad de canicas en cada contenedor.
color (str): Color de las barras en el histograma (por defecto es skyblue).
figure_size (tuple): Tamaño del gráfico (por defecto (10, 6)).
simular_maquina_galton(num_canicas=3000, niveles=12, color='skyblue', figure_size=(10, 6), semilla=None)
Función principal que une las funciones de simulación y graficación. Ejecuta la simulacion y genera el grafico con los resultados.

Parametros:
num_canicas (int): Número de canicas a simular.
niveles (int): Número de niveles.
color (str): Color de las barras del histograma.
figure_size (tuple): Tamaño de la figura del histograma.
semilla (int, opcional): Semilla para resultados reproducibles.
Como Usarlo
Para ejecutar el programa, puedes simplemente llamar a la función simular_maquina_galton() con los parametros deseados.

Ejemplo:

python
Copy code
simular_maquina_galton(num_canicas=3000, niveles=12, color='steelblue', figure_size=(12, 7), semilla=42)
Este ejemplo ejecuta la simulacion con 3000 canicas, 12 niveles, barras en color steelblue, un tamaño de figura de (12, 7), y una semilla 42 para obtener resultados consistentes cada vez que se ejecute.

Manejo de Errores
El programa incluye validaciones para asegurar que se utilicen valores válidos en los parametros. Posibles errores incluyen:

Error de valor: Si algún parámetro numérico no es positivo o si figure_size no es una tupla de dos números positivos.
Error de tipo: Si algún parametro no es del tipo esperado.
Error inesperado: Se captura cualquier otro error y muestra un mensaje amigable al usuario.
Ejemplo de Resultado
Cuando ejecutas el programa, se muestra un histograma con la distribucion final de las canicas en los diferentes contenedores, dando un vistazo a como la distribucion de una "campana" aparece con decisiones aleatorias.
