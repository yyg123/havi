# coding=utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os as _os
import json as _json


@csrf_exempt
def process(request):
    data = _json.loads(request.POST.get('data', ''))
    print data
    size = int(data["size"])

    #进程的ID
    id = int(data["id"])

    path = _os.path.abspath(_os.path.join(_os.getcwd(),"log/log1"))
    lines = []
    f=open(path,"r")
    try:
        for line in f:
            lines.append(line.rstrip("\n"))
            if 0< size <len(lines):
                lines.pop(0)
    finally:
        f.close()
    print lines
    data = {
        "result": "success",
        "lines": lines
    }
    return JsonResponse(data)
