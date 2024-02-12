from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to='images/gallery/')
    content = models.TextField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.image.url