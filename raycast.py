from ursina.entity import Entity
from ursina import *     
app = Ursina()
d = Entity(parent=app, position=(0,0,2), model='cube', color=color.orange, collider='box', scale=2)
e = Entity(model='cube', color=color.lime)

camera.position = (0, 15, -15)
camera.look_at(e)
speed = .01
rotation_speed = .1
intersection_marker = Entity(model='cube', scale=.2, color=color.red)

def update():
    e.position += e.forward * held_keys['w'] * speed
    e.position += e.left * held_keys['a'] * speed
    e.position += e.back * held_keys['s'] * speed
    e.position += e.right * held_keys['d'] * speed

    e.rotation_y -= held_keys['q'] * rotation_speed
    e.rotation_y += held_keys['e'] * rotation_speed

    ray = boxcast(e.world_position, e.forward, 3, thickness=.3, debug=False)
    intersection_marker.world_position = ray.world_point
    intersection_marker.visible = ray.hit
    if ray.hit:
        d.color = color.azure
    else:
        d.color = color.orange

t = time.time()
ray = boxcast(e.world_position, e.forward, 3, thickness=.3, debug=False)
print(time.time() - t)
raycast((0,0,-2), (0,0,1), 5, debug=False)

EditorCamera()
app.run()  