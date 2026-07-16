
from typing import List
"""
Question 1:
Rotate the elements of an array by k positions.
	* You are given an array of integers.
	* Ask the user to input:
	* The direction of rotation (`left` or `right`)
	* The number of positions `k`
	* If the direction is left, shift the elements towards the left by `k` positions.
	* If the direction is right, shift the elements towards the right by `k` positions.
	* The rotation should be circular, meaning elements shifted out from one side should reappear on the other side.

Input:
numbers = [1, 2, 3, 4, 5]
direction = right
k = 2

Output:
[4, 5, 1, 2, 3]

Input:
numbers = [1, 2, 3, 4, 5]
direction = left
k = 2

Output:
[3, 4, 5, 1, 2]

Constraints:
* Do not use `while` loops
* Use only `for` loops for iteration
* Do not use inbuilt rotation functions
"""

def rotate(numbers: List[int], direction: str, k: int) -> List[int]:
    if direction == 'right':
        for i in range(k):
            pop = numbers.pop()
            numbers.insert(0, pop)
    elif direction == 'left':
        for i in range(k):
            pop = numbers.pop(0)
            numbers.append(pop)
    return numbers
print(rotate([1, 2, 3, 4, 5], 'right', 2))
print(rotate([1, 2, 3, 4, 5], 'left', 2))
'''
>>>
[4, 5, 1, 2, 3]
[3, 4, 5, 1, 2]
'''


'''
Question 2:
Find all the leaders in an array.
	* A leader is an element that is greater than or equal to all the elements to its right.
	* You are given an array of integers.
	* Traverse the array to identify all such leader elements.
	* A leader should satisfy the condition:
	* It must be greater than or equal to every element on its right side.
	* Store all the leader elements in a list and display the result.

Input:
arr = [9, 10, 2, 4, 8, 5]

Output:
[10, 8, 5]

Input:
arr = [16, 17, 4, 3, 5, 2]

Output:
[17, 5, 2]

Constraints:
	* Use only loops for traversal
	* Do not use unnecessary extra variables like flags
	* Avoid using built-in functions for direct computation
	* The solution should correctly check all elements to the right of each element
'''

def Leaders(arr: List[int]) -> List[int]:
    o_list = []
    for i in range(len(arr)):
        count = 0
        for k in range(i+1, len(arr)):
            if arr[k] > arr[i]:
                count += 1
        if count == 0:
            o_list.append(arr[i])
    return o_list
print(Leaders([9, 10, 2, 4, 8, 5]))
print(Leaders([16, 17, 4, 3, 5, 2]))
'''
>>>
[10, 8, 5]
[17, 5, 2]
'''

'''
Question 3:
Find all contiguous subarrays whose product is less than or equal to k.

* You are given an array of positive integers and an integer k.
* A subarray is a contiguous part of the array.
* Generate all possible contiguous subarrays.
* For each subarray, calculate the product of its elements.
* Select only those subarrays whose product is less than or equal to k.
* Print all such subarrays and also print their total count.

Input:
arr = [1, 2, 3, 4, 5]
k = 10

Output:
8
[1], [2], [3], [4], [5], [1,2], [1,2,3], [2,3]

Input:
arr = [2, 5, 3]
k = 10

Output:
4
[2], [5], [3], [2,5]

Constraints:
* Use only loops for generating subarrays
* Do not use inbuilt functions for subarray generation
* Each subarray must be contiguous
* The product should be calculated manually
* Ensure correct handling of all possible subarrays
'''

from typing import List

def contiguous_subarray(arr: List[int], k: int) -> List[List[int]]:
    result = []
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            if product <= k:
                result.append(arr[i:j+1])
            else:
                break
    print(len(result))
    return result
print(contiguous_subarray([1, 2, 3, 4, 5], 10))
print(contiguous_subarray([2, 5, 3], 10))
'''
8
[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3], [4], [5]]
4
[[2], [2, 5], [5], [3]]
'''


"""
Question 4:
Group domain names based on their extensions.

* You are given a list of domain strings.
* Each domain contains a name and an extension separated by a dot (.).
* Extract:
* The domain name (before the dot)
* The extension (after the dot)
* Group all domain names based on their extensions.
* Store the result in a dictionary where:
* Key → extension
* Value → list of domain names having that extension

Input:
domain_list = ['amazon.com', 'indeed.in', 'google.com', 'python.py']

Output:
{
'com': ['amazon', 'google'],
'in': ['indeed'],
'py': ['python']
}


Input:
domain_list = ['test.org', 'code.py', 'learn.org']

Output:
{
'org': ['test', 'learn'],
'py': ['code']
}

Constraints:
* Use only loops for traversal
* Do not use inbuilt functions like split()
* Extract domain name and extension manually
* Maintain proper grouping in dictionary
* Preserve all domain names under correct extension
"""

from typing import Dict, List
def group_domain(domain_list: List[str]) -> Dict[str, List[str]]:
    freq = {}
    for i in domain_list:
        idx = i.index('.')
        val = i[0:idx]
        key = i[idx:]
        if key not in freq:
            freq[key] = [val]
        else:
            old_vals = freq[key]
            freq[key] = [val] + old_vals
    
    return freq
print(group_domain(['amazon.com', 'indeed.in', 'google.com', 'python.py']))
print(group_domain(['test.org', 'code.py', 'learn.org']))
'''
{'.com': ['google', 'amazon'], '.in': ['indeed'], '.py': ['python']}
{'.org': ['learn', 'test'], '.py': ['code']}
'''


"""
Question 5:
WAP to print a sequence pattern where consecutive natural numbers are printed
continuously in increasing triangular groups separated by spaces, based on the given value of n.

Input : 3
Output : 
   1   
   23   
   456
"""

def triangular_pattern(num: int) -> None:
    place_val = 1
    for i in range(1, num+1):
        print()
        for j in range(1, i+1):
            print(place_val, end="")
            place_val += 1
triangular_pattern(3)
'''
1
23
456
'''


"""
Question 6:
WAP to rotate the digits of a given number to the left or right by a specified number of positions using pure Python logic.

Sample Input / Output :
Input :
Number : 12345
Direction : left
Shift : 1

Output : 23451


Input :
Number : 23456
Direction : right
Shift : 2

Output : 56234
"""

def shift_digits(Number: int, Direction: str, Shift: int) -> int:
    str_number = str(Number)
    Shift %= len(str_number)
    print(f'The Shift is {Shift}')
    if Direction == 'left':
        return str_number[Shift:] + str_number[:Shift]
    
    elif Direction == 'right':
        return str_number[-Shift:] + str_number[:-Shift]
        
print(shift_digits(123456789, 'right', 7))

'''
The Shift is 7
345678912
'''


"""
Question 7:
WAP to print all 3-digit numbers in which the product of the first digit and the
last digit is equal to the middle digit using pure Python logic.

Output :
100 111 122 133 144 155
"""

def equal_product(num: int) -> int:
    for i in range(100, num+1):
        first_digit = i // 100
        middle_digit = (i // 10) % 10
        last_digit = i % 10
        
        result = first_digit * last_digit
        if result == middle_digit:
            print(i, end=' ')
        # return i if result ==  middle_digit else 'Not equal'
        
equal_product(999)
'''
100 111 122 133 144 155 166 177 188 199 200 221 242 263 284 300 331 362 393 400 441 482 500 551 600 661 700 771 800 881 900 991 
'''

