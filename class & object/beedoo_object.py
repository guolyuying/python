from beedoo_class import beedoo

beedoo1 = beedoo("helmet_antenna", 2, "unknown", True) # creates a new INSTANCE
beedoo2 = beedoo("pigtail", 6, "hair", True)
beedoo3 = beedoo("weight_selecter", 3, "metal+plastic", False)
beedoo4 = beedoo("cod_gun_chain", 5, "plastic", False)

print(beedoo4.name)
print(beedoo4.franticness)
print(beedoo4.size)
print(beedoo4.material)


result = beedoo1.beeg()
print(result)





