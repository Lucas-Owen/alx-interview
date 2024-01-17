#!/usr/bin/python3
"""This module defines the minOperations function"""


def get_max_divisor_less_than(n):
	"""Returns the maximum positive integer that can divide n completely"""
	if n <= 1:
		return 1
	for i in range(n - 1, 0, -1):
		if n % i == 0:
			return i


def minOperations(n):
	"""Returns the minimum number of operations required to solve for n"""
	if n <= 1:
		return 0
	result = 0
	while n != 1:
		temp = get_max_divisor_less_than(n)
		result += n / temp
		n = temp
	return result
