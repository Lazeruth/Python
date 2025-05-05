# calculate the carbs in cat food. Can be either wet or dry food.

def instructions():
    print('You will need to have the protein %, fat %, fiber %, ash %, and moisture % to calculate.')
    print('If there is no ash % listed, then assume 7% ash content for dry and 3% ash content for wet\n')
    print('Enter 0 to quit program')


instructions()


while True:

    protein = float(input('Enter the protein %\n'))
    if protein == 0:
        print('Exiting program')
        break
    fat = float(input('Enter the fat %\n'))
    if fat == 0:
        print('Exiting program')
        break
    fiber = float(input('Enter the fiber %\n'))
    if fiber == 0:
        print('Exiting program')
        break
    ash = float(input('Enter the ash %\n'))
    if ash == 0:
        print('Exiting program')
        break
    moisture = float(input('Enter the moisture %\n'))
    if moisture == 0:
        print('Exiting program')
        break

    carbs = round(100 - protein - fat - fiber - ash - moisture, 2)

    dry_matter = round(100 - moisture, 2)

    actual_carbs = round((carbs / dry_matter) * 100, 2)

    print('\nTotal carbs are', carbs, 'and actual carbs are', actual_carbs)
