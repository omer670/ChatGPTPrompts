import openai # Install via "pip install openai"
import inspect

# A docstring example
def square(n):
    """Takes in a number n and returns the square of n"""
    return n**2


def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr