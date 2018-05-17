# -*- encoding=utf8 -*-

# This script collects all food from fields
# and creates new food (wheat).
# This is a simple example how we can automate
# any Android game with Airtest framework.

from airtest.core.api import *

auto_setup(__file__)


carrot = Template(r"tpl1526539603051.png", record_pos=(0.078, -0.018), resolution=(1920, 1080))
wheat = Template(r"tpl1526539660349.png", record_pos=(0.189, 0.019), resolution=(1920, 1080))
empty_ground = Template(r"tpl1526542142544.png", record_pos=(-0.046, -0.106), resolution=(1920, 1080))
wheat_corn = Template(r"tpl1526540071043.png", record_pos=(-0.21, 0.193), resolution=(1920, 1080))



def collect_food(food_type):
    pos = exists(food_type)
    
    while (pos):
        touch(pos)
        touch(pos)
        pos = exists(food_type)


def create_new_food(food_corn_type):
    pos = exists(empty_ground)

    while (pos):
        touch(pos)
        touch(food_corn_type)
        swipe(food_corn_type, pos)


# Start the game:
start_app("com.playrix.township")

# Wait untill game will start and try to get daily bonus:
try:
    wait(Template(r"tpl1526538460045.png", record_pos=(0.003, 0.214), resolution=(1920, 1080)), 40)
    touch(Template(r"tpl1526538469927.png", record_pos=(0.003, 0.215), resolution=(1920, 1080)))
except:
    print('No daily bonus, okay..')


# Collect all food (you can add more different food here):
collect_food(carrot)
collect_food(wheat)

# Create more wheat (this method can be more smart and create
# limited amount of different food):
create_new_food(wheat_corn)

# This is it, run this script every 20 minutes and you
# will have unlimited amount of wheat :)
# Note - this is just an example, and we don't controll the
# available space in barn and etc. - so, sometimes script failed.