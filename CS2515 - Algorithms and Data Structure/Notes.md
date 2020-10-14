<details>
<summary>Table of Content</summary>
<!-- TOC -->

- [CS2515 Week 1](#cs2515-week-1)
  - [Abstract Data Types](#abstract-data-types)
  - [What is the point](#what-is-the-point)
    - [Proper Implementation](#proper-implementation)
    - [Efficiency](#efficiency)
  - [What is the point (Cont.)](#what-is-the-point-cont)
  - [What we will use](#what-we-will-use)
    - [Python 3](#python-3)
  - [Module Requirements](#module-requirements)
  - [Excercise: Checking for String Anagrams](#excercise-checking-for-string-anagrams)
- [CS2515 Week 2](#cs2515-week-2)
  - [Count distinct items in non-decreasing list](#count-distinct-items-in-non-decreasing-list)
  - [Complexity Analysis](#complexity-analysis)
  - [Big O (The Upper Bound)](#big-o-the-upper-bound)
    - [The Standard Functions](#the-standard-functions)
      - [Constant](#constant)
      - [Logarithmic](#logarithmic)
      - [Linear](#linear)
      - [Log Linear](#log-linear)
      - [Quadratic](#quadratic)
      - [Cubic](#cubic)
      - [Exponential](#exponential)

</details>

---

# CS2515 Week 1

## Abstract Data Types

**Doesn't necessarily specify how they should be used**

- Does it work as it should
- How long does it take
- How much memory and recourses does it use

---

## What is the point

### Proper Implementation

1. Programs must be correct

   - Not just bug free but working as best as possible

2. Programs should be efficient
   - Programs that take too long to run are useless
   - Understand the implication of choosing certain **Library Functions** in regard to **Runtime** and **Memory** use
   - Implications of different **Design Pattern** choices
     - What might be easier for you to code may be worse for the programs **Runtime** overall

### Efficiency

1. Faster machines mean users expect to solve bigger problems faster
2. Some problems have known limits in their efficiency

---

## What is the point (Cont.)

1. You must advertise and explain code to other programmers _in ways they will understand_

   - State the **Abstract Data Types** used
     - Experienced Programmers will know how to interact with them
   - State the **Data Structures** and **Algorithms** you've implemented

2. You should not break standard **Design Patterns** and **Principles**
   - Understand the specificed ways you're meant to interact with the **Data**
   - Don't interact with it in any others ways

---

## What we will use

### Python 3

- Understanding **Library Functions**
- Learn how to implement **Code** and **Data Structures** properly
- Practice coding skills regularly

---

## Module Requirements

- Most lab classes wont be a hand-in style assignment but they are still important for growing your skills and understanding
- Using things thought during CS113 - Foundations of Computer Science II ([Reference past material if needed](https://bit.ly/3l0GQrG))
- There is no text book here are some recommended reading if you feel the need

  - [Data Structures and Algorithms in Python, Goodrich, Tamassia and Goldwasser, Wiley](http://87.120.36.5/main/2481000/d32f9c32d0c494496dcda7843f0c5b43/Michael%20H.%20Goldwasser%2C%20Roberto%20Tamassia%2C%20Michael%20T.%20Goodrich%20-%20Data%20Structures%20and%20Algorithms%20in%20Python-John%20Wiley%20%26%20Sons%20%282018%29.epub)

  - [Problem Solving with Algorithms and Data Structures, Miller and Ranum](http://87.120.36.5/main/2061000/ae007a68c3c7fe1e5abecbad87d16703/Miller%20B.N.%2C%20Ranum%20D.L.%20-%20Problem%20Solving%20with%20Algorithms%20and%20Data%20Structures%20Using%20Python.%20Release%203.0.pdf)

  - [Data Structures and Algorithms with Python, Lee and Hubbard, Springer](http://87.120.36.5/main/1310000/0b6a4d4811cce0d8ca288cada2c21872/%28Undergraduate%20Topics%20in%20Computer%20Science%29%20Kent%20D.%20Lee%2C%20Steve%20Hubbard%20-%20Data%20Structures%20and%20Algorithms%20with%20Python-Springer%20%282015%29.pdf)

---

<br>

<br>

## Excercise: Checking for String Anagrams

- What **Algorithms** could we use?

**Replace - O(n&#x00B2;)**

```
for each element (x) of str1
  found = False
  i=0
  while (not found) and (i < len(str))
    if x == str2[i]
      found = True
      str2[i] = Null
    else
      i += 1
  if (not found)
    return False
return True
```

**Sort - O(n log n)**

```
sort(str1)
sort(str2)
for each i from 0 to len(str1)-1
  if str1[i] != str2[i]
    return False
return True
```

**Count - O(2|x|+2n)**

```
arr = [alphabet]
//Create an array (arr) with one cell for each character in the alphabet

for each x in str1
  arr[x] += 1
for each x in str2
  arr[x] -= 1
for each element of arr
  if element != 0
    return false
```

---

# CS2515 Week 2

## Count distinct items in non-decreasing list

- First Attempt

```Python
def unique_check1(inputlist):
  count = 0
  for i in range(len(inputlist)):
    unique = True
    for j in inputlist[i+1:]:
      if inputlist[i] == j:
        unique = False
    if unique:
      count = count + 1
  return count
```

- Second Attempt

```Python
def unique_check2(inputlist):
  count = 1
  for i in range(len(inputlist)-1):
    if inputlist[i] != inputlist[i+1]:
      count = count + 1
  return count
```

## Complexity Analysis

- Difference in running time for small lists doesn't matter

> listExamples.perf_check_random(50)
> List length: 50
> Count 1 time : 0.005830757669173181 36
> Count 2 time : 0.004983992257621139 36

- But for big lists it makes a big difference

> listExamples.perf_check_random(500)
> List length: 500
> Count 1 time : 0.03003369679208845 381
> Count 2 time : 0.006122982653323561 381
> listExamples.perf_check_random(5000)
> List length: 5000
> Count 1 time : 2.237111685331911 3803
> Count 2 time : 0.0075630900682881474 3803
> listExamples.perf_check_random(50000)

- For lists of length 50000, the second method is 10000 times faster

> List length: 50000
> Count 1 time : 231.77267158718314 37429
> Count 2 time : 0.025658405560534447 37429

- Both algorithms are _correct_
- At high-level pseudocode, they look similar
- But (when implemented in Python) their runtimes are significantly different on large lists

## Big O (The Upper Bound)

- We use the Big-Oh notation to restrict the functions we need to deal with
- Any polynomial with highest degree k is O(n<sup>k</sup>)
  - Big Oh gives an upper bound on the growth rate of the function•any function that is O(n<sup>k</sup>) is also O(n<sup>k+1</sup>)

### The Standard Functions

- We will consider **7 standard functions** to describe the worst-case upper bounds
  - **Constant**
  - **Logarithmic**
  - **Linear**
  - **Log linear**
  - **Quadratic**
  - **Cubic**
  - **Exponential**

#### Constant

- f(n) = c, for some fixed constant value c
- The running time of the function is independent of thesize of the input
- E.g. a function which returns the value in the first position in a list
  - Doesn't matter how long the list is
  - We say such a function is O(1)

#### Logarithmic

- f(n) = log<sub>b</sub>n, for some fixed constant value b
- The log of a number is the power to which the base must be raised to give the number
- log<sub>b</sub>n = x if and only if b<sup>x</sup> = n

![](https://i.gyazo.com/675355d21e931655e25fd9c13721eaaa.png)

#### Linear

- f(n) = n
- Typically, this comes from an algorithm with a single loop that iterates over each element of an input list

#### Log Linear

- f(n) = n log n
- We will see later a number of sorting algorithms with complexity O(n log n)
- Typically, the algorithm is doing something like binary search, but repeating it once for each element in the list

#### Quadratic

- f(n) = n<sup>2</sup>
- Typically this comes from algorithms with a nested loopwhere we are iterating over the same structure

#### Cubic

- f(n) = n<sup>3</sup>
- Typically this comes from algorithms with a doubly nested loop where we are iterating over the same structure
- We can go higher, to any arbitrary degree
- Very few of the algorithms we will consider in this modulehave run time approaching this complexity

#### Exponential

- f(n) = c<sup>n</sup>, for some constant c
- Typically this comes from algorithms with a loop where the number of operations increases by a factor of c each time round the loop
- Algorithms with exponential running time are considered inefficient, although we will see some practical algorithms of this sort later in the degree program

![](https://i.gyazo.com/59634109a68a29c81a85ed7e219854f9.png)
