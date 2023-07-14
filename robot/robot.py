import wpilib
import wpilibextra
import commands2
import subsystems.drivetrain
import oi
from wpilibextra.coroutine.coroutine_robot import CoroutineRobot
class Robot(CoroutineRobot):
    def robot_start(self):
        self.scheduler = commands2.CommandScheduler.getInstance()
        self.drivetrain = subsystems.drivetrain.Drivetrain(self)
        self.scheduler.registerSubsystem(self.drivetrain)
        self.driverstation = wpilib.DriverStation
        self.oi = oi.OI(self)
        while True:
            yield
            self.scheduler.run()
    def disabled_mode(self):
        self.scheduler.cancelAll()
        self.drivetrain.stop()
    def teleop_mode(self):
        self.scheduler.cancelAll()
        while True:
            yield
if __name__ == "__main__":
    wpilib.run(Robot)
        
       
     
            