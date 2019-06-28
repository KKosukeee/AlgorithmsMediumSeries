#### 

This story is eligible to be part of the metered paywall. [Learn
more](https://help.medium.com/hc/en-us/articles/360018834314)

# Data Structures and Algorithms Revisited: Part 3

![](https://cdn-images-1.medium.com/max/1600/1*9FamdLBX9v4XTTANCGDY0A.jpeg)
<span class="figcaption_hack">Image source:
[https://www.azquotes.com/quote/592442?ref=data-structures](https://www.azquotes.com/quote/592442?ref=data-structures)</span>

Hello, I’m Kosuke Kuzuoka, an AI research engineer at DeNA Co., Ltd. This is my
third post in the Data Structures and Algorithms Revisited series. I talked
about the most common data structures in my previous post, but couldn’t cover
stacks and queues due to space constraints, so I decided to talk about stacks
and queues in this blog post. As in the previous post, I will talk about how
these data structures work with the implementation in Python.

This blog post is meant for beginners or people who want to learn the basics of
CS topics. If you are new to data structure topics, then you might want to go
back and read my previous posts to understand the terminology used in this blog
post. I will leave all links to the previous blog posts. With that being said,
let’s dive in!

1.  [Part 1: What are Data Structures and
Algorithms?](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-1-bffbcea48762)
1.  [Part 2: Most Widely Used Data Structures (Arrays and
Linked-Lists)](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-2-96b42a58ecde)
1.  [Part 3: Most Widely Used Data Structures (Stacks and
Queues)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part3-f9cc5534afcf)
*
1.  [Part 4: Searching and Sorting (Binary
Search)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-4-e5576e1f53f3)
1.  [Part 5: Searching and Sorting (Recursion and
DP)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-5-d71dcb256c18)

### List-Based Collections: Stacks

A stack data structure is perhaps one of the most intuitive data structures
around. A stack is just like a stack of objects in real life — you keep adding
elements on top, and you have easy access to remove or look up the top element.
To get the bottom element from a stack, you have to remove all the elements
until you reach the bottom. This nature of how elements are retrieved and added
has a particular name. Because the element you get first from the stack is the
element you added in last, it is simply called *last in, first out* or **LIFO**
for short. Simple enough. Now let’s look at what a stack looks like to
understand it visually.

Here we have 5 elements in a stack. Adding an element into a stack is called a
*push* operation, and you add a new element on the top, just like in the figure
above. When you want to get an element from a stack, you *pop* the top element
from the stack. There is an operation called *peek*, which simply gets a value
of the top element without popping it from the stack. Those operations are very
efficient and in most cases, it will only take constant time or O(1) — I said
“most cases” here, because it depends on underlying data structure you use to
implement a stack. Now we understand how stack data structures work visually.
Let’s look at the implementation using the LinkedList class from the previous
post to understand the time complexities!

Here I implemented a stack using the LinkedList class. Whenever a *push*
operation is called, I simply add the element as the head of the linked-list by
calling the *append_left* function of the LinkedList class, so the operation
runs in O(1) — I update the head value with the input element and assign its
next value to the previous head node. The *pop* operation is the opposite of the
*push* operation. What I do to *pop* an element out of the stack is simply get
the head node and update the head node with the previous head’s next node. This
runs in O(1) as well, because the operations have nothing to do with the length
of the list. The *peek* operation is as simple as it looks. It returns the head
node value without calling the* pop *operation. As you might guess, this runs in
O(1) as well.

Previously I said that common operations for a stack data structure run in O(1)
in most cases. This is the case with my implementation, but if you were to
implement a stack with an array, then it could be O(n) for *push* and *pop*
operations in the worst case, because inserting and removing an element from an
array takes O(n) in the worst case — again, this depends on the programming
language. We can say the same thing for a queue data structure as well. Just
keep in mind that runtime complexity for stacks and queues could differ by
implementation, so the next time you are asked in the coding interview, you can
nail it ;)

### List-Based Collections: Queues

Just like stacks, queues are intuitive and easy to understand. A queue is just
like a bunch of people waiting for a famous restaurant — the people who have
waited the longest get in to the restaurant first and leave the queue first.
Unlike a stack, the first element added into a queue is the one that gets out
first. This structure is explained as *first in, first out* or **FIFO** for
short. You can think about it as the only difference between queues and stacks
being in the removal process. In a stack we remove the item that was most
recently added; in a queue, we remove the item that was least recently added.
Now let’s look at what a queue looks like to understand it visually!

Here we have the same elements as we had in the stack example. You can see that
the first element or the least recently added element gets out first with the
queue example, while the last element or the most recently added element gets
out first with the stack example. The operation for adding an element into a
queue is called *enqueue*, and getting an element out of the queue is called
*dequeue*, while they were *push* and *pop* for a stack respectively. Looking at
the value of the least recently added element without actually *dequeueing* is
called *peek* just like with a stack. Now we know the common operations for a
queue data structure. Let’s look at it in code to see how we can implement this
using the LinkedList class!

Just like before, I used the LinkedList class from the previous post to
implement a queue. The only difference in the implementation from the stack
example is whether I’m adding the new element as its head or as its tail. With
the implementation above, I simply add a new element as its tail by calling the
*append_right* method of the LinkedList class. The LinkedList class has two
pointers for its head node as well as its tail node, so adding a new node to its
tail runs in O(1) — it updates the current tail’s next property to the new node
and updates the tail pointer. The *dequeue* operation and *peek* operation are
the same as the stack implementation and they both run in O(1). Just like
stacks, the runtimes for *enqueue* and *dequeue* operations vary with the data
structure you use to implement it. I implemented a queue using a linked-list
data structure, and it should run in O(1) for the common operations. Let’s see
if this is the case!

I created a queue with difference size ranging from 1 to 1000 inclusive. Then I
called *enqueue*, *dequeue* and *peek* operation. You can see that each
operation takes almost the same amount of time and there is almost no
correlation between the size of the list and the runtime. This means that each
operation runs in O(1). Now we understand how stacks and queues work and how we
can implement them in code using the LinkedList class. Let’s sum them up!

### Conclusion

In this blog post, I talked about stacks and queues. Stacks and queues are
intuitive and easy to implement compared to other data structures. If you are
preparing yourself for an upcoming coding interview, this knowledge will
definitely help you to get through it. Keep in mind that in most programming
languages, those data structures are implemented for you as built-in packages or
as external modules, so you don’t really have to implement them yourself. I was
once asked a question like “implement a queue using linked-lists and arrays,
then analyse the complexities”. I knew how I can implement it using different
data structures and I could make it. So knowing how they work is very important,
even though you don’t really create it on your own.

Thanks for reading through this blog post. I hope this blog post helped you
understand about stacks and queues. Next time I will talk about the searching
and sorting algorithms and share the implementation using the data structures
that I covered so far in this blog series. But in the meantime, please don’t
forget to leave claps and I will see you in the next post ASAP :D

* [Data Structures](https://medium.com/tag/data-structures?source=post)
* [Algorithms](https://medium.com/tag/algorithms?source=post)
* [Computer Science](https://medium.com/tag/computer-science?source=post)
* [Programming](https://medium.com/tag/programming?source=post)
* [Python](https://medium.com/tag/python?source=post)

### [Kosuke Kuzuoka](https://medium.com/@kousukekuzuoka)

Self-taught AI research engineer at DeNA Co., Ltd. passionate about self-driving
car technology and deep learning.
