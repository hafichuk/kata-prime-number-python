kata-prime-number-python
========================

Prime Factors Kata

This kata is designed to help you get used to doing test driven development.

Explanation

Write a method that takes in an integer and returns all prime factors for that number. For example, passing in the number 4 would return a list containing 2,2. Notice I said method…don’t go creating a complicated class or project structure. Just create a test fixture and put a method right in there ;-).

Goals

Start with the simplest implementation possible. Don’t try to find a solution all at once. This kata will help you create the muscle memory to start with the most naive solution first. In fact, I’m recommending you write your tests in this order (again, only write enough code to make each test pass):

primes for 0, returns empty list
primes for 1, returns empty list
primes for 2, returns 2
primes for 3, returns 3
primes for 4, returns 2,2
primes for 5, returns 5
primes for 6, returns 2,3
primes for 9, returns 3,3
primes for 2147483647, returns 2147483647


ref: http://amirrajan.net/meta/2013/10/06/TDD-the-wombo-combo-of-software-dev/