def max_product_subarray(arr_length, arr):
    dp = [arr[0]]
    result = arr[0]
    for i in range(1,arr_length):
        if (arr[i] * dp[i - 1] > arr[i]):
            dp.append(arr[i] * dp[i - 1]) 
        else:
            dp.append(arr[i])
        if (dp[i] > result):
            result = dp[i]    
    print("Maximum product of contigous sequece {}".format(result))

arr_length = int(input("Enter number of elements you want in array: "))
arr = []
for index in range(arr_length): 
    element = float(input("Enter elements you want in array: "))
    arr.append(element)
print(arr)

max_product_subarray(arr_length, arr)
# =.1,17,1,5,.05,2,4,1,.7 ,.02,12,.3,
# 10, .1, 17, 1, 5, 2, .05, 2, 12, 4, 1, 5, .7, .08