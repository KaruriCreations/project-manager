class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
        }
    
class Project:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
                            }
    
class Task:
    def __init__(self, title, project_title, status='pending'):
        self.title = title
        self.project_title = project_title
        self.status = status

    def to_dict(self):
        return {
            'title': self.title,
            'project_title': self.project_title,
            'status': self.status
        }
    
