import matplotlib.pyplot as plt
import random

def simular_canicas(num_canicas, niveles):
    """
    Simula el trayecto de una cantidad de canicas a través de una máquina de Galton.
    
    Args:
        num_canicas (int): Número de canicas a simular (debe ser un entero positivo).
        niveles (int): Número de niveles de obstáculos (debe ser un entero positivo).
    
    Returns:
        list: Lista con la cantidad de canicas en cada contenedor final.
    """
    # Validación de entrada
    if not isinstance(num_canicas, int) or num_canicas <= 0:
        raise ValueError("El número de canicas debe ser un entero positivo.")
    if not isinstance(niveles, int) or niveles <= 0:
        raise ValueError("El número de niveles debe ser un entero positivo.")
    
    contenedores = [0] * (niveles + 1)
    
    for _ in range(num_canicas):
        movimientos_derecha = sum(random.choice([0, 1]) for _ in range(niveles))
        contenedores[movimientos_derecha] += 1
    
    return contenedores

def graficar_histograma(contenedores, color='skyblue', figure_size=(10, 6)):
    """
    Genera un histograma que representa la distribución de canicas en los contenedores.
    
    Args:
        contenedores (list): Lista con la cantidad de canicas en cada contenedor.
        color (str): Color de las barras del histograma.
        figure_size (tuple): Tamaño de la figura, debe ser un par de valores positivos.
    """
    # Validación de entrada
    if not isinstance(contenedores, list) or not all(isinstance(x, int) for x in contenedores):
        raise ValueError("El parámetro 'contenedores' debe ser una lista de enteros.")
    if not isinstance(figure_size, tuple) or len(figure_size) != 2 or not all(isinstance(dim, (int, float)) and dim > 0 for dim in figure_size):
        raise ValueError("El tamaño de la figura debe ser una tupla de dos valores positivos.")
    
    plt.figure(figsize=figure_size)
    plt.bar(range(len(contenedores)), contenedores, color=color, edgecolor='black')
    plt.xlabel("Contenedor")
    plt.ylabel("Cantidad de canicas")
    plt.title("Simulación de Máquina de Galton - Distribución de Canicas")
    plt.xticks(range(len(contenedores)))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def simular_maquina_galton(num_canicas=3000, niveles=12, color='skyblue', figure_size=(10, 6), semilla=None):
    """
    Función principal para ejecutar la simulación completa de la máquina de Galton y graficar el resultado.
    
    Args:
        num_canicas (int): Número de canicas a simular.
        niveles (int): Número de niveles de la máquina de Galton.
        color (str): Color de las barras del histograma.
        figure_size (tuple): Tamaño de la figura del histograma.
        semilla (int, optional): Semilla para la generación aleatoria (para reproducibilidad).
    """
    try:
        # Validación de semilla
        if semilla is not None and not isinstance(semilla, int):
            raise ValueError("La semilla debe ser un número entero.")
        
        if semilla is not None:
            random.seed(semilla)  # Fija la semilla si se proporciona
        
        # Ejecuta la simulación
        contenedores = simular_canicas(num_canicas, niveles)
        
        # Genera el gráfico
        graficar_histograma(contenedores, color=color, figure_size=figure_size)
    
    except ValueError as e:
        print(f"Error de valor: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamada principal de la simulación
simular_maquina_galton(num_canicas=3000, niveles=12, color='steelblue', figure_size=(12, 7), semilla=42)
