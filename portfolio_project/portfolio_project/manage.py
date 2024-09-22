# manage.py
import os
import sys
import environ

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
    environ.Env.read_env()  # Load environment variables from .env file
    
    # Debugging: Print environment variables
    print(f"DB_NAME: {os.getenv('DB_NAME')}")
    print(f"EMAIL_HOST_USER: {os.getenv('EMAIL_HOST_USER')}")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
