import wpilibextra.customcontroller
from wpilibextra.customcontroller.custom_button import CustomButton
class OI:
    def __init__(self, robot: "Robot"):
        self.robot = robot
        self.driver = XboxCommandController(0)
        @self.robot.drivetrain.setDefaultCommand
        def _():
            ...