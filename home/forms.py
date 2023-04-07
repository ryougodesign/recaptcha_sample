from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

# ReCaptchaログインフォーム
class ReCaptchaLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["placeholder"] = "ユーザーID"
        self.fields["password"].widget.attrs["placeholder"] = "パスワード"

    recaptcha = ReCaptchaField(label="", widget=ReCaptchaV3())