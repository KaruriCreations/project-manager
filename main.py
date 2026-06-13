import argparse
import storage
from models import Project, Task, User
from rich.console import Console

console = Console()
USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

def add_user(args):
    # 1. Load what is ALREADY saved in the file
    existing_users = storage.load_users(USERS_FILE)
    
    # 2. Instantiate your new user
    user = User(name=args.name, email=args.email)
    
    # 3. Add them to the existing list
    existing_users.append(user)
    
    # 4. Save the FULL list back to disk
    storage.save_users(existing_users, USERS_FILE)
    console.print(f"User '{args.name}' added successfully!")

def add_project(args):
    # 1. Load what is ALREADY saved in the file
    existing_projects = storage.load_projects(PROJECTS_FILE)
    
    # 2. Append and save the whole collection
    project = Project(title=args.title, description=args.description, user_name=args.user)
    existing_projects.append(project)
    
    storage.save_projects(existing_projects, PROJECTS_FILE)
    console.print(f"Project '{args.title}' added successfully!")

def add_task(args):
    # 1. Load what is ALREADY saved in the file
    existing_tasks = storage.load_tasks(TASKS_FILE)
    
    # 2. Append and save the whole collection
    task = Task(title=args.title, description=args.description, project_title=args.project)
    existing_tasks.append(task)
    
    storage.save_tasks(existing_tasks, TASKS_FILE)
    console.print(f"Task '{args.title}' added successfully!")
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()

    # Add user command
    user_parser = subparsers.add_parser("add_user", help="Add a new user")
    user_parser.add_argument("--name", required=True, help="Name of the user")
    user_parser.add_argument("--email", required=True, help="Email of the user")
    user_parser.set_defaults(func=add_user)

    # Add project command
    project_parser = subparsers.add_parser("add_project", help="Add a new project")
    project_parser.add_argument("--title", required=True, help="Title of the project")
    project_parser.add_argument("--description", required=True, help="Description of the project")
    project_parser.add_argument("--user", required=True, help="Name of the user associated with the project")
    project_parser.set_defaults(func=add_project)

    # Add task command
    task_parser = subparsers.add_parser("add_task", help="Add a new task")
    task_parser.add_argument("--title", required=True, help="Title of the task")
    task_parser.add_argument("--description", required=True, help="Description of the task")
    task_parser.add_argument("--project", required=True, help="Title of the project associated with the task")
    task_parser.set_defaults(func=add_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()