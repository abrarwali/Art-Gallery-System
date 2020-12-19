from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout, login , authenticate
from django.contrib.auth.models import User

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'Register.html'
    form_class = UserRegisterForm
    # success_url = '/thanks/'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,context={'form': self.form_class})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # user = User()
        if form.is_valid():
            print("Form Validated.")
            username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            form.save()

            messages.success(request,f'Account Created Successfully for {username}')
        else:
            messages.error(request,'Invalid Credentials! Try Again')
            return render(request,self.template_name,{'form':form})
        return redirect('home')

class UserLoginView(LoginView):
    template_name = 'Login.html'
    form_class = AuthenticationForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'form':self.form_class})
    def post(self,request):
            form = self.form_class(request.POST)
            username=self.request.POST['username']
            password=self.request.POST['password']
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                print(f'{user} is logged in.')
                messages.success(request,'You are now logged in')
                return redirect('home')
            else:
                messages.error(request,'Invalid Credentials')
                return render(request, self.template_name, {'form': form})
class UserLogoutView(LogoutView):
    def get(self,request):
        logout(request)
        messages.success(request, 'You are now logged Out')
        return render(request,'index.html')

