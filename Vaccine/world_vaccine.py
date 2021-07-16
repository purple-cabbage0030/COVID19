from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import platform
import requests


class Crawling():
    def vaccine():
        world_vac = pd.read_csv('vaccinations.csv')
        world_vac = world_vac.fillna(0)
        g1 = world_vac.groupby(world_vac['location']).sum().reset_index()
        g1 = g1.drop(['total_vaccinations_per_hundred','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred','daily_vaccinations_per_million'],axis=1)
        del_nat = ['Africa', 'Anguilla', 'Aruba', 'Asia', 'Bermuda', 'British Virgin Islands',
        'Cayman Islands', 'Cook Islands', 'Curacao', 'England', 'Europe', 'European Union', 
        'Faeroe Islands', 'Falkland Islands', 'French Polynesia', 'Gibraltar', 'Greenland',
        'Guernsey', 'High income', 'Hong Kong', 'Isle of Man', 'Jersey', 'Kosovo', 'Low income',
        'Lower middle income', 'Macao', 'Montserrat', 'New Caledonia', 'Niue', 'North America',
        'Northern Cyprus', 'Northern Ireland', 'Oceania', 'Palestine', 'Pitcairn', 'Saint Helena',
        'Scotland', 'Sint Maarten (Dutch part)', 'South America', 'Taiwan', 'Turks and Caicos Islands',
        'Upper middle income', 'Wales', 'Wallis and Futuna', 'World','Bonaire Sint Eustatius and Saba', 
        'Egypt', 'Kyrgyzstan', 'Nauru', 'Syria', 'Tonga', 'Turkmenistan','Tuvalu', 'Venezuela']

        n_index = []
        for i in range(len(g1)):
            for j in range(len(del_nat)):
                if g1['location'][i] == del_nat[j]:
                    n_index.append(i)
        g1.drop(index=n_index, inplace=True)
        vac_data = g1.reset_index()
        del vac_data['index']
        vac_data.to_csv("./total_vaccine.csv", index = False)


if __name__ == "__main__":
    Crawling.vaccine()