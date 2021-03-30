class Settings:
    '''A class to manage all setting for our machine'''

    def __init__(self):
        # Screen settings
        self.header_style = {
                            'text-align': 'center', 
                            'color': 'white', 
                            'font-family': 'Helvetica',
                            'background-color': 'dodgerblue',
                            'top' : '0px',
                            #'width': '100%',
                            'margin' : '0px',
                            'padding' : '0px',
                            'border' : '0px'
        }
        self.dropdown_style = {
                    'position': 'left',
                    'top': '14px',
                    'right': '0px',
                    'width': '200px',
                    'height': '0',
                    'border-color': 'transparent transparent #fff transparent',
                    'font-family': 'Helvetica',
                    }
        self.div_style = {
                        'width': '100%', 
                        'text-align': 'center',
                        'border-color': 'transparent transparent #fff transparent',
                        'font-family': 'Helvetica',
                        'color': 'dodgerblue',
                        'font-size': '50px'
                        }
        self.background_style = {
            'background-image':'url("https://i.postimg.cc/TwHQGj6C/65.png")', 
            'background-size' : 'cover',
            'height': '100%', 
            'width': '100%',
            'position':'absolute',
            'background-repeat': 'no-repeat',
            'margin' : '0px',
            'padding' : '0px',
            'border' : '0px'
        }
    
    


