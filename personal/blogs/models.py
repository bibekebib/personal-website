from django.db import models


# Create your models here.

class Author(models.Model):
    Name= models.CharField(max_length=255)
    image= models.ImageField()
    email = models.EmailField()
    def __str__(self):
        return self.Name


class Categories(models.Model):
    division = models.CharField(max_length=255)

    def __str__(self):
        return self.division

STATUS=(
    (0,'Draft'),
    (1,'Publish')
) 
TYPES=(
    (0,'blogs'),
   (1,'Technical-writings')
)   
class post(models.Model):
    title = models.CharField(max_length=255, help_text="Enter title")
    slug = models.SlugField(max_length=255, unique=True,help_text="It will auto-complete automically!")
    image = models.ImageField(upload_to='images/',help_text="enter feature image of post")
    content =models.TextField(help_text="Enter your post")
    author = models.ForeignKey(Author, on_delete=models.CASCADE,help_text='select author')
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE,help_text='select category')
    Address= models.CharField(max_length=255,help_text="enter the present address")
    Published_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status= models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-Published_on']

    def __str__(self):
        return self.title

''' def _get_unique_slug(self):
        slug=slugify(self.title)
        unique_slug  = slug
        num = 1
        while post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug
        super().save(*args, **kwargs)'''

class Contacted(models.Model):
    Name = models.CharField(max_length=255, blank=False)
    Email = models.EmailField(blank=False)
    Subject = models.CharField(max_length=255)
    Message  = models.TextField(blank=False)

