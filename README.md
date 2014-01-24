# starterkit

![Starter kit](http://i43.tinypic.com/dztnpe.png)

### Setting up
```
$ git clone https://github.com/alveyworld-dev/starterkit
$ cd starterkit
$ python main.py
```

### Resources
* [Intro to game design](https://docs.google.com/presentation/d/11oSHUDFR2WoMJXsoLWD1vtIr-BZaxDjECcIPFVro8iA/edit?usp=sharing)
* [Using sprites](https://github.com/alveyworld-dev/starterkit/wiki/Sprites)
* [Setting a background](https://github.com/alveyworld-dev/starterkit/wiki/Background)
* [Audio](https://github.com/alveyworld-dev/starterkit/wiki/Audio)

### Overview
* `resources/` - Any game resources: fonts, sprites, sounds, music, etc.
* `source/` - Game source code
    - `draw.py` - Handles the `draw()` function
    - `game.py` - Global game variables
    - `graphics.py` - Helpful graphics functions
    - `sprite.py` - Sprite class
    - `update.py` - Handles the `update()` function

### Modifications
There are two main parts of the starter kit that you will want to start your
modifications to.

#### Game loop
The game loop is contained in `main.py`, and simply repeats `update` and `draw`
 until exited.

#### Update
`update` is where you will want to do all your math and basic game logic.
```python
def update():
    """
    Update game world here
    """

    # insert logic here
    
    return
```

#### Draw
`draw` is simply that - drawing the game world.  You should refrain from doing
and logic code in `draw`, use it simply for drawing.
```python
def draw():
    """
    Drawing logic
    """

    # Fill the screen with black
    game.screen.fill((240, 240, 240))
    
    # insert logic here

    # Don't change these
    pygame.display.update()
    pygame.display.flip()

    return
```
Notice that there is some code already in the function: you shouldn't change
these unless you know what you are doing.  Simply insert your own code after
the comment "insert logic here".

#### Init
The `game.init` function (located in the `source/game.py` file) can be modified to contain game-wide initilization routines, and is run once before the game loop starts.  It is useful to put variable assignments, resource loading, and any other setup that might need doing here.
```python
...
my_var = 0

def init():
    game.sprites["player"] = Sprite("player.png")
    my_var = game.sprites["player"].rect
    return
```

#### Using sprites
Using the `Sprite` class, it is possible to easily abstract the process of loading images, storing position, and drawing.

A sprite can be created by importing `sprite.Sprite` and providing it the filename of the image that will represent it and a position (as as tuple)
```python
from sprite import Sprite

my_sprite = Sprite("my_image.png", (50, 50))
```
The `Sprite` class contains several useful properties which can be manipulated at runtime:
* `Sprite.rect` - Rectangle describing sprite image, useful for collision detection
* `Sprite.image` - Texture representing the sprite
Sprites can be draw by invoking the `Sprite.draw` function.
```
my_sprite = Sprite("my_image.png", (50, 50))
my_sprite.draw()
```

Inside `game.py` exists a dictionary called `sprites`, which can be used to store and access sprites throughout the game.
```python
import game
from sprite import Sprite

my_sprite = Sprite("my_image.png")
game.sprites["player"] = my_sprite
```

#### Resources
When providing arguments to functions or classes that allow filenames to be taken (for example, the `sprite` class),
the files should be placed in the `resources/` folder.  When referencing your file, it is only nessisary to name
the file itself, not the full path.  For example:
```python
my_sprite = Sprite("test.png", (50, 50))
```
becomes
```python
my_sprite = Sprite("resources/test.png", (50, 50))
```

#### Keyboard input
You can check for keyboard input in the `update` function like so:
```python
for key in keys:
    if key == pygame.K_LEFT: # do whatever
```

### License
```
Copyright 2014 Joshua Beitler, Brandon Bench, Alveyworld

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
```