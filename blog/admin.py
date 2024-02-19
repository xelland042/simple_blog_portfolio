from django.contrib import admin

from blog.models import Page, Image, Link, Description, Title


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 1


class TitleInline(admin.TabularInline):
    model = Title
    extra = 1


class PageAdmin(admin.ModelAdmin):
    inlines = [TitleInline, ImageInline, DescriptionInline, LinkInline]


admin.site.register(Page, PageAdmin)
admin.site.register(Title)
admin.site.register(Image)
admin.site.register(Description)
admin.site.register(Link)
