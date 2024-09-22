from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from .models import Project
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail





def send_email(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        website = request.POST.get('website', 'N/A')  # Optional field

        # Email subject and message
        subject = f"Contact Form Submission from {name}"
        message = (
            f"Name: {name}\n"
            f"Mobile: {mobile}\n"
            f"Email: {email}\n"
            f"Website: {website}\n\n"
            f"Message:\n{message_text}"
        )
        recipient_list = ["dixitaman611@gmail.com"]
        from_email = settings.DEFAULT_FROM_EMAIL

        # Send email
        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, "Your message has been successfully sent!")
        except Exception as e:
            messages.error(request, f"Failed to send message: {e}")

        return redirect('/contact/')
    
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url="/login_page")
def projects(request):
     # For now, let's use a hardcoded list of projects
    minor_projects = [
        {"id": 1, "name": "BMI Calculator", "image_url": "/static/img/minor7.jpg", "description": "The BMI calculator is a useful tool that measures whether you are overweight, underweight, or just right. Using technology like HTML, CSS, JavaScript.", 
        'github_url': 'https://github.com/dixit611/webdev/tree/main/bmi-calculator',
        'live_url': 'https://aman-dixit-bmi-calculator.netlify.app',
        },

        {"id": 2, "name": "Spotify Clone", "image_url": "/static/img/minor2.jpg", "description": "Make a Spotify Clone using HTML, CSS , JavaScript and we can play music audio song.",
        'github_url': 'https://github.com/dixit611/only-frontend-project-/tree/main/Spotify-Clone-master',
        'live_url': 'https://aman-dixit-sporify.netlify.app',},

        {"id": 3, "name": "Email Reader", "image_url": "/static/img/minor3.jpg", "description": "Developed Email Reader using HTML, Bootstrap, and Django.To fetch details from a database in Django | DBsqlite | etc.",
        'github_url': 'https://github.com/dixit611/only-frontend-project-',
        'live_url': 'https://your-live-project-url-1',},

        {"id": 4, "name": "Translator Web", "image_url": "/static/img/minor4.jpg", "description": " Translate text in 5 languages and also translated texts with integrated writing tools | API | Voice translator | etc.",
        'github_url': 'https://github.com/dixit611/Translator',
        'live_url': 'https://your-live-project-url-1',},

        {"id": 5, "name": "Clock", "image_url": "/static/img/minor5.jpg", "description": "Clock Instrument that measures the passage of time. The technology used HTML, CSS, JavaScript | etc.",
        'github_url': 'https://github.com/dixit611/only-frontend-project-',
        'live_url': 'https://aman-dixit-clock.netlify.app',},

        {"id": 6, "name": "Video Call Web", "image_url": "/static/img/minor6.jpg", "description": "Online Video Calls, Meetings and Conferencing. Real-time meetings by Google. Using your browser, share your video, desktop, and presentations with teammates and customers. Technology use Zegocloud",
        'github_url': 'https://github.com/dixit611/only-frontend-project-/blob/main/videocall.html',
        'live_url': 'https://aman-video-call-app.netlify.app',},
    ]

    major_projects = [
        {"id": 7, "name": "Student Study Portal", 
         "image_url": "/static/img/major2.jpg", 
         "description": " Developed a comprehensive online platform for students to access study materials, submit assignments. The portal includes features such as user authentication, youtube api, wikipedia etc |  The portal includes functionalities for creating, updating, and deleting notes, and Integrated rich text editor supporting Python, C and JavaScript. Sections for YouTube and DuckDuckGo search Scientific calculator Links to W3Schools and Wikipedia resources,Video call using Zegocloud and API integration. youtubesearchpython || import wikipedia) || sqLite 3 database || Responsive Design || USER-FRIENDLY.",
        'github_url': 'https://github.com/dixit611/studentsPortal',
        'live_url': 'https://your-live-project-url-1',},

        {"id": 8, "name": "E-Book Store", "image_url": "/static/img/major3.jpg", "description": "Developed a fully functional E-Book Store using MERN stack.This project involved creating a dynamic and user-friendly platform where users can browse, search, and purchase e-books.Responsive Design | User Authentication | Responsive UI | Log-in Panel | Bcrypt | Shopping Cart | Search.",
        'github_url': 'https://github.com/dixit611/webdev/tree/main/E-Book-Store/bookStoreApp-master',
        'live_url': 'https://your-live-project-url-1',},

        {"id": 9, "name": "Machine Learning Tools", "image_url": "/static/img/major4.jpg", "description": "Description for major project 3",
        'github_url': 'https://github.com/dixit611',
        'live_url': 'https://your-live-project-url-1',},
    ]

    return render(request, 'projects.html', {
        'minor_projects': minor_projects,
        'major_projects': major_projects,
    })

@login_required(login_url="/login_page")
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html', {'project': project})


def contact(request):
    return render(request, 'contact.html')


# def certifications(request):
#     certifications = range(9)
#     return render(request, 'certifications.html', {'certifications': certifications})

# @login_required(login_url="/login_page")
# def certification_detail_view(request, id):
#     return render(request, 'certification_detail.html', {'id': id})

# Updated certifications function with 11 certifications
def certifications(request):
    certifications = range(1, 13)  # Adjust to handle 11 certifications
    return render(request, 'certifications.html', {'certifications': certifications})

# Keep login protection on detail view
@login_required(login_url="/login_page")
def certification_detail_view(request, id):
    certification_name = f"Certification {id}"  # Example placeholder for name
    certification_image = f"certificate{id}.jpg"  # Assuming static path aligns
    certification_pdf = f"certificate{id}.pdf"  # Assuming PDF path aligns

    context = {
        'id': id,
        'certification': certification_image,  # Pass image name to template
        'pdf_path': certification_pdf  # Pass PDF name to template
    }

    return render(request, 'certification_detail.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username exists
        user_exists = User.objects.filter(username=username).exists()

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if not user_exists:
            # Username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login_page/')
        elif user is None:
            # Password is incorrect
            messages.error(request, 'Invalid password')
            return redirect('/login_page/')
        else:
            # Successful login
            login(request, user)
            return redirect('/projects/')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login_page/')




def register(request):
   if request.method == "POST":
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      username = request.POST.get('username')
      password = request.POST.get('password')


      user = User.objects.filter(username = username)

      if user.exists():
         messages.info(request, 'Username is already taken')
         return redirect('/register/')


      user = User.objects.create(
         first_name = first_name,
         last_name = last_name,
         username = username,
        #  password = password
      )
      user.set_password(password)
      user.save()
      messages.info(request, 'Account create successfully')

      return redirect('/register/')

   return render(request, 'register.html')



