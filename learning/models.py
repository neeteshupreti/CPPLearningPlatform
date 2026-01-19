from django.db import models
from django.contrib.auth.models import User


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField()
    is_locked = models.BooleanField(default=True)
    image = models.ImageField(upload_to='chapter_images/')

    def __str__(self):
        return self.title


class Quiz(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name='quizzes'
    )
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.chapter.title} - {self.title}"


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)

    correct_option = models.IntegerField(
        choices=[
            (1, 'Option 1'),
            (2, 'Option 2'),
            (3, 'Option 3'),
            (4, 'Option 4'),
        ]
    )

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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="learning_profile")
    xp = models.IntegerField(default=0)
    # other fields

    def __str__(self):
        return self.user.username

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    xp_required = models.IntegerField()

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"
