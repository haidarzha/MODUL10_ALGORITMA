def bubble_sort_rekursif(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return bubble_sort_rekursif(arr, n - 1)

data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("List Sebelum Disorting:")
print(data)

sorted_data = bubble_sort_rekursif(data.copy())
print("\nList Yang Sudah Disorting:")
print(sorted_data)
