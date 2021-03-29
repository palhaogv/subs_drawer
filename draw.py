import pandas as pd
import numpy as np


class RandomSelector:
    def __init__(self):
        self.df = pd.read_excel('subs.xlsx')

    def ban_select(self):
        self.lineb = np.random.randint(0,(len(self.df)))
        self.ban = self.df.iloc[self.lineb, 0].split(',')[0]
        return f'O sorteado para ganhar um BAN foi:', f'{self.ban.upper()}'
        

    def skin_select(self):
        self.lines = np.random.randint(0,(len(self.df)))
        self.skin = self.df.iloc[self.lines, 0].split(',')[0]
        return f'O sorteado para ganhar um SKIN foi:', f'{self.skin.upper()}'




