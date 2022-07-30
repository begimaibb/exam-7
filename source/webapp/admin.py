from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_display_links = ['question']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question', 'created_at']
    readonly_fields = ['created_at']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text', 'poll']
    list_display_links = ['choice_text']
    list_filter = ['choice_text']
    search_fields = ['choice_text']
    fields = ['choice_text', "poll"]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'choice', 'created_at']
    list_display_links = ['poll']
    list_filter = ['poll']
    search_fields = ['poll']
    fields = ["choice"]
    readonly_fields = ["poll", "created_at"]


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
