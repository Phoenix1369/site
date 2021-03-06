import re

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from judge.models.problem import Problem
from judge.models.profile import Profile

__all__ = ['MiscConfig', 'validate_regex', 'NavigationBar', 'BlogPost', 'Solution']


class MiscConfig(models.Model):
    key = models.CharField(max_length=30, db_index=True)
    value = models.TextField(blank=True)

    def __unicode__(self):
        return self.key

    class Meta:
        verbose_name = _('configuration item')
        verbose_name_plural = _('miscellaneous configuration')


def validate_regex(regex):
    try:
        re.compile(regex, re.VERBOSE)
    except re.error as e:
        raise ValidationError('Invalid regex: %s' % e.message)


class NavigationBar(MPTTModel):
    class Meta:
        verbose_name = _('navigation item')
        verbose_name_plural = _('navigation bar')

    class MPTTMeta:
        order_insertion_by = ['order']

    order = models.PositiveIntegerField(db_index=True, verbose_name=_('order'))
    key = models.CharField(max_length=10, unique=True, verbose_name=_('identifier'))
    label = models.CharField(max_length=20, verbose_name=_('label'))
    path = models.CharField(max_length=255, verbose_name=_('link path'))
    regex = models.TextField(verbose_name=_('highlight regex'), validators=[validate_regex])
    parent = TreeForeignKey('self', verbose_name=_('parent item'), null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.label

    @property
    def pattern(self, cache={}):
        # A cache with a bad policy is an alias for memory leak
        # Thankfully, there will never be too many regexes to cache.
        if self.regex in cache:
            return cache[self.regex]
        else:
            pattern = cache[self.regex] = re.compile(self.regex, re.VERBOSE)
            return pattern


class BlogPost(models.Model):
    title = models.CharField(verbose_name=_('post title'), max_length=100)
    authors = models.ManyToManyField(Profile, verbose_name=_('authors'), blank=True)
    slug = models.SlugField(verbose_name=_('slug'))
    visible = models.BooleanField(verbose_name=_('public visibility'), default=False)
    sticky = models.BooleanField(verbose_name=_('sticky'), default=False)
    publish_on = models.DateTimeField(verbose_name=_('publish after'))
    content = models.TextField(verbose_name=_('post content'))
    summary = models.TextField(verbose_name=_('post summary'), blank=True)
    og_image = models.CharField(verbose_name=_('openGraph image'), default='', max_length=150, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', args=(self.id, self.slug))

    class Meta:
        permissions = (
            ('see_hidden_post', 'See hidden posts'),
        )
        verbose_name = _('blog post')
        verbose_name_plural = _('blog posts')


class Solution(models.Model):
    url = models.CharField('URL', max_length=100, db_index=True, blank=True)
    title = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    publish_on = models.DateTimeField()
    content = models.TextField()
    authors = models.ManyToManyField(Profile, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.SET_NULL, verbose_name=_('associated problem'),
                                null=True, blank=True)

    def get_absolute_url(self):
        return reverse('solution', args=[self.url])

    def __unicode__(self):
        return self.title

    class Meta:
        permissions = (
            ('see_private_solution', 'See hidden solutions'),
        )
        verbose_name = _('solution')
        verbose_name_plural = _('solutions')
