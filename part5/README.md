#### 

This story is eligible to be part of the metered paywall. [Learn
more](https://help.medium.com/hc/en-us/articles/360018834314)

# Data Structures and Algorithms Revisited: Part 5

![](https://cdn-images-1.medium.com/max/1600/1*Z7_xA5Pa2P9uyUABfsvvBA.jpeg)
<span class="figcaption_hack">Image source:
[https://www.azquotes.com/quote/669649?ref=computer-science](https://www.azquotes.com/quote/669649?ref=computer-science)</span>

Hi, I’m Kosuke Kuzuoka, an AI research engineer at DeNA Co., Ltd. This is the
fifth post in the Data Structures and Algorithms Revisited series. In the
previous post, I said that I would talk about sorting algorithms in this post,
but I realized that we need to understand how recursion and DP work in order to
understand the implementations of sorting algorithms. Recursion and DP are a
little hard to understand at first, but if you understand how they work, then
you can solve complicated problems with relatively fewer lines of code, and more
efficiently.

It’s worth mentioning that recursion is rarely used in real life software
development, because of the limitations in the[ call
stack](https://en.wikipedia.org/wiki/Call_stack). But this doesn’t necessarily
mean that you don’t have to learn these concepts, and if you are preparing
yourself for upcoming coding interviews, recursion and DP are must-know
concepts!

This blog post is meant for people who want to learn the basics of CS topics or
people who are preparing for upcoming coding interviews. If you are new to this
topic, I will highly recommend to go back to some of the previous posts in this
series to get familiar with the basics and terminology used in this post. I left
all links to the previous posts below. With that being said, let’s jump right
in!

1.  [Part 1: What are Data Structures and
Algorithms?](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-1-bffbcea48762)
1.  [Part 2: Most Widely Used Data Structures (Arrays and
Linked-Lists)](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-2-96b42a58ecde)
1.  [Part 3: Most Widely Used Data Structures (Stacks and
Queues)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part3-f9cc5534afcf)
1.  [Part 4: Searching and Sorting (Binary
Search)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-4-e5576e1f53f3)
1.  [Part 5: Searching and Sorting (Recursion and
DP)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-5-d71dcb256c18)
*

### What is Recursion?

Recursion is the way to simplify a complicated problem into smaller subproblems
by calling itself recursively. A recursive function consists of two cases, a
*base case* and a *recursive case*. You can think of a base case as a
termination condition, so when a base case is executed, your function should
stop calling itself recursively. On the other hand, a recursive case is the case
that you call your function recursively, so that the recursive call continues,
until it meets the terminate condition — the base case!

To better understand how recursion work, I implemented a function that solves a
very famous problem, the *n*th [Fibonacci
sequence](https://en.wikipedia.org/wiki/Fibonacci_number). Let’s look at the
implementation to understand how recursion works and how base cases and
recursive cases are defined.

The function that I implemented here finds the *n*th Fibonacci sequence
recursively. Let’s imagine that we are trying to find 5th Fibonacci sequence.
Initially, the argument *n* is set to 5. The first thing it does is that it
checks if *n* is less than 2 at line 9. In our case *n* is 5, so this condition
is not met, so it then calls itself twice with the arguments *n* set as 4 and 3
at line 12. Instead of returning the result when *n* is 5, it first calculates
4th and 3rd Fibonacci sequence. When *n* is 4, it calculates the 3rd and 2nd
Fibonacci sequence, and this goes on and on. Eventually, *n* gets to less than 2
(i.e. 0 or 1), and when that condition is met, it simply returns 1 or 0
according to the value of *n *at line 10. The base case in the function is
really important, because without the base case, this function falls into an
infinite loop.

Recursive calls are added into a stack, and popped when there is no more
recursive calls. I think it’s a little hard to understand what I mean by using
only an implementation above, so I created a diagram to illustrate what it looks
like. Let’s look at the diagram below to understand this.

I visualized a recursive tree here. Red lines represent the first recursive
path, and the bottom-left *fib(1)* is the one that hits the base case first, and
returns the value to the parent recursive call — the *fib(2)* in this case. The
parent recursive call of the *fib(1)* and the *fib(0)* needs to get values
returned not only from the *fib(1)*, but also the *fib(0)* as well, so it waits
until the *fib(0)* call is returned. When *fib(2)* has values returned from both
children, it simply adds those values, and returns to its parent recursive call
— the *fib(3)*. This pattern continues until there is no parent recursive call.
This happens when the value of *fib(5)* is returned, and that is the value that
is eventually returned by calling the *fib* function.

It’s worth mentioning that every recursive problem can be solved with an
iterative function as well. In fact, often an iterative approach is more
efficient than a recursive approach, because you can use early termination with
an iterative function, while you can’t with a recursive function. Now the
question is when you should use a recursive function over an iterative function.
I suggest you to use a recursive function whenever you think the solution in an
iterative way isn’t straight forward, or when you think that a recursive
function makes the problem a lot easier.

### **What is DP?**

We discussed about how recursion works by dividing a complicated problem into
smaller subproblems. Now let’s briefly talk about their runtimes. In the example
with the Fibonacci sequence, the recursive function called itself twice within a
recursive call. Every doubled recursive call calls itself twice and this goes on
and on, until the base case condition is met. You can think of it as doubling
our calls *n* times, which makes the runtime for the Fibonacci sequence
O(2^*n*). This is really inefficient after all, because it runs exponential to
the input argument *n*. Is there any other way that I can improve this runtime?
This is where the Dynamic Programming or DP technique comes into play!

If we analyse the recursive tree from the recursion section, we see where the
problem is happening. Let’s look at the diagram we used to explain how recursion
works to find the bottleneck!

You can see that we are calling *fib(2)* and *fib(3)* three times and twice
respectively, even though the answers don’t change for every call. This is an
inefficient operation, because it calculates the subtree of *fib(3)* and
*fib(2)* again and again. One thing we can do to optimize this is to store the
results for every *n*th Fibonacci sequence, so when we are asked to recalculate
*fib(2)*, you can immediately return the value without calculating it again. Let
me implement this using a dictionary called *memo*!

The main changes that I made here are checking if *n* is present in *memo*
dictionary before the recursive case. When the key exists in the dictionary, it
immediately returns the value. I simply store *n*th, *n-1*th and *n-2*th
Fibonacci sequence for every function call from line 16 to 18 to avoid
duplicated calculations. Everything else remains almost the same. The technique
of storing the results temporary to avoid duplicated calculation is called
memoization (NOT memorization!), and by using a data structure which efficiently
looks up a particular value (like the hash-map used in the above
implementation), you can immediately return it with O(1) time.

Now that the function should have improved, let’s compare it with previous
runtime! Because we only calculate *fib(3)* and *fib(2)* once, and this applies
not only to *fib(3)* or *fib(2)*, but for every *n*, this function runs in
linear time to the input argument *n*, so the runtime is O(*n*)! This is a
significant improvement compared to O(2^*n*). To prove this, let’s look at the
figure below where I compared both functions with the exact same inputs.

The function using DP runs much faster than the naive recursive function. In
fact, it looks like a constant time solution, which isn’t the case, but it
illustrates how a simple function can be improved significantly with relatively
small changes. The point of using DP is that we don’t do the duplicated
calculations for values that are calculated previously, so the function runs
more efficiently. You should use a DP technique whenever you find overlaps in
the computations, because it improves the runtime a lot. Now let’s move on to an
interview question that can be solved with the knowledge that you have got from
this blog post.

### Interview Question Time!

This question is found on[ LeetCode](https://leetcode.com/). You can check the[
original question](https://leetcode.com/problems/climbing-stairs/) and its
solution as well. As always, try to solve it on your own at first. If you are
stuck, then try to look at some of the hints that I left below. Often, the naive
solution that you come up first isn’t the optimal one. Try to think about what
you can improve from the naive solution. Good luck!

    You are climbing a stair case. It takes 
     steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

     Given 
     will be a positive integer.


     2
     2
     There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps


     3
     3
     There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

**Hint 1:** Given that you know *N* ways to get *i-1*th stair and *M* ways to
get *i-2*th stair, how many ways are there to reach *i*th stair?

**Hint 2:** Can you construct an array of length *n+1* with each element
representing a number of ways to get to the element?

You can check my implementation for this question
[here](https://github.com/KKosukeee/CodingQuestions/blob/master/LeetCode/70_climbing_stairs.py).
Compare it with your solution, and if you come up with a more efficient solution
than mine, please let me know in the comments, so I can check it out later!

### Conclusion

In this blog post, I talked about recursion and DP. Those topics are often asked
about in coding interviews, and to crack coding interviews, you have to know how
you can implement a recursive function and how you can improve the function
using DP. Recursion and DP are hard to understand, so I highly recommend you to
follow some of the simple examples, and try solving some easy questions on
LeetCode or another platform.

Thanks for reading this blog post. I hope it helped you understand the concept
of recursion and DP. In the next post we go back and talk about sorting
algorithms using the technique we learned in this blog post. Please leave me
some claps if you liked this post, otherwise I’ll see you in the next post :D

* [Algorithms](https://medium.com/tag/algorithms?source=post)
* [Data Structures](https://medium.com/tag/data-structures?source=post)
* [Computer Science](https://medium.com/tag/computer-science?source=post)
* [Recursion](https://medium.com/tag/recursion?source=post)
* [Dynamic Programming](https://medium.com/tag/dynamic-programming?source=post)

### [Kosuke Kuzuoka](https://medium.com/@kousukekuzuoka)

Self-taught AI research engineer at DeNA Co., Ltd. passionate about self-driving
car technology and deep learning.
