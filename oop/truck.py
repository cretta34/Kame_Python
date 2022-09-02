from car import Car


class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loadings):
        super().__init__(model_name, mileage, manufacturer)
        self._max_loadings = max_loadings
        self._loadings = 0

    def gas(self):
        if self._loadings > self._max_loadings:
            print("重量オーバーなので走れません")
            print(f"最低でも{self._loadings - self._max_loadings}tの荷物を降ろしてください")
        else:
            super().gas()

    def load(self, weight):
        if weight > 0:
            print(f"{weight}tの荷物を積みました")
            self._loadings += weight
        else:
            if self._loadings <= -weight:
                print(f"{self._loadings}t全ての荷物を降ろしました")
                self._loadings = 0
            else:
                print(f"{-weight}tの荷物を降ろしました")
                # weightは負の値なので、+=で足し算をする
                self._loadings += weight
        print(f"現在の積載量は{self._loadings}tです")
        if self._loadings > self._max_loadings:
            print(f"最大積載量を{self._loadings - self._max_loadings}tオーバーしています")


if __name__ == "__main__":
    isuzu_truck = Truck('トラックA', 6, 'いすゞ', 10)
    isuzu_truck.gas()
    isuzu_truck.load(5)
    isuzu_truck.load(-3)
    isuzu_truck.load(10)
    isuzu_truck.gas()
    isuzu_truck.load(-30)
