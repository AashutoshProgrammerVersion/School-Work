monsters_info_file = open("monsters_simple.txt", "r")
monsters_info = monsters_info_file.readlines()
monsters_info_dictionary = {}

for line in monsters_info:
    name, description = line.strip().split(",")
    monsters_info_dictionary[name] = description

monsters_info_file.close()

monsters_names_lowercase = [name.lower() for name in monsters_info_dictionary.keys()]
print("This program was made by Aashutosh")
monster_to_find = input("What monster would you like to find? Type here it in (try to get the letters and its order right): ")

if monster_to_find in monsters_info_dictionary.keys():
    print("Description: " + monsters_info_dictionary[monster_to_find])
elif monster_to_find in monsters_names_lowercase:
    for monster_name in monsters_info_dictionary.keys():
        if monster_to_find == monster_name.lower():
            monster_to_find = monster_name
            print("Description: " + monsters_info_dictionary[monster_to_find])
else:
    import difflib
    close_matches = difflib.get_close_matches(monster_to_find.lower(), monsters_names_lowercase)

    if len(close_matches) == 0:
        print("No monster as such is there.")
    else:
        print("Check if you meant any of these:")
        for possible_monster_name in close_matches:
            print(possible_monster_name)