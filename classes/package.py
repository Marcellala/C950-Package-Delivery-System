class Package:
    def __init__(self, packageID, address, city, state, zipcode, delivery_deadline, mass, notes):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.notes = notes
        self.time_left_hub = None
        self.delivery_timestamp = None

    def convert_pseudotime(self, pseudotime):
        hours = int(pseudotime)
        minutes = int((pseudotime - float(hours)) * 60)
        string_time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)
        return string_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.packageID, self.address, self.city, self.state,
                                                           self.zipcode, self.delivery_deadline, self.mass, self.notes,
                                                           self.convert_pseudotime(self.time_left_hub),
                                                           self.convert_pseudotime(self.delivery_timestamp))
