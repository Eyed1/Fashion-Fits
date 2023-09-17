import user
import warnings
warnings.filterwarnings("ignore")

a, b = user.get_clothes(-1, "hot")
#print(len(a))
#print(len(b))

print(a[0], user.pair_func(a[0], "hot"))
print(a[1], user.pair_func(a[1], "hot"))

print(b[0], user.trip_func(b[0], "hot"))
print(b[1], user.trip_func(b[1], "hot"))
