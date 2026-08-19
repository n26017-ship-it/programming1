class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "しゃり"

    def show_attributes(self):
        print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))
        print("price: {}円".format(self.price))

class Katsuo(Nigiri):
    top="かつお"
    topping="生姜とねぎ"
    price=100

    def show_attributes(self):
        super().show_attributes()
        print("topping:{}".format(self.topping))

K1=Katsuo()
K1.show_attributes()
