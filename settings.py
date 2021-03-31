class Settings:
    '''A class to manage all machine settings '''

    def __init__(self):
        #Header style
        self.header_style = {
                            'text-align': 'center', 
                            'color': 'white', 
                            'font-family': 'Consolas',
                            'background-color': 'rgb(17, 166, 224)',
                            'top' : '0px',
                            'margin' : '0px',
                            'padding' : '0px',
                            'border' : '0px'
        }

        #First bracket style
        self.bracket_style1 = {
                            'display': 'block', 
                            'content': '""', 
                            'margin-top': '4.5%'
        }

        #Second bracket style
        self.bracket_style2 = {
                            'display': 'block', 
                            'content': '""', 
                            'margin-top': '9%'
        }

        #Dropdown button style
        self.dropdown_style = {
                            'position': 'left',
                            'top': '14px',
                            'right': '0px',
                            'width': '200px',
                            'height': '0px',
                            'border-color': 'transparent transparent #fff transparent',
                            'font-family': 'Consolas',
        }

        #Announcing message style
        self.div_style1 = {
                            'width': '100%', 
                            'text-align': 'center',
                            'border-color': 'transparent transparent #fff transparent',
                            'font-family': 'Consolas',
                            'color': 'rgb(17, 166, 224)',
                            'font-size': '50px',
                            'margin' : '0',
                            'padding' : '0',
                            'text-transform' : 'uppercase',
                            '-webkit-text-fill-color': 'transparent',
                            '-webkit-text-stroke-width': '2px'
        }
        
        #Banned name style
        self.div_style_ban = {
                            'text-align': 'center',
                            #'border-color': '#fff',
                            'font-family': 'Consolas',
                            'color': 'red',
                            'font-size': '50px',
                            'margin' : '0',
                            'padding' : '0',
                            'font-weight': '700'
        }

        #Skin winner style
        self.div_style_skin = {
                            'width': '100%', 
                            'text-align': 'center',
                            'border-color': 'transparent transparent #fff transparent',
                            'font-family': 'Consolas',
                            'color': 'green',
                            'font-size': '50px',
                            'margin' : '0',
                            'padding' : '0',
                            'font-weight': '700'
        }

        #Background_style
        self.background_style = {
                            'background-image':'url("https://i.postimg.cc/TwHQGj6C/65.png")', 
                            'background-size' : 'cover',
                            'height': '100%', 
                            'width': '100%',
                            'position':'absolute',
                            'background-repeat': 'no-repeat',
                            'margin' : '0',
                            'padding' : '0',
                            'border' : '0',
                            'box-sizing': 'border-box'
        }
