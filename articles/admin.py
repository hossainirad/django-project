from django.contrib import admin
from .models import Articles
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.first_name

    user_info.short_description = 'last name'


class ArticleInAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'author', 'date')

    def user_info(self, obj):
        return obj.first_name


admin.site.register(Articles, ArticleInAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

