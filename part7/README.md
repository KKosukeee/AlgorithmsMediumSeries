### Data Structures and Algorithms Revisited: Part 7

Hi, I’m Kosuke Kuzuoka, an AI research engineer at DeNA Co., Ltd. This is the
seventh post in the Data Structures and Algorithms Revisited series. In this
blog post, I will talk about what’s known as one of the best sorting algorithms,
called quick sort, and compare it with other algorithms that I described in my
last blog post. A quick sort is a sorting algorithm that is optimized for both
runtime and space complexities. I will implement it in code, so that we can
compare with other sorting algorithms to see when it’s better over others.

This blog post contains concepts that are described in my previous posts. If you
aren’t sure about them, or if you want to refresh your memory, please visit my
previous posts in order to understand the content of this blog post. I will
leave all links to my previous posts below. With that being said, let’s jump
right in!

1.  [Part 1: What are Data Structures and
Algorithms?](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-1-bffbcea48762?source=post_page---------------------------)
1.  [Part 2: Most Widely Used Data Structures (Arrays and
Linked-Lists)](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-2-96b42a58ecde?source=post_page---------------------------)
1.  [Part 3: Most Widely Used Data Structures (Stacks and
Queues)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part3-f9cc5534afcf?source=post_page---------------------------)
1.  [Part 4: Searching and Sorting (Binary
Search)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-4-e5576e1f53f3?source=post_page---------------------------)
1.  [Part 5: Searching and Sorting (Recursion and
DP)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-5-d71dcb256c18?source=post_page---------------------------)
1.  [Part 6: Searching and Sorting (Bubble Sort and Merge
Sort)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-6-8f13a8ac558)
1.  Part 7: Searching and Sorting (Quick Sort and Comparisons)*

### What is Quick Sort?

A quick sort is a sorting algorithm that is optimized in both time and space
complexities. We saw a bubble sort and a merge sort in the previous post. A
bubble sort is an in-place algorithm that runs in O(N²), while a merge sort runs
O(Nlog(N)), but consumes O(N) memory. It would be nice if there is a sorting
algorithm that runs in O(Nlog(N)) in time, and O(1) in space, and that is
exactly where a quick sort comes into play!

A quick sort is a divide and conquer algorithm that works by picking an index
called a *pivot*, then partitioning the array, such that all the elements with
values less than the pivot move to the left side of the pivot, and all the
elements with values larger than the pivot move to the right side of the pivot.
After moving elements to the left and right side of the pivot, the pivot will be
in the correct position. This operation is done for each element in the array,
so that all elements will end up in the correct position. The important thing in
this algorithm is how you select the pivot. Poor selection of the pivot leads
this algorithm to run like a bubble sort, but in general the best and average
case for this algorithm works like a merge sort. Rather than explaining how it
works, let’s look at the code I created!

The implementation consists of two parts. The first part is the *partition*
function which partitions the array and returns the pivot, such that all
elements to the left and to the right are smaller and larger than the pivot
respectively. We do this in linear time by swapping an element every time we
find an element that is smaller than the pivot with the value that is larger
than the pivot from line 17 to 21. The pivot is picked as the right-most element
at line 15 for simplicity, and the new index for the pivot is returned at line
24, after partitioning is done. All we need to do is call the *partition*
function recursively until all elements are in the right place. Let’s quickly
look at how we can implement that below.

We know that the *partition* function returns a pivot, and the pivot is in the
correct position. Once the pivot is in the correct position, all we need to do
is sort the left and right halves of the array by calling the *quick_sort*
function recursively at line 20 and 22. The halved array picks a pivot and
partitions the elements, then calls for its left and right half, and this
continues until there is only one element left (base case at line 15). One
important thing for *quick_sort* function is excluding the pivot element by
subtracting and adding 1 to the pivot at line 20 and 22 respectively, otherwise
it falls into an infinite recursion. Now we know how we implement a quick sort,
let’s talk about the complexities next!

Unfortunately, the runtime for a quick sort is not very simple. I mentioned that
the performance of a quick sort depends on how you chose the pivot. In the
implementation above, I picked the right-most element as the pivot. If the pivot
is in the correct position i.e. the largest number among the array, the
*partition* function simply returns the last index in the array, and doesn’t
partition in half at all. If this happens for all the elements in the array,
it’s simply the same as looping through the elements one by one and finding the
correct position for each element. This behavior is very similar to a bubble
sort and not surprisingly, the runtime becomes O(*N²*) just like a bubble sort.

![](https://cdn-images-1.medium.com/max/1600/1*xjUsrPI5VzOJx2BVF22pOA.png)

What do you think makes a quick sort runs faster than the situation that I
described above? Let’s now consider a case where every *partition* call
partitions an array roughly in half using the figure above. There are initially
*N* elements in the array and first *partition* call roughly partitions an array
in half (*N/2*). Then for the halved array gets in half for the next call
(*N/4*). This goes on and on until there is only one element left, and you can
see that this behavior is similar to a merge sort. Since the *partition*
operation takes linear time and we call for *log(N)* times i.e. the height of
the recursion tree, the runtime becomes O(*Nlog(N)*). Not surpassingly, this
runtime is the same as a merge sort!

The space complexity for a quick sort is very simple. It doesn’t use any
additional memory, except the negligible space used for the recursion stack. So
we can conclude that the space complexity for a quick sort is O(*1*) just like a
bubble sort. I would say that a quick sort is somewhat in between a bubble and a
merge sort. It’s worth mentioning that the pivot is carefully selected in most
implementations such that every *partition* call roughly partitions the array in
half, hence the runtime becomes O(*Nlog(N)*). Now let’s look at the performance
of the sorting algorithms that I described so far in this blog post series.

### Comparisons

So far, I described and implemented some of the well-known sorting algorithms, a
bubble, merge and quick sort. Here I quickly compared all sorting algorithms
that I covered in this blog post series. I have tested three cases here to see
how each sorting algorithm performed. For all cases, I didn’t change the
implementation that I described in the previous post. If you aren’t sure about
how I implemented a bubble and a merge sort, please go back and read the
previous post (the link in the beginning of the post).

![](https://cdn-images-1.medium.com/max/1600/1*GxADykFpKsj4tQj8dgAt0Q.png)
<span class="figcaption_hack">Fig 1. Comparison between a bubble, merge and quick sort using the same array of
same length and values</span>

A bubble, merge and quick sort are compared with the same array composed of
random integers. You can clearly see that the performance of a bubble sort is
worse than other sorting algorithms such that you can’t see the difference
between a merge and a quick sort. Now we know that a bubble sort is too slow,
let’s ignore a bubble sort, and see how a merge and a quick sort perform.

![](https://cdn-images-1.medium.com/max/1600/1*2rBzVuxNsEqneid8uUd5OA.png)
<span class="figcaption_hack">Fig 2. Comparison between a merge and a quick sort. Arrays used for the
comparison are the same for both</span>

Here I compared a merge and a quick sort with arrays of the same length and the
same values composed of randomly generated integers. You can see that the
performance of these sorting algorithms are very competitive, but a quick sort
looks slightly better. In fact, the slight difference isn’t really important.
The important thing to see is how the runtime grows as the # of elements gets
bigger. We can say that both algorithms grow in a similar way, and this is true
since they are both O(*Nlog(N)*) time in average cases. Now let’s look at the
worst scenario for a quick sort.

![](https://cdn-images-1.medium.com/max/1600/1*MQ1oD50iIdkJ_7aHXqeBqQ.png)
<span class="figcaption_hack">Fig 3. Comparison between a merge and a quick sort. The arrays for a quick sort
were sorted (worst situation)</span>

Here again, I compared a merge and a quick sort, but the input array for a quick
sort was already sorted, so that the runtime for a quick sort becomes the worst
scenario (see the explanation in the preceding section). It really doesn’t
matter for a merge sort, because a merge sort divides an array exactly in half
and merges no matter what the values are. In this case the runtime for a quick
sort becomes O(*N²*) and a merge sort becomes O(*Nlog(N)*) as usual. This
illustrates how important the pivot selection policy is, and with my current
implementation, it doesn’t perform well. Let’s now conclude ourselves!

### Conclusion

In this blog post, I explained what’s known as one of the best sorting
algorithms, a quick sort, and compared with other sorting algorithms that I
covered in this blog post series. It’s worth knowing when these sorting
algorithms work well and when not, so that you can use right sorting algorithm
at the right time. I also covered three sorting algorithms, but these are not
all of the options, and there are a lot more than those three that I covered. If
you are interested in other sorting algorithms, please go check the link in the
end of the post!

I will now move on to the topic of mapping and hashing. Also I’m planning to
start a blog post series on scalable system design as well as tips for cracking
coding interviews (I’m trying to output what I learned!). Thanks for reading
through the post, and I will see you in the next post!

<br> 
### Data Structures and Algorithms Revisited: Part 7

Hi, I’m Kosuke Kuzuoka, an AI research engineer at DeNA Co., Ltd. This is the
seventh post in the Data Structures and Algorithms Revisited series. In this
blog post, I will talk about what’s known as one of the best sorting algorithms,
called quick sort, and compare it with other algorithms that I described in my
last blog post. A quick sort is a sorting algorithm that is optimized for both
runtime and space complexities. I will implement it in code, so that we can
compare with other sorting algorithms to see when it’s better over others.

This blog post contains concepts that are described in my previous posts. If you
aren’t sure about them, or if you want to refresh your memory, please visit my
previous posts in order to understand the content of this blog post. I will
leave all links to my previous posts below. With that being said, let’s jump
right in!

1.  [Part 1: What are Data Structures and
Algorithms?](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-1-bffbcea48762?source=post_page---------------------------)
1.  [Part 2: Most Widely Used Data Structures (Arrays and
Linked-Lists)](https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-2-96b42a58ecde?source=post_page---------------------------)
1.  [Part 3: Most Widely Used Data Structures (Stacks and
Queues)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part3-f9cc5534afcf?source=post_page---------------------------)
1.  [Part 4: Searching and Sorting (Binary
Search)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-4-e5576e1f53f3?source=post_page---------------------------)
1.  [Part 5: Searching and Sorting (Recursion and
DP)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-5-d71dcb256c18?source=post_page---------------------------)
1.  [Part 6: Searching and Sorting (Bubble Sort and Merge
Sort)](https://medium.com/@kousukekuzuoka/data-structures-and-algorithms-revisited-part-6-8f13a8ac558)
1.  Part 7: Searching and Sorting (Quick Sort and Comparisons)*

### What is Quick Sort?

A quick sort is a sorting algorithm that is optimized in both time and space
complexities. We saw a bubble sort and a merge sort in the previous post. A
bubble sort is an in-place algorithm that runs in O(N²), while a merge sort runs
O(Nlog(N)), but consumes O(N) memory. It would be nice if there is a sorting
algorithm that runs in O(Nlog(N)) in time, and O(1) in space, and that is
exactly where a quick sort comes into play!

A quick sort is a divide and conquer algorithm that works by picking an index
called a *pivot*, then partitioning the array, such that all the elements with
values less than the pivot move to the left side of the pivot, and all the
elements with values larger than the pivot move to the right side of the pivot.
After moving elements to the left and right side of the pivot, the pivot will be
in the correct position. This operation is done for each element in the array,
so that all elements will end up in the correct position. The important thing in
this algorithm is how you select the pivot. Poor selection of the pivot leads
this algorithm to run like a bubble sort, but in general the best and average
case for this algorithm works like a merge sort. Rather than explaining how it
works, let’s look at the code I created!

The implementation consists of two parts. The first part is the *partition*
function which partitions the array and returns the pivot, such that all
elements to the left and to the right are smaller and larger than the pivot
respectively. We do this in linear time by swapping an element every time we
find an element that is smaller than the pivot with the value that is larger
than the pivot from line 17 to 21. The pivot is picked as the right-most element
at line 15 for simplicity, and the new index for the pivot is returned at line
24, after partitioning is done. All we need to do is call the *partition*
function recursively until all elements are in the right place. Let’s quickly
look at how we can implement that below.

We know that the *partition* function returns a pivot, and the pivot is in the
correct position. Once the pivot is in the correct position, all we need to do
is sort the left and right halves of the array by calling the *quick_sort*
function recursively at line 20 and 22. The halved array picks a pivot and
partitions the elements, then calls for its left and right half, and this
continues until there is only one element left (base case at line 15). One
important thing for *quick_sort* function is excluding the pivot element by
subtracting and adding 1 to the pivot at line 20 and 22 respectively, otherwise
it falls into an infinite recursion. Now we know how we implement a quick sort,
let’s talk about the complexities next!

Unfortunately, the runtime for a quick sort is not very simple. I mentioned that
the performance of a quick sort depends on how you chose the pivot. In the
implementation above, I picked the right-most element as the pivot. If the pivot
is in the correct position i.e. the largest number among the array, the
*partition* function simply returns the last index in the array, and doesn’t
partition in half at all. If this happens for all the elements in the array,
it’s simply the same as looping through the elements one by one and finding the
correct position for each element. This behavior is very similar to a bubble
sort and not surprisingly, the runtime becomes O(*N²*) just like a bubble sort.

![](https://cdn-images-1.medium.com/max/1600/1*xjUsrPI5VzOJx2BVF22pOA.png)

What do you think makes a quick sort runs faster than the situation that I
described above? Let’s now consider a case where every *partition* call
partitions an array roughly in half using the figure above. There are initially
*N* elements in the array and first *partition* call roughly partitions an array
in half (*N/2*). Then for the halved array gets in half for the next call
(*N/4*). This goes on and on until there is only one element left, and you can
see that this behavior is similar to a merge sort. Since the *partition*
operation takes linear time and we call for *log(N)* times i.e. the height of
the recursion tree, the runtime becomes O(*Nlog(N)*). Not surpassingly, this
runtime is the same as a merge sort!

The space complexity for a quick sort is very simple. It doesn’t use any
additional memory, except the negligible space used for the recursion stack. So
we can conclude that the space complexity for a quick sort is O(*1*) just like a
bubble sort. I would say that a quick sort is somewhat in between a bubble and a
merge sort. It’s worth mentioning that the pivot is carefully selected in most
implementations such that every *partition* call roughly partitions the array in
half, hence the runtime becomes O(*Nlog(N)*). Now let’s look at the performance
of the sorting algorithms that I described so far in this blog post series.

### Comparisons

So far, I described and implemented some of the well-known sorting algorithms, a
bubble, merge and quick sort. Here I quickly compared all sorting algorithms
that I covered in this blog post series. I have tested three cases here to see
how each sorting algorithm performed. For all cases, I didn’t change the
implementation that I described in the previous post. If you aren’t sure about
how I implemented a bubble and a merge sort, please go back and read the
previous post (the link in the beginning of the post).

![](https://cdn-images-1.medium.com/max/1600/1*GxADykFpKsj4tQj8dgAt0Q.png)
<span class="figcaption_hack">Fig 1. Comparison between a bubble, merge and quick sort using the same array of
same length and values</span>

A bubble, merge and quick sort are compared with the same array composed of
random integers. You can clearly see that the performance of a bubble sort is
worse than other sorting algorithms such that you can’t see the difference
between a merge and a quick sort. Now we know that a bubble sort is too slow,
let’s ignore a bubble sort, and see how a merge and a quick sort perform.

![](https://cdn-images-1.medium.com/max/1600/1*2rBzVuxNsEqneid8uUd5OA.png)
<span class="figcaption_hack">Fig 2. Comparison between a merge and a quick sort. Arrays used for the
comparison are the same for both</span>

Here I compared a merge and a quick sort with arrays of the same length and the
same values composed of randomly generated integers. You can see that the
performance of these sorting algorithms are very competitive, but a quick sort
looks slightly better. In fact, the slight difference isn’t really important.
The important thing to see is how the runtime grows as the # of elements gets
bigger. We can say that both algorithms grow in a similar way, and this is true
since they are both O(*Nlog(N)*) time in average cases. Now let’s look at the
worst scenario for a quick sort.

![](https://cdn-images-1.medium.com/max/1600/1*MQ1oD50iIdkJ_7aHXqeBqQ.png)
<span class="figcaption_hack">Fig 3. Comparison between a merge and a quick sort. The arrays for a quick sort
were sorted (worst situation)</span>

Here again, I compared a merge and a quick sort, but the input array for a quick
sort was already sorted, so that the runtime for a quick sort becomes the worst
scenario (see the explanation in the preceding section). It really doesn’t
matter for a merge sort, because a merge sort divides an array exactly in half
and merges no matter what the values are. In this case the runtime for a quick
sort becomes O(*N²*) and a merge sort becomes O(*Nlog(N)*) as usual. This
illustrates how important the pivot selection policy is, and with my current
implementation, it doesn’t perform well. Let’s now conclude ourselves!

### Conclusion

In this blog post, I explained what’s known as one of the best sorting
algorithms, a quick sort, and compared with other sorting algorithms that I
covered in this blog post series. It’s worth knowing when these sorting
algorithms work well and when not, so that you can use right sorting algorithm
at the right time. I also covered three sorting algorithms, but these are not
all of the options, and there are a lot more than those three that I covered. If
you are interested in other sorting algorithms, please go check the link in the
end of the post!

I will now move on to the topic of mapping and hashing. Also I’m planning to
start a blog post series on scalable system design as well as tips for cracking
coding interviews (I’m trying to output what I learned!). Thanks for reading
through the post, and I will see you in the next post!

<br> 
