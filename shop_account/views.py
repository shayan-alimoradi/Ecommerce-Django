# Standard-library import
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse, reverse_lazy
from django.views import View

# Local import
from shop_order.models import OrderItem
from .tokens import account_activation_token
from .forms import (
    SignInForm,
    SignUpForm,
    ProfileForm,
)


class SignIn(View):
    template_name = 'account/sign_in.html'
    form_class = SignInForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            human = True
            data = form.cleaned_data
            remember = form.cleaned_data['remember']
            user = authenticate(request, email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(68400)
                return redirect('/')
            else:
                form.add_error('email', 'Email or Password is incorrect')
        else:
            messages.error(request, 'invalid Recaptcha', 'danger')
        return render(request, self.template_name, {'form': form})


class SignUp(View):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(email=data['email'], username=data['username'],
            password=data['password'])
            user.is_active = False
            user.save()
            domain = get_current_site(request).domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            url = reverse('account:activate', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            link = 'http://' + domain + url
            email = EmailMessage(
                'Activation link for registeration',
                link,
                'shayan.aimoradii@gmail.com',
                [data['email']]
            )
            email.send(fail_silently=False)
            messages.info(request, 'Please confirm your email address to complete the registration')
            return redirect('account:sign-in')
        return render(request, 'account/sign_up.html', {'form': form})


class ActiveEmail(View):
    def get(self, request, uidb64, token):
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=user_id)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('account:sign-in')
        else:
            messages.error(request, 'Activation link is invalid!', 'danger')


class Logout(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'logged out successfully')
        return redirect('/')


class UserProfile(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'account/profile.html'
    login_url = 'account:sign-in'
    model = User
    form_class = ProfileForm
    success_message = 'Profile Updated Successfully'
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class ChangePassword(LoginRequiredMixin, View):
    login_url = 'account:sign-in'
    template_name = 'account/change_pass.html'

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        url = request.META.get('HTTP_REFERER')
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Successfully Changed', 'success')
            return redirect(url)
        return render(request, self.template_name, {'form': form})


class UserPanel(LoginRequiredMixin, View):
    template_name = 'account/user_panel.html'
    login_url = 'account:sign-in'

    def get(self, request):
        return render(request, self.template_name)


class ResetPassword(auth_views.PasswordResetView):
    template_name = 'account/reset.html'
    email_template_name = 'account/link.html'
    success_url = reverse_lazy('account:done')


class DonePassword(auth_views.PasswordResetDoneView):
    template_name = 'account/done.html'


class ConfirmPassword(auth_views.PasswordResetConfirmView):
    template_name = 'account/confirm.html'
    success_url = reverse_lazy('account:complete')


class CompeletePassword(auth_views.PasswordResetCompleteView):
    template_name = 'account/complete.html'


def history(request):
    items = OrderItem.objects.filter(user_id=request.user.id)
    return render(request, 'account/history.html', {'items': items})
