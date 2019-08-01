### Data Structures and Algorithms Revisited: Part 6

![](https://cdn-images-1.medium.com/max/1600/0*Ef-UsHDbg90SEmeN.jpg)
<span class="figcaption_hack">Image Source:
[https://www.azquotes.com/quote/1025195?ref=algorithms](https://www.azquotes.com/quote/1025195?ref=algorithms)</span>

Hi, I’m Kosuke Kuzuoka, an AI research engineer at DeNA Co., Ltd. This is the
sixth post in the Data Structures and Algorithms Revisited series. In this blog
post, I will talk about some of the most popular sorting algorithms, and
implementing them in code. In fact, most programming languages have built-in
sorting functions, but it’s always good to understand how they work and their
pros and cons.

I assume that you are already familiar with concepts like recursion and
terminology like runtime and space complexities. If you aren’t familiar with
them, you can go back and read some of my posts to better understand those
concepts. I will leave all links to the previous posts below, in case you missed
reading them. With that being said, let’s jump right in!

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
1.  Part 6: Searching and Sorting (Bubble Sort and Merge Sort) *

### What is Sorting?

Unlike searching, which finds a specific element in an array, sorting changes
the order of the elements in an array, such that the new array is in ascending
or descending order. You can think of a sorting algorithm as a function that
spits out a sorted array given an unsorted array as its input.

There are a couple sorting algorithms that exist. Some of them are optimized in
terms of the runtime complexities, while other algorithms are optimized in terms
of the space complexities. Let’s look at some popular sorting algorithms in the
following sections!

### What is Bubble Sort?

Bubble sort is a simple naive solution that sorts elements in an array by moving
the largest element to the rightmost place at each iteration. It’s called bubble
sort because the largest element in the array “bubbles” up to the top at each
iteration. If you follow the operation *N* times, where *N* is the length of the
array, the whole array will be sorted in ascending order. I implemented a bubble
sort below, so that we can see how this works step by step.

The outer loop runs N times, puts one element in the right position at a time by
calling the inner loop. The inner loop compares adjacent elements and swaps the
elements if they aren’t in the right order from line 16–17. After looping *i*
times with the outer loop, there will be *i* elements that are in the right
position on the right side of an array. This means that we don’t have to loop
through *N* times in the inner loop, so I simply ignore the elements that are
already sorted at line 13. Now let’s analyse the runtime and space complexities
for this algorithm.

Because of the nested loop which runs *N* times in the worst case for both, it’s
easy to see that this algorithm takes O(*N*²) times. One thing you should
realize is that this algorithm doesn’t use any additional memory. A sorting
algorithm that doesn’t use any additional memory is called an *in-place sorting
algorithm*, and the space complexity for such algorithms is always O(1). This is
important, because as the array that needs to be sorted gets bigger and bigger,
the memory that you need to allocate for the algorithm to be done becomes more
important. Let’s look at another sorting algorithm now!

### What is Merge Sort?

Merge sort sorts an array by recursively halving the array until there is only
one element left, then reconstructing the divided sub-arrays by recursively
merging each element according to the comparison. The problem is simplified by
dividing the array into smaller pieces, and all you need to do to solve the
entire problem is solve each sub-problem in the same manner. This algorithm
design is called *divide and conquer*, and the merge sort is a very good example
to explain how divide and conquer simplifies a problem. Let’s look at the merge
sort in code to analyse its time and space complexities.

The above implementation first divides an array in half, and calls itself
recursively for the left and right halves of the array from line 17 to 18. This
recursion will continue, until the length of the sub-array is less than or equal
to 1. When there are no more elements in the array to divide, the function
simply returns its input, and the returned value will be sorted according to the
comparison from line 26 to 31. The parts of the array that are sorted will be
then returned at line 43, and this will continue until the whole array is
sorted. Now, let’s analyse the runtime and space complexities for the merge
sort!

An important thing to notice here is that unlike the bubble sort which sorts an
array in-place, this algorithm is allocating an additional array in order to
construct a sorted sub-array. You can see that I initialized an array at line 14
then appended an element from either the left or right half of the array from
line 26 to 31 within a loop. In fact, the space complexity is worse than the
bubble sort. The space complexity for this algorithm is O(*N*), which you can
think that the array created at line 14 can never get bigger than the original
array, hence O(*N*). Because the array gets divided in half at every call, and
every element in the sub-arrays for each level will be sorted one by one, the
runtime for the merge sort is O(*Nlog(N)*). It turns out that the merge sort is
more optimal in runtime, and worse in space.

### Conclusion

I explained how bubble sort and merge sort work in this blog post. As I
mentioned in the beginning of this blog post, most programming languages have
these sorting algorithms implemented, and there is no point implementing them
from scratch. It’s still good to understand how they work, so that you can
answer a question like, “What is the worst runtime complexity of bubble sort and
when does it happen?” I was literally asked that question in one of the
interviews that I had, and intuitive understanding of the sorting algorithms
really helped me to answer the question instantly.

I hope this blog post helped you to understand bubble sort and merge sort. In
the next post, I will talk about another sorting algorithm, that is perhaps
considered one of the best sorting algorithms in terms of both runtime and space
complexity. In the end of the next post, I will compare the runtime complexities
for each sorting algorithm that I described so far. For now, please don’t forget
to leave some claps if you like the blog post. I will see you in the next post
:D

<br> 
