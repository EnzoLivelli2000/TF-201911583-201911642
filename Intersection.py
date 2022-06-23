class Intersection:
    def __init__(self, id, name, idBeginStreet, idEndStreet, idBeginInter, idEndInter, distance, velocity, cost1, cost2, latitudeBeginInter,longitudeBeginInter, latitudEndInter, longitudeEndInter ):
        self.id = id
        self.name = name
        self.idBeginStreet = idBeginStreet
        self.idEndStreet = idEndStreet
        self.idBeginInter = idBeginInter
        self.idEndInter = idEndInter
        self.distance = distance
        self.velocity = velocity
        self.cost1 = cost1
        self.cost2 = cost2
        self.latitudeBeginInter = latitudeBeginInter
        self.longitudeBeginInter = longitudeBeginInter
        self.latitudeEndInter = latitudEndInter
        self.longitudeEndInter = longitudeEndInter

    def getName(self):
        return self.name
    def getIdBeginInter(self):
        return self.idBeginInter
    def getIdEndInter(self):
        return self.idEndInter
    def getId(self):
        return self.id
    def getLatitudeBeginInter(self):
        return self.latitudeBeginInter
    def getLongitudeBeginInter(self):
        return self.longitudeBeginInter
    def getLatitudeEndInter(self):
        return self.latitudeEndInter
    def getLongitudeEndInter(self):
        return self.longitudeEndInter
    def getDistance(self):
        return self.distance
        