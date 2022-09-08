from django.contrib import admin
from .models import Questao, Alternativa

# Register your models here.
class AlternativaInline(admin.TabularInline):
    model = Alternativa

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AlternativaInline
    ]
    class Meta:
        model = Questao

admin.site.register(Questao, QuestionAdmin)
admin.site.register(Alternativa)
