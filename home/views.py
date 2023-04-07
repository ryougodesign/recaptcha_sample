from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .forms import ReCaptchaLoginForm

# ログインページ
class LoginPage(LoginView):

    # レンダリングに使用するHTMLパス
    template_name = "login.html"

    # ログインに使用するフォーム
    form_class = ReCaptchaLoginForm

    # ログイン完了後に遷移するURL
    success_url = 'home'

# ログイン完了ページ
class HomePage(TemplateView):
    template_name = "home.html"