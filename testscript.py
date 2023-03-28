from extras.scripts import Script, MultiObjectVar


class TestScriptRoot(Script):
    devices = MultiObjectVar(
        model=Device,
    )

    def run(self, data, commit):
        self.log_success("test")
