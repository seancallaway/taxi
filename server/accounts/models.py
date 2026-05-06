from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    @property
    def group(self):
        groups = self.groups.all()
        return groups[0].name if groups else None

