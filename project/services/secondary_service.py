from project.services.base_service import BaseService

class SecondaryService(BaseService):
    INITIAL_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"
        return f"{self.name} Secondary Service:\nRobots: {' '.join(rob.name for rob in self.robots)}"
