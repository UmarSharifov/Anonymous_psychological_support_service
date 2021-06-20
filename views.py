from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from psyco.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from psyco.forms import *
from django.views.generic import View
# Create your views here.
from django.urls import reverse
from django.contrib.auth.models import Group

def registration(request):
    if request.method == 'POST':
        created = Group.objects.get(name='Student')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user = User.objects.get(username=username)
            user.groups.add(created)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def index(request):
    News = news_model.objects.all()
    Horoscope = Horoscope_model.objects.all()
    user_role=""
    l = list()
    for g in request.user.groups.all():
        l.append(g.name)
    try:
        if l[0] == 'Specialist':
            user_role = 'Specialist'
    except:
        pass
    ctx = {
        'news': News,
        'horoscope': Horoscope,
        'user_role': user_role,
    }
    return render(request, 'index.html', context=ctx)

def horoscope(request, horo):
    Horoscope = Horoscope_model.objects.all()
    current_horo = Horoscope_model.objects.get(name=horo)
    ctx = {
        'horoscope': Horoscope,
        'current_horo': current_horo,

    }
    return render(request, 'horoscope.html', context=ctx)

def news(request, news_id):
    current_news = news_model.objects.get(id = news_id)
    all_newses = news_model.objects.all()
    ctx = {
        'current_news': current_news,
        'all_newses': all_newses
    }
    return render(request, 'news.html', context=ctx)


def message(request):
    if Message.objects.filter(author=request.user).exists():
        if Room.objects.filter(Student=request.user).exists():
            student_room = Room.objects.get(Student=request.user)
            return redirect('dialog', room_id=student_room.id)
    message = request.GET.get('message')
    if message != '' and message is not None:
        _message = Message(author=request.user, message=message)
        _message.save()
    message_history = Message.objects.filter(author=request.user)
    return render(request, 'messages.html', context={'messages': message_history,})

def message_list(request):
    if User.is_authenticated:
        l = list()
        list_of_users = list()
        for g in request.user.groups.all():
            l.append(g.name)
        try:
            if l[0] == 'Specialist':
                list_of_students = User.objects.filter(groups__name='Student')
                for i in list_of_students:
                    if Room.objects.filter(Student=i).exists():
                        pass
                    else:
                        list_of_users.append(i)
                ctx = {
                    'users': list_of_users,
                }
                return render(request, 'message_list.html', context=ctx)
            else:
                return redirect('login')
        except:
            return redirect('login')


def create_room(request, user_id):
    if Room.objects.filter(Student=User.objects.get(id=user_id)).exists():
        current_room = Room.objects.get(Student=User.objects.get(id=user_id))
        if current_room.Specialist == request.user:
            return redirect('dialog', room_id=current_room.id)
        return redirect('login') #сюда добавим удевомление, типо другой специалист уже работает с этим студентом
    else:
        temp_Room = Room(Student=User.objects.get(id=user_id), Specialist=request.user)
        temp_Room.save()
        student_messages = Message.objects.filter(author=User.objects.get(id=user_id))
        for i in student_messages:
            temp_Dialog = Dialog(Owner='S', RoomDialog=temp_Room,MessageDialog=i.message, pub_date=i.pub_date)
            temp_Dialog.save()
        return redirect('dialog', room_id=temp_Room.id)

def dialog(request, room_id):
    current_room = Room.objects.get(id=room_id)
    message = request.GET.get('message')
    if message != '' and message is not None:
        l = list()
        for g in request.user.groups.all():
            l.append(g.name)
        try:
            if l[0] == 'Specialist':
                temp = Dialog(Owner='T', RoomDialog=current_room, MessageDialog=message)
                temp.save()
            else:
                temp = Dialog(Owner='S', RoomDialog=current_room, MessageDialog=message)
                temp.save()
            return redirect('dialog', room_id=room_id)
        except:
            pass
    current_dialog = Dialog.objects.filter(RoomDialog=current_room)
    return render(request, 'dialog.html', context={
        'dialog':current_dialog,
    })

def specialist_conversations(request):
    l = list()
    for g in request.user.groups.all():
        l.append(g.name)
        if l[0] == 'Specialist':
            room_list = Room.objects.filter(Specialist=request.user)
            return render(request, 'conversations.html', context={
                'room_list': room_list,
            })
        else:
            return redirect('login')