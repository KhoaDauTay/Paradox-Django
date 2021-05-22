# Section 6: Dive into Django Rest
## Lesson overview
- Learn overview and how to using ViewSet and Serializer in Django REST with special Case

## Overview
- A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().
- Now, I will introduce the ViewSet type, the functions commonly used in it

## ViewSet
- The ViewSet class inherits from APIView. You can use any of the standard attributes such as permission_classes, authentication_classes in order to control the API policy on the viewset.

- The ViewSet class does not provide any implementations of actions. In order to use a ViewSet class you'll override the class and define the action implementations explicitly.
- Example: Using ViewSet, ViewSet won't issue actions like create, list,... we'll have to add.
    - Reference ViewSet Attributes and method: [Docs](https://www.cdrf.co/3.12/rest_framework.viewsets/ViewSet.html)
    ```
    class StudentViewSet(viewsets.ViewSet):

        def list(self, request):
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)

        def retrieve(self, request, pk=None):
            queryset = Student.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = StudentSerializer(user)
            return Response(serializer.data)
    ```
## Generic ViewSet
- The GenericViewSet class inherits from GenericAPIView, and provides the default set of get_object, get_queryset methods and other generic view base behavior, but does not include any actions by default.

- In order to use a GenericViewSet class you'll override the class and either mixin the required mixin classes, or define the action implementations explicitly.
- The only difference between ViewSet and GenericViewSet is that it provides generic methods like get_object and get_queryset.

    ```
    class StudentGenericViewSet(viewsets.GenericViewSet):

        def get_queryset(self):
            queryset = Student.objects.all()
            return queryset

        def get_object(self):
            queryset = self.get_queryset()
            obj = queryset.get(pk=self.kwargs['pk'])
            return obj

        def list(self, request):
            queryset = self.get_queryset()
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)

        def retrieve(self, request, **kwargs):
            obj = self.get_object()
            serializer = StudentSerializer(obj)
            return Response(serializer.data)
    ```
## ModelViewSet
- It provides all the actions by default (i.e .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()).

- Most of the times we use this because it provides the generic functionality so, we simply need to override the attributes like queryset , serializer_class , permission_classesand authentication_classes.

- If we any conditional logic then we can override methods like get_object, get_queryset, get_permission_classes, etc.

    ```
    from rest_framework import viewsets
    from .models import Student
    from .serializers import StudentSerializer

    class StudentModelViewSet(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
    ```
## Show config urls
    ```
    router = DefaultRouter()
    router.register('student-viewset', views.StudentViewSet, basename='student_vs')
    router.register('student-generic-viewset', views.StudentGenericViewSet, basename='student_gvs')
    router.register('student-model-viewset', views.StudentModelViewSet, basename='student_mvs')
    urlpatterns = router.urls
    ```
- Student ViewSet Urls

    ```
    '^student-viewset/$'
    '^student-viewset/(?P<pk>[^/.]+)/$'
    ```
- Student GenericViewSet Urls

    ```
    '^student-generic-viewset/$'
    '^student-generic-viewset/(?P<pk>[^/.]+)/$'
    ```
- Student ModelViewSet Urls
    ```
    '^student-model-viewset/$'
    '^student-model-viewset/(?P<pk>[^/.]+)/$'
    ```
## Code: [django-oauth-docker](https://github.com/KhoaDauTay/Django-Oauth-Docker)