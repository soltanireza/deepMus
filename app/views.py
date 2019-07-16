from django.shortcuts import render, redirect
from predict import generate
from .models import Tech, Content, Sticker


def index(request):
    techs = Tech.objects.all()[:3]
    contents = Content.objects.all()[:2]
    stickers = Sticker.objects.all()[:9]
    context = {
        'techs': techs,
        'contents': contents,
        'stickers': stickers,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def predict(request):
    generate()
    return redirect('predicted')


def predicted(request):
    return render(request, 'predicted.html')


def question(request):
    return render(request, 'question.html')


def question(request):
    return render(request, 'question.html')


def samples(request):
    return render(request, 'samples.html')


