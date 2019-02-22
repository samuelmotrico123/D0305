from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Samuel'
    conhecimentos = ['HTML','CSS','JavaScript', 'Python','Django','Git']
    return render(request,'index.html',{'conhecimentos': conhecimentos, 'nome': nome})