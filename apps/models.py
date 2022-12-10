from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, SlugField, ForeignKey, SET_NULL, ManyToManyField, DateField, CASCADE, \
    DateTimeField, IntegerField, TextField, URLField, TextChoices
from django.utils.html import format_html
from django.utils.text import slugify
from django_resized import ResizedImageField


class Category(models.Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    image = ResizedImageField(null=True, blank=True, default='default_category_image.jpeg', upload_to='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategoriyalar"
        verbose_name = 'Kategoriya'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Post.objects.filter(slug=self.slug).exists():
            slug = Post.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.name:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)

    @property
    def post_count(self):
        return self.post_set.filter(status='active').count()


class Post(models.Model):
    class StatusChoise(TextChoices):
        PENDING = 'pending', 'Kutilmoqda'
        ACTIVE = 'active', 'Activlashgan'
        CANCEL = 'cancel', 'Rad etilgan'

    title = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    content = RichTextUploadingField()
    author = ForeignKey('apps.User', SET_NULL, null=True, blank=True)
    image = ResizedImageField(null=True, blank=True, default='default.jpg', upload_to='posts')
    category = ManyToManyField(Category, related_name='post_set')
    status = CharField(max_length=55, choices=StatusChoise.choices, default=StatusChoise.PENDING)
    views = IntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Postlar"
        verbose_name = 'Post'

    def __str__(self):
        return self.title

    def submit_buttons(self ,):  # NOQA
        if self.status == Post.StatusChoise.PENDING:
            return format_html(f'''
            <a href="active/{self.id}" class="button" >Active</a>
            <a href="cancel/{self.id}" class="button" >Cancel</a>
            ''')
        return format_html("<b>Ko'rib chiqilgan</b>")

    @property
    def comment_count(self):
        return self.comment_set.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.slug:
            while Post.objects.filter(slug=self.slug).exists():
                slug = Post.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

        super().save(*args, **kwargs)


class Comment(models.Model):
    text = TextField()
    author = ForeignKey('apps.User', SET_NULL, null=True, blank=True)
    post = ForeignKey(Post, CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Izohlar"
        verbose_name = 'Izoh'


class User(AbstractUser):
    phone = CharField(max_length=15, null=True, blank=True)
    about = TextField(null=True, blank=True)
    birthday = DateField(null=True, blank=True)
    image = ResizedImageField(null=True, blank=True, default='auth.png', upload_to='authors')
    workspace = CharField(max_length=255, null=True, blank=True)
    gender = CharField(max_length=15, null=True, blank=True)
    address = CharField(max_length=255, null=True, blank=True)
    facebook_url = URLField(null=True, blank=True)
    twitter_url = URLField(null=True, blank=True)
    instagram_url = URLField(null=True, blank=True)
    dribbble_url = URLField(null=True, blank=True)
