from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()

    def full_name(self) -> str:
        if self.middle_name == "":
            return f'{self.last_name}, {self.first_name}'
        return f'{self.last_name}, {self.first_name} {self.middle_name}'

    def __str__(self) -> str:
        return self.full_name()
