from django.contrib import admin
from .models import Chapter, Quiz, Question, UserAnswer
from django.contrib.admin.sites import AlreadyRegistered
from .models import Badge, UserProfile, Achievement, UserAchievement


# Safely register models
for model in [Chapter, Quiz, Question, UserAnswer]:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

# Badge Admin
@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')  # Columns you can see
    search_fields = ('name',)

# User Profile Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'xp')
    filter_horizontal = ('badges',)  # Allows adding/removing badges easily

# Optional: Achievements
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'xp_required', 'chapter')

# Optional: UserAchievement
@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'badge', 'earned_at')