from django.contrib import admin

from .models import Choice, Question, Props, Photos

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']

class PhotoPlaces(admin.TabularInline):
	model = Photos
	extra = 3

class PropsAdmin(admin.ModelAdmin):
	inlines = [PhotoPlaces]
	list_display = ('props_title', 'pub_date')
    



admin.site.register(Question, QuestionAdmin)
admin.site.register(Props, PropsAdmin)

