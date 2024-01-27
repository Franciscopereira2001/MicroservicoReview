from django.shortcuts import render
from reviewPedidos.serializers import *
from rest_framework import permissions, viewsets

# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-timestamp')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]    