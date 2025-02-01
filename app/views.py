from django.shortcuts import render, redirect
from .models import Home, About, Profile, Category, Skills, Portfolio, ContactFormLog

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    try:
        home = Home.objects.latest('updated')
    except ObjectDoesNotExist:
        home = None  

    # print("Home Object:", home)  # For Debug

    about = About.objects.order_by('-updated').first()
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()

    context = {
        "home": home,
        "about": about,
        "categories": categories,
        "portfolios": portfolios,
    }

    return render(request, 'index.html', context)

def contact_form(request):
    # print(f"request.POST : {request.POST}")

    if request.method == 'POST':

        # name = request.POST['name']   # Raises KeyError if 'name' is missing

        name = request.POST.get('name')  # Returns None if 'name' is missing

        email = request.POST.get('user_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # print(f"name : {name}")
        # print(f"request.POST : {request.POST}")

        context = {
            "name" : name,
            "email" : email,
            "subject" : subject,
            "message" : message
        }

        html_content = render_to_string('email.html', context)

        is_success = False
        is_error = False
        error_message = ""

        try:
            send_mail (
            subject = subject, #it will appears as email title

            # message = f"{name} - {email} - {message}", #it will appears as email body
            message = None, #it will be email body, but this is set to 'None', bcoz defaultly this variable should be present for send_mail func()
            html_message = html_content,  # In above, we defined this variable

            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.EMAIL_HOST_USER],
            fail_silently = False
        )
        except Exception as e:

            is_error = True
            error_message = str(e)

            # print(f"email is failed")  #THIS O/P WILL SHOW IN CMD (TERMINAL)
            messages.error(request, "There's an error occured, retry to send the email..!!")

        else:
            is_success = True
            
            # print(f"Email has been send out")
            messages.success(request, "Email has been sent successfully")

        ContactFormLog.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
            action_time = timezone.now(),
            is_error = is_error,
            is_success = is_success,
            error_message = error_message,
        )

    return redirect('index')