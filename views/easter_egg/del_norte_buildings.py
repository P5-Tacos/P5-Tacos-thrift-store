import json

a_buildings = [101, 102, 107, 124, 125, 126, 136, 135, 148, 144, 150, 151]
p_buildings = [101, 104, 107, 108,111, 116]
n_buildings = [113, 122]
m_buildings = [116, 101]

l1_buildings = [101, 102, 103, 104]
l2_buildings = [110, 111, 112, 113, 114, 115, 116, 117, 118]

k2_buildings = [101, 102, 103, 104, 105, 106]

j1_buildings = [101, 102, 103, 104, 105, 106]
j2_buildings = [110, 111, 112, 113, 114, 115, 116, 117, 118]

g1_buildings = [101, 102, 103, 104]
g2_buildings = [110, 111, 112, 113, 114, 115, 116, 117, 118]

e2_buildings = [101, 102, 103, 104, 105, 106]

d1_buildings = [101, 102, 103, 104]
d2_buildings = [110, 111, 112, 113, 114, 115, 116, 117, 118]

b_buildings = [111, 113, 115, 121, 123, 125, 128]

all_buildings_list = [a_buildings, p_buildings, n_buildings, m_buildings, l1_buildings, l2_buildings, k2_buildings, j1_buildings, j2_buildings, g1_buildings, g2_buildings, e2_buildings, d1_buildings, d2_buildings, b_buildings]
food_court = []
administration = []
library = []

all_buildings_dict = {
    "a_buildings": a_buildings,
    "p_buildings": p_buildings,
    "n_buildings": n_buildings,
    "m_buildings": m_buildings,
    "l1_buildings": l1_buildings,
    "l2_buildings": l2_buildings,
    "k2_buildings": k2_buildings,
    "j1_buildings": j1_buildings,
    "j2_buildings": j2_buildings,
    "g1_buildings": g1_buildings,
    "g2_buildings": g2_buildings,
    "e2_buildings": e2_buildings,
    "d1_buildings": d1_buildings,
    "d2_buildings": d2_buildings,
    "b_buildings": b_buildings
}

a_buildings_str = []
p_buildings_str = []
n_buildings_str = []
m_buildings_str = []

l1_buildings_str = []
l2_buildings_str = []

k2_buildings_str = []

j1_buildings_str = []
j2_buildings_str = []

g1_buildings_str = []
g2_buildings_str = []

e2_buildings_str = []

d1_buildings_str = []
d2_buildings_str = []

b_buildings_str = []

all_buildings_list_str = [a_buildings_str, p_buildings_str, n_buildings_str, m_buildings_str, l1_buildings_str, l2_buildings_str, k2_buildings_str, j1_buildings_str, j2_buildings_str, g1_buildings_str, g2_buildings_str, e2_buildings_str, d1_buildings_str, d2_buildings_str, b_buildings_str]

a = 0
for i in all_buildings_dict:
    first_letter = i[0]
    list_rooms = all_buildings_dict[i]

    x = 0
    #print("this is a value:" + str(a))
    building_to_append_to = all_buildings_list_str[a]
    for b in list_rooms:
        #print(str(first_letter) + str(list_rooms[x]))
        item_to_append = str(first_letter) + str(list_rooms[x])
        x = x + 1
        building_to_append_to.append(item_to_append)
        #print(first_letter + str(list_rooms[b]))
    a = a + 1
#print(all_buildings_list_str)

#this dict can be replaced with a loop that itteratrs through the list wtih str values to rplace each dict value
all_buildings_dict_str = {
    "a_buildings": {"room": a_buildings_str},
    "p_buildings": {"room": p_buildings_str},
    "n_buildings": {"room": n_buildings_str},
    "m_buildings": {"room": m_buildings_str},
    "l1_buildings": {"room": l1_buildings_str},
    "l2_buildings": {"room": l2_buildings_str},
    "k2_buildings": {"room": k2_buildings_str},
    "j1_buildings": {"room": j1_buildings_str},
    "j2_buildings": {"room": j2_buildings_str},
    "g1_buildings": {"room": g1_buildings_str},
    "g2_buildings": {"room": g2_buildings_str},
    "e2_buildings": {"room": e2_buildings_str},
    "d1_buildings": {"room": d1_buildings_str},
    "d2_buildings": {"room": d2_buildings_str},
    "b_buildings": {"room": b_buildings_str}
}

#print(all_buildings_dict_str)

#from python to JSON
json_all_building = json.dumps(all_buildings_dict_str)
#print(json_all_building)

def all_buildings_dict_str():
    return [a_buildings_str, p_buildings_str, n_buildings_str, m_buildings_str, l1_buildings_str, l2_buildings_str, k2_buildings_str, j1_buildings_str, j2_buildings_str, g1_buildings_str, g2_buildings_str, e2_buildings_str, d1_buildings_str, d2_buildings_str, b_buildings_str]
#print(str([a_buildings_str, p_buildings_str, n_buildings_str, m_buildings_str, l1_buildings_str, l2_buildings_str, k2_buildings_str, j1_buildings_str, j2_buildings_str, g1_buildings_str, g2_buildings_str, e2_buildings_str, d1_buildings_str, d2_buildings_str, b_buildings_str]))
