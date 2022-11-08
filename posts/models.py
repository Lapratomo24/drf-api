from django.db import models

# Create your models here.


class Post(models.model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../photo_react_main'
        )

    class Meta:
        ordering: ['-created_at']

    def __str__(self):
        return f"{self.id}{self.title}"
    
    
