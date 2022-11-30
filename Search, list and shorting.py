print("===== Search, list and shorting =====")

temukan = int(input("Masukkan angka yang dicari : "))
list = [1,5,20,12,43,55,17,7,9,100]

def bubble(array):
    n = len(array)
    
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return array

def mencari(array, find):
    for i in range(len(array)):
        if array[i] == find:
            return i
    return -1

print("Sesudah di shorting : ", bubble(list))

h = mencari(list,temukan)

if (h == -1):
    print("Elemen tidak ditemukan pada list!")
else :
    print("Elemen ditemukan pada posisi ke-",h)