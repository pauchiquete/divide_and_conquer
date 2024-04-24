def buscar_numero_iterativo(n, x):
  """
  Función para buscar un número entero 'x' dentro del rango [1, n] utilizando un enfoque iterativo.

  Argumentos:
    n: El límite superior del rango de búsqueda (un entero positivo).
    x: El número a buscar (un entero).

  Retorno:
    Si se encuentra el número 'x', se devuelve su valor y el número de intentos realizados.
    Si no se encuentra, se devuelve 'None'.
  """

  bajo = 1
  alto = n
  contador = 0

  while bajo <= alto:
    mitad = (bajo + alto) // 2

    if mitad == x:
      print(f"El número es {mitad} y se encontró en {contador} intentos.")
      return mitad, contador
    elif mitad < x:
      bajo = mitad + 1
    else:
      alto = mitad - 1

    contador += 1

  print("Número no encontrado.")
  return None

def buscar_numero_recursivo(n, x, bajo=1, alto=None, contador=0):
  """
  Función para buscar un número entero 'x' dentro del rango [1, n] utilizando un enfoque recursivo.

  Argumentos:
    n: El límite superior del rango de búsqueda (un entero positivo).
    x: El número a buscar (un entero).
    bajo: El límite inferior actual del rango de búsqueda (por defecto, 1).
    alto: El límite superior actual del rango de búsqueda (por defecto, 'n').
    contador: El número de intentos realizados hasta el momento (por defecto, 0).

  Retorno:
    Si se encuentra el número 'x', se devuelve su valor y el número de intentos realizados.
    Si no se encuentra, se devuelve 'None'.
  """

  if alto is None:
    alto = n

  if bajo > alto:
    print("Número no encontrado.")
    return None

  mitad = (bajo + alto) // 2

  if mitad == x:
    print(f"El número es {mitad} y se encontró en {contador} intentos.")
    return mitad, contador
  elif x < mitad:
    return buscar_numero_recursivo(n, x, bajo, mitad - 1, contador + 1)
  else:
    return buscar_numero_recursivo(n, x, mitad + 1, alto, contador + 1)

def main():
  """
  Función principal para obtener los valores de 'n' y 'x', llamar a las funciones de búsqueda y mostrar los resultados.
  """

  n = int(input("Introduce el valor de n: "))
  x = int(input("Introduce el número a adivinar: "))

  print("\nMétodo Iterativo:")
  resultado_iterativo = buscar_numero_iterativo(n, x)
  if resultado_iterativo:
    numero_encontrado, intentos_iterativos = resultado_iterativo
    print(f"Número encontrado: {numero_encontrado}")
    print(f"Número de intentos: {intentos_iterativos}")

  print("\nMétodo Recursivo:")
  resultado_recursivo = buscar_numero_recursivo(n, x)
  if resultado_recursivo:
    numero_encontrado, intentos_recursivos = resultado_recursivo
    print(f"Número encontrado: {numero_encontrado}")
    print(f"Número de intentos: {intentos_recursivos}")

if __name__ == "__main__":
  main()