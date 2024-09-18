from django.shortcuts import render


# Create your views here.
def t4_main_page(request):
    return render(request, 't4_platform.html')


def t4_games_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'games': games}
    return render(request, 't4_games.html', context=context)


def t4_cart_page(request):
    return render(request, 't4_cart.html')