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

封装后的 ListAPIView
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

其他的类同理
下面是默认配置
```py
DEFAULT_SUCCESS_RESPONSE_CONFIG = {
    // ListAPIView
    'get': {
        'code': 200,
        'msg': '数据获取成功',
    },
    // CreateAPIView
    'post': {
        'code': 201,
        'msg': '数据创建成功',
    },
    // UpdateAPIView
    'patch': {
        'code': 202,
        'msg': '数据局部更新成功',
    },
    //  UpdateAPIView
    'put': {
        'code': 203,
        'msg': '数据已全部更新成功',
    },
    // DestoryAPIView
    'delete': {
        'code': 204,
        'msg': '数据删除成功',
    },
    // RetrieveAPIView
    'retrieve': {
        'code': 205,
        'msg': '数据创建成功',
    },
}
```




