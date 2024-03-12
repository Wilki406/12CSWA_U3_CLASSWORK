elements = []
def selectionSort(elements):
    for i in range(len(elements)):  # iterate through the length of elements
        smallest = i  # assume current value is the lowest
        for k in range(i + 1, len(elements)):  # iterate through the unsorted portion of the list to find the minimum
            if elements[k] < elements[smallest]:  # if the current element is < than the element update min index
                smallest = k  # swap current element with lowest element
        if smallest != i:  # if the current smallest element is not equal to the current element
            # Swap the current element with the minimum element found
            temp = elements[smallest]
            elements[smallest] = elements[i]
            elements[i] = temp
    return elements 



while True: # While state is True
    userInput = (input("Enter a number to add to the list of elements or enter text 'NEXT' to continue\n")) # Get user input on what to add to element list
    if userInput == "NEXT": # if continue types next continue with algorithm
        print(f" Unsorted: {elements}") # print unsorted elements
        print(f" Sorted: {selectionSort(elements)}") # print sorted elements
        break # stop the loop
    else: # else accept values
        elements.append(int(userInput)) # append/add to the element list
