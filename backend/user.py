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
    return cd.get_clothes(db_path, user_num)

def add_clothes(clothe, user_num):
    cd.add_clothes(db_path, clothe, user_num)

def add_inventory(inventory, user_num):
    cd.add_clothes(db_path, inventory, user_num)

def pair_func(cloth, weather):
    top = get_name.get_id(cloth[0][2])
    bottom = get_name.get_id(cloth[1][2])
    reg2 = open("./data_files/regressor_size2.pkl", "rb")
    regress = pickle.load(reg2)
    prob = regress.predict([[top, bottom]])
    works = hard_code.find_match_pair(top, bottom)
    if not works:
        prob -= 0.5
    weather_sum = get_name.get_weather(top, weather) + get_name.get_weather(bottom, weather)
    prob -= 0.5*weather_sum
    return prob

def trip_func(cloth, weather):
    inner = get_name.get_id(cloth[0][2])
    outer = get_name.get_id(cloth[1][2])
    bottom = get_name.get_id(cloth[2][2])
    reg3 = open("./data_files/regressor_size3.pkl", "rb")
    regress = pickle.load(reg3)
    prob = regress.predict([[inner, outer, bottom]])
    works = hard_code.find_match_triple(inner, outer, bottom)
    if not works:
        prob -= 0.5
    weather_sum = get_name.get_weather(outer, weather) + get_name.get_weather(bottom, weather)
    prob -= 0.5*weather_sum
    return prob

def get_clothes(user_num, weather):
    return find_best.get_best(db_path, user_num, weather, pair_func, trip_func)

