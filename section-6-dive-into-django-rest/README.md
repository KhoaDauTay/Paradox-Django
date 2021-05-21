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
    class UserViewSet(viewsets.ViewSet):
        permission_classes = (IsAuthenticated,)

        """
        Example empty viewset demonstrating the standard
        actions that will be handled by a router class.

        If you're using format suffixes, make sure to also include
        the `format=None` keyword argument for each action.
        """

        def list(self, request):
            pass

        def create(self, request):
            pass

        def retrieve(self, request, pk=None):
            pass

        def update(self, request, pk=None):
            pass

        def partial_update(self, request, pk=None):
            pass

        def destroy(self, request, pk=None):
            pass
    ```
## Generic ViewSet
- The GenericViewSet class inherits from GenericAPIView, and provides the default set of get_object, get_queryset methods and other generic view base behavior, but does not include any actions by default.

- In order to use a GenericViewSet class you'll override the class and either mixin the required mixin classes, or define the action implementations explicitly.
- Unlike ViewSet, GenericViewSet provides us with available properties such as: quertset, lookup field

    ```
    
    ```
## ModelViewSet
## ReadOnlyModelViewSet