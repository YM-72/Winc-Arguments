# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting = 'Hello, <name>!'):
    n_greet = greeting.replace('<name>', name)
    #print(n_greet)
    return(n_greet)

# Greet
name = 'Duck'
greeting = 'Hello, <name>!'
greet(name, greeting)

    
def force(mass, body = "earth"):
    planets = {
    "sun": 274,
    "jupiter": 24.92,
    "neptune": 11.15,
    "saturn": 10.44,
    "earth": 9.798,
    "uranus": 8.87,
    "venus": 8.87,
    "mars": 3.71,
    "mercury": 3.7,
    "moon": 1.62,
    "pluto": 0.58
    }
    planet_grav = (planets[body])
    planet_grav_round = float(f'{planet_grav:.1f}')
    the_force = (float(mass)*planet_grav_round)
    #print (the_force)
    return (the_force)

   

# Force
mass = 0.1 # an apple
body = 'earth'
force(mass, body)

def pull(m1, m2, d):
    g = 6.674*(10**-11)
    f = (g*m1*m2)/(d**2)
    #print (f)
    return(f)

# Gravity
m1 = 800
m2 = 1500
d = 3
pull = (m1, m2, d)
    


