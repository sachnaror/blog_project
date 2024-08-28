from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import BlogPost, CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'mobile')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email', 'mobile', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'mobile', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'mobile')
    ordering = ('email',)

# The `BlogPostAdmin` class is customizing the admin interface for the `BlogPost` model in Django.

# Here's what each attribute is doing:

# 1. `list_display`: This attribute specifies the fields that should be displayed in the list view of the admin interface. In this case, it displays the `heading`, `author`, and `timestamp` of each blog post.
# 2. `list_filter`: This attribute specifies the fields by which the list of blog posts can be filtered. In this case, it allows filtering by `author` and `timestamp`.
# 3. `search_fields`: This attribute specifies the fields by which the list of blog posts can be searched. In this case, it allows searching by `heading` and `content`.
# 4. `get_queryset`: This method customizes the queryset of blog posts displayed in the admin interface. If the user is a superuser, all blog posts are displayed. Otherwise, only the blog posts authored by the user are displayed.
# 5. `has_change_permission`: This method customizes the permission to change a blog post. If the user is a superuser or the author of the blog post, they have permission to change it. Otherwise, they do not.
# 6. `has_delete_permission`: This method customizes the permission to delete a blog post. If the user is a superuser or the author of the blog post, they have permission to delete it. Otherwise, they do not.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('heading', 'author', 'timestamp')
    list_filter = ('author', 'timestamp')
    search_fields = ('heading', 'content')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj or request.user.is_superuser:
            return True
        return obj.author == request.user

    def has_delete_permission(self, request, obj=None):
        if not obj or request.user.is_superuser:
            return True
        return obj.author == request.user

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
