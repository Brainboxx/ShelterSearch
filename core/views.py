from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.models import User
from properties.models import Property
from agents.models import Agents
from blog.models import BlogPost
# Create your views here.


def home(request):
    latest_properties = Property.objects.all()[:9]
    best_agents = Agents.objects.all()[:3]
    latest_news = BlogPost.objects.all()[:3]
    context = {
        'latest_properties': latest_properties,
        'best_agents': best_agents,
        'latest_news': latest_news
    }
    return render(request, 'core/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject=f'New message from {name}',
            message=message,
            from_email=email,
            recipient_list=['chineduudochuku66@gmail.com'],
            fail_silently=False
        )
        return render(request, 'core/success.html')
    return render(request, 'core/contact.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'core/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or not password:
            # Display an error message
            error_message = 'Please provide a username and password.'
            return render(request, 'register.html', {'error_message': error_message})
        if password2 != password:
            error_message = 'Passwords does not match'
            return render(request, 'core/register.html', {'error_message': error_message})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')


class AboutView(View):
    agents = Agents.objects.all()[:3]

    def get(self, request):
        return render(request, 'core/about.html', {'agents': self.agents})

    def post(self, request):
        return redirect('core/about.html', {'agents': self.agents})
