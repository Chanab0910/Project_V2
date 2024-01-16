from analyse_results import Analyse

class GeneralAnalysis:
    def __init__(self):
        self.analyse = Analyse()
        self.dict_of_countries_place_came = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                     'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                     'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0, 'Iceland': 0,
                                     'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                     'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                     'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                     'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

        self.dict_of_countries_average_goals_scored = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                             'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                             'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0,
                                             'Iceland': 0,
                                             'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                             'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                             'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                             'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

        self.dict_of_countries_average_goals_conceded = {'Argentina': [0,0,0,0,0,0], 'Australia': [0,0,0,0,0,0], 'Austria': [0,0,0,0,0,0], 'Belgium': [0,0,0,0,0,0],
                                                       'Canada': [0,0,0,0,0,0],
                                                       'Croatia':[0,0,0,0,0,0], 'Czech Republic': [0,0,0,0,0,0], 'Denmark':[0,0,0,0,0,0],
                                                       'England': [0,0,0,0,0,0], 'Finland': [0,0,0,0,0,0], 'France': [0,0,0,0,0,0], 'Germany': [0,0,0,0,0,0],
                                                       'Hungary': [0,0,0,0,0,0],
                                                       'Iceland': [0,0,0,0,0,0],
                                                       'Ireland': [0,0,0,0,0], 'Italy': [0,0,0,0,0], 'Mexico': [0,0,0,0,0], 'Ghana': [0,0,0,0,0],
                                                       'Netherlands': [0,0,0,0,0], 'Morocco': [0,0,0,0,0], 'Norway': [0,0,0,0,0], 'Poland': [0,0,0,0,0],
                                                       'Portugal': [0,0,0,0,0],
                                                       'Romania': [0,0,0,0,0], 'Scotland': [0,0,0,0,0], 'Spain': [0,0,0,0,0], 'Sweden': [0,0,0,0,0],
                                                       'Ukraine': [0,0,0,0,0],
                                                       'USA': [0,0,0,0,0], 'Wales': [0,0,0,0,0], 'Japan': [0,0,0,0,0], 'China': [0,0,0,0,0]}


    def get_stats(self):
        self.get_average_goals()
        self.get_final_result()
        self.get_average_goals_conceded()

    def get_final_result(self):
        for country in self.dict_of_countries_place_came:
            self.dict_place = self.analyse.furthest_got_and_average_place(country)
            group_num = self.dict_place['Group']
            R16_num = self.dict_place['Round of 16']
            quarter_num = self.dict_place['Quarter-final']
            semi_num = self.dict_place['Semi-final']
            final_num = self.dict_place['Final']
            win_num = self.dict_place['Win']
            places = [group_num,R16_num,quarter_num,semi_num,final_num, win_num]
            self.dict_of_countries_place_came[country] = places

        for country in self.dict_of_countries_place_came:
            '''order in terms of: won most times then got to final most times etc going down untill a country has a better stat '''



    def get_average_goals(self):
        for country in self.dict_of_countries_average_goals_scored:
            average = self.analyse.get_all_goals_and_games_played(country)
            self.dict_of_countries_average_goals_scored[country] = average
        self.dict_of_countries_average_goals_scored = sorted(self.dict_of_countries_average_goals_scored)

    def get_average_goals_conceded(self):
        for country in self.dict_of_countries_average_goals_conceded:
            average = self.analyse.get_all_goals_and_games_played(country)
            self.dict_of_countries_average_goals_conceded[country] = average
        self.dict_of_countries_average_goals_conceded = sorted(self.dict_of_countries_average_goals_conceded)




if __name__ == '__main__':
    g = GeneralAnalysis()
    g.get_final_result()