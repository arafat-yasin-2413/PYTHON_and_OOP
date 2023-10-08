# inheritance vs. Composition

class CPU:
    def __init__(self,cores):
        self.core = cores


class RAM:
    def __init__(self,size):
        self.size = size


class HardDrive:
    def __init__(self,capacity):
        self.capacity = capacity

# Computer has a cpu
# Computer has a ram
# Computer has a hard drive
class Computer:
    def __init__(self,cores,ram_size,hd_capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)



mac = Computer(8,16,512)
print(mac.cpu)
print(mac.ram)
print(mac.hard_disc)