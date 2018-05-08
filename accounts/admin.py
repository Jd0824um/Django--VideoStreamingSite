from django.contrib import admin
from accounts.models import UserProfile

# Adds columns to the user profiles in the admin site
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'phone', 'description', 'city', 'state', 'created_date' )

    # Sorts by created date
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-created_date', 'user')
        return queryset


admin.site.register(UserProfile, UserProfileAdmin)
