def bs(data, item, low, high):
    location = 0
    while(low <= high and location == 0):
        mid = (low+high)//2
        if(item == data[mid]):
            location = mid
        elif (item < data[mid]) :
            high = mid - 1
        else:
            low = mid + 1
    return location


data = [1, 3, 5, 6, 7, 9, 10, 14, 17, 19]
n = 10
location = bs(data, 17, 0, n - 1)
print(location)
