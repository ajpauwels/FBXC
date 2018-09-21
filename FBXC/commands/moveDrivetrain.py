from wpilib.command import TimedCommand
from FBXC.systems import subsystems

class MoveDrivetrain(TimedCommand):
    def __init__(self, distance, timeoutInSeconds):
        super().__init__('move drivetrain %d inches' % distance, timeoutInSeconds)

        self.distance = distance
        self.requires(subsystems.dt)

    def initialize(self):
        subsystems.dt.moveEncoder(self.distance)