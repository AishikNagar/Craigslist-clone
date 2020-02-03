from django.db import models

# Create your models here.
# Whenever we add new stuff to the database, we make migrations to ensure they are recorded
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'