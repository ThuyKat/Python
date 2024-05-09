# Intuition

Pairs of brackets can be either nested inside each other like {[]} or placed outside of each other {}[]. The string is a combination of these. With our eyes, we normally check from the innermost pairs, always in the form of a complete open-close pair: (), [], or {}. Then once it's valid, we move to the next outer pair to check its validity until the outermost pairs are completed.

The key problem is how to find the innermost pair to start with.

## Approach

To find the innermost pair to start the validation process, I iterate through the loop from start to finish. When I find a complete pair of brackets, that becomes my validation starting point. But how can I continue by comparing the next outer pair after that pair in Python? Removing the pair from the original string has no use because the string is immutable, and the loop will still run from the 0 index to the last index of the original string, not the adjusted string.

To solve this:

1. I create an empty string called "check".
2. Every iteration, if the bracket is one of the open brackets, I add it to the empty string "check".
3. If the bracket is one of the close brackets, we need to check if it makes a complete pair with the last one.
4. If the pair is found, I remove the last element of "check" from "check".
5. If the pair is not found, we return False, indicating that the string is invalid.

This approach allows us to validate the brackets by finding the innermost pair and moving to the next outer pair for validation.

IMPROVEMENT:
1. Instead of removing the last element of "check" from "check", we use a pointer to point to the index of the bracket in consideration.
2. Pointer = pointer +1 if we iterate through an open bracket, and pointer = pointer -1 if we iterate through a close bracket
3. So after a close bracket went through step 3 as above, by adding pointer = pointer -1, we now focus on testing the next open bracket which is the one at index = pointer -1 
