
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import (CreateModelMixin as _CreateModelMixin,
                                   ListModelMixin as _ListModelMixin,
                                   UpdateModelMixin as _UpdateModelMixin,
                                   DestroyModelMixin as _DestroyModelMixin,
                                   RetrieveModelMixin as _RetrieveModelMixin)

def data_format(cls, data, method):
    if cls.insert_config:
        cls.success_status[method]['data'] = data
        ret = cls.success_status[method]
    else:
        ret = data
    return ret


class CreateModelMixin(_CreateModelMixin):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        ret = data_format(self, serializer.data, 'post')
        return Response(ret, status=status.HTTP_201_CREATED, headers=headers)


class ListModelMixin(_ListModelMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        ret = data_format(self, serializer.data, 'get')
        return Response(ret)


class RetrieveModelMixin(_RetrieveModelMixin):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ret = data_format(self, serializer.data, 'retrieve')
        return Response(ret)


class UpdateModelMixin(_UpdateModelMixin):
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        ret = data_format(self, serializer.data, 'patch' if partial else 'put')
        return Response(ret)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin(_DestroyModelMixin):
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        ret = data_format(self, None, 'delete')
        return Response(ret, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
