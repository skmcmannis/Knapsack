# Knapsack

Solves a modified version of the 'knapsack' problem, where there are multiple knapsacks (people)
that can be filled, each with it's own weight limit. The program takes a text file as input,
which contains test cases to run through the algorithm. Each test case contains a list of 
items by value and weight, as well as a list of people and their weight capacity. Output is written
to a file, and consists of the total value carried by all people, as well as the items each
person carried.

Input file is organized as follows:

First line: number of test cases in the file

Next line: number of item value/weight pairs to follow in this test case
Next lines: items, represented as pairs of integers 'value' and 'weight', respectively
Next line: number of people (knapsacks) to follow in this test case
Next lines: the capacity of each person (knapsack)
...repeated for each test case