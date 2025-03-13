from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from .models import Module
import json



def index(request: HttpRequest):
    
    modules = Module.objects.all()  # Получаем все модули из базы данных
    if request.method == "POST":
        print('index')
        selected_modules = request.POST.getlist('selected_modules[]')
        mode = request.POST.get('test_type')
        
        if mode == 'edit':
            module=Module.objects.filter(title=selected_modules[0])
            print('редактирование модуля:', module)
            redirect('edit_module',)
        elif mode == 'cards':
            print('просмотр карточек')
        elif mode == 'test':
            print('тестирование')

    
    return render(request, "base/index.html", {"modules": modules})

def delete_module(request):
    print('редактир')
    if request.method == "POST":
        
        id = request.POST['del_id']
        Module.objects.filter(id=id).delete()
        return redirect('index')

def create_module(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = json.loads(request.POST.get("words"))
        Module.objects.create(title=title, cards=description)
        return redirect("index")

    return render(request, "base/edit_module.html")

def edit_module(request: HttpRequest):
    id = request.POST['edit_id']
    module=Module.objects.get(id=id)
    
    return render(request, "base/edit_module.html",context={'module':module})

def view_cards(request: HttpRequest):
    words={}
    for id in request.POST.getlist('selected_modules'):
        module=Module.objects.get(id=id)
        words.update(module.cards)
    
    return render(request, "base/card_mode.html",context={'words':words})

def start_test(request: HttpRequest):
    words={}
    for id in request.POST.getlist('selected_modules'):
        module=Module.objects.get(id=id)
        words.update(module.cards)
    
    return render(request, "base/test_mode.html",context={'words':words})
        
    
