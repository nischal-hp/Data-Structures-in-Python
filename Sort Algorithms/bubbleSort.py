def bubbleSort(elements):
    for i in range(len(elements)):
        for i in range(0,len(elements)-1):
            if elements[i]>elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
    return elements

print(bubbleSort([4,3,2,1]))


# There are a couple of inefficiencies here. 
# 1) We do not need to iterate the inner for loop throughout the entire length, we can stop it 
# before we encounter already sorted elements. 
# 2) If we pass in an already sorted array. We don't need to go through the entire process.
# In just first pass, we can check if swapping happened or not using a flag. 
# If swapping did not happen even once, that means we have an already sorted list. 
# Can break out of the loop and time complexity will be O(n)

def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False   
        for j in range(size-1-i):      #  Efficiency Step 1 
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True  

        if not swapped:              #  Efficiency Step 2
            break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)