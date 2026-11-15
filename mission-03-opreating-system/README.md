| Information explored              | What it tells you                          | Your observation (privacy-safe)       |
|-----------------------------------|--------------------------------------------|---------------------------------------|
| Operating system / system details | Shows which operating system is running    | macOS (version redacted)              |
| Current account identity          | Shows the currently logged-in user         | User: [redacted]                      |
| Available and used storage        | Shows free and used disk space             | Storage details redacted              |
| System activity snapshot          | Shows currently running processes          | Multiple processes were running       |

### Task 3.2 – Understand processes

**What is a process?**  
A process is a program that is currently running on the computer.

**What does the PID column represent?**  
PID means Process ID. It is a unique number given to every running process so the system can identify it.

**Two examples of processes:**
- Browser (like Chrome or Safari)
- Text editor (like VS Code or TextEdit)

### Task 3.3 – Understand paths and permissions

**Difference between Absolute path and Relative path:**

- **Absolute path** → Poora path hota hai jo root se start hota hai.  
  Example: `/Users/[redacted]/digital-detective-xxxx/mission-03-operating-system`

- **Relative path** → Current folder se related path hota hai.  
  Example: `mission-03-operating-system` ya `../mission-02-terminal`

**Permissions:**

Jab `ls -l` command chalaya to file ke permissions kuch is tarah dikhte hain jaise:

`-rw-r--r--`

Isme owner ke permissions hote hain:
- `r` = Read (file padh sakta hai)
- `w` = Write (file edit kar sakta hai)
- `x` = Execute (file run kar sakta hai)

Mere practice file mein owner ke paas **read** aur **write** permission thi.

### Task 3.4 – Explain operating-system responsibilities

| OS responsibility          | Your explanation                                      | Example                          |
|----------------------------|-------------------------------------------------------|----------------------------------|
| Process management         | OS manages all running programs and gives them time to run | Running Chrome and VS Code together |
| Memory management          | OS manages RAM and gives memory to programs when needed | Giving memory to a browser when many tabs are open |
| Device management          | OS controls hardware devices like keyboard, mouse, printer | Using keyboard to type and mouse to click |
| File management            | OS organises and manages files and folders on storage | Creating, saving and deleting files |
| User interface / shell     | OS provides a way for users to interact with the computer | Terminal or graphical desktop |
| Security and permissions   | OS controls who can access files and system resources | File permissions (read, write, execute) |