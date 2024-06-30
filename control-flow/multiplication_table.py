#!/bin/bash
#Creating a multiplication number by using for llop
number = int(input("Enter a number to see its multiplication table: "))
product = 0
for i in range(1,11):
	product = number * i
	print(f"{number} * {i} = {product}")
