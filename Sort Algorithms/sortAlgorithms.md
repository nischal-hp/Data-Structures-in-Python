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

## Quick Sort : Divide and Conquer
Here, we choose a pivot element first. All elements to the left of pivot should be lesser than it.
All elements to the right of it, should be greater than it.
Once pivot is in the right position, it will be sorted.
Pick a different pivot in the left subarray and recursively repeat the steps until all elements are sorted.
Same goes with the right subarray.

Hence, by using partitioning technique we esentially divide the array into two; and thus follow the divide and conquer approach.
There are 2 types of partitioning techniques: 
1) Hoare Partition - British Scientist who invented Quick Sort. The original method.
2) Lomuto Partition

# Hoare Partition
Any element can be chosen as the pivot element. Lets choose the left most element as pivot element.
Two pointers are then used, start pointer - element next to pivot element.
end pointer - last element of array.
Start with start pointer, keep incrementing it until we find an element which is greater than pivot element.
Stop once we find. Then start decrementing the end pointer, until we find an element which is lesser than pivot element.
if both conditions are satisfied, swap elements at start and end pointer locations. 
Continue the process from the same locations; dont reset the pointers.
We stop the process when end crosses over the start pointer. At this step, swap the pivot element with the end element.
Now we will see that all elements to left of pivot are less than it, and all elements to right of pivot are greater than it.

# Lomuto Partition
Choose last element as pivot element. Then we start p index(partition index) from the first. 
We go on iterating until we find an element which is greater than pivot.
Stop at this place. Now start an i index which starts from p index, and goes on incrementing
until we find a value which is less than or equal to the value of pivot.
Now swap the 2 elements. Continue incrementing p index till the end of array.
By the end of it, we would have the pivot element at the right position. 

Average Time: O(nlogn)
Worst case : O(n^2), when the array is already sorted

## Merge Sort 
This works on Divide and Conquer approach.
The underlying working is based on merging two sorted arrays into a single sorted array.
Take the first element of two sorted arrays. Compare them and put the lowest out of them in the new sorted array.
Increment the counter in the array which had the lowest element. Keep repeating the process until we are done with
all the elements in both the arrays.

Since array with single element is sorted. The first step is to divide the unsorted array into single element arrays.
Next we go on combining two at a time, to go on building the sorted array.

We can create another array to store the sorted elements. But a more efficient way would be to use the original array
and modify it in-place.

Time Complexity : O(nlogn)

This is used by Tim Sort, which is the default sort we get with python. Tim Sort is a hybrid sort algorithm
which uses a combination of Merge Sort and Insertion Sort, to work well with the real world data.

## Shell Sort
This is an optimization over Insertion sort. The issues with Insertion sort are :
1) If there is a lower value towards the right side of the pointer, then we will end doing lot of comparisions and swaps.
Have to compare with each value. Once found the right place, have to swap other elements and move them up a place in the array.

The intuition for Shell Sort is to have heavier elements on right hand side and lesser elements on left hand side.
They might not necessarily be sorted, but this will help us later in the sorting process.

# Algorithm:
1. Start with a gap of n/2 and sort the sub-arrays. (Ex: For an array with [3,4,1,2] and gap=2. We choose alternate elements for the subarray. Sort elements 1 and 3; then elements 2 and 4. The final sorted array in this case is [1,2,3,4])
2. Go on reducing gap by n/2 and keep on sorting the subarrays. (i.e n/4, n/8 and so on).
3. Last iteration should have gap=1, which is same as Insertion sort.

# Time Complexity:
Worst Case : O(n^2) (worst known worst case gap sequence)
O(nlog^2n) (best known worst case gap sequence)

Best Case : O(nlogn) (most gap sequences)
O(nlog^2n) (best known worst case gap sequence)

## Selection Sort
FOr the first index, choose the minimum element from the remaining array, and swap the 2 elements.
For second index, choose the minimum element from the unsorted array, and swap the 2 elements.
Continue the same process, till the end of the array.

# Time Complexity:
O(n^2), since we will have 2 for loops





