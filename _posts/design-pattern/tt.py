class Invoker:
    def __init__(self):
        self.cmds = []

    def add_cmd(self, cmd):
        self.cmds.append(cmd)

    def run(self): 
        for cmd in self.cmds:
            cmd.execute()


class Cmd1:
    def execute(self):
        print("Do cmd1")
        Business1().do_someting()


class Cmd2:
    def execute(self):
        print("Do cmd1")
        Business2().do_someting()


class Business1:
    def do_someting(self):
        print("business1 is workong")


class Business2:
    def do_someting(self):
        print("businee2 is working")


if __name__ == '__main__':
    invoker = Invoker()
    invoker.add_cmd(Cmd1())
    invoker.add_cmd(Cmd2())
    invoker.run()



