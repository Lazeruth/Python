
import pygame
import time

# Initialize pygame
pygame.init()


# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Velocity")


# Define colors
WHITE = (255, 255, 255)


# Define the font for rendering text
font = pygame.font.SysFont('High Tower Text', 24)


# Define the game screens
def welcome():
    text = font.render('-' * 120, True, WHITE)
    window.blit(text, (40, 40))
    text = font.render(' ' * 40 + 'Welcome to Escape Velocity', True, WHITE)
    window.blit(text, (40, 80))
    text = font.render('-' * 120, True, WHITE)
    window.blit(text, (40, 120))


def intro():
    text = font.render('''As you journey through the vast expanse of the GMLR42 – Major Planetary System, your ship is 
suddenly ambushed by a fierce Unknown Luminous Entity. In a desperate attempt to evade its grasp, you make a 
frantic escape and manage to take refuge on the nearby planet of GMLR42 – Minor. After repairing your damaged ship, 
you set out to explore the area and discover that there are seven mysterious objects floating in space around 
GMLR42 – Minor. Perhaps these enigmatic objects hold clues to the whereabouts of the Unknown Luminous Entity. 
However, you realize that facing such a formidable foe without proper preparation could be your undoing. 
It would be wise to study these objects and accept any help they may offer before confronting the Unknown 
Luminous Entity.\n''', True, WHITE)
    window.blit(text, (40, 160))


def menu():
    text = font.render('-' * 120, True, WHITE)
    window.blit(text, (40, 360))
    text = font.render('\nMovement directions: North, East, South, West', True, WHITE)
    window.blit(text, (40, 400))
    text = font.render('Typing End will end the game.\n', True, WHITE)
    window.blit(text, (40, 440))
    text = font.render('-' * 120, True, WHITE)
    window.blit(text, (40, 480))


def player_location(current_planet, planets, player_inventory):
    window.fill((0, 0, 0))
    text = font.render('-' * 120, True, WHITE)
    window.blit(text, (40, 40))
    text = font.render('You touch down on {}'.format(current_planet), True, WHITE)
    window.blit(text, (40, 80))
    text = font.render('\n{}'.format(planets[current_planet]['Desc']), True, WHITE)
    window.blit(text, (40, 120))
    text = font.render('\nYou have the following items in your inventory: {}'.format(player_inventory), True, WHITE)
    window.blit(text, (40, 160))
    text = font.render('-' * 120, True, WHITE)
    window.blit(text, (40, 200))
    pygame.display.flip()


def win_scenario():
    text = font.render('''Congratulations! With all six items now in your possession, your cloaking device enables you 
    to launch a surprise attack on your foe! By utilizing the Relic of Knowledge, you merge the Relic of Power with your 
    anti-matter rail gun and employ the Relic of Enfeeblement to weaken your opponent. With your ship's plating now 
    reinforced, you withstand a massive strike from the Unknown Luminous Entity, allowing you to unleash a fatal blow 
    with your anti-matter rail gun and claim victory over your enemy!\n
    Thank you for playing!''', True, WHITE)
    window.blit(text, (40, 240))
    pygame.display.flip()


def lose_scenario():
    text = font.render('''The Unknown Luminous Entity lands a devastating blow on your ship, causing irreparable damage 
    to your life support systems and hull. Without the aid of the six scattered items located across GMLR42 - Major, 
    your ship cannot be repaired and your journey comes to an unfortunate end.\n
    Better luck next time!''', True, WHITE)
    window.blit(text, (40, 240))
    pygame.display.flip()


# Dictionary that connects all the planets and items
planets = {
    'GMLR42-Minor': {'East': 'GammaNu', 'Desc': 'This planet orbits a pulsating blue star, causing everything on its '
                     'surface to glow with a faint blue light.'},
    'GammaNu': {'East': 'ZetaRho', 'South': 'DeltaEpsilon', 'West': 'GMLR42-Minor', 'Item': 'Relic Of Knowledge',
                'Desc': 'A violent storm rages perpetually on this planet, with winds strong enough to tear apart the '
                'strongest of structures.'},
    'ZetaRho': {'West': 'GammaNu', 'South': 'OmicronPi', 'Item': 'Relic Of Power', 'Desc': 'The planet is entirely '
                'covered in a deep, crystalline ice sheet, with sparkling frozen spires that jut out of the '
                'ground like needles.'},
    'OmicronPi': {'West': 'DeltaEpsilon', 'North': 'ZetaRho', 'South': 'KappaXi', 'Item': 'Cloaking Device',
                  'Desc': 'The planets surface is covered in a vibrant, iridescent flora that seems to pulsate with '
                  'life.'},
    'DeltaEpsilon': {'North': 'GammaNu', 'East': 'OmicronPi', 'South': 'Tenebris', 'West': 'Tau',
                     'Item': 'Relic Of Enfeeblement',
                     'Desc': 'A series of massive geysers spew molten lava and boiling steam '
                     'high into the sky, making the planet a deadly and unpredictable place to explore.'},
    'Tau': {'East': 'DeltaEpsilon', 'Item': 'Anti-matter Rail Gun', 'Desc': 'The planet is completely devoid of life, '
            'and the only structures that can be found are the ruins of an ancient civilization that seem to predate '
            'the universe itself.'},
    'KappaXi': {'North': 'OmicronPi', 'Item': 'Reinforced Ship Plating', 'Desc': 'Every inch of the planets surface '
                'is covered in a dense, maze-like forest, with towering trees that block out the sky and twisting vines'
                'that seem to move of their own accord.'}
}

# Create list of directions to error check user input
directions = ['North', 'East', 'South', 'West']


# Create the player inventory
player_inventory = []


# Set the player to the current starting planet
current_planet = 'GMLR42-Minor'


# Call the welcome, intro, and menu screens
welcome()
intro()
time.sleep(10)
menu()
time.sleep(4)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_location(current_planet, planets, player_inventory)

    # Picking up the items and adding them to the player's inventory
    if current_planet != 'Tenebris' and 'Item' in planets[current_planet].keys():
        text = font.render('\nYou see a {} in the distance.'.format(planets[current_planet]['Item']), True, WHITE)
        window.blit(text, (40, 240))
        text = font.render('\nDo you want to take the {}? Y or N'.format(planets[current_planet]['Item']), True, WHITE)
        window.blit(text, (40, 280))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        player_inventory.append(planets[current_planet]['Item'])
                        print('\nYou pick up the {}.'.format(planets[current_planet]['Item']))
                        print('\nCurrent inventory:', player_inventory)
                        del planets[current_planet]['Item']
                        if len(player_inventory) == 6:
                            win_scenario()
                            break
                        pygame.time.wait(1000)
                        break
                    elif event.key == pygame.K_n:
                        print('You leave the {}.'.format(planets[current_planet]['Item']))
                        pygame.time.wait(1000)
                        break
                elif event.type == pygame.QUIT:
                    running = False
                    break

            if len(player_inventory) == 6 or running == False:
                break

    # Moving the player between the different planets
    command = input('\nWhat direction would you like to take off in?\n')

    if command in directions:
        if command in planets[current_planet]:
            current_planet = planets[current_planet][command]

            # Win/Lose scenario
            if current_planet == 'Tenebris':
                if len(player_inventory) == 6:
                    win_scenario()
                else:
                    lose_scenario()
                pygame.time.wait(3000)
                running = False

        # Not an exit
        else:
            print('\nIt is not safe to take off in that direction!')

    # Ending the game
    elif command == 'End':
        print('\nQuitting so soon? Thanks for playing! Goodbye')
        pygame.time.wait(1000)
        running = False

    # Invalid user input
    else:
        print('Please enter a valid movement command')

# Quit the game
pygame.quit()
