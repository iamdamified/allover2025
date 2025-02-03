from django.db import models


class PersonManager(models.Manager):
    def active_users(self):
        return self.filter(is_active=True)