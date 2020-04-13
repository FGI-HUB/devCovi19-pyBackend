from django.db import models
from django.utils import timezone
from django.conf import settings


class StephTrackedModel(models.Model):
    is_archived = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    modified_date = models.DateTimeField(null=True, editable=False , blank=True)
    # created_by = models.ForeignKey("", null=True, editable=False, blank=True, on_delete=models.DO_NOTHING, related_name="+")
    # modified_by = models.ForeignKey("", null=True, editable=False, blank=True, on_delete=models.DO_NOTHING, related_name="+")

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(StephTrackedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-created_date']


news_upload_path = "news"
class News(StephTrackedModel):
    title = models.CharField(max_length=150, default='')
    slug = models.SlugField()
    content = models.TextField(default='')
    picture = models.FileField(upload_to=news_upload_path, null=True)
    picture_thumbnail = models.FileField(upload_to=news_upload_path, null=True, blank=True)

    def __str__(self):
        return self.title
