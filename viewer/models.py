from django.db import models


class Image(models.Model):
    name = models.CharField(
        max_length=300
    )
    shoot_date = models.DateField(
        null=True,
        blank=True,
    )
    upload = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(        
    )
    
    description = models.TextField(
        null=True,
        blank=True,        
    )

    active = models.BooleanField(
        default=True
    )

    