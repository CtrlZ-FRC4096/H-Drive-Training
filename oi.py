from wpilibextra.customcontroller import XboxCommandController
from wpilibextra.customcontroller.custom_button import CustomButton
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from robot import Robot
class OI:
    def __init__(self, robot: "Robot"):
        self.robot = robot
        self.driver = XboxCommandController(0)
        @self.robot.drivetrain.setDefaultCommand
        def _():
            while True:
                yield
                frontback = self.driver.LEFT_JOY_Y()
                leftright = self.driver.RIGHT_JOY_X()
                self.robot.drivetrain.tank_drive(leftright, frontback)