# This Python file uses the following encoding: utf-8
import random
from additional_lists import male_names_list, female_names_list, profession_list, title_list, peasant_title_profession_dict
from additional_funcs import with_probability


class GoodCharacter:
    def __init__(
            self,
            sex,
            age,
            name,
            feudal_staircase,
            children=None,
            partner=None,
            title=None,
            profession=None,
            father=None,
            mother=None,
            ):
            self.sex = sex
            self.age = age
            self.father = father
            self.mother = mother
            self.name = name
            self.feudal_staircase = feudal_staircase
            self.children = children
            self.partner = partner
            self.title = title
            self.profession = profession

    def __dict__(self):
        character = {
                "name": self.name,
                "age": self.age,
                "father": self.father,
                "mother": self.mother,
                "feudal_staircase": self.feudal_staircase,
                "children": self.children,
                "partner": self.partner,
                "title": self.title,
                "profession": self.profession,
        }
        return character

    def __repr__(self):
        return self.name + " " + str(self.age)

    @staticmethod
    def marriage(husband, wife):
        husband.partner = wife
        wife.partner = husband

    def str_represent(self):
        avocation = ""
        if self.feudal_staircase == "peasant":
            avocation = peasant_title_profession_dict["peasant"]
        elif self.title:
            avocation = peasant_title_profession_dict[self.title]
        elif self.profession:
            avocation = peasant_title_profession_dict[self.profession]

        main_character_decsription = f"""
        Имя: {self.name}, 
        Возраст: {self.age}
        {avocation}
        мать:
        {self.mother.str_represent() if self.mother else ""}
        отец:
        {self.father.str_represent() if self.father else ""}
        """
        return main_character_decsription



def get_older_character(potential_parent,age_of_character):
    if potential_parent.age - age_of_character > 14:
        return True
    return False


def get_same_age_character(potential_partner, character):
    if (potential_partner.age - character.age < 14) and (potential_partner.sex != character.sex) and (potential_partner.partner is None) and (potential_partner.age > 16):
        return True
    return False


def generate_families(feudal_staircase,  numb_of_characters):
    list_of_characters = []
    for i in range(numb_of_characters):
        character_sex = random.choice(["male", "female"])
        if character_sex == "male":
            character_name = random.choice(male_names_list)
        else:
            character_name = random.choice(female_names_list)
        character_age = random.randint(0, 70)
        character_peasant = feudal_staircase
        character = GoodCharacter(sex=character_sex, age=character_age, name=character_name, feudal_staircase=character_peasant, children=[])
        list_of_characters.append(character)
    for char in list_of_characters:
        if char.age < 16:
            potential_parent_list = sorted(filter(lambda x: get_older_character(x, char.age), list_of_characters), key= lambda x: x.age)
            potential_father_list = list(filter(lambda x: True if x.sex == "male" else False, potential_parent_list))
            potential_mother_list = list(filter(lambda x: True if x.sex == "female" else False, potential_parent_list))
            if potential_father_list == [] or potential_mother_list == []:
                continue
            if with_probability(80):  # с вероятностью 80% есть отец и мать
                father = random.choice(potential_father_list[:len(potential_father_list)//2+1])
                mother = random.choice(potential_mother_list[:len(potential_mother_list)//2+1])
                if not (father.partner or mother.partner):  # если кто-то из родителей ещё не женат, то родители автоматически становятся парой
                    char.mother = mother
                    char.father = father
                    mother.children.append(char)
                    father.children.append(char)
                    GoodCharacter.marriage(father, mother)
                else:
                    if father.partner:
                        char.father = father
                        char.mother = father.partner
                        father.children.append(char)
                        father.partner.children.append(char)
                    else:
                        char.mother = mother
                        char.father = mother.partner
                        mother.children.append(char)
                        mother.partner.children.append(char)
            else:
                if with_probability(50):  # если у ребенка один родитель, с вероятностью 50% это отец
                    father = random.choice(potential_father_list[:len(potential_father_list) // 2 + 1])
                    char.father = father
                    father.children.append(char)
                else:
                    mother = random.choice(potential_mother_list[:len(potential_mother_list) // 2 + 1])
                    char.mother = mother
                    mother.children.append(char)
        else:
            if char.sex == "male" and (char.partner is None):
                if with_probability(50):
                    potential_wife_list = list(filter(lambda x: get_same_age_character(x, char), list_of_characters))
                    if potential_wife_list:
                        potential_wife = random.choice(potential_wife_list)
                        GoodCharacter.marriage(char, potential_wife)
            elif char.sex == "female" and (char.partner is None):
                if with_probability(50):
                    potential_husband_list = list(filter(lambda x: get_same_age_character(x, char), list_of_characters))
                    if potential_husband_list:
                        potential_husband = random.choice(potential_husband_list)
                        GoodCharacter.marriage(potential_husband, char)
    return list_of_characters


def take_professions(citizen_list):
    for citizen in citizen_list:
        citizen.profession = random.choice(profession_list)


def take_titles(noble_list):
    have_queen_or_king = False
    for noble in noble_list:
        if noble.age > 15:
            if not have_queen_or_king:
                if noble.sex == "male":
                    noble.title = "king"
                    if noble.partner:
                        noble.partner.title = "queen"
                else:
                    noble.title = "queen"
                    if noble.partner:
                        noble.partner.title = "king"
                if children := noble.children:
                    for child in children:
                        if child.sex == "male":
                            child.title = "prince"
                        else:
                            child.title = "princess"
                have_queen_or_king = True
            elif not noble.title:
                noble.title = random.choice(title_list)
                if children := noble.children:
                    for child in children:
                       child.title = noble.title


def generate_characters(numb_of_characters):
    list_of_characters = []
    number_of_peasants = (numb_of_characters * random.randint(60, 71)) // 100
    number_of_citizen = numb_of_characters - number_of_peasants - ((numb_of_characters * random.randint(5, 10)) // 100)
    number_of_noble = numb_of_characters - number_of_peasants - number_of_citizen
    list_of_peasants = generate_families("peasant", number_of_peasants)
    list_of_citizen = generate_families("citizen", number_of_citizen)
    take_professions(list_of_citizen)
    list_of_noble = generate_families("noble", number_of_noble)
    take_titles(list_of_noble)
    list_of_characters.extend(list_of_peasants)
    list_of_characters.extend(list_of_citizen)
    list_of_characters.extend(list_of_noble)
    list_of_characters = list(filter(lambda x: False if x.age< 16 and x.mother is None and x.father is None else True, list_of_characters))
    return list_of_characters

characters = generate_characters(100)
main_character = random.choice(characters)
print(main_character.str_represent())