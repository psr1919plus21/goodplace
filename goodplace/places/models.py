from django.forms.models import modelform_factory
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Props(models.Model):
    props_title = models.CharField(max_length=200)
    props_city = models.CharField(default="city", max_length=200)
    props_street = models.CharField(default="street", max_length=200)
    props_home = models.IntegerField(default=1)
    props_place = models.IntegerField(default=1)
    props_sleepplace = models.IntegerField(default=1)
    props_rating = models.FloatField(default=0)
    props_state = models.BooleanField(default=False)
    props_price = models.IntegerField(default=0)
    props_postfix = models.CharField(default="mes", max_length=20)
    props_authorname = models.CharField(default="ivan", max_length=20)
    props_authorlastname = models.CharField(default="ivanov", max_length=20)
    props_authorpatronymic = models.CharField(default="ivanovich", max_length=20)
    props_authorphone = models.IntegerField(default=0)
    props_howater = models.BooleanField(default=False)
    props_internet = models.BooleanField(default=False)
    props_washmachine = models.BooleanField(default=False)
    props_furniture = models.BooleanField(default=False)
    props_linens = models.BooleanField(default=False)
    props_utensils = models.BooleanField(default=False)
    props_microwave = models.BooleanField(default=False)
    props_kids = models.BooleanField(default=False)
    props_pets = models.BooleanField(default=False)
    props_addinfo = models.TextField(default="text")
    pub_date = models.DateTimeField('date published')

class Photos(models.Model):
	photoprop = models.ForeignKey(Props)
	props_photourl = models.CharField(default="/static/img/photoplace/default.jpg", max_length=200)

PropsForm = modelform_factory(Props, fields=('props_title', 'props_city', 'props_street', 'props_home', 'props_place', 'props_sleepplace', 'props_rating', 'props_state', 'props_price', 'props_postfix', 'props_authorname', 'props_authorlastname', 'props_authorpatronymic', 'props_authorphone', 'props_howater', 'props_internet', 'props_washmachine', 'props_furniture', 'props_linens', 'props_utensils', 'props_microwave', 'props_kids', 'props_pets', 'props_addinfo', 'pub_date'))

# class PropsForm(ModelForm):
#     class Meta:
#         model = Props
#         fields = ['props_title', 'props_city', 'props_street', 'props_home', 'props_place', 'props_sleepplace', 'props_rating', 'props_state', 'props_price', 'props_postfix', 'props_authorname', 'props_authorlastname', 'props_authorpatronymic', 'props_authorphone', 'props_howater', 'props_internet', 'props_washmachine', 'props_furniture', 'props_linens', 'props_utensils', 'props_microwave', 'props_kids', 'props_pets', 'props_addinfo', 'pub_date']
