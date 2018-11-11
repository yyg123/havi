# coding=utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process(request):
    #获取相应的数据的逻辑
    data = {
        "result": "success",
        "data": {
            "nodes": ["10.121.143.1", "10.121.105.75"],
            "permissions": ["测试", "研发", "PM"],
            "configs": ["云", "本地"]
        }
    }
    return JsonResponse(data)
