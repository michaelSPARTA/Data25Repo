class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location -> (Longitude = {self.longitude}, Latitude = {self.latitude})"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(bham_academy)
