def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:     # Keep on iterating until the we find a spot where anchor element is greater than prev element
            elements[j+1] = elements[j]    # This is just moving the array in-place
            j = j - 1
        elements[j+1] = anchor    # Finally when the condition is satisfied, insert the anchor element there

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)
    #
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')