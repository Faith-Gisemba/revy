class Drum:
    def __init__(self,material,size): 
        self.material = material
        self.size = size
        # self.name=name

    # def show(self):
    #     pass

class Djembe(Drum):
    # def __init__(self,material,size):
    #     super().__init__(material,size)


    def show(self):
        print("Djembe: Has wide range of tones")


class Talking_Drum(Drum):
    def __init__(self,material,size,shape):
        super().__init__(material,size,shape)

    def show(self):
        print(f"Talking_Drum: Mimics the lines of human speech {self.size} and {self.shape}")


class Bourgarabou(Drum):
    def __init__(self,material,size):
        super().__init__(material,size)

    def show(self):
        print("Bourgarabou: Has deep rich bass tones")


# djembe = Djembe()
# talking_drum = Talking_Drum("Leather", 78)
# bourgarabou = Bourgarabou(3,5)
# djembe.show()
# talking_drum.show()
# bourgarabou.show()
talking_drum = Talking_Drum("cotton",56,"Oval")
talking_drum.show()

