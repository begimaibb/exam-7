from django.db import models

# Create your models here.
from django.urls import reverse


class Poll(models.Model):
    question = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Question")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")

    def __str__(self):
        return f"{self.id}. {self.question} {self.created_at}"

    def get_absolute_url(self):
        return reverse("poll_view", kwargs={"pk": self.pk})

    def upper(self):
        return self.question.upper()

    class Meta:
        db_table = "polls"
        verbose_name = "Poll"
        verbose_name_plural = "Polls"


class Choice(models.Model):
    choice_text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Choice")
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, related_name="choices",
                             verbose_name='Poll')

    def __str__(self):
        return f"{self.id}. {self.choice_text} {self.poll}"

    class Meta:
        db_table = "choices"
        verbose_name = "Choice"
        verbose_name_plural = "Choices"


class Answer(models.Model):
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, related_name="answers",
                             verbose_name='Poll')
    choice = models.ForeignKey("webapp.Choice", on_delete=models.CASCADE, related_name="answers",
                               verbose_name='Choice')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")

    def __str__(self):
        return f"{self.id}. {self.poll} {self.choice}"

    class Meta:
        db_table = "answers"
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

