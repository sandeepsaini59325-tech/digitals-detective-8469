### Task 5.1 – Convert numbers by hand

**1. Decimal 13 to Binary**
- 13 ÷ 2 = 6 remainder 1
- 6 ÷ 2 = 3 remainder 0
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1  
**Answer: 1101**

**2. Decimal 25 to Binary**
- 25 ÷ 2 = 12 remainder 1
- 12 ÷ 2 = 6 remainder 0
- 6 ÷ 2 = 3 remainder 0
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1  
**Answer: 11001**

**3. Binary 1010 to Decimal**
- (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)  
- 8 + 0 + 2 + 0 = **10**

**4. Binary 1101 to Decimal**
- (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)  
- 8 + 4 + 0 + 1 = **13**

**5. Hexadecimal A to Decimal**
- A = 10  
**Answer: 10**

**6. Hexadecimal 1F to Decimal**
- 1 × 16 = 16  
- F = 15  
- 16 + 15 = **31**

**7. Binary 1111 to Hexadecimal**
- Binary 1111 = Decimal 15  
- 15 = F in Hexadecimal  
**Answer: F**

### Task 5.2 – Verify using Python

Python interactive mode mein yeh commands chalayi:

| Expression                  | Result     | Matches manual calculation? |
|----------------------------|------------|-----------------------------|
| `bin(13)`                  | `0b1101`   | Yes                         |
| `bin(25)`                  | `0b11001`  | Yes                         |
| `int('1010', 2)`           | `10`       | Yes                         |
| `int('1101', 2)`           | `13`       | Yes                         |
| `hex(10)`                  | `0xa`      | Yes                         |
| `int('1F', 16)`            | `31`       | Yes                         |
| `hex(15)`                  | `0xf`      | Yes                         |

**Note:**  
- `bin()` decimal ko binary mein convert karta hai  
- `int(value, 2)` binary ko decimal mein convert karta hai  
- `hex()` decimal ko hexadecimal mein convert karta hai  
- `int(value, 16)` hexadecimal ko decimal mein convert karta hai  

Sab results mere manual calculations se match kiye.

### Task 5.4 – How is text stored?

**ASCII codes:**
- Uppercase **A** → 65
- Lowercase **a** → 97

**Why does a computer need an encoding standard?**  
Computer only understands numbers (0 and 1). Encoding standards like ASCII and UTF-8 convert letters and symbols into numbers so the computer can store and process text.

**Example of a character not in basic ASCII:**  
₹ (Indian Rupee symbol) or e