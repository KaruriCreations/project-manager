# Project Manager CLI

A robust, object-oriented command-line tool built in Python to manage users, projects, and tasks with local JSON persistence. 

## Features
- **Object-Oriented Design:** Encapsulated models for Users, Projects, and Tasks.
- **CLI Interface:** Clean, modular commands powered by `argparse` with styled output via `rich`.
- **Persistent Storage:** Data is automatically saved and loaded from local JSON files.
- **Separation of Concerns:** Distinct layers for models, data storage, and the user interface.

## Prerequisites
- Python 3.14+
- `pipenv` (optional, for dependency management)

## Installation

You can install the required packages using either `pip` or `pipenv`.

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using pipenv:**
```bash
pipenv install
pipenv shell
```

## Usage

The CLI supports several subcommands. Use `python main.py -h` for help.

### User Management
Add a new user to the system:
```bash
python main.py add_user --name "John Doe" --email "john@example.com"
```

### Project Management
Add a new project and assign it to an existing user:
```bash
python main.py add_project --title "API Rewrite" --description "Rewriting the backend in FastAPI" --user "John Doe"
```

### Task Management
Add a task to an existing project:
```bash
python main.py add_task --title "Setup Database" --description "Initialize PostgreSQL" --project "API Rewrite"
```

Mark a task as completed:
```bash
python main.py complete_task --title "Setup Database"
```

## Project Structure

- `main.py` - The CLI entry point handling argument parsing and terminal output.
- `models.py` - Core classes defining the structure and behavior of entities.
- `storage.py` - File I/O layer handling JSON serialization and deserialization.
- `tests.py` - Unit testing suite for core components.
- `data/` - Directory storing the persistent `.json` files.

## Running Tests

To verify the integrity of the project models, run the test suite using pytest:
```bash
pytest tests.py
```
