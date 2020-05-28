# from ursina import *

# app = Ursina()

# player = Entity(model='cube', color=color.orange, scale_y=2)

# def update():   # update gets automatically called.
#     player.x += held_keys['d'] * .1
#     player.x -= held_keys['a'] * .1

# app.run() 
# from ursina import *

# # create a window
# app = Ursina()

# # most things in ursina are Entities. An Entity is a thing you place in the world.
# # you can think of them as GameObjects in Unity or Actors in Unreal.
# # the first paramenter tells us the Entity's model will be a 3d-model called 'cube'.
# # ursina includes some basic models like 'cube', 'sphere' and 'quad'.

# # the next parameter tells us the model's color should be orange.

# # 'scale_y=2' tells us how big the entity should be in the vertical axis, how tall it should be.
# # in ursina, positive x is right, positive y is up, and positive z is forward.

# player = Entity(model='cube', color=color.orange, scale_y=2)

# # create a function called 'update'.
# # this will automatically get called by the engine every frame.

# def update():
# 	player.x += held_keys['d'] * time.dt
# 	player.x -= held_keys['a'] * time.dt
# 	player.y += held_keys['w'] * time.dt
# 	player.y -= held_keys['s'] * time.dt

# # this part will make the player move left or right based on our input.
# # to check which keys are held down, we can check the held_keys dictionary.
# # 0 means not pressed and 1 means pressed.
# # time.dt is simply the time since the last frame. by multiplying with this, the
# # player will move at the same speed regardless of how fast the game runs.


# def input(key):
# 	pass
# 	# if key == 'w':
# 	# 	player.y += 1
# 	# 	invoke(setattr, player, 'y', player.y-1, delay=.25)
# 	# if key == 's':
# 	# 	player.y += 1
# 	# 	invoke(setattr, player, 'y', player.y-1, delay=.25)


# # start running the game
# app.run()


from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


app = Ursina()
window.color = color.light_gray
camera.orthographic = True
camera.fov = 20

ground = Entity(
    model = 'cube',
    color = color.olive.tint(-.4),
    z = -.1,
    y = -1,
    origin_y = .5,
    scale = (1000, 100, 10),
    collider = 'box',
    ignore = True,
    )

random.seed(4)
for i in range(10):
    Entity(
        model='cube', color=color.dark_gray, collider='box', ignore=True,
        position=(random.randint(-20,20), random.randint(0,10)),
        scale=(random.randint(1,20), random.randint(1,5), 10)
        )


player = PlatformerController2d(color=color.green.tint(-.3))
player.x=1
player.y = raycast(player.world_position, player.down).world_point[1]
camera.smooth_follow.offset[1] = 5

window.size = (window.fullscreen_size[0]//2, window.fullscreen_size[1]//2)
window.position = (int(window.size[0]), int(window.size[1]-(window.size[1]/2)))
window.borderless = False
window.fullscreen = False

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')

app.run()