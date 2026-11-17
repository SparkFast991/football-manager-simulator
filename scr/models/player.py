class Player:
    def __init__(self, name, age,attack, defense,International_Reputation, stamina,position,market_value,potential,emotions,nationality,club,number):
        self.name = name
        self.age = age
        self.position = position
        self.market_value = market_value
        self.potential = potential
        self.emotions = emotions
        self.nationality = nationality
        self.club = club
        self.number = number
        self.attack = attack
        self.defense = defense
        self.stamina = stamina
        self.International_Reputation = International_Reputation
    def calculate_overall_rating(self):
        if self.position == "ST" or self.position == "RW" or self.position == "LW":
            rating = (self.attack*0.8 + self.defense*0.05 + self.stamina*0.15)+self.International_Reputation
        if self.position == "CM " or self.position == "CAM":
            rating = (self.attack*0.5 + self.defense*0.3 + self.stamina*0.2)+self.International_Reputation
        if self.position == "CB" or self.position == "LB " or self.position == "RB":
            rating = (self.attack*0.1 + self.defense*0.75 + self.stamina*0.15)+self.International_Reputation
        return rating