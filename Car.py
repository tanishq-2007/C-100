class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print('started')

    def stop(self):
        print('stopped')

    def accelerate(self):
        print('acclerating...')
    
    def change_gear(self):
        print('gear Changed')

audi = Car('A6','Red','Audi','100 kmph')
print(audi.color)
audi.start()
audi.change_gear()