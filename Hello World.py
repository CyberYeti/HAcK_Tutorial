print("goodbye World")

def median(inp):
    l = len(inp)
    i1 = l//2
    i2 = i1 - 1

    if l%2 == 0:
        return (inp[i1] + inp[i2])/2
    else:
        return inp[i1]
    
arr = [1,2,3,4,5]
arr2 = [1,2,3,4]

print(median(arr))
print(median(arr2))