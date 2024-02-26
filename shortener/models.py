from django.db import models
from random import choices, shuffle
import string
from django.template.defaultfilters import slugify

# Create your models here.


class ShortURL(models.Model):
    # URL to be dhortened.
    link = models.CharField(max_length=2048)
    stat = models.IntegerField(default=0)
    # The shortened version.
    slug = models.SlugField(unique=True, blank=True)

    def get_short_url(self):
        return self.slug

    def get_stat(self):
        """Returns the number of clicks on this url."""
        return self.stat

    def save(self, **kwags):
        if not self.slug:
            choice_pool = list(string.ascii_letters + string.digits)
            shuffle(choice_pool)
            random_string = choices(choice_pool, k=6)
            unique_slug = ''.join(random_string)
            while ShortURL.objects.filter(slug=unique_slug).exists():
                # Generate random string of length 6 containing both upper and lowercases.
                shuffle(choice_pool)
                random_string = choices(choice_pool, k=6)
                unique_slug = ''.join(random_string)
            self.slug = slugify(unique_slug)
        super().save(**kwags)

    def __str__(self):
        return f"{self.slug} -> {self.link}"
