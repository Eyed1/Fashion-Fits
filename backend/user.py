import sys
import get_name
import find_best
import hard_code
import pickle
from sklearn.ensemble import RandomForestRegressor
sys.path.append("../database")
import clothe_database as cd

db_path = "../database/fashion.db"

def get_clothes(user_num):
    return cd.get_clothes(db_path, user_num = -1)

def add_clothes(clothe, user_num):
    cd.add_clothes(db_path, clothe, user_num = -1)

def add_inventory(inventory, user_num = -1):
    cd.add_clothes(db_path, inventory, user_num)

def pair_func(cloth, weather):
    #print(cloth[0])
    top = cloth[0][2]
    bottom = cloth[1][2]
    #print(top, bottom)
    reg2 = open("./data_files/regressor_size2.pkl", "rb")
    regress = pickle.load(reg2)
    prob = regress.predict([[top, bottom]])
    works = hard_code.find_match_pair(cloth[0], cloth[1])
    if not works:
        prob -= 0.5
    weather_sum = get_name.get_weather(top, weather) + get_name.get_weather(bottom, weather)
    prob -= 0.5*weather_sum
    return prob

def trip_func(cloth, weather):
    inner = cloth[0][2]
    outer = cloth[1][2]
    bottom = cloth[2][2]
    reg3 = open("./data_files/regressor_size3.pkl", "rb")
    regress = pickle.load(reg3)
    prob = regress.predict([[inner, outer, bottom]])
    works = hard_code.find_match_triple(cloth[0], cloth[1], cloth[2])
    if not works:
        prob -= 0.4
    weather_sum = get_name.get_weather(outer, weather) + get_name.get_weather(bottom, weather)
    prob -= 0.4*weather_sum
    return prob

def get_clothes(user_num, weather):
    return find_best.get_best(db_path, user_num, weather, pair_func, trip_func)

