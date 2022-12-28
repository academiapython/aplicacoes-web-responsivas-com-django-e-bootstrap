from django.contrib import admin
from .models import Post, Topico, Tag, Comentario, Situacao, PostSituacao, Assunto
# Register your models here.

class TopicoInline(admin.TabularInline):
    model = Topico
    extra = 1


class TagInline(admin.TabularInline):
    model = Tag.posts.through
    extra = 1


class AssuntoInline(admin.TabularInline):
    model = Assunto.posts.through
    extra = 1


class SituacaoInline(admin.TabularInline):
    model = PostSituacao
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        TopicoInline,
        TagInline,
        AssuntoInline,
        SituacaoInline,
    ]
    class Meta:
        model = Post


class SituacaoAdmin(admin.ModelAdmin):
    inlines = [
        SituacaoInline
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Topico)
admin.site.register(Tag)
admin.site.register(Comentario)
admin.site.register(Situacao, SituacaoAdmin)
admin.site.register(PostSituacao)
admin.site.register(Assunto)
