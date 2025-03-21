from random import shuffle
def create_boxes():#create 5 boxes with 1 treasure
    boxes = ['empty', 'empty', 'empty', 'treasure', 'empty']
    shuffle(boxes)
    return boxes

def player_pick():#player pick a box to find the treasure
    guess = ''
    while guess not in ['0', '1', '2', '3', '4']:
        guess = input('Pick a box (0~4): ')
    return int(guess)

def check_result(boxes, guess):#check the result if the player found the treasure
    if boxes[guess] == 'treasure':
        print('You found the treasure!!')
    else:
        print('You found nothing...')

boxes = create_boxes()#create_boxes() will return a list of boxes
guess = player_pick()#player_pick() will return the index of the box that the player picked
check_result(boxes, guess)#check_result() will check if the player found the treasure
