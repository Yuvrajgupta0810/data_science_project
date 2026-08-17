# data_science_project

First Non-Repeating Character

This program finds the first character in a string that appears only once.
If no such character exists, it prints -1.

How to run:
1. Open terminal in this folder.
2. Run: python main.py
3. Enter a string when asked.
4. It will print the first non-repeating character, or -1 if none exists.

Example:
Input: swiss
Output: w

Input: aabbcc
Output: -1

Notes:
- Works for empty strings, single character strings, and strings with spaces.
- Comparison is case sensitive (a and A are treated differently).
- Time complexity: O(n)

Second project

The idea is to first calculate the expected sum of all numbers from 1 to N+1 using the formula (N+1)*(N+2)/2. Then, subtract each number in the given array from this sum. The number left after all the subtractions is the missing number. This method takes O(n) time because we go through the array once and uses O(1) extra space because no additional array or data structure is needed
