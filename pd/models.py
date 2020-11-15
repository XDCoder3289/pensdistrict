from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from ckeditor.fields import RichTextField

class Category(models.Model):
    pen_category = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pen_category)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '1. Categories'

    def __str__(self):
        return self.pen_category


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    post_name = models.CharField(max_length=128, unique=True)
    featured_image = models.ImageField(blank=True)
    excerpt = models.CharField(max_length=97, blank=True, null=True)
    starting_content = RichTextField(default="Write the beginning of your article here")
    conclusion = RichTextField(default="Write the ending sentences here")
    date = models.DateTimeField(default=now)
    meta_description = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_name)
        super(Post, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = '3. Posts'
        ordering = ['-date',]


    def __str__(self):
        return self.post_name

class PenInPost(models.Model):
    pen_is_in = models.ForeignKey(Post, on_delete=models.CASCADE)
    pen_name = models.CharField(max_length=128)
    short_description = RichTextField(blank=True, null=True)
    post = RichTextField(blank=True, null=True)
    button_copy = models.CharField(max_length=200, blank=True, null=True)
    pen_image = models.ImageField()
    amazon_link = models.URLField()
    rating = models.CharField(max_length=3, default=4)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = '4. Pens To Be Added'

    def __str__(self):
        return self.pen_name
