from random import shuffle

def create_boxes():
    """Create 5 boxes with 1 treasure and shuffle them."""
    boxes = ['empty', 'empty', 'empty', 'treasure', 'empty']
    shuffle(boxes)
    return boxes

def player_pick():
    """Allow the player to pick a box by entering a number between 0 and 4."""
    guess = ''
    while guess not in ['0', '1', '2', '3', '4']:
        guess = input('Pick a box (0~4): ')
    return int(guess)

def check_result(boxes, guess):
    """Check if the player found the treasure."""
    if boxes[guess] == 'treasure':
        print('You found the treasure!! 🎉')
    else:
        print('You found nothing... 😢')

if __name__ == "__main__":
    boxes = create_boxes()  # Generate boxes
    guess = player_pick()  # Get player's guess
    check_result(boxes, guess)  # Check result

