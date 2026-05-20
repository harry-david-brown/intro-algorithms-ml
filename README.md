# Introduction to Algorithms and Machine Learning

Working through *Introduction to Algorithms and Machine Learning* by Justin Skycak.

---

## One-time setup (per machine)

### macOS / Linux

```bash
git clone https://github.com/YOUR_USERNAME/intro-algorithms-ml.git
cd intro-algorithms-ml
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
git clone https://github.com/YOUR_USERNAME/intro-algorithms-ml.git
cd intro-algorithms-ml
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> If PowerShell blocks the activation script, run:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## Daily workflow

### Starting a session

```bash
# macOS / Linux
source .venv/bin/activate
git pull

# Windows
.venv\Scripts\Activate.ps1
git pull
```

### Running tests for a chapter

```bash
# From the repo root (venv active)
python -m chapters.ch01_intro_exercises.tests
```

### Ending a session — always commit before switching machines

```bash
git add .
git commit -m "ch01: implement check_if_symmetric and convert_to_numbers"
git push
```

WIP commits are fine:
```bash
git commit -m "WIP: ch03 recursive sequences — fib done, collatz in progress"
```

---

## Project structure

```
intro-algorithms-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── utils/
│   └── test_runner.py      # shared test harness (import into every tests.py)
└── chapters/
    ├── ch01_intro_exercises/
    │   ├── exercises.py    # your implementations
    │   └── tests.py        # your tests
    ├── ch02_number_bases/
    │   ├── exercises.py
    │   └── tests.py
    └── ...                 # one folder per chapter, same pattern
```

Each chapter follows the same pattern:
- `exercises.py` — your implementations (no external libs unless the chapter says so)
- `tests.py` — your tests, using `utils/test_runner.py`

---

## Python version

Python 3.10+ (uses `list[int]` and `dict[str, int]` type hints directly).
Check your version: `python3 --version`
