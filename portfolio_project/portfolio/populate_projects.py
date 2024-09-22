# Import necessary modules and Django settings
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from portfolio.models import Project

def populate_projects():
    # Create minor projects
    for i in range(1, 11):
        Project.objects.create(
            title=f"Minor Project {i}",
            image="path/to/image.jpg",  # Replace with actual image path or handle file uploads programmatically
            github_url="https://github.com/dixit611",
            live_url="#"
        )

    # Create major projects
    for i in range(1, 6):
        Project.objects.create(
            title=f"Major Project {i}",
            image="path/to/image.jpg",  # Replace with actual image path or handle file uploads programmatically
            github_url="https://github.com/dixit611",
            live_url="#"
        )

if __name__ == '__main__':
    populate_projects()
