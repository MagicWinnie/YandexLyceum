class Service:
    def __init__(self, address, id):
        self.address = address
        self.id = id
        self.d = {'address': address, 'id': id}

    def arrival_time(self):
        return len(self.address)

    def get(self):
        return self.d


class Ambulance(Service):
    def __init__(self, address, id, mode, severity):
        super().__init__(address, id)
        self.d['mode'] = mode
        self.d['severity'] = severity


class Firefighters(Service):
    def __init__(self, address, id, mode, victims):
        super().__init__(address, id)
        self.d['mode'] = mode
        self.d['victims'] = victims


class Police(Service):
    def __init__(self, address, id, mode, victims, armament_required):
        super().__init__(address, id)
        self.d['mode'] = mode
        self.d['victims'] = victims
        self.d['armament_required'] = armament_required
