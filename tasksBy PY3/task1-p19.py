arr = [0 for x in range(0, 3)]
rst = []

for a in arr:
    arr[a] = input("input a int number :")
    if int(arr[a]) % 2 == 1:
        rst.append(arr[a])
        # print(arr[a])
if len(rst) > 0 :
    rst.sort()
    print(rst[-1]) 
else:
    print('no odd number')