
from decorator import subcommand

class Helper:
    def __init__(self, repo_path):
        self._repo_path = repo_path
        pass

    @subcommand("A")
    def funcA(self):
        '''run subcommand to invoke A'''
        print("invoked A")

    @subcommand
    def funcB(self):
        print("invoked B")