from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView, TemplateView

from apps.intern.forms import UserCreateForm, LoginForm


# Create your views here.



class Sign(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        # Hash password using make_password() function
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)




class Login(View):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = 'home'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()  # Get the custom user model
        user = User.objects.filter(email=email).first()
        if user is not None:
            authenticated_user = authenticate(request, email=user.email, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                context = {
                    'user_email': authenticated_user.email,
                    'user_first_name': authenticated_user.first_name,
                    'user_last_name': authenticated_user.last_name,
                }
                return render(request, 'home.html', context)
            else:
                messages.error(request, 'Incorrect password. Please try again.')
        else:
            messages.error(request, 'User with this email does not exist.')

        return render(request, self.template_name, {'form': self.form_class()})

class HomeView(TemplateView):
    template_name = 'home.html'


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('user_login'))


