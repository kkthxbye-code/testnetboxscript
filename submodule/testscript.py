from extras.scripts import Script, MultiObjectVar

class TestScript(Script):
    class Meta:
        name = "Add Device Type Components"
        description = "Add missing components to selected devices"

    devices = MultiObjectVar(
        model=Device
    )

    def run(self, data, commit):
        self.log_success("testscript1")