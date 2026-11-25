### Task 5.3 – Build a small number converter

**Python Program (`number_converter.py`):**

```python``
decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)
hexadecimal = hex(decimal)

print("Binary:", binary)
print("Hexadecimal:", hexadecimal)