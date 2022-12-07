from django.http import HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect, HttpResponseNotFound, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Главная страница")
def Posts(request, id=2):
    return HttpResponse(f"Посты {id}")
def popular(request,id=2):
    return HttpResponse(f"Популярные посты {id}")
def lastPosts(request, id=2):
    return HttpResponse(f"Последние опубликованные посты {id}")
def allPosts(request, id=2):
    return HttpResponse(f"Весь набор постов {id}")
def comments(request,id=2):
    return HttpResponse(f"Комментарии: {id}")
def questions(request,id=2):
    return HttpResponse(f"Лайки: {id}")
def user(request):
    log = request.GET.get('log')
    passwd = request.GET.get("passwd")
    return HttpResponse(f"""
    <p>Логин:{log} <p>
    <p>Пароль: {passwd} <p>
    """)
def about(request):
    return HttpResponse("About")
def contacts(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")
def error(request):
    return HttpResponseNotFound("Загрузка страницы была завершена ошибкой")
def inicilization(request, access):
    if access == 'admin':
        return HttpResponse('Доступ предоставлен')
    else:
        return HttpResponse('Доступ заблокирован')
def json(request):
    log = request.GET.get('log')
    passwd = request.GET.get("passwd")
    person = {'log': log,'passwd': passwd,}
    return JsonResponse(person)
def set(request):
    username = request.GET.get('username', 'undefined')

    response = HttpResponse(f'Приветствую Вас, {username}')

    response.set_cookie('username', username)
    return response
def get(request):
    username = request.COOKIES['username']
    return HttpResponse(f'Приветствую Вас, {username}')
    