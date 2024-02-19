from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from blog.models import Page, Image, Link, Title, Description


from blog.models import Page, Image, Link, Title, Description


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ('description',)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('link',)


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('title',)


class PageSerializer(serializers.ModelSerializer):
    titles = TitleSerializer(many=True)
    images = ImageSerializer(many=True)
    descriptions = DescriptionSerializer(many=True)
    links = LinkSerializer(many=True)

    class Meta:
        model = Page
        fields = ('id', 'name', 'titles', 'images', 'descriptions', 'links')
