from django.contrib import admin
from flashers.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'created']}),
        ('Flash Card Info', {'fields': ['category', 'question', 'answer']})
    ]
    list_display = ('category', 'created', 'user')
    list_filter = ['category']
    search_fields = ['question', 'answer']


admin.site.register(Post, PostAdmin)
