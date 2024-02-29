from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=80,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


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
    image_file = models.ImageField(
        upload_to='images/'
    )    
    
    description = models.TextField(
        null=True,
        blank=True,        
    )

    active = models.BooleanField(
        default=True
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    like_counts = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.name} - {self.upload.date()}"