# Python Virtual Environment (venv) 



## 📌 What is a Virtual Environment?

A **virtual environment (venv)** is an isolated Python environment that allows you to install packages for a specific project without affecting the global system or other projects.

👉 Benefits:

* Avoid dependency conflicts
* Keep projects independent
* Clean system environment

---

##  Check Python Installation

```bash
py --version
```

---

##  Create Virtual Environment

```bash
py -m venv myenv
```

This creates a folder named `myenv`.

---

##  Activate Virtual Environment (Windows)

```bash
myenv\Scripts\activate
```

After activation:

```
(myenv) C:\your-project>
```

---

##  Install Packages

```bash
pip install <module_name>
```

Example:

```bash
pip install pyjokes
```

If pip doesn’t work:

```bash
py -m pip install pyjokes
```

---

##  Run Python File

```bash
python filename.py
```

Example:

```bash
python modules.py
```

---

##  Deactivate Virtual Environment

```bash
deactivate
```

---

##  Save & Reuse Dependencies

Save installed packages:

```bash
pip freeze > requirements.txt
```

Install later:

```bash
pip install -r requirements.txt
```

---

##  VS Code Setup

1. Open project folder
2. Press `Ctrl + Shift + P`
3. Select: `Python: Select Interpreter`
4. Choose:

```
myenv\Scripts\python.exe
```

---

##  Common Errors & Fixes

###  CommandNotFoundException

➡ Usually caused by spaces in folder names

✔ Fix:

*  `New course`
*  `New_course`

---

###  pip not working

```bash
py -m pip install <module_name>
```

---

###  Module not found

➡ Package not installed in venv

 Fix:

```bash
pip install <module_name>
```

---

##  Best Practices

* Always activate venv before installing or running
* Use one venv per project
* Avoid spaces in folder names
* Don’t install packages globally unless needed

---

##  Complete Workflow

```bash
cd my_project
py -m venv myenv
myenv\Scripts\activate
pip install pyjokes
python modules.py
```

---

## Project Structure

```
my_project/
│
├── myenv/
├── modules.py
├── requirements.txt
└── README.md
```

---

##  Summary

* `venv` = isolated Python environment
* Keeps dependencies project-specific
* Prevents conflicts
* Essential for development

---


