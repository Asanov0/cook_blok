from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .import models


class RecipeInLine(admin.StackedInline):
    model = models.Recipe
    extra = 1



@admin.register(models.Post)
class  PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'cteate_at', 'id']
    inlines = [RecipeInLine]



@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'serves', 'prep_time', 'cook_time', 'ingredients', 'directions', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Coments)
