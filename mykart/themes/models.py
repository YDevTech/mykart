from django.db import models

# Model for theme
class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    caption=models.TextField()


