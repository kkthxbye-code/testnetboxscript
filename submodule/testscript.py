from extras.scripts import Script, MultiObjectVar
from extras.scripts.util.common import common_stuff

class TestScript(Script):
    class Meta:
        name = "Add Device Type Components"
        description = "Add missing components to selected devices"

    devices = MultiObjectVar(
        model=Device
    )

    def run(self, data, commit):
        self.log_success("testscript1")