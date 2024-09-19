from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.



def sign_up_by_html(request):
    users = [
        {'username': 'user1', 'password': 'qwerty123', 'age': 18},
        {'username': 'user2', 'password': 'qwerty124', 'age': 20},
        {'username': 'user3', 'password': 'qwerty125', 'age': 22},
    ]

    if request.method == 'POST':
        info = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['password_error'] = 'Пароли не совпадают'

        if int(age) < 18:
            info['age_error'] = 'Вы должны быть старше 18'

        for user in users:
            if user['username'] == username:
                info['user_exists_error'] = 'Пользователь уже существует'

        if info:
            return render(request, 'registration_page.html', {'info': info})
        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    users = [
        {'username': 'user1', 'password': 'qwerty123', 'age': 18},
        {'username': 'user2', 'password': 'qwerty124', 'age': 20},
        {'username': 'user3', 'password': 'qwerty125', 'age': 22},
    ]
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')
            if password != repeat_password:
                info['password_error'] = 'Пароли не совпадают'

            for user in users:
                if user['username'] == username:
                    info['user_exists_error'] = 'Пользователь уже существует'

            if info:
                return render(request, 'registration_page.html', {'form': form, 'info': info})
            return HttpResponse(f'Приветствуем, {username}!')

        if form.errors.as_data()['age']:
            info['age_error'] = form.errors.as_data()['age'][0].message
            return render(request, 'registration_page.html', {'form': form, 'info': info})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})