from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField


class User(AbstractUser):
    photo = ImageField(upload_to='photos', null=True, blank=True)

    @property
    def group(self):
        groups = self.groups.all()
        return groups[0].name if groups else None

