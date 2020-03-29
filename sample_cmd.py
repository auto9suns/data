from cmd import Cmd
import os
from random_sample import randomSample, randomData

class Client(Cmd):
    prompt = 'samplecreator> '
    intro = 'Welcome to sample generator'
    def __init__(self):
        Cmd.__init__(self)
        self.tablestore = {}
        self.currenttable = None

    def emptyline(self):
        print ('please input command!')

    def default(self, line):
        print ('the command you type: {l}, doesnt exist'.format(l=line))

    def do_tcreate(self, name):
        if not name:
            print("table name is missing, table not created")
        else:
            self.tablestore[name] = randomSample()
            self.currenttable = name
            print("table: {t} created, default line: {c}".format(t=name, c=self.tablestore[name].row_number))

    def parse_cmd(self, cmd):
        if cmd:
            return cmd.split()
        else:
            print("cmd is not valid")

    def do_tswitch(self, cmd):
        if cmd in self.tablestore.keys():
            self.currenttable = cmd
        else:
            print("table name wrong {t}".format(t=cmd))


    def do_tupdate(self, cmd):
        # missing cmd validation
        if self.parse_cmd(cmd)[0].lower() == 'name':
            self.tablestore[self.parse_cmd(cmd)[1]] = self.tablestore.pop(self.currenttable)
            self.currenttable = self.parse_cmd(cmd)[1]
        if self.parse_cmd(cmd)[0].lower() == 'length':
            self.tablestore[self.currenttable].row_number = self.parse_cmd(cmd)[1]

    def do_showt(self, cmd):
        if self.tablestore:
            for table in self.tablestore:
                print ("name: {t}, length: {c}".format(t=table, c=self.tablestore[table].row_number))
        else:
            print ("no table has been created")



if __name__ == "__main__":
    client = Client()
    client.cmdloop()