from django import form 


class LoginForm(forms.Form):
    login_email = forms.CharField(label='Your name', max_length=100)
    login_password = forms.CharField(label='password', max_length=200)
    
