import pytest
from models import User, Task, Project

def test_user_creation():
    user = User(name="testuser", email="test@gmail.com")
    #test that the property attributes are working correctly
    assert user.name == "testuser"
    assert user.email == "test@gmail.com"
    
    #test that storing the data in a dictionary works correctly
    data = user.to_dict()
    assert data['name'] == "testuser"
    assert data['email'] == "test@gmail.com"

def test_project_creation():
    project = Project(title="Test Project", description="A test project", user_name="testuser")
    #test that the property attributes are working correctly
    assert project.title == "Test Project"
    assert project.description == "A test project"
    assert project.user_name == "testuser"
    
    #test that storing the data in a dictionary works correctly
    data = project.to_dict()
    assert data['title'] == "Test Project"
    assert data['description'] == "A test project"
    assert data['user_name'] == "testuser"

def test_task_creation():
    task = Task(title="Test Task", description="A test task", project_title="Test Project")
    #test that the property attributes are working correctly
    assert task.title == "Test Task"
    assert task.description == "A test task"
    assert task.project_title == "Test Project"
    assert task.status == "pending"
    
    #test that storing the data in a dictionary works correctly
    data = task.to_dict()
    assert data['title'] == "Test Task"
    assert data['description'] == "A test task"
    assert data['project_title'] == "Test Project"
    assert data['status'] == "pending"  

def test_task_completion():
    task = Task(title="Test Task", description="A test task", project_title="Test Project")
    #test that the initial status is pending
    assert task.status == "pending"
    
    #complete the task and test that the status updates correctly
    task.complete_a_task()
    assert task.status == "completed"