#### 

This story is eligible to be part of the metered paywall. [Learn
more](https://help.medium.com/hc/en-us/articles/360018834314)

# Data Structures and Algorithms Revisited: Part 2

![](https://cdn-images-1.medium.com/max/1600/0*3AQ-I1E5rbktxYVo.jpg)
<span class="figcaption_hack">Image source:
[https://www.azquotes.com/quote/755272?ref=data-structures](https://www.azquotes.com/quote/755272?ref=data-structures)</span>

Hello, I’m Kosuke Kuzuoka, an AI research engineer at DeNA Co., Ltd. This is my
second post in the Data Structures and Algorithms Revisited series. In this blog
post, I will explain about the most common data structures and how they work,
then briefly talk about the pros and cons for each data structure.

This blog post is meant for beginners or people who want to learn the basics
about CS topics. If you haven’t read my first post, you might want to go back
and read it to understand the terminology used in this blog post. I will leave
links to all the posts in this series. Let’s dive in!

1.  [Part 1: What are Data Structures and
Algorithms?](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-1-bffbcea48762)
1.  [Part 2: Most Widely Used Data Structures (Arrays and Linked-Lists)
*](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-2-96b42a58ecde)
1.  [Part 3: Most Widely Used Data Structures (Stacks and
Queues)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part3-f9cc5534afcf)
1.  [Part 4: Searching and Sorting (Binary
Search)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-4-e5576e1f53f3)
1.  [Part 5: Searching and Sorting (Recursion and
DP)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-5-d71dcb256c18)

### List-Based Collections: Arrays

Arrays are perhaps one of the most common data structures used in software
development. As I briefly mentioned in the first blog post, arrays are great
because they are very easy to use, and they have constant time for looking up an
element if you know the index. But I also mentioned that they are not really
efficient for insertion and deletion operations. Let’s look at how an array
works in order to understand those properties.

Here we have 5 elements in an array (shown in blue) with same integer data type.
The red text represents the indices for the elements. The way an array stores
each element is that it remembers the memory location for the first element
annotated as the bold black consecutive zeros on the bottom left of the figure.
Then every time you specify an index i, the array will look for a memory
location of* initial location + (i * data size)*, where the data size for each
integer is 8 bit in the example above and represented as hex numbers. This works
because it allocated consecutive memory when you specified the size of the
array. This is one of the reasons why an array can’t store multiple data types
in a lower-level language, such as C++ or C.

Indexing with arrays works well and runs in constant or O(1). That’s great. Now
let’s see why insertion and deletion with arrays takes linear time or O(n). In
order to understand why this is the case, we need to understand how insertion
and deletion operations with an array work. Let’s look at the figure below!

Here we have the same array as before, and we will try to add a new element in
the middle. What we need to do here is shift all the elements after the middle
by one to the right to make a space for the new element, then insert the new
element into the middle. Now let’s think about what happens when you insert an
element at the beginning of the array. You need to shift all the elements in the
array before insertion by one to make the space, then add the element in the
beginning. Shifting an element takes O(1) time, but you have to do it for n
elements. This makes the runtime for insertion O(n) in the worst case!

The way deletion works is similar — it removes an element and shifts elements by
one to the left, instead of right. I won’t go into the details of how deletion
works. The takeaway here is that arrays are efficient for looking up a value,
but not for insertion and deletion. I would say that in most cases arrays are
enough, but if you often modify the length of the array by inserting and
deleting, then you might want to consider using a different data structure with
simpler insertion and deletion operations, and possibly more efficient than
O(n). Let’s look at some different data structures which have simpler insertion
and deletion operations than arrays!

### List-Based Collections: Linked-lists

Linked-lists are another data structure which have some good properties that
other data structures don’t have. A linked-list has what’s called a node. A node
is just like an element in an array, but each node has its value and reference
to the next node or the link. This is the main reason why they’re called
linked-lists. Let’s see what a linked-list looks like!

As you can see we have boxes just like arrays, but each box now has a reference
to the next node, unlike arrays. Each linked-list has what’s called a head node,
which is simply the first node of the list. Unlike arrays, you can’t get an item
by simply specifying an index, rather, you have to traverse the list to get an
item. Linked-lists can be easily implemented in code using two classes,
LinkedList and Node classes. I implemented LinkedList and Node class in code to
further discuss the runtime of common operations, such as insertion and
deletion.

Insertion and deletion with a linked-list is fairly simple and easy to
implement, unlike the array data structure. Let’s look at the code for inserting
an element into a linked-list in order to analyze the runtime for the operation.

Here I used a for loop to reach the node just before where I want to insert a
node. Then I assigned the previous node’s next attribute to the new node, and
set its next to the previous node’s next. This way we can insert an element into
a linked-list. Now what do you think will be the runtime for this operation? If
we were to insert an element at the end of the list, then we have to go all the
way to the end node. Updating the previous node’s next and the new node’s next
only takes O(1). The overall result is that it takes O(n).

Since the deletion operation is similar to the insertion operation, I won’t go
into the details of how the deletion operation works. You can check out my
implementation of deletion with linked-lists if you are interested, but again it
is really similar to the insertion operation. Let’s talk about lookup operation
with linked-lists. We know that the lookup operation with arrays takes O(1).
What do you think it takes for linked-lists to look up a value? I implemented a
lookup method for LinkedList class to analyze the runtime.

Here I simply use a while loop to traverse the linked-list to get the node with
the position specified by the input. As soon as I hit the node, we simply return
the value of the node. This is simple enough, now let’s think about the runtime.
If I want to get the value of the last node, I first have to traverse the list
all the way to the last node. This takes O(n), and in the worst case a simple
operation like a lookup takes linear time, while arrays do the same with O(1).

Now, you might wonder why we would use a linked-list instead of an array. When
you modify the size of an array in lower-level languages, what’s happening
behind the scenes is that it copies all the elements in the array and creates a
new array with the new size and copied elements. The same thing happens for
deletion. This is not very efficient or intuitive, but a linked-list can do this
in a relatively simple way. Also, we looked at this in terms of Big-O notation,
but if we were to talk about the best time complexity, then linked-lists have
constant time — this happens when you insert a node in the head, while arrays
are still O(n).

### Conclusion

In this blog post, I talked about arrays and linked-lists and how they work for
common operations, such as looking up an element or insertion. To understand
what’s happening under the hood is really important to determine when to use
arrays over linked-lists and vice versa. It’s also important to notice that the
way arrays work differs in different languages and implementations — especially
between lower-level languages and higher-level languages.

Thanks a lot for reading through this blog post. I hope this blog post helped
you understand what’s under the hood for common data structures. Using the right
data structures at the right times really helps you write efficient code. I will
talk about stacks and queues in the next blog post and implementation in Python
as well. In the meantime, please leave 50 claps if you like the post to motivate
my next blog post :D

* [Programming](https://medium.com/tag/programming?source=post)
* [Data Structures](https://medium.com/tag/data-structures?source=post)
* [Algorithms](https://medium.com/tag/algorithms?source=post)
* [Python](https://medium.com/tag/python?source=post)
* [Computer Science](https://medium.com/tag/computer-science?source=post)

### [Kosuke Kuzuoka](https://medium.com/@kousukekuzuoka)

Self-taught AI research engineer at DeNA Co., Ltd. passionate about self-driving
car technology and deep learning.
