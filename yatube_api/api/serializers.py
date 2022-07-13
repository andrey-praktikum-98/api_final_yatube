from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True,
                                        default=(serializers
                                                 .CurrentUserDefault()))
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        user = get_object_or_404(User, username=data['following'].username)
        if user == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписываться на себя'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
