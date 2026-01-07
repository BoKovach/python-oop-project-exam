from project.services.base_service import BaseService

class MainService(BaseService):
    INITIAL_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Main Service:\nRobots: none"
        return f"{self.name} Main Service:\nRobots: {' '.join(rob.name for rob in self.robots)}"