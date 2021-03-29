class Settings:
    '''A class to manage all setting for our machine'''

    def __init__(self):
        # Screen settings
        self.dropdown_style = {
                    'background-color':'DodgerBlue',
                    'position': 'left',
                    'top': '14px',
                    'right': '0px',
                    'width': '200px',
                    'height': '0',
                    'border-color': 'transparent transparent #fff transparent',
                    'font-family': 'Helvetica',
                    'color': 'DodgerBlue'
                    }
        self.div_style = {
                        'width': '100%', 
                        'text-align': 'center',
                        'border-color': 'transparent transparent #fff transparent',
                        'font-family': 'Helvetica',
                        'color': 'DodgerBlue',
                        'font-size': '50px'
                        }