## 🔹 What is the `map()` Function?

## The `map()` function applies a **given function** to **each item** of an **iterable** (like list, tuple, etc.) and returns a **map object** (which is an iterator). You can convert it to a list, tuple, or any other collection.

## 🔹 Syntax: map(function, iterable)


### ✅ Parameters:
## - **function**: A function that you want to apply to each item.
## - **iterable**: One or more iterable(s) (like list, tuple, etc.)

### ✅ Return:
## - Returns a `map` object (which is an iterator), which can be converted using `list()`, `tuple()`, etc.

## 🔹 Example 1: Using `map()` with a built-in function

numbers = [1, 2, 3, 4, 5]
squared = map(pow, numbers, [2]*len(numbers))  # pow(x, 2) = x^2
print(list(squared))

## **Output:** [1, 4, 9, 16, 25]

## 🔹 Example 2: Using `map()` with a custom function

def double(x):
    return x * 2

nums = [1, 2, 3, 4]
result = map(double, nums)
print(list(result))

## **Output:** [2, 4, 6, 8]

## 🔹 Example 3: Using `map()` with `lambda` function

nums = [5, 10, 15]
result = map(lambda x: x + 1, nums)
print(list(result))

## 🔸 **Output:** [6, 11, 16]

## 🔹 Example 4: Using `map()` with multiple iterables

a = [1, 2, 3]
b = [4, 5, 6]
result = map(lambda x, y: x + y, a, b)
print(list(result))

## 🔸 **Output:** [5, 7, 9]

## 🔹 Example 5: Convert string items to integers using `map()`

str_numbers = ['1', '2', '3']
int_numbers = list(map(int, str_numbers))
print(int_numbers)

## 🔸 **Output:** [1, 2, 3]

## 🔹 Important Notes

## - `map()` does **not** change the original list.
## - It returns a `map` object, which is **lazy** (does not process items until needed).
## - You need to convert the map object to list/tuple to see the result.

