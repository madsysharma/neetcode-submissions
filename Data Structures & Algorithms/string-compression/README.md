# PROBLEM:
You are given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars. For example, 10 is represented as ["1","0"].
Let k be the length of the compressed string s. You must modify the first k characters of chars array and return k.
You must write an algorithm that uses only constant extra space.

# SOLUTION:
- We can traverse the array and club consecutive identical chars together. And for each group, write the character followed by its count, if group length > 1. 
  * First build the compressed string in a separate buffer, and then copy back to original arr.
  * Time complexity: O(n) or O(n^2) depending on the language.
  * Space complexity: O(n)
- But, to enhance efficiency, we can compress the array using two pointers.
  * One ptr for reading i, the other for writing k.
  * We know the compressed form is never larger than the original: thus, we can safely overwrite the array as we go. This eliminates the need for extra space.
  * Time complexity: O(n)
  * Space complexity: O(1)
