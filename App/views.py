from django.shortcuts import render


def Home(request):
    return render(request, 'base.html', {})


def Map(request):
    return render(request, 'map.html', {'title': 'Map'})


def Card(request):
    return render(request, 'cardflip.html', {'title': 'Card'})
