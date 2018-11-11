# coding=utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from havi import Mission, ALL_MISSION
import random

@csrf_exempt
def process(request):

    # Mission.loadAll() 实际上应该使用这个方法

    mission = Mission()

    mission.id = random.randint(0,999)
    mission.user = "123"
    mission.password = "123123"
    mission.config = "云"
    mission.node = "10.121.143.1"
    mission.permission = "PM"

    missions = []
    # missions.append(mission)
    # missions.append(mission)
    # missions.append(mission)
    # missions.append(mission)
    # missions.append(mission)
    for mission in ALL_MISSION.values():
        missions.append(mission)

    data = {
        "result": "success",
        "data": [mission.toJSON() for mission in missions]
    }
    return JsonResponse(data)
