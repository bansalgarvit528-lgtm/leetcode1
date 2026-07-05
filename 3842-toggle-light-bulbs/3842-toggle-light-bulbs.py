class Solution:
    def toggleLightBulbs(self, bulbs):
        on = set()

        for bulb in bulbs:
            if bulb in on:
                on.remove(bulb)
            else:
                on.add(bulb)

        return sorted(on)