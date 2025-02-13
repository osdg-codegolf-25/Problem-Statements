# Problem-Statements

## Problem 1: Haunted Addition Ritual

### Problem Statement

You have been cursed with an endless series of numbers, and the only way to break the spell is to add them together. Given pairs of numbers across multiple test cases, compute their sum to dispel the haunting presence of unfinished calculations.

### Input/Output Format
The first line contains a single integer `t` — the number of test cases.
`2t` lines follow.
Each test case consists of two lines:
The first line contains an integer `a`.
The second line contains an integer `b`.

For each test case, output a single integer — the sum of `a` and `b`.

## Problem 2: Spooky Numbers

### Problem Statement

Let's call a positive integer spooky if it has only one non-zero digit.

For example: 
- 10, 2, 3, 1000, 9000 are spooky numbers.
- 101, 2934 are not spooky numbers.

For a given number `n`, find the number of spooky numbers `x` such that `1 <= x <= n`

### Input/Output Format

The first line contains a positive integer `t`: the number of test cases.

The following `t` lines contain one number each. For each number `n`, output the number of spooky numbers `x` such that `1 <= x <= n`

## Problem 3: The Cursed Alchemy of Indices

### Problem Statement

You are given a sequence made up of the characters i and j. You can repeatedly modify this sequence using the following operations:

- Find any adjacent "ij" and change it to "jk", increasing your count by 1.
- Find any adjacent "ji" and change it to "kj", increasing your count by 1.

Your task is to determine the maximum count you can achieve by applying these operations as many times as possible.

### Input/Output Format

The first line contains an integer `t`: the number of test cases.

Each test case consists of a single line containing a string s, which consists only of the characters i and j.

For each test case, output a single integer — the highest count achievable through the allowed modifications.

