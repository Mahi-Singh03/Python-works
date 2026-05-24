# Rock Paper Scissors Game in Python

This program creates a simple **Rock, Paper, Scissors** game where:

* The user enters a choice
* The computer randomly selects a choice
* The winner is decided using conditions

---

# Complete Code

```python
import random

choices = {
    "r":"rock",
    "p":"paper",
    "s":"scissors"
}

computer_choice = random.choice(list(choices.keys()))

user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ")

if user_choice not in choices:
    print("Invalid choice. Please choose r, p, or s.")

else:
    print(f"Computer chose: {choices[computer_choice]}")
    print(f"You chose: {choices[user_choice]}")

    if computer_choice == user_choice:
        print("It's a tie!")

    elif (
        (computer_choice == "r" and user_choice == "s") or
        (computer_choice == "p" and user_choice == "r") or
        (computer_choice == "s" and user_choice == "p")
    ):
        print("Computer wins!")

    else:
        print("You win!")
```

---

# Step-by-Step Explanation

## 1. Importing the Random Module

```python
import random
```

### Explanation

* `random` is a built-in Python module.
* It is used to generate random values.
* In this game, it helps the computer make a random choice.

---

## 2. Creating the Dictionary

```python
choices = {
    "r":"rock",
    "p":"paper",
    "s":"scissors"
}
```

### Explanation

This is a **dictionary**.

A dictionary stores data in **key-value pairs**.

| Key | Value    |
| --- | -------- |
| r   | rock     |
| p   | paper    |
| s   | scissors |

The dictionary converts short forms into readable words.

Example:

```python
choices["r"]
```

Output:

```python
rock
```

---

## 3. Computer Random Choice

```python
computer_choice = random.choice(list(choices.keys()))
```

### Explanation

* `choices.keys()` gets all keys from the dictionary.
* `list()` converts them into a list.
* `random.choice()` selects one random value.

Possible outputs:

```python
r
p
s
```

---

## 4. Taking User Input

```python
user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ")
```

### Explanation

* `input()` is used to take data from the user.
* The text inside input is shown to the user.

Example:

```python
Enter your choice (r for rock, p for paper, s for scissors):
```

---

## 5. Checking Invalid Input

```python
if user_choice not in choices:
```

### Explanation

This checks whether the user's choice exists in the dictionary.

Valid choices:

```python
r
p
s
```

If the user enters something else like `x`, the condition becomes TRUE.

---

## 6. Invalid Choice Message

```python
print("Invalid choice. Please choose r, p, or s.")
```

This line runs only when the user enters an invalid value.

---

## 7. Else Block

```python
else:
```

If the input is valid, the program continues inside the `else` block.

---

## 8. Showing Computer Choice

```python
print(f"Computer chose: {choices[computer_choice]}")
```

### Explanation

This uses an **f-string**.

Example:

```python
computer_choice = "r"
```

Output:

```python
Computer chose: rock
```

---

## 9. Showing User Choice

```python
print(f"You chose: {choices[user_choice]}")
```

Works the same way as the computer choice.

---

## 10. Checking Tie Condition

```python
if computer_choice == user_choice:
```

If both choices are the same, it is a tie.

---

## 11. Tie Message

```python
print("It's a tie!")
```

---

## 12. Checking Computer Win Conditions

```python
elif (
    (computer_choice == "r" and user_choice == "s") or
    (computer_choice == "p" and user_choice == "r") or
    (computer_choice == "s" and user_choice == "p")
):
```

### Explanation

This checks all situations where the computer wins.

### Rule 1

```python
computer_choice == "r" and user_choice == "s"
```

Rock beats scissors.

### Rule 2

```python
computer_choice == "p" and user_choice == "r"
```

Paper beats rock.

### Rule 3

```python
computer_choice == "s" and user_choice == "p"
```

Scissors beats paper.

---

## 13. Computer Wins Message

```python
print("Computer wins!")
```

---

## 14. Final Else Block

```python
else:
    print("You win!")
```

If:

* It is NOT a tie
* The computer does NOT win

then the user wins.

---

# Example Outputs

## Example 1 — User Wins

```python
Computer chose: rock
You chose: paper
You win!
```

## Example 2 — Computer Wins

```python
Computer chose: scissors
You chose: paper
Computer wins!
```

## Example 3 — Tie

```python
Computer chose: rock
You chose: rock
It's a tie!
```

---

# Concepts Used in This Program

| Concept              | Purpose                   |
| -------------------- | ------------------------- |
| import               | Import modules            |
| random.choice()      | Random selection          |
| dictionary           | Store key-value pairs     |
| input()              | Take user input           |
| if/elif/else         | Decision making           |
| logical operators    | Check multiple conditions |
| f-string             | Format output             |
| comparison operators | Compare values            |

---

# Summary

This project teaches:

* Dictionaries
* User input
* Random module
* Conditional statements
* Logical operators
* Game logic
* f-strings

It is a great beginner Python project because it combines multiple core concepts together.
