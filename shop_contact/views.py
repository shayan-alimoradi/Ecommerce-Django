from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        content = request.POST['content']
        body = email + '\n' + full_name + '\n' + subject + '\n' + content
        form = EmailMessage(
            'Contact Page',
            body,
            'test',
            ('shayan.aimoradii@gmail.com',)
        )
        messages.success(request, 'Thanks for your viewpoint', 'primary')
        form.send(fail_silently=False)
    return render(request, 'contact/contact.html')