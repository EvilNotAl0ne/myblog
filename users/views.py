from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from myblog.settings import LOGIN_REDIRECT_URL
from .forms import UserRegistrationFrom


def register(request):
    # Если ножали кнопку регистрации (это метод POST)
    if request.method == 'POST':
        # Создаем объект формы с данными из запроса
        user_form = UserRegistrationFrom(request.POST)
        # Валидация формы (правильность введение данных)
        if user_form.is_valid():
            # Создание объекта с полями формы (без сохранения в БД)
            new_user = user_form.save(commit=False)
            # Хэширование пароля пользователя
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохранения пользователя в БД
            new_user.save()
            context = {'title': 'Успешная регистрация', 'new_user': new_user}
            return render(request, template_name='users/register_done.html', context=context)

    # Метод GET - отрисовка страницы регистрации
    user_form = UserRegistrationFrom()
    context = {'title': 'Регистрация', 'register_form': user_form}
    return render(request, template_name='users/register.html', context=context)

def log_in(request):
    #Создания формыаутификации
    form = AuthenticationForm(request, request.POST)
    #Проверка формы
    if form.is_valid():
        #Получение логина и пароля из формы
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #Аутификация пользователя (проверка наличия пользователя и пароля)
        user = authenticate(username=username, password=password)
        if user:
            #
            login(request, user)
            #
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)


def log_out(request):
    logout(request)
    return redirect('blog:index')


def user_detail(request, pk):
    pass

def change_password(request):
    pass