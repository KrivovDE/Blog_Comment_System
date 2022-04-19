from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/")

    def __str__(self):
        return self.title

    def get_summary(self):
        """Получаем первые 100 символов поля content,
           для корректного отображения, при выводе всех Post"""

        return self.content[:100]
