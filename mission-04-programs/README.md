### Task 4.1 – Create and run a Python program

**What I did:**
1. Created a file named `hello.py` inside `mission-04-programs` folder.
2. Wrote this code inside the file:

```python
print("Hello from Python")

### Task 4.2 – Compare compiler and interpreter

| Point                          | Compiler                                      | Interpreter                                  |
|--------------------------------|-----------------------------------------------|----------------------------------------------|
| When translation / execution happens | Translates the whole program first, then runs it | Translates and runs the program line by line |
| Typical output                 | Creates an executable file                    | Directly shows the result                    |
| One example                    | C, C++                                        | Python, JavaScript                           |
| One advantage                  | Runs faster after compilation                 | Easier to test and find errors               |

**Explanation:**

A compiler translates the entire program into machine code before running it.  
An interpreter translates and executes the program line by line at the same time.  
Because of this, compiled programs usually run faster, while interpreted programs are easier to test and debug.  
Python uses an interpreter, which is why we can run the code directly using the `python3` command.