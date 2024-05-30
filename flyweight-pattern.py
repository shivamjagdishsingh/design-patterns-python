from enum import Enum

class EthnicityFlyweight:
    def __init__(self, ethnicity):
        self.ethnicity = ethnicity

class EthnicityFactory:
    ethnicities = {}

    @staticmethod
    def get_ethenicity(ethnicity):
        if ethnicity not in EthnicityFactory.ethnicities:
            EthnicityFactory.ethnicities[ethnicity] = EthnicityFlyweight(ethnicity)
        return EthnicityFactory.ethnicities[ethnicity]

class Player:
    def __init__(self, ethnicity, rank):
        self.ethnicity_flyweight = EthnicityFactory.get_ethenicity(ethnicity)
        self.rank = rank

    def render(self):
        print(f"Character: {self.ethnicity_flyweight.ethnicity}, Font Size: {self.rank}")

class Ethnicity(Enum):
    AMERICAN = "AMERICAN"
    AFRICAN = "AFRICAN"
    EUROPEAN = "EUROPEAN"
    EASTASIAN = "EASTASIAN"
    WESTASIAN = "WESTASIAN"
    INDIAN = "INDIAN"

# Client code
characters = []
characters.append(Player(Ethnicity.INDIAN, 12))
characters.append(Player(Ethnicity.EUROPEAN, 14))
characters.append(Player(Ethnicity.INDIAN, 2))

for character in characters:
    character.render()

print(EthnicityFactory.ethnicities)

# Output
# Character: Ethnicity.INDIAN, Font Size: 12
# Character: Ethnicity.EUROPEAN, Font Size: 14
# Character: Ethnicity.INDIAN, Font Size: 2
# {<Ethnicity.INDIAN: 'INDIAN'>: <__main__.EthnicityFlyweight object at 0x00000257E2D6E090>, <Ethnicity.EUROPEAN: 'EUROPEAN'>: <__main__.EthnicityFlyweight object at 0x00000257E2D6D160>}