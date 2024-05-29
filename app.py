def quicksort(arr):
    # Caso Base: Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Selección del Pivote: Usamos el primer elemento de la lista como pivote
    pivot = arr[0]
    
    # Partición de la Lista: Dividimos en sublistas menores y mayores al pivote
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    # Llamadas Recursivas y Combinación de Resultados: Ordenamos las sublistas y combinamos
    return quicksort(left) + [pivot] + quicksort(right)

# Prueba de la Implementación
example_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(example_list)
print(f"Lista original: {example_list}")
print(f"Lista ordenada: {sorted_list}")
