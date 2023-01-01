from django.conf import settings
from django.db import models
from django.utils import timezone

# defines our model
# Post is the name of the model
# models.Model means that the Post is a django model. So, django knows that it has to be stored in the database
class Post(models.Model):
    # models.ForeignKey links to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.CharField is how we define text with a limited number of characters
    title = models.CharField(max_length=200)
    # models.TextField is for long text without a limit
    text = models.TextField()
    # models.DateTimeField is for date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
