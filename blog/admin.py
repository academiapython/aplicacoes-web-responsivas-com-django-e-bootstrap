from django.contrib import admin
from .models import Post, Topico
# Register your models here.

class TopicoInline(admin.TabularInline):
    model = Topico


class PostAdmin(admin.ModelAdmin):
    inlines = [
        TopicoInline
    ]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Topico)