import re

class CatType():

    # self.__Name string
    # self.__Description string
    # self.__Weight real
    # self.__Length real
    # self.__LifeExpectancy real
    # self.__ImageUrl string
    def __init__(self, Name, Description, Weight, Length, LifeExpectancy, ImageUrl):
        self.__Name = Name
        self.__Description = Description
        self.__Weight = Weight
        self.__Length = Length
        self.__LifeExpectancy = LifeExpectancy
        self.__ImageUrl = ImageUrl

    def GetCatDetails(self):
        return tuple(self.__Name, self.__Description, self.__Weight, self.__Length, self.__LifeExpectancy, self.__ImageUrl)
    
    def GetCatLife(self):
        return self.__LifeExpectancy, self.__Name



list_of_cats = []

with open("CutestCats.txt", "r") as file:
    all_lines = [x.strip().replace("â€™", "'") for x in file.readlines() if x != "\n"]
    
    for i in range(5):
        Name = all_lines[i * 7]


        Description = all_lines[(i * 7) + 1]


        list_of_weights = [int(x) for x in re.findall(r'\d+', all_lines[(i * 7) + 2])]
        Weight = sum(list_of_weights) / len(list_of_weights)

        if ("foot" in (all_lines[(i * 7) + 3]).lower()) or ("feet" in (all_lines[(i * 7) + 3]).lower()):
            list_of_lengths = [int(x) for x in re.findall(r'\d+', all_lines[(i * 7) + 3])]

            if "a foot" in all_lines[(i * 7) + 3].lower():
                list_of_lengths.append(1)
            if "half" in all_lines[(i * 7) + 3].lower():
                list_of_lengths.append(0.5)

            Length = 30.48 * (sum(list_of_lengths) / len(list_of_lengths))

        if ("inches" in (all_lines[(i * 7) + 3]).lower()) or ("inch" in (all_lines[(i * 7) + 3]).lower()):
            list_of_lengths = [int(x) for x in re.findall(r'\d+', all_lines[(i * 7) + 3])]

            Length = 2.54 * (sum(list_of_lengths) / len(list_of_lengths))


        list_of_life_expectancies = [int(x) for x in re.findall(r'\d+', all_lines[(i * 7) + 5])]
        LifeExpectancy = sum(list_of_life_expectancies) / len(list_of_life_expectancies)


        ImageUrl = all_lines[(i * 7) + 6]


        list_of_cats.append(CatType(Name, Description, Weight, Length, LifeExpectancy, ImageUrl))



def CatsSortedByLifeExpectancy():
    sorted_cats = sorted(list_of_cats, key=lambda cat: cat.GetCatLife()[0])
    return sorted_cats