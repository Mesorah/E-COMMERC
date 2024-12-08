from django.contrib.auth.views import LoginView, LogoutView
from authors.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class AuthorRegisterView(CreateView):
    template_name = "authors/pages/base_page.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('authors:login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Register',
            'msg': 'Registre-se'
        })

        return context


class AuthorLoginView(LoginView):
    template_name = "authors/pages/base_page.html"
    # redirect_authenticated_user = True
    success_url = reverse_lazy('home:index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Login',
            'msg': 'Logue-se'
        })

        return context

    def get_redirect_url(self):
        return self.success_url


class AuthorLogoutView(LogoutView):
    template_name = "authors/pages/base_page.html"
    success_url = reverse_lazy('authors:login')

    def get_redirect_url(self):
        return self.success_url
