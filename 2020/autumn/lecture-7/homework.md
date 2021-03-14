# Homework

## Exercise 1 - Sets

We asked the students in each REDI class to state their native languages and got the results: 

  * Python class: russian, french, arabic, arabic, arabic, arabic, farsi
  * Java class: english, kurdish, arabic, arabic, french 

Based on these data sets, we would like the answer the following questions:  

  1. How many different, *unique* languages do we have in each class?
  1. What are the languages spoken in *both* classes?
  1. What are the languages that are found in only one class (not in both)?
  1. What are languages found in the Python class but not in the Java class?

If you want, you can use the following template for the result.
You still need to do the calculations :)

```python
# How many different, unique languages do we have in each class?
print('Spoken languages Java:', )
print('Spoken languages Python:', )

# What are the languages spoken in both classes?
print('All languages:', )

# What are common languages between the two classes?
print('Common languages:', )

# What are the languages that are found in only one class (not in both)?
print('One-class languages:', )

# What are languages found in Python class but not in Java class and vice versa?
print('Python class specific languages:', )
```

## Exercise 2 - Dictionaries

Create a new dictionary called "prices" using the full format with {}, e.g.  
```python
this_is_what_it_looks_like = {
    'Key 1' : 'Value 1',
    'Key 2' : 'Value 2',
}
```

Put these values in your prices dictionary:

```
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
```

Create another dictionary called "stock", containing the following values:

```
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15,
"mango": 700
```


1. Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format:
```
apple
price: 2
stock: 6
```

2. Let's determine how much money you would make if you sold all of your food.

  * Create a variable called total and set it to zero.
  * Loop through the prices dictionaries.For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
  * Finally, outside your loop, print the total.


## Challenge Exercise: Grade System

***

***This is optional, please only attempt it if you are eager to learn more!
It is supposed to be challenging.***

***

The aim of this exercise is to make a gradebook for the students of a teacher.

Given the following example dicts:

```python
lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
```  

1. Create a list of students. For each student in your students list, print out that student's data, as follows:

    - print the student's name
    - print the student's homework
    - print the student's quizzes
    - print the student's tests

2. Write a function average that takes a list of numbers and returns the average.

    - Define a function called average that has one argument, numbers.
    - use the built-in sum() function with a numbers list as a parameter. 
    - Use float() to convert total and store the result in total.
    - Divide total by the length of the numbers list. Use the built-in *len()* function to calculate that.

3. Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns the weighted average.

    - Define a function called get_average that takes one argument called student.
    - Make a variable homework that stores the average() of student["homework"].
    - Repeat step 2 for "quizzes" and "tests".
    - Multiply the 3 averages by their weights and return the sum of those three. Weight for homeworks is 10%, for quizzes it's 30% and for tests it's 60%.

4. Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.

    - Inside your function, test score using a chain of if: / elif: / else: statements, like so:

    ```
    If score is 90 or above: return "A"
    Else if score is 80 or above: return "B"
    Else if score is 70 or above: return "C"
    Else if score is 60 or above: return "D"
    Otherwise: return "F"
    ```

    - Finally, test your function. Call your get_letter_grade function with the result of get_average(lloyd). Print the resulting letter grade.

5. Define a function called get_class_average that has one argument, students. You can expect students to be a list containing your three students.

    - First, make an empty list called results.
    - For each student item in the class list, calculate get_average(student) and then call results.append() with that result.
    - Finally, return the result of calling average() with results.

6. Finally, print out the result of calling get_class_averagewith your students list. Your students should be [lloyd, alice, tyler].

7. Then, print the result of get_letter_grade for the class's average.