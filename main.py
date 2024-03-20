import time

# Decorator function to measure the execution time of a function
def speed_calc_decorator(function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()  # Get the current time before executing the function
        result = function(*args, **kwargs)  # Execute the decorated function
        end_time = time.time()  # Get the current time after executing the function
        run_time = end_time - start_time  # Calculate the execution time
        print(f"{function.__name__} run speed: {run_time}s")  # Print the execution time
        return result
    return wrapper_function

# Example functions to test the decorator
@speed_calc_decorator
def fast_function():
    for _ in range(1000000):
        pass

@speed_calc_decorator
def slow_function():
    time.sleep(2)

# Call the functions to see the execution time
fast_function()
slow_function()

# In Python, *args and **kwargs are special syntax used in function definitions that allow you to pass a variable number of arguments to a function.

# *args: This notation allows a function to accept any number of positional arguments. When *args is used in a function definition, it collects all positional arguments into a tuple.
# You can then iterate over this tuple or access individual elements by index. The name args is a convention, but you can use any name preceded by the asterisk (*).

# **kwargs: This notation allows a function to accept any number of keyword arguments. When **kwargs is used in a function definition,
# it collects all keyword arguments into a dictionary, where the keys are the argument names and the values are the corresponding argument values. Again, kwargs is a convention, but you can use any name preceded by the double asterisk (**).
