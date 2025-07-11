import random
import pgzrun

HEIGHT=600
WIDTH=800

start_speed = 10
ITEMS=["bag","battery","bottle","chips"]

final_level=6
current_level=1

#lose the game
game_over=False

#win the game
game_complete=False

items=[]
animations=[]

def draw():
    global items, current_level, game_complete, game_over
    screen.clear()
    screen.blit("bground", (0,0))

    if game_over:
        display_message("GAME OVER", "Try again.")
    elif game_complete:
        display_message("YOU WON", "Well done.")
    else:
        for item in items:
            item.draw()

def display_message(heading,subheading):
    screen.draw.text(heading, fontsize=60, center=(400,300), color="black")
    screen.draw.text(subheading, fontsize=30, center=(400,330), color="blue")

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

#Make items
#1. select random items from ITEMS list
#2. create actors and add it to items list
#3. do the items with correct positions - layout items
#4. move the objects down with animation - animate items

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(0, number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gaps_size = WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gaps_size
        item.x= new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = start_speed-current_level
        animation = animate(item, duration = duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global items, current_level, animations, game_complete
    stop_animation(animations)
    if current_level == final_level:
        game_complete = True
    else:
        current_level = current_level+1
        animations=[]
        items=[]

def stop_animation(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
    
pgzrun.go()
