from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale
from django.contrib.auth import get_user_model

# User = get_user_model()

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_admin', 'is_producer')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_admin', 'is_producer')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'is_producer', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_admin', 'is_producer', 'groups', 'user_permissions')}
#         ),
#     )
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#     ordering = ('username',)

# admin.site.register(CustomUser, UserAdmin)
admin.site.register(Producer)

# admin.site.register(CustomUser, UserAdmin)

# admin.site.register(Producer, UserAdmin)
admin.site.register(Product)
admin.site.register(Province)
admin.site.register(Supplier)
admin.site.register(CompanyClient)
admin.site.register(PersonalClient)
admin.site.register(Purchase)
admin.site.register(Sale)
