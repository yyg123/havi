# coding=utf-8

class Mission():
    def __init__(self):
        self.id = 0
        self.user = ""
        self.password = ""
        self.node = ""
        self.permission = ""
        self.config = ""
        self.createTS = -1

    def toJSON(self):
        return {
            "id":self.id,
            "user": self.user,
            "password": self.password,
            "node": self.node,
            "permission": self.permission,
            "config": self.config,
            "createTS": self.createTS
        }

    @staticmethod
    def fromJSON(o):
        """
        :rtype:Mission
        """
        mission = Mission()
        mission.id = int(o["id"]) if "id" in o else 0
        mission.user = o["user"]
        mission.password = o["password"]
        mission.node = o["node"]
        mission.permission = o["permission"]
        mission.config = o["config"]
        mission.createTS = o["createTS"]
        return mission

    @staticmethod
    def loadAll():
        """
        :rtype: list[Mission]
        """
        #把存储的所有的mission信息拿出，并封装成Mission
        # x = []
        # x.append(Mission())
        return []

    @staticmethod
    def submit(mission):
        ALL_MISSION[mission.id] = mission

if False:
    ALL_MISSION = dict()

if not "_inited" in globals():
    ALL_MISSION = {}
    _inited = True