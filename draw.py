import pandas as pd
import numpy as np


class RandomSelector:
    """Class for all the machine functions to operate the machine tricks"""
    def __init__(self):
        """Get the excel file and transform it as a pandas dataframe"""
        self.df = pd.read_excel('subs.xlsx')

    def ban_select(self):
        """Select a random subscriber name that will be ban, 
        and return the message that is going to be the webpage output"""
        self.lineb = np.random.randint(0,(len(self.df)))
        self.ban = self.df.iloc[self.lineb, 0].split(',')[0]
        return f'O sorteado para ganhar um BAN foi:', f'{self.ban.upper()}\U0001F6AB'

    def skin_select(self):
        """Select a random subscriber name that will win a csgo skin, 
        and return the message that is going to be the webpage output"""
        self.lines = np.random.randint(0,(len(self.df)))
        self.skin = self.df.iloc[self.lines, 0].split(',')[0]
        return f'O sorteado para ganhar uma SKIN foi:', f'{self.skin.upper()}\U0001F52A'




