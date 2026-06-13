class User:
    def __init__(self, name, email):
        self.__name = name        # Truly Private attribute
        self.__email = email      # Truly Private attribute
        self.projects = []

    # --- PROPERTY GETTERS ---
    # This allows other files to safely read user.name without modifying it
    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            'name': self.__name,
            'email': self.__email,
        }
    
class Project:
    def __init__(self, title, description, user_name):
        self.__title = title              # Private
        self.__description = description  # Private
        self.__user_name = user_name      # Private link string
        self.tasks = []

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def user_name(self):
        return self.__user_name

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            'title': self.__title,
            'description': self.__description,
            'user_name': self.__user_name
        }
    
class Task:
    def __init__(self, title, description, project_title, status='pending'):
        self.__title = title                  # Private
        self.__description = description      # Private
        self.__project_title = project_title  # Private
        self.status = status                  # Left public so CLI can update it easily!

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def project_title(self):
        return self.__project_title

    def to_dict(self):
        return {
            'title': self.__title,
            'description': self.__description,
            'project_title': self.__project_title,
            'status': self.status
        }
    
    def complete_a_task(self):
        self.status = 'completed'