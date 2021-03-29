class Settings:
    '''A class to manage all setting for our machine'''

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.initial_text_position = (50, 50)
        self.question_position = (50, 100)
        self.result_position = (50, 150)

        #Color settings
        self.light_blue = (135, 206, 235)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)