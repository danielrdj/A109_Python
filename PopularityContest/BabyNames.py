#########################################
# Daniel Johnson
# Assignment 6.2
# 4/26/19
#
# Description: This class holds information for single baby names
#########################################

class BabyName:
    def __init__(self, rank, name, num_birth):
        self.name = name
        self.rank = rank
        self.num_birth = num_birth

    def __str__(self):
        return"Name:", self.name, "\nRank:", self.rank, "\nNumber of Births:", self.num_birth

    def __gt__(self, baby_name_object):
        if self.num_birth > baby_name_object.num_birth:
            return True
        else:
            return False

    def __lt__(self, baby_name_object):
        if self.num_birth > baby_name_object.num_birth:
            return False
        else:
            return True
