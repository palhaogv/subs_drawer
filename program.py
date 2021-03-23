import pandas as pd
import os
import numpy as np
import sys
import pygame
from settings import Settings
from draw import RandomSelector

class Program:
    def __init__(self):
        '''Initialize the program'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Roleta do BT0')


        # Set the background color
        self.bg_color = self.settings.white

        #Initial text
        self.initial_text = self.settings.font.render('Olá, comédia! Como está voce?', True, self.settings.green, self.settings.blue)
        self.initial_text_rect = self.initial_text.get_rect()
        self.initial_text_rect.topleft = self.settings.initial_text_position

    
    def run_program(self):
        '''Start the main loop for the program.'''
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            elif event.type == pygame.KEYDOWN:
                self._event(event)
            
    
    def _event(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_o:
            self.question = self.settings.font.render('Voce deseja sortear um BAN ou uma SKIN? Aperte B para ban ou S para skin.', True, self.settings.green, self.settings.blue)
            self.question_rect = self.question.get_rect()
            self.question_rect.topleft = self.settings.question_position
            self.screen.blit(self.question, self.question_rect)
        
        '''for event in pygame.event.get():
            if event.type == pygame.K_b:
                self.ban = RandomSelector().ban_select
                self.result = self.settings.font.render(f'Quem vai levar o BAN é... {self.ban}. PARABÉNS, F.')
                self.result_rect = self.result.get_rect()
                self.result_rect.topleft = self.settings.result_position
                self.screen.blit(self.result, self.result_rect)'''

    
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        # Redraw the screen during each pass trough the loop.
        self.screen.fill(self.bg_color)
        self.screen.blit(self.initial_text, self.initial_text_rect)
        # Make the most recently draw screen visible. 
        pygame.display.flip()

if __name__ == 'main':
    #Make a program instance, and run the program.
    ai = Program()
    ai.run_program()

Program().run_program()
