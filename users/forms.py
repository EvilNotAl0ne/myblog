from django import forms
from django.contrib.auth import get_user_model

#Получения тякущей модели пользователя
User = get_user_model()

#Создание формы регистрации пользователя
class UserRegistrationFrom(forms.ModelForm):
    #Создание дополнительного поля пороля для повторного ввода при регистрации
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совподают!')
        return cleaned_data['password2']

    class Meta:
        model = User
        fields = ('username', 'password',
                  'first_name', 'last_name', 'email',
                  'phone', 'citi')