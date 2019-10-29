def mergeArrays(lst1, lst2):
    lst = []
    i = 0
    j = 0
    k = []
    while (i < len(lst1) or j < len(lst2)):
        if lst1[i] < lst2[j]:
            print("i = ", i)
            k.append(lst1[i])
            print("k from i ",k)
            i += 1

        elif lst1[i] > lst2[j]:

            print("j = ", j)
            k.append(lst2[j])
            print("k from j ",k)
            j += 1
    print(k)


arr1 = [1, 3, 4, 5, 21, 32]
arr2 = [2, 6, 7, 8, 10, 19]

mergeArrays(arr1, arr2)
