from django.contrib import admin
from .models import Topic, Challenge, AboutMe, Hobby, Skill

# Admin for Topics + Challenges
class ChallengeInline(admin.TabularInline):
    model = Challenge
    extra = 1

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [ChallengeInline]
    list_display = ('title', 'order')

# Admin for AboutMe + Hobbies + Skills
class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    inlines = [HobbyInline, SkillInline]
    list_display = ('name',)
