## Bubble Sort : 
In an array, we compare two consecutive elements and swap them, based on which is greater. 
Towards the end of first pass, we will have the highest element in the array towards the last position.
Same process is repeated (n-1) times, to sort the entire array.

Ex: For array [4,3,2,1].
In First pass : 
4 >3, hence [3,4,2,1]
At end of first pass : [3,2,1,4]
At end of second pass : [2,1,3,4]
Repeat this for all elements.

Time Complexity : O(n^2), since it is 2 for loops, on within each other.
It could be reduced to O(n), if an already sorted list is passed to it.
See code implementation for more details. 

Space Complexity : O(1), no extra space is used.

The sorting works on strings too, since we can use comparision operators on strings as well.

## Insertion Sort : 
When given an unsorted array, we create another array. 
We go on adding element by element to the new array, such that the sorted order is maintained always.
Ex: given = [3,4,1]
Create new = []
Insert 3, new = [3]
Insert 4, new [3,4]
Repeat this for all the elements. 

But this causes O(n) space complexity. This can be avoided by using the original array itself.
We can use a pointer. Any element towards left, will be a sorted array, and to the right will be unsorted.
When elements are moved from right of of the pointer to the left, they have to be put in the correct position.

We consider first element to be sorted, then start with the second element in this case.

Time Complexity (Worst Case): O(n^2) comparisions and swaps. 
Best Case : O(n) comparisions and O(1) swaps.
Space : O(1), or O(n) depending on implementation.

It is only used for smaller list sorting, due to large time complexity. But the implementation is simple in Python.