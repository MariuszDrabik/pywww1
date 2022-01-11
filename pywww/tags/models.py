from django.db import models


class Tags(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return f'TAG: {self.name} with slug: {self.slug}'
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: Optional[str] = ..., update_fields: Optional[Iterable[str]] = ...) -> None:
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
