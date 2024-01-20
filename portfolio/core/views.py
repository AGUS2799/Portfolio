from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from .models import About, Education, Experience, Portfolio
from .forms import ContactForm
from .forms import ContactForm
from django.urls import reverse

# Create your views here.
class HomeView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all()
        context['education'] = Education.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        context['form'] = ContactForm
        return context

class ContactView(TemplateView):
    template_name = "core/contact_message.html"

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

        mail = EmailMessage(
            f"Portfolio new message.\n\nSubject:{subject}\n\n",
            f"From {name} <{email}>\n Message:{message}",
            "portfolio@portfolio.com",
            ["chinop2799@gmail.com"],
            reply_to=[email]

        )
        try:
            email.send()
            return redirect(reverse('home:contact-m')+"?ok")
        
        except:
            return redirect(reverse('home:contact-m')+"?fail")
        
    return redirect(reverse('home:home'))
