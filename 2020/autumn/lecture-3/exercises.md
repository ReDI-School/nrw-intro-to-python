# Exercises

## Exercise 1

Write a short program that prints one of several messages to the user based on their input.

First, prompt the user about whether they want to continue or not.

If the user responds with either no or n, print the phrase Exiting. Try to match the following
output if a user answers with no or n:  

```output
Would you like to continue? no
Exiting
```  

If the user responds with either yes or y, the output should instead look like this:  

```output
Would you like to continue? yes
Continuing ...
```  

If the user responds with anything else, e.g. `python`, please match the following output:  

```output
Would you like to continue? python 
Please try again and respond with yes or no.
```  

Hints:
- The input function can be used to prompt a user
- The comparison for equality, `==` could be used here
- The print function is used to print output on the screen

Save your code as a file with the name `lesson3-ex1-YourNameOrNickname.py` and upload it to the classroom if you want to.  

## Exercise 2

You are tasked with developing a program that calculates various shapes depending on the user's input. We
would like to see at least two different shapes, for example:
- Area of a circle, `2*Pi*R^2` (Assume Pi as 3.14)
- Area of a rectangle, x*y

*Feel free to come up with different or more shapes, as long as you can get the necessary parameters from your user input!*

To accomplish this, you need to make sure that:
- The user is prompted what they want to caluclate
- The input is in the correct format


Hints:
- Remember the input() and print() functions
- Remember to use if, elif and else
- There may be some nesting, and multiple input() functions, depending on the shapes you chose


Save your code as a file with the name `lesson3-ex2-YourNameOrNickname.py` and upload it to the classroom if you want to. 