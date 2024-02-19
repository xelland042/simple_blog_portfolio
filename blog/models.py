from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Page(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Image(BaseModel):
    image = models.ImageField(upload_to='images/')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.id} - {self.image}'


class Title(BaseModel):
    title = models.CharField(max_length=255)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='titles')

    def __str__(self):
        return f'{self.id} - {self.title}'


class Description(BaseModel):
    description = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='descriptions')

    def __str__(self):
        return f'{self.id}'


class Link(BaseModel):
    link = models.CharField(max_length=255)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return f'{self.id} - {self.link}'
