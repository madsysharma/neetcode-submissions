# PROBLEM:
You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:
m is the number of valid elements in nums1,
n is the number of elements in nums2.

The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.
Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.

# SOLUTION:
- Brute force approach involves copying all elements to the end of nums1, and sorting the whole array.
  * Time complexity: O((m+n)log⁡(m+n))
  * Space complexity: O(1) or O(m+n) depending on the sorting algorithm.
- But nums1 and nums2 are already sorted! We can thus use merge sort.
  * Beware! If we write directly into nums1 from the front, we run the risk of overwriting elements we still need.
  * So first we copy nums1 to a temp arr, then we merge both sources into nums1.
  * Time complexity: O(m+n)
  * Space complexity: O(m)
- But here’s the catch: we know that nums1 has empty space of size n at the end! So if we write elements from the back, we don’t run the overwriting risk.
  * By comparing the largest remaining elements from both arrays, and putting the largest one in the current end position, we don’t need extra space for merging.
  * Time complexity: O(m+n)
  * Space complexity: O(1) extra space.
