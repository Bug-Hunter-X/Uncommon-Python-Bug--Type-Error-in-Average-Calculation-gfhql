# Uncommon Python Bug: Type Error in Average Calculation

This repository demonstrates a subtle bug in a Python function designed to calculate the average of a list of numbers. The bug arises from the function's failure to handle non-numeric data types within the input list and its less-than-ideal treatment of empty input lists. The provided solution showcases a more robust implementation that addresses these potential issues.

## Bug Description
The original `calculate_average` function correctly calculates the average when provided with a list of numbers. However, if the input list is empty, it returns 0.  More importantly, it throws a `TypeError` if the list contains non-numeric elements. 

## Solution
The solution improves the function's error handling by explicitly checking for the presence of non-numeric data and providing a more informative error message.  It also provides a more standard way to handle empty lists.
