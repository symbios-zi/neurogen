from django.db import models
from django.utils import timezone

from services.parser.google import Parser


class Keywords(models.Model):
    word = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def parse(self):
        parser = Parser(self.word)
        result = parser.parse()

        for serp in result.serps:
            for link in serp.links:
                if link.link:
                    obj, created = Site.objects.update_or_create(
                        url=link.link, title=link.link, position=link.rank, keyword=self,
                        defaults={'url': link.link},
                    )

    class Meta:
        db_table = "keywords"


class Site(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    position = models.IntegerField()
    keyword = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        db_table = "sites"
