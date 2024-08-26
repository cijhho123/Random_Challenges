# Solving problems using a Turing Machine

## Background
Those problems were given as an extra tasks in the "Models of computation & Complexity " course of the CS department at BGU.  
We were given several tasks and needed to implement an algorithm using a Turing Machine to sovle them. The task is written with Python via Google Colab using a tool called Turing Machine Tutor

The "Turing Machine Tutor" can be found [here](https://github.com/Turing-Machine-Tutor/)

## Task 1
Create a Deterministic Turing machine that decide the following languages:  
wDw - all the words in the form u$u, for any word u  
successor  - two binary strings w1 and w2 representing naturals n1 and n2 return True if n2=n1+1. Technically, we assume that the strings are given in an interleaved fashion, one bit of the first, one of the second and a delimiter (#)
a2n_bn -  a^{2n}b^{n} for any natural number n  

## Task 2
Create a Deterministic Multi-Tape Turing machine that calculate the following functions:   
IsPalindrom - check if a word is a palindrom  
DivideByTwo -  gets a unary string and returns a unary string of half the length of the input
LogBaseTwo  - gets a unary string and returns a unary string of length log 2 of the length of the input string

