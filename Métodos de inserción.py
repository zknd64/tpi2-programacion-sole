A = [20,19,26,24,28,30,17,18,19,20,26,23,22,25,24,27,29,20,19,17,18,19,20,21,23,27,29,30,40,35,29,36,37,38,18,19,20,35,34,36,24,29,28,20,24,26,20,27,26,18,19,17,19,18]

# Implementación de Ordenamiento por Inserción
for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    # Desplaza los elementos mayores que 'key' una posición adelante
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key

print(A)

