def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    numbers = [34, 2, 56, 23, 89, 15, 31, 87, 200, 28]
    target = int(input("Masukkan Angka: "))
    print("Tablenya")
    sorted_numbers = bubble_sort(numbers)
    print(sorted_numbers)
    print(f"Targetnya: {target}")
    index = binary_search(sorted_numbers, target)
    if index != -1:
        print(f"Elemen {target} ditemukan pada indeks {index}.")
    else:
        print(f"Elemen {target} tidak ditemukan dalam list setelah sorting.")