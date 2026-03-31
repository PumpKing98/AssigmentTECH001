class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom  # Thang máy bắt đầu ở tầng thấp nhất
        
    def floor_up(self):
        print(f"Thang máy đang ở tầng: {self.current_floor}")
        if self.current_floor < self.top:
            self.current_floor += 1
        if self.current_floor == self.top:
            print(f"Thang máy đang ở tầng: {self.current_floor}")
           
            
    def floor_down(self):
        print(f"Thang máy đang ở tầng: {self.current_floor}")
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        if self.current_floor == self.top:
            print(f"Thang máy đang ở tầng: {self.current_floor}")
            
    def go_to_floor(self, target):
        print(f"--- Di chuyển đến tầng {target} ---")
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
        print("Đã đến đích.")

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
        
    def run_elevator(self, elevator_index, destination):
        if 0 <= elevator_index < len(self.elevators):
            print(f"Điều khiển thang máy số {elevator_index}:")
            self.elevators[elevator_index] .go_to_floor(destination)
        else:
            print("Thang máy không tồn tại!")
    def fire_alarms(self):
        print("CHÁY!! VỀ TẦNG TRỆT")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)

bottom_floor = int(input('Nhập tầng thấp nhất của tòa nhà:'))
top_floor = int(input('Nhập tầng cao nhất của tòa nhà:'))
thang_may = int(input('Nhập số lượng thang máy của tòa nhà:'))
my_building = Building(bottom_floor, top_floor, thang_may)
while True:
    which_elevator = int(input("Thang máy bạn muốn đi:")) - 1 #Người dùng không chọn tầng 0#
    which_floor = int(input("Tầng bạn muốn đi:")) 
    my_building.run_elevator(which_elevator, which_floor)
    tiep_tuc = input(" Bạn muốn đi tiếp không ( Enter để dừng):")
    if tiep_tuc == {}:
        break


