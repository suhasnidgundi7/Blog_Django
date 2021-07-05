from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignUpForm, UserEditForm, CreateUserProfilePageForm, UpdateUserProfilePageForm
from blog.models import Profile

# Create your views here.
class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = UpdateUserProfilePageForm
    template_name = "registration/edit_profile_page.html"
    success_url = reverse_lazy('home')

class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = CreateUserProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')
class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context

class PasswordsChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user