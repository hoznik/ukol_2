import geocoder 
import math

def geocode_cities(pocet_mest): 
    souradnice_list=[]
    for i in range(pocet_mest):
        result = geocoder.osm(mesta_list[i]).current_result
        if result is not None:
            muj_tuple = (result.eastnorth[1],result.eastnorth[0])
            souradnice_list.append(muj_tuple)

    with open('souradnice.txt', 'w') as f:
        for souradnice in souradnice_list:
            f.write("{},{}\n".format(souradnice[0],souradnice[1]))

def vzdalenost_bodu(souradnice_1,souradnice_2):
    vzdalenost = math.dist([souradnice_1[0],souradnice_1[1]],[souradnice_2[0],souradnice_2[1]])
    return vzdalenost

def reverse(souradnice):
    with open("reverzni.txt", "w") as f:
        for coord in souradnice:
            result = geocoder.osm([coord[0], coord[1]], method='reverse')
            f.write("coordinates: {}, {} - city: {}, county: {}, country: {}\n".format(coord[0], coord[1], result.current_result.city, result.current_result.county, result.current_result.country))
      
            



with open('coordinates.csv', 'r', encoding='UTF-8') as f:
    souradnice_list = [line.rstrip() for line in f]
souradnice_list.remove(souradnice_list[0])

with open('world-cities.csv', 'r', encoding='UTF-8') as f:
    mesta_list = [line.rstrip() for line in f]
mesta_list.remove(mesta_list[0])

souradnice_body=[]
for i in range(0,len(souradnice_list),2):
    souradnice = (float(souradnice_list[i].split("\"")[3]), float(souradnice_list[i+1].split("\"")[3]) )
    souradnice_body.append(souradnice)

souradnice_mesta=[]

with open('souradnice.txt', 'r', encoding='UTF-8') as f:
    radky = [line.rstrip() for line in f]
    for mesto in radky:
        dvojice = mesto.split(",")
        souradnice_mesta.append((float(dvojice[0]),float(dvojice[1])))

min = 99999999999999999
dvojice_bodu=[]
for bod in souradnice_body:
    for mesto in souradnice_mesta: 
        vzdalenost = vzdalenost_bodu(bod,mesto)
        if vzdalenost < min:
            min = vzdalenost
            min_mesto = mesto
    dvojice_bodu.append((bod,min_mesto))

with open('nejblizsi_body.txt', 'w') as f:
        for bod in dvojice_bodu:
            f.write("N {} E {} ===== N {} E {}\n".format(bod[0][0],bod[0][1],bod[1][0],bod[1][1]))
            
reverse(souradnice_body)
geocode_cities(70)


        





