from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null = True)
    age = models.IntegerField(null = True)
    creation_date = models.DateTimeField(null=False, auto_now_add=True)
    updation_date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "author_model"
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="author_blog")
    time_to_read = models.IntegerField(null=True)
    tagline = models.TextField()
    creation_date = models.DateTimeField(null=False, auto_now_add=True)
    updation_date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "blog_model"
