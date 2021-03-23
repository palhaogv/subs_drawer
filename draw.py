import pandas as pd
import os
import numpy as np
import sys
import pygame

class RandomSelector:
    def __init__(self):
        self.df = pd.read_excel('subs.xlsx')

    def ban_select(self):
        self.lineb = np.random.randint(0,(len(self.df)))
        self.ban = self.df.iloc[self.lineb, 0].split(',')[0]
        #return print(f'O sorteado para o BAN foi: {self.ban}')
        return self.ban

    def skin_select(self):
        self.lines = np.random.randint(0,(len(self.df)))
        self.skin = self.df.iloc[self.lines, 0].split(',')[0]
        while True:
            if self.lines == self.lineb:
                self.lines = np.random.randint(0,(len(self.df)))
            else:
                break

        return print(f'O sorteado para o BAN foi: {self.skin}')

    def question(self):
        self.quest = input(str('Voc'))

    
