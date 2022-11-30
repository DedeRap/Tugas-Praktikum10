print("===== Bubble Short Rekursif =====")

def menukar(list, i, j):
    a = list[i]
    list[i] = list[j]
    list[j] = a
    
def bubbleshort(list, b):
    for i in range(b - 1):
        if list[i] > list[i + 1]:
            menukar(list, i, i + 1)
    if b - 1 > 1 :
        bubbleshort(list, b - 1)
        
l = [1, 5, 7, 35, 90, 57]
bubbleshort(l, len(l))
print("List setelah dishorting :")
print(l)