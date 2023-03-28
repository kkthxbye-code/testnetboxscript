from extras.scripts import Script, MultiObjectVar
from extras.scripts.util.common import common_stuff

class TestScriptRoot(Script):
    devices = MultiObjectVar(
        model=Device,
    )

    def run(self, data, commit):
        self.log_success("test")
