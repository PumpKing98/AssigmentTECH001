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
    if tiep_tuc == (""):
        break
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_in_speed):
        self.current_speed += change_in_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'='*20} {self.name} {'='*20}")
        header = f"{'Biển số':<12} | {'Tốc độ tối đa':<15} | {'Tốc độ hiện tại':<15} | {'Quãng đường':<15}"
        print(header)
        print("-" * len(header))
        for car in self.cars:
            print(f"{car.registration_number:<12} | {car.max_speed:<15} | {car.current_speed:<15} | {car.travelled_distance:<12.1f} km")
        print("-" * len(header))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False
if __name__ == "__main__":
    all_cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_v = random.randint(100, 200)
        all_cars.append(Car(reg_num, max_v))
    derby_race = Race("Grand Demolition Derby", 8000, all_cars)
    hours_count = 0
    while not derby_race.race_finished():
        derby_race.hour_passes()
        hours_count += 1
        if hours_count % 10 == 0:
            print(f"\nĐã qua {hours_count} giờ đua.")
            derby_race.print_status()
    print(f"\n kết thúc sau {hours_count} giờ")
    derby_race.print_status()

