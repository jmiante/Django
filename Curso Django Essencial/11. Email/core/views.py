from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm


def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Code Band'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('home')
    return render(request, 'subscriptions/home.html', {'form': form})