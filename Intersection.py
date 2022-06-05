class Intersection:
    def __init__(self, id, name, idBeginStreet, idEndStreet, idBeginInter, idEndInter, distance, velocity, cost1, cost2, latitudeStreet,longitudeStreet, latitudInter, longitudeInter ):
        self.id = id
        self.name = name
        self.idBeginStreet = idBeginStreet
        self.idEndStreet = idEndStreet
        self.idBeginInter = idBeginInter
        self.idEndInter = idEndInter
        self.sitance = distance
        self.velocity = velocity
        self.cost1 = cost1
        self.cost2 = cost2
        self.latitudeStreet = latitudeStreet
        self.longitudeStreet = longitudeStreet
        self.latitudeInter = latitudInter
        self.longitudeInter = longitudeInter

    def getName(self):
        return self.name
    def getidBeginInter(self):
        return self.idBeginInter
    def getidEndInter(self):
        return self.idEndInter
    def getId(self):
        return self.id
    def getIdBeginStreet(self):
        return self.idBeginStreet
    def getIdEndStreet(self):
        return self.idEndStreet
    def getLatitudeInter(self):
        return self.latitudeInter
    def getLongitudeInter(self):
        return self.longitudeInter
        