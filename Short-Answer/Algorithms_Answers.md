#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The first line, a = 0, is a simple variable assignment, so we'll give that a value of 1.

The while loop is interesting, because it cubes the value of the input size, which increases the number of operations within the loop by an order of n^3.

The operation within the loop then negates the cubing occuring in the loop definition, so you could say the loop occurs n^3 times minus n^2 times, or n times.
The operation itself is given a value of 1.

So in the final analysis, the algorithm has a complexity of:

O(1 + n^3 + 1 - n^2)

Which then resolves to:

O(2 + n)

Or:

O(n)

b) Again, the first line receives a value of 1, for the variable assignment.

The for loop gets a value of n, because it's time complexity is linear in correlation to the input size.

1 for the third line.

Then the nested while loop makes it intersting. It occurs (n - 1) / 2 times because as it iterates, it doubles the value of j.

The final line gets a value of 1/2 because it's also within the while loop, and will only execute as long as the condition is met, same as the previous line.

The final breakdown sees the algorithm complexity as:

O(1 + n + 1/2 + (n/2) + 1/2)

O(2 + n + n/2 )

O(n log n)

c) In the best case, this algorithm has a complexity of O(1); that is, if the input value is 0.

Otherwise, the function returns the number of ears we know we have on an individual bunny, and the recursive call which decrements the number of bunnies input by one, working us toward our base case as we add the number of ears to the returned sum.

That line occurs n times, because it is dependent upon the input value.

So in the final analysis, we have a time complexity of:

O(n)

## Exercise II

For this one, I think the naive solution would be just to cycle through the floors from the top down and see where the eggs stop breaking, then return that value.

But the goal is to minimize the eggs broken, so one way we might do that is to split the number of floors into two halves, lets call them top_half and bottom_half.

We can then start at the high end of bottom_half to see if eggs break at its highest index. If so, we can eliminate top_half entirely. We know the egg breaking floor is within bottom_half.

We could then start at the 0th of bottom_half and work our way up to see which floor is the opponent of the ovum.

If on the other hand, the top end of bottom_half doesn't break any eggs, we can discard bottom_half and recurse the halving operation on top_half, running through all of the same steps until we find our eggnemy floor.

Based on the halving feature of this algorithm, the final runtime complexity would be:

O(log n)
