import json
from models import User, Project, Task

# --- FILE INPUT/OUTPUT LAYER ---

def read_json(filepath):
    if not filepath:
        raise ValueError("Filepath cannot be empty.")
    try:
        with open(filepath, "r") as file:
            #using json.load() instead of file.read() to make the data into python objects
            content = json.load(file)
            return content
    except FileNotFoundError:
        # returns an empty list if the file doesn't exist yet
        return []

def write_json(filepath, data):
    if not filepath:
        raise ValueError("Filepath cannot be empty.")
    with open(filepath, "w") as file:
        #using json.dump() to write the data into the file in JSON format
        json.dump(data, file, indent=4)


# --- DATA SAVING LAYER ---

def save_users(users, filepath):
    if not isinstance(users, list):
        raise ValueError("Users should be a list of User objects.")
    users_data = [user.to_dict() for user in users]
    write_json(filepath, users_data)

def save_projects(projects, filepath):
    if not isinstance(projects, list):
        raise ValueError("Projects should be a list of Project objects.")
    projects_data = [project.to_dict() for project in projects]
    write_json(filepath, projects_data)

def save_tasks(tasks, filepath):
    if not isinstance(tasks, list):
        raise ValueError("Tasks should be a list of Task objects.")
    tasks_data = [task.to_dict() for task in tasks]
    write_json(filepath, tasks_data)


# --- DATA LOADING LAYER ---

def load_users(filepath):
    if not filepath:
        raise ValueError("Filepath cannot be empty.")
    content = read_json(filepath)
    
    loaded_users = []
    for user in content:
        loaded_users.append(User(user['name'], user['email']))
    return loaded_users

def load_projects(filepath):
    if not filepath:
        raise ValueError("Filepath cannot be empty.")
    content = read_json(filepath)
    
    loaded_projects = []
    for project in content:
        loaded_projects.append(Project(project['title'], project['description'], project['user_name']))
    return loaded_projects

def load_tasks(filepath):
    if not filepath:
        raise ValueError("Filepath cannot be empty.")
    content = read_json(filepath)
    
    loaded_tasks = []
    for task in content:
        loaded_tasks.append(Task(task['title'], task['project_title'], task['status']))
    return loaded_tasks