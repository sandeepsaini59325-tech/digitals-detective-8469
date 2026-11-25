### Task 6.1 – Understand the basic Git workflow

| Git operation              | What it does in your own words |
|----------------------------|--------------------------------|
| Check repository status    | `git status` se pata chalta hai kaunsi files change hui hain aur kaunsi stage/commit ke liye ready hain |
| Stage selected changes     | `git add filename` se selected file ko staging area mein daalte hain (commit ke liye ready karte hain) |
| Create a commit            | `git commit -m "message"` se staged changes ko permanent save kar dete hain with a message |
| View commit history        | `git log` se pehle ke saare commits dekh sakte hain |

**Difference between Staging and Committing:**
- **Staging** (`git add`) → Changes ko temporarily select karna (jaise packing before saving)
- **Committing** (`git commit`) → Selected changes ko permanently save kar dena with a message

### Task 6.2 – Create and use a branch

**What I did:**

1. Created a new branch:
```bash
git checkout -b update-about

### Task 6.3 – Create a Pull Request

**Steps I followed:**

1. GitHub pe apna repository khola.
2. `update-about` branch ko `main` branch se compare kiya.
3. **Pull Request** create kiya (`update-about` → `main`).
4. Description mein likha: “Added My Learning section in README”.
5. Pull Request create kar diya.
6. (Instructor ne merge karne ko kaha ho to) Merge kar diya.
7. Local system mein wapas `main` branch pe aaya:

```bash
git checkout main
git pull origin main


```markdown
### Task 6.4 – Git Command Glossary

| Git Operation              | What it does (in simple words)                              |
|----------------------------|-------------------------------------------------------------|
| Initialise a repository    | `git init` – Naya Git repository banata hai                 |
| Check status               | `git status` – Kaunsi files change hui hain yeh dikhata hai |
| Stage changes              | `git add` – Files ko commit ke liye ready karta hai         |
| Commit changes             | `git commit` – Changes ko permanently save karta hai        |
| View history               | `git log` – Pehle ke saare commits dikhata hai              |
| Create or list branches    | `git branch` – Branches banata ya list dikhata hai          |
| Switch branches            | `git checkout` – Ek branch se doosri branch pe jata hai     |
| Publish changes            | `git push` – Local changes ko GitHub pe bhejta hai          |
| Retrieve remote changes    | `git pull` – GitHub se latest changes lata hai              |