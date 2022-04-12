class EternityBell:
    def __init__(self, sound, size, volume):
        self.sound = sound
        self.size = size
        self.volume = volume

    def __sub__(self, other):
        new_sound = min(self.sound, other.sound, key=lambda x: (len(x), x))
        new_size = (self.size + other.size) // 2
        new_volume = max(self.volume, other.volume)

        return EternityBell(new_sound, new_size, new_volume)

    def __iadd__(self, line):
        self.sound += "-" + line
        return self

    def __mul__(self, num):
        return [
            EternityBell(
                self.sound,
                max(1, self.size // num),
                max(1, self.volume % num)
            ) for _ in range(num)
        ]

    def __str__(self):
        return f"A bell of size {self.size} rings loudly ({self.volume}): ringing {self.sound.capitalize()}."

    def __repr__(self):
        return f"EternityBell('{self.sound}', {self.size}, {self.volume})"
