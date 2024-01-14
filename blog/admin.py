from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from . import models
from .models import Tag,Post,Category
from django.contrib.auth import get_user_model
from import_export.admin import ImportExportMixin,ExportActionModelAdmin
from import_export import resources, fields,widgets

User = get_user_model()

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1

class PostResource(resources.ModelResource):
 
    post_tags =  fields.Field(attribute='tags', column_name='Теги',widget=widgets.ManyToManyWidget(Tag, field='name', separator=' '))
    author = fields.Field(
       attribute="author",
       column_name="Автор",
       widget=widgets.ForeignKeyWidget(User, "username")
   )
    category = fields.Field(
       attribute="category",
       column_name="Категория",
       widget=widgets.ForeignKeyWidget(Category, "name")
   )
    class Meta:
        model = Post
    
        fields = ("id","title","text","author","category","post_tags","image","create_at",)
        
        
    
    def get_export_headers(self):
        headers = []
        for field in self.get_fields():
            model_fields = self.Meta.model._meta.get_fields()
            header = next((x.verbose_name for x in model_fields if x.name == field.column_name), field.column_name)
            headers.append(header)
        return headers

@admin.register(models.Post)
class PostAdmin(ImportExportMixin,ExportActionModelAdmin,SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]
    prepopulated_fields = {'slug': ('title', 'category'), }
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True
    resource_class = PostResource

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "post"]


@admin.register(models.Comment)
class CommentAdmin(SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
