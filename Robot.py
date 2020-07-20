class Robot:
    def __init__(self, name, ios, ports):
        self.name = name
        self.ios = ios
        self.ports = ports

        
    def introduce_self(self):
        print ("Router name is " + self.name + " and the operating system is "+ self.ios + " and it has " + str(self.ports) + " interfaces.") 
