class greeting:
    def hello(self, name=None):
        if name is not None:
            print("Hello",name)
        else:
            print("Hello")
mygreeting = greeting()
mygreeting.hello("Chris")
mygreeting.hello()