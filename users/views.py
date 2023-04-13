from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)

class MyLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))