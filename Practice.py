class Info_car :
    def __init__(self, name, type, produce, range): # 차량 정보를 입력하는 함수
        self.name = name # 차량이름
        self.type = type # 기름종류(전기차일시 "전기", 수소차일시 "수소"로 기입)
        self.produce = produce # 생산연도
        self.range = range # 주행거리
    def info(self):  # 차랑 정보를 출력하는 함수
        print(f"차량종류 : {self.name}")
        print(f"기름종류 : {self.type}")
        print(f"생산연도 : {self.produce}")
        print(f"주행거리 : {self.range}")
    def type_car(self): # 차량 기름 종류에 따른 사고방지를 위한 주유 방법을 안내하는 함수
        if self.type == "휘발유" : # 휘발유 주유 방법
            print("사고방지를 위해 시동을 끄고 주유하고 노란색 혹은 빨간색 노즐을 사용해주세요.")
        elif self.type == "경유" : # 경유 주유 방법
            print("사고방지를 위해 시동을 끄고 주유하고 초록색 노즐을 사용해주세요.")
        else : # 전기차, 수소차 주유 방법
            print("사고방지를 위해 시동을 끄고 충전하되 충전이 완료되면 플러그를 뽑아주세요.")
    def tire_car(self): # 차량의 타이어 마모상태를 점검하는 함수
        a = int(input("타이어를 교체했던 키로수를 알려주세요.")) # 마지막 타이어 교체 키로수 입력
        b = int(self.range) - a # 타이어 교체 후 주행거리 계산
        # 타어이 교체 시기에 따른 안내
        if b >= 60000 :
            print(f"타이어 교체를 안한지 {b}km 되었으므로 당장 교체해주세요.")
        elif 60000 > b >= 45000 :
            print(f"타이어 교체를 안한지 {b}km 되었으므로 여유가 있으실 때 교체해주세요.")
        else :
            print(f"타어이 교체를 안한지 {b}km 되었으므로 아직 교체를 안하셔도 무방합니다.")
    def produce_car(self): # 차량 구매 후 몇 년이 지났는지 확인하는 함수
        a = int(input("몇 년도인지 입력해주세요(예시 : 24년-> 2024 :"))
        b = a - int(self.produce) # 현재와 차량 생산연도의 차이 계산
        print(f"이 차량은 {b}년된 차량입니다.")
    def range_car(self): # 차량 엔진오일 교체를 위한 함수
        a = int(input("마지막 엔진오일 교체 주행거리를 입력하세요 :"))
        b = int(self.range) - a # 마지막 엔진오일 교체 후 주행거리 계산 함수
        # 엔진오일 교체 여부 안내
        if b >= 10000 :
            print("안전을 위해 엔진오일을 교환하세요.")
        else :
            print("엔진오일을 안갈아도 무방합니다.")

# (반드시 입력)본인의 차량 정보 입력 - > 예시) my_car = Info_car("제네시스", "경유", "2020", "45000")
# 차량 정보를 출력하는 함수 호출법 -> my_car.info()
# 주유 방법을 안내하는 함수 출력법 -> my_car.type_car()
# 차량의 타이어 교체 여부를 알려주는 함수 출력법 -> my_car.tire_car()
# 차량이 구매 후 몇 년이 지났는지 알려주는 함수 출력법 -> my_car.produce_car()
# 차량 엔진오일 교체 여부를 알려주는 함수 출력법 -> my_car.range_car()