from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import SubscribeForm
from django.core.mail import EmailMessage


def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Code Band'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')

            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                reply_to=[settings.EMAIL_HOST_USER],
                headers={'Message-ID': 'foo'},
            )

            email.attach_file(r'C:\relatorio1.pdf')

            email.send()

            messages.success(request, 'Success!')
            return redirect('home')
    return render(request, 'subscriptions/home.html', {'form': form})
