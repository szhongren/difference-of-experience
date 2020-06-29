from enum import Enum
from random import random, randint
from pprint import pprint

BASE_R_SCORE = 0.0001
INTERACTIONS_PER_DAY = 3
A_TOTAL = 76 * 300
B_TOTAL = 13 * 300
C_TOTAL = 11 * 300
TOTAL_PEOPLE = A_TOTAL + B_TOTAL + C_TOTAL
DAYS = 60
ECHO_CHAMBER = False

class Race(Enum):
    A = 1
    B = 2
    C = 3

class InteractionsSummary:
    def __init__(self):
        self.total_people = 0
        self.total_interactions = 0
        self.total_good_interactions = 0
        self.total_bad_interactions = 0
        self.total_r_score = 0

    def add_interactions(self, interactions):
        self.total_people += 1
        good_interactions = interactions["good"]
        bad_interactions = interactions["bad"]
        self.total_interactions += good_interactions + bad_interactions
        self.total_good_interactions += good_interactions
        self.total_bad_interactions += bad_interactions
    
    def add_r_score(self, r_score):
        self.total_r_score += r_score

class Person:
    def __init__(self, race=Race.A):
        self.race = race
        self.interactions = {
            "bad": 0,
            "good": 0,
        }
        self.r_score = BASE_R_SCORE
    
    def interact_with(self, other_person):
        if other_person.race == self.race:
            other_person.interactions["good"] += 1
            if ECHO_CHAMBER:
                other_person.r_score *= 1.001
            return

        if random() <= self.r_score:
            other_person.interactions["bad"] += 1
            if ECHO_CHAMBER:
                other_person.r_score *= 1.01
        else:
            other_person.interactions["good"] += 1
            if ECHO_CHAMBER:
                other_person.r_score *= .99

def main():
    people = [Person(Race.A) for _ in range(A_TOTAL)] + [Person(Race.B) for _ in range(B_TOTAL)] + [Person(Race.C) for _ in range(C_TOTAL)]
    for day in range(DAYS):
        for i, person in enumerate(people):
            for _ in range(INTERACTIONS_PER_DAY):
                other_i = randint(0, TOTAL_PEOPLE - 1)
                while other_i == i:
                    other_i = randint(0, TOTAL_PEOPLE - 1)
                other_person = people[other_i]
                person.interact_with(other_person)
                other_person.interact_with(person)
        print(f"day: {day}")
    interactions_summaries = {
        Race.A: InteractionsSummary(),
        Race.B: InteractionsSummary(),
        Race.C: InteractionsSummary()
    }
    for person in people:
        interactions_summaries[person.race].add_interactions(person.interactions)
        interactions_summaries[person.race].add_r_score(person.r_score)
        # print(tup)
    for k, v in interactions_summaries.items():
        print(k)
        print(f"total people: {v.total_people}")
        print(f"average interactions: {v.total_interactions / v.total_people}")
        print(f"average bad interactions: {v.total_bad_interactions / v.total_people}")
        print(f"average good interactions: {v.total_good_interactions / v.total_people}")
        print(f"average prevalance: {v.total_r_score / v.total_people}")

if __name__ == "__main__":
    main()