from django.contrib import admin
from blog.models import Post,Category,comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class Postadmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_views','status','login_require','published_date','created_date')
    list_filter = ('status','author',)
    ordering = ('-created_date',)
    search_fields = ['title','content'],
    summernote_fields = ('content',)
class commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved',)
    ordering = ('-created_date',)
    search_fields = ['name' ,'post']


admin.site.register(comment,commentadmin)
admin.site.register(Category)
admin.site.register(Post,Postadmin)