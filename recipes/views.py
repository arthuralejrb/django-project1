from django.shortcuts import render

# Create your views here.


def test_view(request):
    """"""
    return render(request, 'recipes/test.html', context={
        'name': 'balma',
    })
