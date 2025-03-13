from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from .models import Module
import json



def index(request: HttpRequest):
    modules = Module.objects.all()  # Получаем все модули из базы данных
    if request.method == "POST":
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
     if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        Module.objects.filter(title=title).delete()
        return JsonResponse({"success": True})

def create_module(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = json.loads(request.POST.get("words"))
        Module.objects.create(title=title, cards=description)
        return redirect("index")

    return render(request, "base/create_module.html")

def edit_module(request: HttpRequest):
    pass

def view_cards(request: HttpRequest):
    pass

def start_test(request: HttpRequest):
    pass
        
    
