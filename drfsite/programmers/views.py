from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Programmers
from .permissions import IsAdminOrReadOnly
from .serializers import ProgrammersSerializer


class ProgrammersAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProgrammersAPIList(generics.ListCreateAPIView):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = ProgrammersAPIListPagination


class ProgrammersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammersSerializer
    permission_classes = (IsAuthenticated, )


class ProgrammersAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammersSerializer
    permission_classes = (IsAdminOrReadOnly, )
