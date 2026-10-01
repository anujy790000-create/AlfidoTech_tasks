# Task 1: Python File Handling and Automation

## 📌 Objective
This task demonstrates core Python skills including:
1. Reading and Writing Files (TXT/CSV)
2. Automation (Rename/Move/Delete)
3. Exception Handling

## 🛠️ How to Run
1. Ensure you have Python installed.
2. Run the script using: `python task1_file_handling.py`

## 📸 Screenshots

### Code Execution in VS Code
![VS Code Screenshot](https://github.com/.../Output%201.png?raw=true)

### Terminal Output
![Terminal Output](https://github.com/.../Output%202.png?raw=true)

## 📖 Explanation of the Code
* **File Handling:** The script uses `open()` with `'w'` and `'r'` modes to write and read both TXT and CSV files.
* **Automation:** The `os` and `shutil` modules are used to rename (`os.rename`), move (`shutil.move`), and delete (`os.remove`) files automatically.
* **Exception Handling:** `try...except` blocks are used to catch `FileNotFoundError` and `OSError` to prevent the script from crashing if files are missing or directories cannot be created.

## 💡 Insights/Learnings
* Learned how to use the `csv` module to parse structured data.
* Understood how to use `os.path.join()` for cross-platform file paths.
* Gained experience in handling errors gracefully using Python's exception handling.
