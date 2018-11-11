# coding=utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from havi import Mission
import json as _json
import subprocess
import sys


@csrf_exempt
def process(request):
    data = _json.loads(request.POST.get('data'))
    mission = Mission.fromJSON(data)


    #在这里添加数据的检测
    if mission.user == "":
        return JsonResponse({"result": "fail", "context":"用户名未填写"})
    print _json.dumps(mission.toJSON())

    child = subprocess.Popen(args="ping www.baidu.com",stdout=sys.stdout, stderr=sys.stderr)
    mission.id = child.pid
    Mission.submit(mission)

    return JsonResponse({"result": "success"})
