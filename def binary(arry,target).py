def binary(arry,target):
    left = 0
    right = len(arry)- 1


    while left <= right: 
        
        mid= left + right // 2
        
        if arry[mid] == target:
            print(f"the index of {target} is {mid}")
        elif arry[mid]>=target:
            right = mid -1
        else:
            arry[mid]<= target
            left  = mid + 1
            
    return -1

arr = list(map(int,input("Enter your list with spaces:-").split()))

target = int(input("Enter your target:-"))

results = binary(arr,target)

if results != -1:
    print(f"the index of {target} is {results}")
else:
    print("No number in the list")

