from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from comment.models import Comment
from user.api import UserLimitSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserLimitSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class CommentCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = CommentCustomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
