from django.shortcuts import render

# Create your views here.


def test_view(request):
    """"""
    return render(request, 'recipes/pages/home.html', context={
        'name': 'balma',
    })
