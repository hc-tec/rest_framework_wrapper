# rest_framework_wrapper
generic以及mixin的二次封装，主要是方便对返回数据的格式进行处理

普通的 ListAPIView
```py
from rest_framework.viewsets.generics import ListAPIView
class ShowTaskTag(generics.ListAPIView):
    queryset = TaskTag.objects.all()
    serializer_class = TaskTagSerializer
```
返回的数据结果
```json
[
    {
        "id": 1,
        "name": "作业"
    },
    {
        "id": 2,
        "name": "阅读"
    },
    {
        "id": 3,
        "name": "自学"
    },
    {
        "id": 4,
        "name": "暑期活动"
    },
    {
        "id": 5,
        "name": "寒假活动"
    }
]
```


```py
from rest_framework_wrapper.generics import ListAPIView
class ShowTaskTag(ListAPIView):
    success_status = {
        'get': {
            'code': 244,
            'msg': '标签获取成功'
        }
    }
    queryset = TaskTag.objects.all()
    serializer_class = TaskTagSerializer
```
返回的数据格式为
```json
{
    "code": 244,
    "msg": "标签获取成功",
    "data": [
        {
            "id": 1,
            "name": "作业"
        },
        {
            "id": 2,
            "name": "阅读"
        },
        {
            "id": 3,
            "name": "自学"
        },
        {
            "id": 4,
            "name": "暑期活动"
        },
        {
            "id": 5,
            "name": "寒假活动"
        }
    ]
}
```




