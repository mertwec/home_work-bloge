from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse


Users = get_user_model() # default user


class Rubric(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(allow_unicode=True,
                            default='',
                            blank=True)
    # slug = AutoSlugField(
    #     populate_from='title',
    #     always_update=True,
    #     unique=True,
    #     null=True
    # )
    active = models.BooleanField(
        verbose_name='is_active?',
        default=True,
    )

    class Meta:
        verbose_name = 'Рубрика'  # отображение названия модели в админке
        verbose_name_plural = 'рубрики'
        ordering = ('title',)  # сортировка по title (в алфавитном порядке)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mapp:post_of_rubric',
                       kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(
        verbose_name='Пост',
    )
    author = models.ForeignKey(
        Users,
        verbose_name='-Author-',
        on_delete=models.CASCADE,
        null=False,
        related_name="Author_of_post",
    )
    rubric = models.ManyToManyField(
        Rubric,
        verbose_name='rubric',
        blank=False,
    )

    browsing = models.IntegerField(
        verbose_name='quantity views',
        default=0,
    )

    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='дата последнего изменения',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Post'
        ordering = ('-pk',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # здесь описываем логику до сохранения объекта
        super().save(*args, **kwargs)


class Comments(models.Model):
    author = models.ForeignKey(
        Users,
        verbose_name='-Author-',
        on_delete=models.CASCADE,
        null=False,
        related_name="Author_of_comment",
    )
    post = models.ForeignKey(
        Post,
        verbose_name='post',
        on_delete=models.CASCADE,
        null=False,
        related_name="Post",
    )

    comment = models.TextField(
        verbose_name='text of comment'
    )

    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,)

    class Meta:
        verbose_name = 'Comment'  # отображение названия модели в админке
        verbose_name_plural = 'comments'
        ordering = ('-created_at',)

    def __str__(self):
        return f'comment to {self.post}'
