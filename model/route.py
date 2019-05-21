# coding=utf-8

class Route:

    def __init__(self,googleRoute,pois):
        self.google_route = googleRoute #rota inicial google
        self.pois = pois #pontos de interesse
        self.route_with_waypoints = False
        self.scores = [] #scores das predições
        self.final_score = 0.0 #score final (apos a aplicacao da equacao)
        self.final_google_route = None #rota final redesehada passando pelos pois
        self.final_distance = 0.0 #distancia da rota final

    def get_pois_coordinates(self):
        pois_return = []
        for poi in self.pois:
            pois_return.append((poi['latitude'],poi['longitude']))
        return pois_return

    #funcao = ([quant pois] * [soma_scores] * 1000) / distancia final
    def get_final_score(self): #aplica a funcao e salva na variavel final_score
        self.final_distance = 0.0
        for l in self.final_google_route['legs']: #soma as distancas das "pernas" das rotas
            self.final_distance += l['distance']['value']
        len_pois = len(self.pois) #quantas posicoes existem no arrayde pois
        sum_score = sum([x[1] for x in self.scores]) #soma todos os scores
        self.final_score = ((len_pois * sum_score)* 1000) / self.final_distance

    def print_final_info(self, legs = False):
        print("Rota por " + self.final_google_route['summary'])
        print("Distancia (metros): " + str(self.final_distance))
        print("Score final : " + str(self.final_score))
        for p in self.pois:
            print(p['name'])
        if(legs):
            for l in self.final_google_route[u'legs']:
                for s in l[u'steps']:
                    print(s[u'html_instructions'])


    