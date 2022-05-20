# Linear Search
In an array, if we go on searching one element after another it is Linear Search.
Time Complexity : O(n)

# Binary Search
This is used on a sorted array.
Find middle element.
If middle element > search element, discard right side of middle element.
If middle element < search element, discard left side of middle element.
Continue the process until we find the element or have iterated through all elements.

Here, 1st iteration takes n/2 elements.
2nd iteration take (n/2) /2 = n/4 elements.
For k iterations, it is n/2^k. Taking log and solving for it, [i.e, 1 = n/2^k and solving for it by taking log] we get,
Time Complexity is O(logn), which is much better than linear search.