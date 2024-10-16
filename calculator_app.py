import streamlit as st
import math

# Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def log(a, base=10):
    if a > 0:
        return math.log(a, base)
    else:
        return "Error! Logarithm undefined for non-positive numbers."

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

# Streamlit App
st.title("Complex Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", format="%.2f")
operation = st.selectbox("Select operation", 
                         ("Add", "Subtract", "Multiply", "Divide", 
                          "Power", "Square Root", "Logarithm", 
                          "Sin", "Cos", "Tan"))

# For operations that need two numbers
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num2 = st.number_input("Enter second number", format="%.2f")

# Calculate and display result
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Power":
        result = power(num1, num2)
    elif operation == "Square Root":
        result = sqrt(num1)
    elif operation == "Logarithm":
        base = st.number_input("Enter logarithm base (default is 10)", value=10)
        result = log(num1, base)
    elif operation == "Sin":
        result = sin(num1)
    elif operation == "Cos":
        result = cos(num1)
    elif operation == "Tan":
        result = tan(num1)

    st.write(f"The result is: {result}")
