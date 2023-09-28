from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_updated']

    def __str__(self) -> str:
        return self.title
