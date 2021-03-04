import robots


class Melon(object):
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon and squash.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return (f"{self.color} {self.weight} lbs {self.melon_type}")

class Squash(object):
    """Winter squash."""

    def __init__(self, squash_type):
        """Initialize melon and squash.

        melon_type: type of melon being built.
        """

        self.squash_type = squash_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
        robots.painterbot.paint(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.squash_type
        else:
            return (f"{self.color} {self.weight} lbs {self.squash_type}")

