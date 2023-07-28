from wpilibextra.coroutine.subsystem import SubsystemBase
import wpilib
import ctre
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from robot import Robot
class Drivetrain(SubsystemBase):
    def __init__(self, robot: "Robot"):
        super().__init__()
        self.robot = robot
        left_motor_1 = ctre.VictorSPX(3)
        left_motor_2 = ctre.VictorSPX(2)
        self.left_motors = wpilib.MotorControllerGroup(left_motor_1, left_motor_2)
        right_motor_1 = ctre.VictorSPX(1)
        right_motor_2 = ctre.VictorSPX(0)
        self.right_motors = wpilib.MotorControllerGroup(right_motor_1, right_motor_2)
        self.middle_motor = ctre.VictorSPX(4)
    
    def stop(self):
        self.left_motors.set(0)
        self.middle_motor.set(0)
        self.right_motors.set(0)
    
    def tank_drive(self, leftright, frontback):
        left = frontback
        right = frontback
        left += leftright
        right -= leftright
        maximum = max(abs(left),abs(right),1)
        left /= maximum
        right /= maximum
        self.left_motors.set(left)
        self.right_motors.set(right)
