from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self) -> str:
        return f'OKOKOKO {self.user} {self.pk}'
