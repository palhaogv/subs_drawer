class Settings:
    '''A class to manage all setting for our machine'''

    def __init__(self):
        # Screen settings
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
                        'color': 'black',
                        'font-size': '50px'
                        }
        self.background_style = {
            'background-image':'url("https://i.postimg.cc/7YGCh1Gy/image.png")', 
            'height': '100%', 
            'width': '100%',
            'min-height': '1080', 
            'min-width': '1920',
            'max-height': '4000', 
            'max-width': '4000',
            'position':'absolute',
            'background-repeat': 'no-repeat'
        }
    
    


