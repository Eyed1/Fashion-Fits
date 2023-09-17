import random

inner_top=[11,15,19,21,272,273,275,285,286,341,342,4454,4495,4496]
outer_top=[23,24,25,256,277,281,289,4455,4456]
pants=[27,28,29,237,238,239,240,241,253,255,278,279,280,282,284,287,288,4458,4459]

intop_match = ["sleeveless top", "tunic", "sweater", "tshirt", "male shirt", "male sweater", "male tshirt", \
        "male track suit", "male sports shirt", "male shirt", "male polo", "male shirt", "sweatshirt", "sweater"]
outtop_match = ["jacket", "coat", "blazer", "track jacket", "male suit jacket", "male suit", "male track jacket",\
        "male formal jacket", "male jacket"]
pants_match = ["jeans", "pants", "shorts", "jeans", "jeans", "jeans", "jeans", "pants", "sweatpants", "shorts", \
        "male jeans", "male suit pants", "male knee-length shorts", "male swim shorts", "male sweatpants", "male track pants",
         "male sports shorts", "male pants", "male pants"]

weather_hot_in = [0, 0.5, 0.5, 0, 0, 0.5, 0, 0.2, 0, 0, 0.2, 0, 0.4, 0.5]
weather_cold_in = [0.5 - weather_hot_in[i] for i in range(len(weather_hot_in))]
weather_hot_out = [0.4, 0.5, 0.5, 0.3, 0.4, 0.4, 0.3, 0.5, 0.4]
weather_cold_out = [0.5 - weather_hot_out[i] for i in range(len(weather_hot_out))]
weather_hot_bottom = [0.3, 0.4, 0, 0.3, 0.3, 0.3, 0.3, 0.4, 0.3, 0, 0.3, 0.5, 0.1, 0, 0.3, 0.2, 0, 0.4, 0.4]
weather_cold_bottom = [0.5 - weather_hot_bottom[i] for i in range(len(weather_hot_bottom))] 

#assert(len(weather_hot_in) == len(inner_top))
#assert(len(weather_hot_out) == len(outer_top))
#assert(len(weather_hot_bottom) == len(pants))

def find_indices(arr, k):
    indices = []
    if k not in arr:
        return -1
    for i in range(len(arr)):
        if arr[i] == k:
            indices.append(i)
    return random.choice(indices)

def get_name(clothe_id):
    if clothe_id in inner_top:
        return intop_match[inner_top.index(clothe_id)]
    if clothe_id in outer_top:
        return outtop_match[outer_top.index(clothe_id)]
    if clothe_id in pants:
        return pants_match[pants.index(clothe_id)]
    return "None"

def get_weather(clothes_id, weather):
    if clothe_id in inner_top:
        if weather == "hot":
            return weather_hot_in[inner_top.index(clothe_id)]
        if weather == "cold":
            return weather_cold_in[inner_top.index(clothe_id)]
    if clothe_id in outer_top:
        if weather == "hot":
            return weather_hot_out[inner_top.index(clothe_id)]
        if weather == "cold":
            return weather_cold_out[inner_top.index(clothe_id)]
    if clothe_id in pants:
        if weather == "hot":
            return weather_hot_bottom[inner_top.index(clothe_id)]
        if weather == "cold":
            return weather_cold_bottom[inner_top.index(clothe_id)]
    return 100 

def get_id(clothe_name):
    if clothe_name in intop_match:
        return inner_top[find_indices(intop_match, clothe_name)]
    if clothe_name in outtop_match:
        return outer_top[find_indices(outtop_match, clothe_name)]
    if clothe_name in pants_match:
        return pants[find_indices(pants_match, clothe_name)]
    return -1


