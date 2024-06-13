from rest_framework import serializers

from product.models.category import Category

class CategorySarializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]