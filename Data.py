class Data(object):

    def __init__(self):
        self.data = []

    def models(self,j):
        self.year = j.year
        self.value = j.value
        self.actor =  j.actor

    def item(self, i):
        return self.actor[self.models()]
