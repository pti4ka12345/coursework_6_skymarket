from rest_framework import serializers


from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name")

    class Meta:
        model = Ad
        fields = '__all__'
