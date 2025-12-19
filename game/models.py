from django.db import models

class Question(models.Model):
    story = models.TextField(help_text="The mission description for Robo-X")
    code = models.TextField(help_text="The C++ code containing the bug")
    hint = models.TextField(help_text="The hint shown when the user is wrong")
    order = models.IntegerField(default=0, help_text="Order in which mission appears")

    def __str__(self):
        return f"Mission: {self.story[:30]}..."

class Option(models.Model):
    # Fixed the 'on_delete' syntax below
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text