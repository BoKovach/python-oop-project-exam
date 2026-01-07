from robots.female_robot import FemaleRobot
from robots.male_robot import MaleRobot
from services.main_service import MainService
from services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.SERVICE_TYPES[service_type](name)
        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_robot(robot_name)
        service = self.find_service(service_name)

        if not self.matching(robot, service):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_service(service_name)
        robot = self.find_robot_in_service(robot_name, service)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.find_service(service_name)
        total_price = sum(rob.price for rob in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(service.details() for service in self.services)

    def find_robot(self, robot_name):
        for rob in self.robots:
            if rob.name == robot_name:
                return rob

    def find_service(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service

    @staticmethod
    def matching(robot, service):
        robot_type = type(robot).__name__
        service_type = type(service).__name__
        if robot_type == "MaleRobot" and service_type == "MainService":
            return True
        if robot_type == "FemaleRobot" and service_type == "SecondaryService":
            return True
        return False

    @staticmethod
    def find_robot_in_service(robot_name, service):
        for robot in service.robots:
            if robot.name == robot_name:
                return robot

