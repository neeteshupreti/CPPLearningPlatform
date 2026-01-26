from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# ----------------------------
# CHAPTER
# ----------------------------
class Chapter(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField()
    is_locked = models.BooleanField(default=True)
    image = models.ImageField(upload_to='chapter_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# ----------------------------
# QUIZ
# ----------------------------
class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.chapter.title} - {self.title}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=[(1,'Option 1'),(2,'Option 2'),(3,'Option 3'),(4,'Option 4')])

    def __str__(self):
        return self.question_text

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.IntegerField()
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.id}"

# ----------------------------
# BADGES & ACHIEVEMENTS
# ----------------------------
class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='badges/', blank=True, null=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    xp_required = models.IntegerField(blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, null=True, blank=True)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, null=True, blank=True)
    earned_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'achievement', 'badge')

    def __str__(self):
        if self.achievement:
            return f"{self.user.username} - {self.achievement.name}"
        elif self.badge:
            return f"{self.user.username} - {self.badge.name}"
        return self.user.username

# ----------------------------
# USER PROFILE
# ----------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="learning_profile")
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    badges = models.ManyToManyField(Badge, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Level {self.level}"


# ----------------------------
# USER CHAPTER COMPLETION
# ----------------------------
class UserChapterCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="completed_chapters")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'chapter')

    def __str__(self):
        return f"{self.user.username} - {self.chapter.title}"

# ----------------------------
# SIGNALS: Automatically create UserProfile for new users
# ----------------------------
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'learning_profile'):
        instance.learning_profile.save()
