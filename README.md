
# Speed Calculator Decorator

This Python decorator measures the execution time of a function and prints the time taken to execute it.

## How It Works

The decorator function `speed_calc_decorator` wraps around another function, allowing it to measure the execution time of that function. Here's how it works:

1. **Decorator Function**: `speed_calc_decorator` is a higher-order function that takes another function as its argument.
2. **Wrapper Function**: Inside `speed_calc_decorator`, a new function called `wrapper_function` is defined. This function:
   - Records the current time before and after executing the decorated function.
   - Calculates the difference between these times to determine the execution time.
   - Prints the execution time along with the name of the decorated function.
   - Returns the result of the decorated function.
3. **Application**: To apply the decorator to a function, use the `@speed_calc_decorator` syntax above the function definition. This indicates that the function should be wrapped by the `speed_calc_decorator` function.

## Example Functions

The decorator can be applied to any function to measure its execution time. Here are some example functions:

- **fast_function**: A fast function that iterates through a large range of numbers.
- **slow_function**: A slow function that sleeps for 2 seconds using `time.sleep()`.

## Usage

1. Define your functions or use existing ones.
2. Decorate the functions you want to measure with `@speed_calc_decorator`.
3. Call the decorated functions as usual.

## Special Syntax

In Python, `*args` and `**kwargs` are special syntax used in function definitions that allow you to pass a variable number of arguments to a function:

- `*args`: Collects all positional arguments into a tuple.
- `**kwargs`: Collects all keyword arguments into a dictionary.

These features allow for flexible function definitions that can handle different types and numbers of arguments.

