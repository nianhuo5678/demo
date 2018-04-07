# -*- encoding: utf-8 -*-
from rest_framework import serializers
from models import User, Article
import hashlib

# 自定义关系字段

class ArticleIDField(serializers.RelatedField):

    def to_representation(self, value):
        return {
            'title' : value.title,
            'id': value.id,
        }

class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
            'user',
            'author_name',
            'created_time',
            'is_liked',
        )


    def get_author_name(self, obj):
        return obj.user.username


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    # articles = ArticleSerializer(many=True, source='article_set')
    # articles = ArticleSerializer(many=True, read_only=True)
    # articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # articles = serializers.SlugRelatedField(many=True, read_only=True,slug_field='title')
    # articles = User.articles
    # articles = serializers.StringRelatedField(many=True)
    # articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='article-detail')
    # articles = serializers.HyperlinkedIdentityField(view_name='article-detail')
    # articles = serializers.SerializerMethodField()
    user_articles = ArticleIDField(read_only=True,many=True)
    articles_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'is_admin',
            'info',
            'last_modified',
            'gender',
            # 'articles',
            'articles_count',
            'user_articles',
        )

    # 加密方法1,override create() 和 update()
    # 需要改两个地方
    # def create(self, validated_data):
    #     raw_password = validated_data.get("password")
    #     encrypted_password = hashlib.sha1(raw_password).hexdigest()
    #     # encrypted_password
    #     validated_data['password'] = encrypted_password
    #     user = User.objects.create(**validated_data)
    #     return user
    #
    # def update(self, instance, validated_data):
    #     raw_password = validated_data.get("password")
    #     encrypted_password = hashlib.sha1(raw_password).hexdigest()
    #     instance.password = encrypted_password
    #     instance.save()
    #     return instance

    # 加密方法2， 重写validate方法
    # update() 和 create() 都会调用这个方法，只需要写一次

    def validate_password(self, value):
        return hashlib.sha1(value).hexdigest()

    # 自定义字段gender
    def get_gender(self, obj):
        gender_str = 'Female'
        return gender_str

    # 自定义字段articles，返回作者对应的文章标题列表
    # def get_articles(self, obj):
    #     titles =[]
    #     for article in obj.user_articles.all():
    #             titles.append(article.title)
    #     return titles

    # 自定义字段articles，返回作者的文章标题列表。使用filter只 is_liked = True 的文章。
    # def get_articles(self, obj):
    #     titles = []
    #     for article in obj.user_articles.filter(is_liked = True):
    #         titles.append(article.title)
    #     return titles


    # 自定义字段articles_count，返回作者的文章数目
    def get_articles_count(self, obj):
        return obj.user_articles.all().count()
