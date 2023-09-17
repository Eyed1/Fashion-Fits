import sys
import os
sys.path.append("../database")
import clothe_database as cd
import gen_pairs

def get_best(db_path, user_num, weather, pair_func, trip_func):
    trips_list, pair_list = gen_pairs.gen_pairs(db_path, user_num)
    print(len(trips_list))
    print(len(pair_list))
    max_val_trip = -1e9
    max_val_pair = -1e9
    best_trip = [-1, -1, -1]
    for trip in trips_list:
        #print(trip)
        if trip_func(trip, weather) > max_val_trip:
            max_val_trip = trip_func(trip, weather)
            best_trip = trip
    best_pair = [-1, -1]
    for pair in pair_list:
        #print(pair)
        if pair_func(pair, weather) > max_val_pair:
            max_val_pair = pair_func(pair, weather)
            best_pair = pair 
    return best_trip, best_pair

def util1(cloth, weather):
    return cloth[0][3] + cloth[1][3] + cloth[2][3]

def util2(cloth, weather):
    return cloth[0][3]+ cloth[1][3]

#db_path = os.getcwd() + "/../database/fashion.db"
#a, b= get_best(db_path, -1, 0, util1, util2)
#print(a)
#print(b)

  
