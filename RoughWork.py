dict = {"Sangee" : 1, "Sabi" : 1, "Thasika" : 3}
arr = []
for i in dict.keys():
    print(dict.get(i))
    arr.append(dict.get(i))
print(arr)   
arr.sort(reverse = True) 
print(arr)  
for i in range(len(arr)):
    val_lis = list(dict.values())
    index   = val_lis.index(arr[i])
    key_lis = list(dict.keys())
    dict[key_lis[index]] = 0
    arr[i] = 0