import random
ARRAY_SIZE = 20
def selectionSort(arr):
    arr_lenght = len(arr);
    for x in range(arr_lenght-1):
        for y in range(x+1,arr_lenght):
            if arr[x]>arr[y]:
                temp = arr[x]
                arr[x] = arr[y]
                arr[y] = temp
List = []
for _ in range(ARRAY_SIZE):
       List.append(random.randint(29,120))
for indx in List:
  print(indx)
selectionSort(List)
print("after :::::::::")
for indx in List:
    print(indx)