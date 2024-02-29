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

# Collision handling in Hash Table - 1) Chaining:
Suppose 2 keys try to map to the same memory location (due to their hash value being same), then a collision occurs.
To avoid collision, can go for Chaining, which is storing a list or a linked list at every location instead of just the value.(linked list wil store both the key and the value, which can be used to later iterate the ll based on key)
That way multiple keys can share the same hash value.
Iterating in this method, can take O(n) in worst case, due to ll use.

# Collision handling in Hash Table - 2) Linear Probing:
When we find out that another value is already occupied in the computed hash value location, we search for the next available empty slot; that is, we go on linearly probing for the next possible location to insert the value into.

# Stack (LIFO)
Real like ex where its useful : 1) clicking the back button on a browser takes us to the last seen page. Browser history/URL is stored in Stack structure. 2) Function calls in any programming language is stored in a stack. Hence the name function stack.
3) When using Undo(ctrl+z) functionality in any editor or program, a stack is used to keep track of the prev operations. 

If we use Array to do this, we have to use Dynamic Array, which has its own cons.
If we use single LL to do this, then will have to traverse all the way to reach the end of ll.

Push/Pop element from Stack : O(1)
Searching element in Stack : O(n)

In Python, stack can be implemented the foll. ways : Using a list, collections.deque, queue.LifoQueue
import collections.deque 
stk = deque()
stk.append(2)
stk.pop()

Cons of using a List as a Stack is internally it is a Dynamic Array. So the cons associated with that will come into play.

collections.deque is internally implemented using a Doubly LL. So it does not have any cons as such.

# Queue (FIFO)
Suppose NY Stock Exchange wants to send out the the prices of a Stock minute by minute through an API synchronous call. Suppose the receiver of the messages(Ex: Yahoo Finance (www.finance.yahoo.com/api/post_price)) is down for any reason, then the data in that timeframe would be lost, since its a synchronous call.
Also suppose, tomorrow if we have to add a new receiver (then the API URL through which the call is made needs to be updated as well). Ex: For Google Finance (www.finance.google.com/api/post_price).
This is a tightly coupled architecture, which is not good.

Alternative is to use a memory buffer, where NYSE goes on posting the stock prices along with the time info in that buffer. Any consumer can then access this buffer, and use it however they want to. This would use a queue structure. This way can ensure Loose Coupling.

The problem of Producer-Consumer tight coupling, could be solved by having a Queue structure in between which ensures loose coupling.

In Python, queue can be implemented the foll. ways : Using a list, collections.deque, queue.LifoQueue
import collections.deque 
stk = deque()
stk.appendLeft(2)

Cons of using a List as a Stack is internally it is a Dynamic Array. So the cons associated with that will come into play.

collections.deque is internally implemented using a Doubly LL. So it does not have any cons as such.

# Tree
When data we want to represent is in heirarchical form, and not in linear form.
Ex: 1) For an E-commerce site, Electronics could be grouped to : laptop, cellphone, tv. 
Cellphone can be further grouped into: iphone, android. And so on...
2) Org structure for a company, 3) Folder structure for an OS

Each entity is called Node. Starts from root node, goes all the way to leaf node.
parent-children relationship and ancestor-descendent relationship exists.

Level 0 stands from Root Node. Level 1 is children of root node and so on.

# Binary Tree and BST
If Maximum children for each node is 2, it's called Binary Tree.
Binary Search Tree is special case of Binary Tree, which also has order associated with the elements.
All values less than current node value, appear to the left of it. And all values greater appear to the right of it.
So all keys are distinct and duplicates are not allowed.

Complete binary tree is a binary tree in which all the levels are completely filled except possibly the lowest one, which is filled from the left. A complete binary tree is just like a full binary tree, but with two major differences. 1) All the leaf elements must lean towards the left. 2) The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

Full binary tree is a special type of binary tree in which every parent node/internal node has either two or no children. It is also known as a proper binary tree.

Thus BST can be used to store something like set() data structure in Python, but for heirarchical data.

Searching for an element becomes easier. Since looking at node value, we can determine whether to traverse left/right subtree.
Every iteration we reduce search space by 1/2.
For a BST with 8 nodes, to search an element we need to do 3 iterations.
Hence, Time Complexity for Searching : O(logn) (log is to base 2)
Insert complexity is also O(logn), since we have to search for elements first, before inserting.

Both are average time. In worst case, it is O(n), that is in case where there is single left subtree with 3 nodes.
Have to search through all nodes in worst case, if the passed value is less than all those.

Traversal Techniques: BFS and DFS(in-order, pre-order, post-order)
in-order : left-root-right
pre-order : root-left-right
post-order : left-right-root

Use of BST : 1) in-order traversal can be used to sort elements in ascending order.
2) Can be used to implement set, since duplicates will be removed.

## Node Deletion in BST
Deletion of node with no child and single child is easy. Just replace the child in the removed node's place.
Deletion of node with 2 children is complicated. Have to rebalance the tree. The steps to be followed in such case:
1) Take minimum from right subtree and copy it to delete node's place (Coz root node should be greater than left subtree,
but less than right subtree)
2) Remove the duplicate entry in the right subtree

Alternate Approach : 
1) Take maximum value from left subtree
2) Delete duplicate node in left subtree

# AVL Tree
AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees for any node cannot be more than one.

# Red-Black Tree
A red-black tree is a kind of self-balancing binary search tree where each node has an extra bit, and that bit is often interpreted as the color (red or black). These colors are used to ensure that the tree remains balanced during insertions and deletions. 

Although the balance of the tree is not perfect, it is good enough to reduce the searching time and maintain it around O(log n) time, where n is the total number of elements in the tree.

Rules That Every Red-Black Tree Follows: 
1. Every node has a color either red or black.
2. The root of the tree is always black.
3. There are no two adjacent red nodes (A red node cannot have a red parent or red child).
4. Every path from a node (including root) to any of its descendants’ NULL nodes has the same number of black nodes.
5. All leaf (NULL) nodes are black nodes.

# N-ary Tree
An n-ary tree is a tree in which each node can have a variable number of children, not limited to two as in a binary tree. In an n-ary tree, a node can have up to n children.

# Trie (Prefix Tree)
A trie, also known as a prefix tree, is a tree data structure used for efficient retrieval of keys in a dataset of strings. Each node in a trie represents a common prefix of a set of strings.

# Graph
Ex: 1) FB friend list is maintained through graph. Each node is a person. All the person's friends are connected to this node,
via an undirected edge. This can used for Friend Suggestions, using mutual friends.
2) A directed graph can be used to show flight routes btw diff countries.
This can be expanded to find out path with minimum stop distance, or path with minimum travel time.
3) Google Maps, 4) Amazon Product Recommendations, 5) Netflix recommendation.

If the edges have a weight, it is called Weighted Graph.

## For Coding Graph in Python : 
Each path can be represented as a tuple of start and end nodes.

## Different Types of Graphs
Directed, Undirected, Weighted, Unweighted, Cyclic, Acyclic, Complete (every node is directly connected to every other node), Bipartite (A graph in which the vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set.), Trees, Sparse Graphs, Dense Graphs.

## Difference Between Tree and Graph
There can be only one path between two nodes in a Tree. Hence, Tree is a special type of graph.
Graphs and Trees are recursive data structures. So the algorithm used on them, should also be a recursive function.

# Recursion Concept
1. Divide big problem into small and simple problem
2. Find a base condition with a simple answer
3. Return or roll back answer from base condition to solve all the other sub-problems.

Ex : To find the sum of numbers from 1 to 5.
This can be split into smaller subproblems as shown below : 
1. 5+ sum of nos from 1 to 4
2. 4+ sum of nos from 1 to 3
3. 3+ sum of nos from 1 to 2
4. 2+ sum of nos from 1 to 1,
we have arrived at the base case, which is sum of nos from 1 to 1, which is 1.
Thus by rolling back the answer from base case, we can solve the other sub-problems too.
