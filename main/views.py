from django.core.mail import BadHeaderError, send_mail
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.views import generic
from .forms import ContactForm
from .models import Freelancer
from django.conf import settings
from django.urls import reverse

# Create your views here.
class FreelanceView(generic.ListView):
    model = Freelancer
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FreelanceView, self).get_context_data(*args, **kwargs)
        context['freelancer_list'] = Freelancer.objects.order_by('-id') #maybe you have to put a "," here but I'm not sure
        context['form'] = ContactForm
        return context


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():

            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            from_email = request.POST.get('email')

            template = get_template('main/contact_form.txt')

            context = {
                'name' : request.POST.get('name'),
                'phone' : request.POST.get('phone'),
                'message' : request.POST.get('message'),
                'from_email' : request.POST.get('email'),
            }
            content = template.render(context)

            email = EmailMessage(
                'New contact for email',
                content,
                from_email,
                [settings.EMAIL_HOST_USER],
                headers = {'Reply to': from_email}
            )

            email.send()
            return reverse('main:index')
