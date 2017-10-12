def get_description():
    """Return random weather, just like the pors"""
    from random import choice
    list = ['rain', 'snow', 'sleet', 'fog', 'sun']
    return choice(list)