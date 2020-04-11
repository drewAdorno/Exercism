def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1]['value'] > arr[i]['value']:
                swap(i - 1, i)
                swapped = True
                    
    return arr

def maximum_value(maximum_weight, items):
    currentWeight=0
    currentValue=0
    
    bubble_sort(items)
    
    for i in range(len(items)-1,-1,-1):
        currentValue+=items[i]['value']
        currentWeight+=items[i]['weight']
        if(currentWeight+items[i-1]['weight']>maximum_weight):
            return currentValue
    return currentValue

