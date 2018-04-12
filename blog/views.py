from rest_framework import viewsets
from models import User, Article
from serializers import UserSerializer, ArticleSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    wset automatically provides `list` and `detail` actions.
    """

    # store encrypted password
    # def perform_create(self, serializer):
    #     raw_password= self.request.data.get("password")
    #     serializer.save(password = hashlib.sha1(raw_password).hexdigest())

    # update last modified tim
    # def perform_update(self, serializer):
    #     raw_password = self.request.data.get("password")
    #     serializer.save(
    #         last_modified = timezone.localtime(timezone.now()),
    #         password = hashlib.sha1(raw_password).hexdigest(),
    #     )

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViesSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer