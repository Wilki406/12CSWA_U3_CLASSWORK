elements = []

def selectionSort(elements):
    for i in range(len(elements)): # iterate through the length of elements
        smallest = i # assume current value is the lowest
        for k in range(i + 1, len(elements)): # iterate through the unsorted portion of the list to find the minimum
            if elements[k] < elements[smallest]: # if the current element is < than the element update min index
                smallest = k # swap current element with lowest element
        if smallest != i: #
            temp = elements[smallest]
            elements[smallest] = elements[i]
            elements[i] = temp
    print(elements)
    return elements










selectionSort(elements)
