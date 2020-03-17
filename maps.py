# coding=utf-8

import googlemaps
import polyline
import poi
from datetime import datetime
from model.route import Route
from recommender import *



gmaps = googlemaps.Client(key='AIzaSyCPlQM2ArMI9NDj2LJYUM7UvOZjiAR_i14')
pois = poi.loadJson()
# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit

def get_directions(startPlace,endPlace,waypoints = None):
    return gmaps.directions(startPlace,endPlace,alternatives=True,waypoints=waypoints)


def poisPorRota(rota,pois,distance):
    pontos_de_rota = polyline.decode(rota['overview_polyline']['points'])

    pois_retorno = []
    for p in pontos_de_rota:
        pois_add = poi.poisInDistance(p,pois,distance)
        for poi_to_add in pois_add:
            if poi_to_add not in pois_retorno:
                pois_retorno.append(poi_to_add)
    return Route(rota,pois_retorno)



start_location = 'Pelourinho'
end_location = 'Praia Tubarão'

def score_by_route(route): # usada para obter informacoes das rotas
    pois_route = poisPorRota(route,pois,300) #chama funcao e passa os parametros pra retornar os pois
    #pois_route é uma variavel do tipo Route (route.py)
    pois_route.final_google_route = get_directions(start_location, end_location,waypoints=pois_route.get_pois_coordinates())[0] #wayponts = por onde a rota passa (pois)
    scores = []
    for p in pois_route.pois:
        scores.append((0,predict(999, p['item_id'])))
    pois_route.scores = scores
    pois_route.get_final_score()
    return pois_route


if __name__ == '__main__':
    routes = get_directions(start_location,end_location) #rotas iniciais
    train()

    pois_routes = [] #array com as rotas

    for route in routes: #para cada rota
        pois_routes.append(score_by_route(route)) #para cada rota a funcao eh chamada

    pois_routes.sort(key=lambda x: x.final_score, reverse=True) #??#

    for p in pois_routes:
        print('-----------')
        p.print_final_info()
        print('-----------')
    print("FIM")
    #print(pois_retorno)
