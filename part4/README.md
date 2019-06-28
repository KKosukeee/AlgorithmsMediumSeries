#### 

This story is eligible to be part of the metered paywall. [Learn
more](https://help.medium.com/hc/en-us/articles/360018834314)

# Data Structures and Algorithms Revisited: Part 4

![](https://cdn-images-1.medium.com/max/1600/1*5He1iI3fwXKpGJXaVeSwOA.jpeg)
<span class="figcaption_hack">Image source:
[https://www.azquotes.com/quote/918951?ref=computer-science](https://www.azquotes.com/quote/918951?ref=computer-science)</span>

Hello, I’m Kosuke Kuzuoka, an AI research engineer at DeNA Co., Ltd. This is my
fourth post in the Data Structures and Algorithms Revisited series. I talked
about common data structures and how they work in my previous posts. In this
blog post I will mainly talk about a searching algorithm, and give you a good
interview question that can be solved by using a searching algorithm. This topic
is really important and frequently asked in coding interviews as well. If you
understand this topic well, then you will be able to write efficient software
and you will have a better chance in your coding interviews!

This blog post is meant for people who want to learn the basics of CS topics or
people who are preparing for upcoming coding interviews. If you are new to this
topic, then you might want to go back and read my previous posts to understand
terminology and data structures used in this blog post. I will leave all links
to my previous posts below. With that being said, let’s dive in!

1.  [Part 1: What are Data Structures and
Algorithms?](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-1-bffbcea48762)
1.  [Part 2: Most Widely Used Data Structures (Arrays and
Linked-Lists)](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-2-96b42a58ecde)
1.  [Part 3: Most Widely Used Data Structures (Stacks and
Queues)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part3-f9cc5534afcf)
1.  [Part 4: Searching and Sorting (Binary
Search)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-4-e5576e1f53f3)
*
1.  [Part 5: Searching and Sorting (Recursion and
DP)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-5-d71dcb256c18)

### What is Searching?

Let’s imagine that you are preparing for an upcoming interview at top tech
company. The questions you will be asked are about the basics of computer
science. Now you want to review an old computer science book from your college
class. You have a bunch of books that are sorted by titles in your bookshelf,
and you know that the book you are looking for is in the bookshelf. How do you
efficiently find the book that you are looking for in this situation?

The simplest solution to this problem would be something like looking for a
title one by one from left to right, and stop searching whenever you find a book
with the same title. Great! You came up with a simple searching algorithm in
real life! The searching algorithm in the context of computer science is almost
the same, but the question will be something like “Given a list of items A and
an item B, search for B in A”, and you have to do it a little more efficiently
than the simple algorithm.

### Binary Search: An Efficient Searching Algorithm

As the example above, the books in the bookshelf are sorted in order so the
leftmost book starts with the letter “A” and the rightmost book starts with the
letter “Z”. You also know that your book’s title starts with a letter “G” —
“Grokking the Computer Science” or whatever. What if you divide the books in
half and look for the first letter in the middle book. If the first letter of
the middle book is, let’s say “M”, then you can say that there is no point to
look in the right half of the books, because “G” doesn’t fall into the range
from “M” to “Z”. You can imagine applying this technique until there is only one
book left and the book should be the one you are looking for. This is exactly
how a binary search works. Let’s look at the figure below to understand this
algorithm visually!

I simplified the example a little bit so it fits in the diagram. The books in
the list (or the bookshelf) are represented with the first letter of their
titles, and the book you are looking for starts with the letter “G”. As I
described in the above section, we first look for the middle book, and compare
the first letter of the titles. Then we cut in half according to the comparison
of their letters. We basically do the same thing repeatedly until there is only
one book left, and this should be the we are looking for. It might look a little
intimidating at first, but if you follow the steps with some examples, then it
will be more intuitive, believe me!

Now let’s look at the implementation in Python. The key here is to remember the
start and end index of whole array at first, then update the start and end index
according to the middle value. The stop condition here is when the start index
equals the end index — meaning they are pointing to the same element.

Here we have a function that does the binary search. The input to the function
is a list of integers and the integer value to search for in the list. The first
thing we do is get the first and the last index of the list at line 12, then cut
it in half for every iteration with a while loop — updating the *low* and *high*
value with *middle* value at line 21 and 23. The key for the implementation
above is how we update the *low* and *high* variable representing the left and
right pointers respectively. If the middle value is larger than the value, then
we know that our value resides in the left half, so we update the right pointer
to point to the middle at line 23. If that’s not the case, then we know that our
value resides in the right half, so we update the left pointer at line 21. This
way we are cutting the array in half every time.

Now let’s talk about the runtime complexity for this algorithm. Because we cut
the list in half for every iteration, the runtime becomes O(log(N)) — log base
2, not 10. If you want to prove it yourself, just imagine that you have 8
elements in the list initially, and next time you cut it in half, so the list
becomes length of 4 and do the same on and on. When you cut it into a half for
the third time, the list gets to a length of 1, and the algorithm terminates.
This is because log(8) is 3, and this holds for any number.

Let’s compare the performance of the binary search and simple linear search. I
randomly created different sizes of array, then ran linear and binary search on
them. The point here is not measuring the precise runtime for both search
algorithms, but comparing the efficiency of both algorithms. Let’s look at it!

It looks like the binary search is a lot more efficient than the linear search.
In fact, the binary search looks like constant time, but this is not the case.
It looks like constant time, because the linear search takes too much time, but
if we zoom into the performance of the binary search, then it should look like a
logarithmic function.

So the binary search works well and it’s pretty efficient. Let’s briefly talk
about its limitations. The binary search works if the list is sorted. If the
list is not sorted, you can still do the binary search after sorting the list,
but sorting a list at most efficiently will be like O(N*log(N)) , so it’s
actually worse than the linear search — linear search runs in linear or O(N),
hence the name. Now we know when binary search can be a good candidate, and when
not. Let’s look at a case where the binary search really shines!

### **Interview Question Time!**

I will give you a good coding question that I found on LeetCode which can be
solved with what you learned in this blog post. Try to apply the knowledge
first. If you can’t solve it efficiently, then look up some hints that I have
left at the bottom of the post. Good luck!

    Write an efficient algorithm that searches for a value in an 
     x 
     matrix. This matrix has the following properties:

    - Integers in each row are sorted from left to right.
    - The first integer of each row is greater than the last integer of the previous row.


    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
     true

Hint 1: Given *m* rows, how can you efficiently decide in which row the target
value possibly resides?

Hint 2: Given *n* items in a row that you get with vertical scanning, how can
you efficiently search for the target value?

If you solved this question and want to compare with my solution, please visit
this [Github
link](https://github.com/KKosukeee/CodingQuestions/blob/master/LeetCode/74_search_a_2d_matrix.py),
so that you can check my solution that I came up with using an efficient search
algorithm. If you have any questions about my solution or if you came up with
even more efficient solution, please leave me a comment in this post, so I can
check it later!

### Conclusion

In this blog post, I talked about an efficient searching algorithm, and how we
can implement it. Then we looked at a problem that we can apply our knowledge to
solve it efficiently. Whenever I see the statement like “given a sorted array,
do X”, I always ask myself if I can apply the binary search to solve it. It’s a
very good starting point to solve a question, and I highly recommend you to do
the same, if you are practicing for upcoming coding interviews.

Thanks for reading this blog post. I hope it helped you understand how binary
search works, and when you should apply it. In the next post I will talk about
sorting algorithms, and implement them in Python as always. I will leave an
interview question for the next post as well, so that you can apply your
knowledge to a real coding question. I will also share my solution to those
questions, so you can compare it with yours. I really hope that you liked this
blog post! If so, please leave some claps, and I will see you in the next post
:D

* [Programming](https://medium.com/tag/programming?source=post)
* [Computer Science](https://medium.com/tag/computer-science?source=post)
* [Algorithms](https://medium.com/tag/algorithms?source=post)
* [Data Structures](https://medium.com/tag/data-structures?source=post)
* [Python](https://medium.com/tag/python?source=post)

### [Kosuke Kuzuoka](https://medium.com/@kousukekuzuoka)

Self-taught AI research engineer at DeNA Co., Ltd. passionate about self-driving
car technology and deep learning.
