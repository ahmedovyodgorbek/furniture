from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel

UserModel = get_user_model()


class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_("title"))
    parent = models.ForeignKey('self',
                               on_delete=models.PROTECT,
                               null=True, blank=True,
                               related_name='children',
                               verbose_name=_("parent"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class BlogTagModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_("title"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogAuthorModel(BaseModel):
    first_name = models.CharField(max_length=128, verbose_name=_("first_name"))
    last_name = models.CharField(max_length=128, verbose_name=_("last_name"))
    avatar = models.ImageField(upload_to='blogs/authors/', verbose_name=_("avatar"))
    description = models.CharField(max_length=255, null=True, blank=True)

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class BlogModel(BaseModel):
    image = models.ImageField(upload_to='blogs', verbose_name=_("image"))
    title = models.CharField(max_length=128, verbose_name=_("title"))
    description = models.TextField(verbose_name=_('description'))

    author = models.ManyToManyField(BlogAuthorModel, related_name='blogs',
                                    verbose_name=_('author'))
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs',
                                        verbose_name=_('categories'))
    tags = models.ManyToManyField(BlogTagModel, related_name='tags',
                                  verbose_name=_('tags'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class BlogCommentModel(BaseModel):
    comment = models.TextField(verbose_name=_('comment'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blog_comments',
                             verbose_name=_('user'))
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name=_('blog'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
