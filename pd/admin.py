from django.contrib import admin
from pd.models import Category, Post, PenInPost

class PenInPostAdmin(admin.ModelAdmin):
    search_fields = ('pen_name',)

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PenInPost, PenInPostAdmin)
