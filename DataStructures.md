Data Structures are like building blocks, using which we can implement any code logic to get the desired result.
Similar to raw materials used for building a house (brick, cement).

# Array:
Time Complexity : 
Lookup by index : O(1), Array traversal : O(n).
Adding element to array : O(n). It has to shift other elements by one index.
Removing element from an array : O(n). Same explanation as above.

In Python list is a dynamic array.
In other languages like Java, there can be static and dynamic array.
Static means array of fixed size; dynamic meaning a block of memory location will be allocated at the beginning(Say 10).
If we add an element at 11th position, it will create new memory block which original+original size*2 (30). 
Copy over all the prev elements and then do the insert.
Overhead of creating new memory block, as well as copying over the elements from old location.
which leads to wastage of resources. 
ArrayList is an example of Dynamic Array in Java.

List can store string, numbers, complex objects or a combo of anything in Python.
There can be 2D, 3D array and so on.

# Linked List :
Used to solve some problems associated with Array. Suppose we insert an element into index 1, all the subsequent elements have to be moved further.
So array insertion complexity is O(n).
Since Python list internally is a dynamic array, it will have all the problems associated with that.
In LL, elements are stored randomly in memory. But they have a reference to the address of the next/prev element depending on the kind of LL.
Adding or removing element becomes easy in such case.
For single LL, insert/delete element at the beginning is O(1). Insert/delete element at the end or in middle : O(n).
LL traversal/ accessing element by value : O(n).
LL has 2 adv over array : 1) Dont need to pre-allocate space. 2) Insertion/Deletion is easier

Double LL has 2 addresses. One to prev and one to next.

Adv. of Array over LL : Accessing element through index is O(1). Whereas in LL accessing element by value is O(n).
Also insert/delete element at start of array is O(1) [although it has cons due to being a dynamic array. Hence it is amortized], compared to LL where it is O(n)

# Hash Table/Dictionary : 
Key passes through a hash function which gives the address of the memory location of the value stored.
Using the hashed value we access the value stored. This all happens in O(1) time on average.
Insertion/Deletion is also O(1) on average.

Hash Map/Hash Table is the internal implementation. Dictionary is python specific implementation of Hash Table.

One implemetation of Hash function is to convert all characters in key to ascii number, sum it up and use the mode(10) value as  the result.

Because of this underlying mechanism we cannot have two keys with same value in Dictionary. Since it would result in the same hash value.