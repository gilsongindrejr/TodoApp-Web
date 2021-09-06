from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'date', '_author', 'is_completed')
    list_filter = ('is_completed',)
    exclude = ['author',]

    def _author(self, instance):
        return f'{instance.author.get_full_name()}'

    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
