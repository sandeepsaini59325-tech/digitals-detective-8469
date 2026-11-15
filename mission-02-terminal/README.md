### Task 2.1 – Explore basic Terminal operations

| Operation / command name     | Command used                          | What it does                              | What I observed                          |
|-----------------------------|---------------------------------------|-------------------------------------------|------------------------------------------|
| Current-directory display   | `pwd`                                 | Shows full path of current folder         | Showed complete path of my folder        |
| Directory listing           | `ls`                                  | Lists files and folders                   | Showed names of files and folders        |
| Detailed listing            | `ls -l`                               | Shows detailed information                | Showed permissions, size, date etc.      |
| Change directory            | `cd ..`                               | Moves to parent folder                    | Current location changed                 |
| Create directory            | `mkdir terminal-practice`             | Creates a new folder                      | New folder created                       |
| Create empty file           | `touch notes.txt`                     | Creates an empty file                     | Empty file created                       |
| Copy file                   | `cp notes.txt notes-copy.txt`         | Creates a copy of the file                | Copy created successfully                |
| Move / rename file          | `mv notes-copy.txt notes-renamed.txt` | Renames or moves the file                 | File name changed                        |
| Display file contents       | `cat notes.txt`                       | Shows the content of the file             | Showed the text inside the file          |

### Task 2.2 – Practise file changes safely

| Question                                              | Answer                                                                 |
|-------------------------------------------------------|------------------------------------------------------------------------|
| Difference between replacing and adding text          | `>` replaces the whole content. `>>` adds text at the end.            |
| Difference between copying and moving a file          | `cp` creates a copy. `mv` renames or moves the original file.         |
| What information does current-directory display give? | It shows the full path of the current folder.                         |
| Why is directory-listing operation useful?            | It helps us see which files and folders are present in the location.  |

### Task 2.3 – Understand flags and pipes

| Concept                          | My Understanding                                                                 |
|----------------------------------|----------------------------------------------------------------------------------|
| What is a flag?                  | A flag is an extra option (like `-l`, `-a`, `-h`) that changes how a command works. |
| What changed when using flags?   | Normal `ls` showed only names. `ls -lah` showed details, hidden files and sizes. |
| What does the pipe (`\|`) do?    | It takes the output of one command and gives it as input to another command.     |
| Example of pipe                  | `ls -l \| head -n 5` shows only the first 5 lines of the detailed list.          |

### Task 2.4 – Understand package managers

| Point                            | Explanation                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| What is a package manager?       | A tool that helps install, update and remove software easily.               |
| Example                          | Homebrew (used on macOS)                                                    |
| Why is it useful?                | It makes software installation fast and safe using simple Terminal commands.|