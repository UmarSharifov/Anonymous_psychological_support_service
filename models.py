from django.db import models
from datetime import date,datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class customUser(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    role = models.BooleanField()

    def __str__(self):
        role = "Teacher"
        if self.role == False:
            role = "Student"
        return str(role) + " | " + str(self.name) + " | " + str(self.login)


class news_model(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news_photo')
    date = models.DateField(default=date.today())
    def __str__(self):
        return str(self.title)


class advice_model(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news_photo')

    def __str__(self):
        return str(self.title)


class Horoscope_model(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    source = models.CharField(max_length=200)
    month = models.CharField(max_length=150)
    interval_start = models.CharField(max_length=50, blank=True, null=True)
    interval_end = models.CharField(max_length=50, blank=True, null=True)
    element = models.CharField(max_length=75, blank=True, null=True)
    element_description = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return str(self.name)




class Message(models.Model):
    author = models.ForeignKey(User, verbose_name=_("User"),on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(_("Message"))
    pub_date = models.DateTimeField(_('Message date'), default=timezone.now)
    is_readed = models.BooleanField(_('Readed'), default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message


class Room(models.Model):
    Student = models.ForeignKey(User, verbose_name=_("Student"), on_delete=models.SET_NULL, null=True, blank=True, related_name='RoomStudent')
    Specialist = models.ForeignKey(User, verbose_name=_("Specialist"), on_delete=models.SET_NULL, null=True, blank=True, related_name='RoomSpecialist')
    def __str__(self):
        return 'Комната № '+ str(self.id)+' '+str(self.Student.username) + ' ' + str(self.Specialist.first_name)

class Dialog(models.Model):
    Owner = models.CharField(max_length=2)
    RoomDialog = models.ForeignKey(Room, verbose_name=_("Room_dialog"), on_delete=models.SET_NULL, null=True, blank=True)
    MessageDialog = models.CharField(max_length=500)
    pub_date = models.DateTimeField(_('Message date'), default=timezone.now)
# class Room(models.Model):
#     from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='send_room')
#     to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='recived_room')
#     def __str__(self):
#         return str(self.id)
#
# class Message(models.Model):
#     from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='send_message')
#     to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='recived_message')
#     room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
#     message = models.CharField(max_length=500)
#     date = models.DateTimeField(default=datetime.now())
#     def __str__(self):
#         return str(self.from_user) + ' ' + str(self.to_user) + ' in room: ' + str(self.room)
#
# class first_message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     message = models.CharField(max_length=500)
#     status = models.CharField(max_length=100)
#     date = models.DateTimeField(default=datetime.now())
#     def __str__(self):
#         return str(self.user.username) + ' Статус: ' +str(self.status) + ' ' + str(self.message)