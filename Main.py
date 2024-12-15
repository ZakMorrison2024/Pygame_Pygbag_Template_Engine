###########################################################################################################################################
###########################################################################################################################################
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pygame",
#   "os",
#   "random",
#   "math",
#   "sys",
#   "threading",
#   "socket",
#   "datetime",
#   "select",
#   "asyncio"
# ]
# ///
#####################################################
## Libraries:
##################################################
import pygame # Pygame
from pygame.locals import QUIT # Locals
import os # Operating Systems Library
import random # Random
import math # Math
import sys # System
import socket # Sockets
import threading # Multi-threading
import datetime # date and time
import select # select
import asyncio # async
###################################################
##################################################
# GLOBAL VARIABLES:
###################################################
# Colours: (RGB)
##################################################
BLACK = (0, 0, 0) # Black
WHITE = (255, 255, 255) # White
GREEN = (0, 255, 0) # Green
RED = (255, 0, 0) # Red
YELLOW = (255,255,0) # Yellow
BLUE = (0,0,255) # Blue
##################################################
### GAME DESCRIPTIVE:
##################################################
Author = "" # Game Director
Co_Author = [] # Game Co-developers
Company = "" # Game Company
Title = "" # Game
Genre = "" # Type of Game
Decription = "" # Info on Game
Date_of_Release = "--/--/----" # Release date of game
Contact = [] # Contact details
Rating_Age = "" # Age rating for game
##################################################
# GAME:
##################################################
abs_cwd_path_ts = os.path.abspath(os.getcwd()) # absolute working directory string
width, height = 960, 540 # Default APR: 16:9 1.777, RESO DIMEN: 960 x 540 px (1920 x 1080 % 2), scale resolution by 2.
FONT = pygame.font.Font(None, 36) # Font
splash_trigger = False # trigger for splash screen
##################################################
### GAME NETWORK:
##################################################
Multiplayer = False # Network mode
player_name = "" # Network alias
hostname = socket.gethostname() # Hostname
My_IP = socket.gethostbyname(hostname) # Player IP address
PORT = 8080 # Player Port
Server = False # Server Mode
Client = False # Client Mode
max_clients = 8 # Max number of connections
online_host_address = "" # Server IP address
online_host_port = "" # Server PORT number
logs = [] # logs for server
##################################################
### GAME SCENES/MAPS:
##################################################
SPLASH = True # Splash Window
MENU = False # Menu Window
ROOM = False # Room Placeholder
# ... add more? ...
################################################
### Camera
################################################
class Camera: # Camera Class
   def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height) # Set boundary
        self.room_width = 0 # Default room width
        self.room_height = 0 # Default room height
   def apply(self, entity):
        return entity.rect.move(self.camera.topleft) # Return Camera
   def move_manually(self,vx,vy):
        x = -vx + int(self.camera.width / 2) # Move Camera along X axis
        y = -vy + int(self.camera.height / 2) # Move Camera along Y axis
        x = min(0, x) # Limit Camera along X axis, min
        y = min(0, y) # Limit Camera along Y axis, min
        x = max(-(self.room_width - self.camera.width), x)  # Limit Camera along X axis, max
        y = max(-(self.room_height - self.camera.height), y) # Limit Camera along Y axis, max
        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height) # Set boundary
   def update(self, target_rect):
        x = -target_rect.centerx + int(self.camera.width / 2) # Move Camera along X axis, following target
        y = -target_rect.centery + int(self.camera.height / 2) # Move Camera along Y axis, following target
        x = min(0, x) # Limit Camera along X axis, min
        y = min(0, y) # Limit Camera along Y axis, min
        x = max(-(self.room_width - self.camera.width), x) # Limit Camera along X axis, max
        y = max(-(self.room_height - self.camera.height), y) # Limit Camera along Y axis, max
        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)  # Set boundary
   def set_room_size(self, width, height):
        self.room_width = width # Set room width
        self.room_height = height # Set room height
camera = Camera(width,height) # intiate camera, set resolusion to default game resolution
##################################################
### Room: ROOM_0. defintions: (Room/Level #0)
##################################################
def room_0(): # Level_0
   width = 1920 # width dimention of level
   height = 1080 # height dimention of level
   max_spawns = 6 # max_number of spawns for NPCs
   NPC_spawn_local_width = width/max_spawns # even of spawns for NPCs
   NPC_spawn_local_height = height/max_spawns # even of spawns for NPCs
   no_of_spawn_points = 1 # spawns tally for NPCs
   spawn_points_enemies = [] # NPC spawn points
   Current_Entities = 0 # Entities on screen/in map
   Max_Entities = 50 # Max Entities on map
   Total_Entities = 100 # Total Level Entities
   Entities_difficulty = 0.10 # Enemy difficulty multiplier
   if no_of_spawn_points < max_spawns:
      spawn_points_enemies[no_of_spawn_points] = [(NPC_spawn_local_width*no_of_spawn_points),(NPC_spawn_local_height*no_of_spawn_points)] # Find locations of spawns for NPCs
      no_of_spawn_points += 1 # tally up
   if current_room == game_levels[0]:
      IN_GAME_TIME += dt # increase level timer
   Camera.set_room_size(width,height) # Set room dimensions with Camera
##################################################
### Room: ROOM_1. defintions: (Room/Level #1)
##################################################
def room_1(): # Level_1
   width = 1920 # width dimention of level
   height = 1080 # height dimention of level
   max_spawns = 8 # max_number of spawns for NPCs
   NPC_spawn_local_width = width/max_spawns # even of spawns for NPCs
   NPC_spawn_local_height = height/max_spawns # even of spawns for NPCs
   no_of_spawn_points = 1 # spawns tally for NPCs
   spawn_points_enemies = []  # NPC spawn points
   Current_Entities = 0 # Entities on screen/in map
   Max_Entities = 75 # Max Entities on map
   Total_Entities = 120 # Total Level Entities
   Entities_difficulty = 0.15 # Enemy difficulty multiplier
   if no_of_spawn_points < max_spawns:
      spawn_points_enemies[no_of_spawn_points] = [(NPC_spawn_local_width*no_of_spawn_points),(NPC_spawn_local_height*no_of_spawn_points)] # Find locations of spawns for NPCs
      no_of_spawn_points += 1 # tally up
   if current_room == game_levels[1]:
      IN_GAME_TIME += dt # increase level timer
   Camera.set_room_size(width,height) # Set room dimensions with Camera
##################################################
### GAME MECHANICAL:
##################################################
dt = 0 # Delta Time/Step-Up Clock
PAUSE = False # For the Pause menu
interacted = False # Variable to know if a pointer had pressed
game_levels = [room_0(),room_1()] # List of all avalible levels
current_room = "splash_room" # To know which stage we're on
room_width = current_room.width # Change Room Dimension
room_height = current_room.height # Change Room Dimension
temporal_measurements = datetime.datetime.now() # Find Date
splash_trigger = False # Splash trigger
##################################################
## BRANDING:
##################################################
### GAME SPLASH SCREEN OBJECT:
class splash(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs/COMPANY_ASSETS/","###-SPLASH_PLACEHOLDER.FILE-###")))
#     self.img_org = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs/COMPANY_ASSETS/","###-SPLASH_PLACEHOLDER.FILE-###")))  - With Pre-Defined PATH Variable
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
   def update(self): # Behaviour loop
      pass
###########################################################################################################################################
##################################################
### Classes/Objects (MENU):
##################################################
################### Button_0 # PLAY
class Button_0(pygame.sprite.Sprite): ### Object Template
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      ## Primary image placeholder:
      self.img_org = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png"))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
   def update(self): # Behaviour loop
      if self.rect.collidepoint(pygame.mouse.get_pos()): # Check collision with mouse
         if interacted == True: # if interacted
            MENU = False # menu finished
            ROOM = True # game room start
            current_rooms = game_levels[0] # game level
            self.kill() # destory button
################### Button_1 # Multiplayer
class Button_1(pygame.sprite.Sprite): ### Object Template
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      ## Primary image placeholder:
      self.img_org =pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png"))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
   def update(self): # Behaviour loop
      if self.rect.collidepoint(pygame.mouse.get_pos()): # Check collision with mouse
         if interacted == True: # if interacted
            Multiplayer = True
            self.kill()
################### Button_2 # SERVER
class Button_2(pygame.sprite.Sprite): ### Object Template
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      ## Primary image placeholder:
      self.img_org = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png")) 
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
   def update(self): # Behaviour loop
      if self.rect.collidepoint(pygame.mouse.get_pos()): # Check collision with mouse
         if interacted == True: # if interacted
            Server = True
            self.kill() # destory button
################### Button_3 # Client
class Button_3(pygame.sprite.Sprite): ### Object Template
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      ## Primary image placeholder:
      self.img_org = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png")) 
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
   def update(self): # Behaviour loop
      if self.rect.collidepoint(pygame.mouse.get_pos()): # Check collision with mouse
         if interacted == True: # if interacted
            Client = True
            self.kill() # destory button
###########################################################################################################################################
##################################################
### Classes/Objects (in-Game):
##################################################
################### Object_0
class Object_0(pygame.sprite.Sprite): ### Object Template, showing features one can add to object to define the objects nature and interactions (Non-playable Character Ver.)
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      ## Primary image placeholder:
      self.img_org = [pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png")),    
         abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE_2-####.png")] # - List Placeholder for second (or more) images for animation # All With Pre-Defined PATH Variable
      ## Secondary image placeholders:
      self.img_attack = [pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_0-####.png")),    
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_1-####.png"),
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_2-####.png")]
     # Death:
      self.image_death = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-CORPSE-####.png"))
     ## Image Loading: (init)
      self.image = self.img_org[0] # Set Default image
      self.img_pre_render = self.img_org[0]
      # Animation Mechanics 
      self.max_frames = len(self.img_pre_render)
      self.current_frame = 0 ## current frame for animation
      self.animation_time = 0.1 ## threshold for next frame (time)
      self.current_time = 0 ## current timing for animation
     ## Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y
      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      # Locals
      self.target = 0 ## chasing this object or coordinate
      self.health = 100 # object life
      self.speed = 3 # object speed
      self.value = 20 # object value
      self.inventory = [] # object invetory
      self.hostile = False # object temperament
      self.damage = 5 # base damage
      self.debuff = 2 # base draw back
      self.damage_calc = 0 # varaible for calculation
      # ... etc etc
   def update(self, dt): # Main behaviour loop
     ## Animation/Image_edit:
     
     self.image = self.img_pre_render
          ## LIFE 
     if self.health <= 0:
           self.death = True
     if self.death == False: # Check if Alive/Active
      # Make instance rotate around point (define point by px,py)
      px,py = self.target.x,self.target.y # center point of rotation
      rel_x, rel_y = round(px - self.rect.x), round(py - self.rect.y) # find difference between target and rect coordinates
      angle = round((180/math.pi)*+math.atan2(rel_x,rel_y)) # Trignometery for rotation
      self.image = pygame.transform.rotate(self.image_clean,angle) # rotate image
      self.rect = self.image.get_rect(center=self.rect.center) # set new boundary/collision_box
      if self.current_frame >= self.max_frame: # Animation Frame loop
          self.current_frame = 0 # reset current frame
          if self.moving == True or self.attacking == True: # Animation Trigger
            if self.moving == True :
                self.img_pre_render = self.img_org # set image pre_render variable to orginal animation
            if self.attacking == True:
                self.img_pre_render = self.img_attack # set image pre_render variable to attack animation
            self.current_time += dt ## Increase animation time
            if self.current_time >= self.animation_time:
                self.current_time = 0 # timing for the animation
                self.current_frame = (self.current_frame + 1) % len(self.img_pre_render) # increase animation step until at max frame
            else:
               self.current_time = 0 # reset
               self.current_frame = 0 # reset
     else:
       self.img_pre_render = self.img_death # Set to dead sprite

       ## Add more functionality Here:
       ## i.e.....:
       if self.target != 0:
            if self.attacking == True:
                 if self.current_frame == 3: # Placeholder number, edit for your needs.
                      self.debuff = self.debuff + (self.debuff*self.target.damage) # increase debuff by targets attack
                      self.damage_calc = self.damage/self.debuff # work out how much damage will be dealth during attack
                      self.target.life -= self.damage_calc # deal said damage
##################################################
##################################################
##################################################
################### Object_1
class Object_1(pygame.sprite.Sprite): ### Object Template, showing features one can add to object to define the objects nature and interactions (playable Character Ver.)
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups)
      ## Primary image placeholder:
      self.img_org =[pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png")),    
         abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE_2-####.png")] # - List Placeholder for second (or more) images for animation # All With Pre-Defined PATH Variable
      ## Secondary image placeholders:
      self.img_attack = [pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_0-####.png")),    
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_1-####.png"),
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_2-####.png")]
      self.image_death = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-CORPSE-####.png"))
      ## Image Loading: (init)
      self.image = self.img_org[0] # Set Default image
      self.img_pre_render = 0
      # Animation Mechanics 
      self.max_frames = len(self.img_pre_render)
      self.current_frame = 0 ## current frame for animation
      self.animation_time = 0.1 ## threshold for next frame (time)
      self.current_time = 0 ## current timing for animation
      ## Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y
      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      # Locals
      self.health = 100 # object life
      self.speed = 3 # object speed
      self.value = 20 # object value
      self.inventory = [] # object invetory
      self.hostile = False # object temperament
      self.damage = 5 # base damage
      self.debuff = 2 # base draw back
      self.damage_calc = 0 # varaible for calculation
      # ... etc etc
   def update(self, dt): # Main behaviour loop
        ## Animation/Image_edit:
        self.image = self.img_pre_render # load pre-rendered sprite
        ## LIFE 
        if self.health <= 0:
          self.death = True ### dead!
        if self.death == False: # Check if Alive/Active
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                 if self.rect.y < room_height and self.rect.y > 0:
                           self.rect.y -= 2 # move up
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                 if self.rect.x < room_width and self.rect.x > 0:
                           self.rect.x += 2 # move right
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                 if self.rect.x < room_width and self.rect.x > 0:
                           self.rect.x -= 2 # move left
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                 if self.rect.y < room_height and self.rect.y > 0:
                           self.rect.y += 2 # move down
           # Make instance rotate around point (define point by px,py)
            mx,my = pygame.mouse.get_pos() # center point of mouse (assuming this game is a top-down or requires the player to face the mouse)
            rel_x, rel_y = round(mx - self.rect.x), round(my - self.rect.y) # find difference between mouse and rect coordinates
            angle = round((180/math.pi)*+math.atan2(rel_x,rel_y)) # Trignometery for rotation
            self.image = pygame.transform.rotate(self.image_clean,angle) # rotate image
            self.rect = self.image.get_rect(center=self.rect.center) # set new boundary
            if self.current_frame >= self.max_frame: # Animation Frame loop
                self.current_frame = 0 # reset current frame
                if self.moving == True or self.attacking == True: # Animation Trigger
                     if self.moving == True :
                         self.img_pre_render = self.img_org # set image pre_render variable to orginal animation
                     if self.attacking == True:
                         self.img_pre_render = self.img_attack # set image pre_render variable to attack animation
                     self.current_time += dt ## Increase animation time
                     if self.current_time >= self.animation_time:
                         self.current_time = 0 # timing for the animation
                         self.current_frame = (self.current_frame + 1) % len(self.img_pre_render) # increase animation step until at max frame
                     else:
                          self.current_time = 0 # reset
                          self.current_frame = 0 # reset
        else:
               self.img_pre_render = self.img_death # Set to dead sprite
       ## Add more functionality Here:
       ## i.e..........:
        if self.target != 0:
            if self.attacking == True:
                 if self.current_frame == 3: # Placeholder number, edit for your needs.
                      self.debuff = self.debuff + (self.debuff*self.target.damage) # increase debuff by targets attack
                      self.damage_calc = self.damage/self.debuff # work out how much damage will be dealth during attack
                      self.target.life -= self.damage_calc # deal said damage
##################################################
##################################################
##################################################
#
# ... add more OBJECTS
#
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
# Initialize Pygame:
pygame.init()
pygame.mixer.init() # audio engine.
# Pygame/Game intialisation:
screen = pygame.display.set_mode((width, height)) # set screen dimension
pygame.display.set_caption("GAME_NAME") ## Change Game title name here
clock = pygame.time.Clock() # game clock
running = True # game running
####################################################################################################
####################################################################################################
#Game Functions
####################################################################################################
####################################################################################################
# Multiplayer Game Logic:
##################################################
   ##################################################
   # Server:
   ##################################################
 #####################
def handle_client(client_socket, client_address, client_message, dt):
   message = client_socket.recv(1024).decode() # recieved 1024 bit socket/buffer
   client[client_address].start_client_timer(dt+120, client_socket) # reset users in-activity timer
   print(f"Player {client_address} said: {message}") # print message
   logs[client_address].append(message) # add to logs
   tot_log = len(list(logs.keys())) # find total logs size
   if tot_log > 0: # if logs greater than nothing
      key_value_log = logs[list(logs.keys())[tot_log]] # use latest log
   else:
      key_value_log = logs[list(logs.keys())[0]] # else use the 0th one
# Send result back to all players
   for client in logs.keys():
      client_socket.send(key_value_log.encode()) # Send data to other clients
 #####################
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # establish connection
    server.bind((My_IP, PORT)) # combine ip + port
    print(My_IP +":"+ PORT)  # print it 
    server.listen(max_clients) # start server
    print("Server listening on port: " +str(PORT)) # ping port
    while True:
        client_socket, client_address = server.accept() # if joined
        print(f"Player connected from {client_address}") # establish connection
        client_socket.setblocking(0) # turn off blocking
        threading.Thread(target=handle_client, args=(client_socket, client_address, logs)).start() # thread for game
        pass
 #####################
def start_client_timer(dt,duration,client_socket):
   if dt > duration: # if delta time greater than timer
      check_client_timeout(client_socket) # probe user
#####################
def check_client_timeout(client_socket): # Test for time out
      try:
         for client in logs.keys(): # if client in logs
          client_socket.send(b"PING") # ping them
          return True # if good, leave to enjoy game
      except socket.error:
         client_socket.close() # else close connection
         return False
   ##################################################
   # Client:
   ##################################################
def send_message(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Establish a connection
            s.setblocking(0) # stop blocking sockets
            s.connect((online_host_address, online_host_port)) # connect to host
            readable, writable, errored = select.select([], [s], [], 0) # find writable buffer
            if writable:
                s.send(message.encode()) # send message
                print("message sent!")
            try:
               data = s.recv(1024) # recieved 1024 bit data buffer
               if data: # if data
                  recv_message(data) # Process data
                  return print("message recieved!")
               else:
                   print("No data received.")
            except BlockingIOError:
                 s.setblocking(0) # turn off block if on
                 print("No data available (BlockingIOError).")
            except Exception as e:
                 print(f"An error occurred: {e}")
    except Exception as e:
         print (f"Error: Unable to connect to server. {e}")
 #####################
def recv_message(message): # recieved message
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # establish connection
            s.setblocking(0) # stop blocking sockets
            readable, writable, errored = select.select([s], [], [], 0) # is readable buffer
            if readable:
                recv_message = s.recv(1024).decode() # read message
                return see_message(recv_message) # read message
    except Exception as e:
       send_message(My_IP +" | "+ temporal_measurements +" : "+"404, Didn't get last message.")
       return "Error: Unable to recieve data from server."
    except BlockingIOError:
       s.setblocking(0)# stop blocking
 #####################
   ##################################################
   # Client and Server:
   ##################################################
def see_message(message): ## see new message
   if message: # if message
            result_text = FONT.render(message, True, RED) # render
      #####################
def multiplayer(): # multiplayer option
################### Client_side
   if Client == True: # if client true
      online_host_address = input("Type in IP of HOST") # ask for ip
      online_host_port = input("Type in PORT of HOST") # ask for port
      if online_host_address:
        if online_host_port: # if successful
            send_message(My_IP +" | "+ temporal_measurements +" : "+"I have connected! Thanks for having me.") # connect
################### Server_side
   if Server == True: # if server
      PORT = input("Please pick a port number i.e. 8080 or 5050") # ask for port
      start_server() # start_server
      print(My_IP) # show IP
      print(PORT) # show PORT
     #####################
##################################################
####################################################################################################
####################################################################################################
#Visual intialisation
####################################################################################################
####################################################################################################
#Groups:
Splash = pygame.sprite.Group() # Splashscreen Group
Player_control = pygame.sprite.Group() # Player Group
Enemy = pygame.sprite.Group() # Enemy Group
Menu = pygame.sprite.Group() # Menu Group
# Branding Objects:
Company_branding = splash(0,0,Splash) # Company_branding_object
# Menu Objects:
Play_button = Button_0(0,0,Menu) # Play_button
Multiplayer_button = Button_1(0,0,Menu) # Multiplayer_button
Server_button = Button_2(0,0,Menu) # Server_button
Client_button = Button_3(0,0,Menu) # Client_button

####################################################################################################
####################################################################################################
#Audio intialisation (PyGBag has some issues with audio, placeholders from a game I made but you get the point!)
####################################################################################################
####################################################################################################
#ouch = pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Player_Hurt.mp3")))
#bang = pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Pistol.mp3")))                                        
#shotgun =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Shotgun.mp3")))    
#overkill =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Overkill.mp3")))    
#rampage =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Rampage.mp3")))    
#melee =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Melee_Grunt.mp3")))    
#death_enemy =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Death_Entities.mp3")))    
#dkill =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_DoubleKill.mp3")))    
#pygame.mixer.music.load(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/MSC_Infraction_AI.mp3")))
#pygame.mixer.music.play()     
####################################################################################################
####################################################################################################
## For device touch mechaninics:
fingers = [] # Touch Register
##################################################
# Primary Game Loop:
##################################################
##################################################
##################################################
async def main(): # Start of game loop
    #Globals (to reach inside game loop):
    global dt, interacted  # Globals
   ##################################################
    #Event System/Control System:
   ##################################################
    while running: # while game is on
     for event in pygame.event.get(): # highlight events
        if event.type == QUIT: # if event == quit
            running = False # close game
            pygame.quit()
            sys.exit()
       ## Pointer inputs:    
       ## Mouse trigger:    
        if event.type == pygame.MOUSEBUTTONDOWN: # if event is mouse button pressed
           interacted = True # interacted == true
        if event.type == pygame.MOUSEBUTTONUP: # if event is mouse button released
           interacted = False # interacted == false
       ## For device touch mechaninics:
        if event.type == pygame.FINGERDOWN: # if event is touch event pressed
           interacted = True # it has been interacted with
           FD_x = event.x * screen.get_height() # record X position of finger
           FD_y = event.y * screen.get_width() # record y position of finger
           fingers[event.finger_id] = FD_x, FD_y # store in list
        if event.type == pygame.FINGERUP: # if event is touch event released
           interacted = False # not interacting with
           fingers.pop(event.finger_id, None) # remove x/y data
      # if event.type == (NEXT_EVENT)
      #      pass
      #  ...
      #  ...
##################################################
##################################################
##################################################
##### Scene Hyirachy:
##################################################
    
    if SPLASH == True: # Splash scene for Branding
       screen.blit(Company_branding,(0,0)) # Small image for publicity 
       Splash.draw(screen) # Draw splash
       if splash_trigger == False: # if trigger activated
           timer = dt + 30   # set timer
           splash_tigger = True # cancel trigger
       if dt > timer: # if timer runs out
         MENU = True # Change Scene
         current_room = "menu_room" # change current_room
         SPLASH = False # End Scene
       pass # Splash screen for Branding
    if MENU == True: # if MENU room is true
       if Multiplayer == False:
          screen.blit(Play_button,(420,200)) # Play_Button 
          screen.blit(Multiplayer_button,(420,280)) # Multiplayer_Button
       if Multiplayer == True:
          screen.blit(Server_button,(420,200)) # Server_Button 
          screen.blit(Client_button,(420,280)) # Client_Button
       Menu.draw(screen) # Draw splash
       pass # Menu to select features
    if ROOM == True: # IF Game Room is True
       obj_Player = Object_1(0,0,Player_control) # Player_object
       NPC_MULTI = [] # Registrat for NPCs
       if current_room == game_levels[0]: # if level one
           if Current_Entities < current_room.Max_Entities and i < current_room.Total_Entities: # if there currently less NPC in view and less than the total in the map
             # Multi-Spawner
               i += 1 # increade by one
               Current_Entities += 1 # increase by one
               NPC_MULTI.append(Object_0(round(random.random(current_room.room_ROOM_width)),round(random.random(current_room.room_ROOM_height)),Enemy)) ## add enemy/NPC
           if i == current_room.Total_Entities or i > current_room.Total_Entities:
                  current_room = game_levels[1] 
                  i = 0
           screen.blit(Player_control,room_width/2,room_height/2) # Render Player
           screen.blit(Enemy,current_room.spawn_points_enemies[round(random.random(current_room.no_of_spawn_points))].x,current_room.spawn_points_enemies[round(random.random(current_room.no_of_spawn_points))].y) # Render Multi-spawned NPCs
           Enemy.draw(screen) # Draw Enemy
           Player_control.draw(screen) # Draw Player
           # ...
       if current_room == game_levels[1]:
           if Current_Entities < current_room.Max_Entities and i < current_room.Total_Entities: # if there currently less NPC in view and less than the total in the map
             # Multi-Spawner
               i += 1 # increade by one
               Current_Entities += 1 # increase by one
               NPC_MULTI.append(Object_0(round(random.random(current_room.room_ROOM_width)),round(random.random(current_room.room_ROOM_height)),Enemy)) ## add enemy/NPC
           if i == current_room.Total_Entities or i > current_room.Total_Entities:
                  current_room = game_levels[2]
                  i = 0
           screen.blit(obj_Player,room_width/2,room_height/2) # Render Player
           screen.blit(NPC_MULTI,current_room.spawn_points_enemies[round(random.random(current_room.no_of_spawn_points))].x,current_room.spawn_points_enemies[round(random.random(current_room.no_of_spawn_points))].y) # Render Multi-spawned NPCs
           Enemy.draw(screen) # Draw Enemy
           Player_control.draw(screen) # Draw Player
    pass # Main game room
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
    ## Final Render/Utility/Debug
##################################################
    dt = clock.tick(60)/1000 # Delta Time counting up from tik
    print(dt) # show delta time
    pygame.display.flip() # Display render for PyGBag
    await asyncio.sleep(0)  # Very important, and keep it 0
######################################################################################################################################################
######################################################################################################################################################
asyncio.run(main()) ## run program
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
##################################################
### Developer Comments/Notes/Plans:###############
##################################################
##################################################
##################################################
### Details:
#####################
# Author:
#   The name of the main developer or development team.
# Co-Author:
#   Names of any co-developers or collaborators involved in the project.
# Company: 
#   The name of the studio or company developing the game.
# Title:
#   The name of the game.
# Genre:
#   The genre of the game (e.g., RPG, Puzzle, Shooter, etc.).
# Decription:
#   A brief overview of the game, including its setting, story, and key gameplay elements.
# Date of Release: 
#   The planned release date of the game, or “TBA” if uncertain.
# Contact:
#   Contact information for business inquiries (e.g., email address).
# Rating_Age:
#   The appropriate age rating for the game (e.g., ESRB, PEGI).
#####################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
### Mechanics:
###################
# Core Gameplay:
#   Describe the primary mechanics and systems that drive the gameplay experience (e.g., combat, exploration, puzzles, etc.).
# Controls:
#   Explain the control scheme and how the player interacts with the game (e.g., keyboard, mouse, gamepad, touch controls).
# Progression:
#   How does the player progress through the game? This could include leveling up, unlocking new areas, or advancing the story.
# Difficulty:
#   What is the game's difficulty level like? Are there different difficulty settings, or does the game adapt to the player's skill level?
# Rewards:
#   What rewards or incentives does the player receive for achieving certain goals (e.g., in-game items, achievements, story progression)?
# Combat/Interactions (if applicable):
#   Describe any combat mechanics, abilities, or interactions with the game world (e.g., weapon mechanics, skills, puzzles, NPC interactions).
# AI Behavior (if applicable):
#   How does the artificial intelligence behave in the game? For example, enemy AI tactics, companion behaviors, or world events.
# Multiplayer (if applicable):
#   If the game has multiplayer, explain the mechanics involved (e.g., co-op, PvP, matchmaking, etc.).
# Replayability:
#   What features encourage players to replay the game (e.g., multiple endings, side quests, procedural generation)?
# Special Features:
#   Highlight any unique mechanics or features that set your game apart, such as time manipulation, unique movement mechanics, or innovative UI design.
#####################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
### Product/Investors:
#####################
# USP:
#   What makes your game stand out? A unique feature, story element, or innovative mechanic that sets it apart.
# Slogan:
#   A catchy phrase or tagline that summarizes the essence or key selling point of the game.
# MVP: 
#   The simplest version of the game with the core features that demonstrate its value. This could be a demo or early access version.
# Pitch:
#   A short, persuasive summary of why the game is worth investing in, highlighting what makes it unique and appealing.
#####################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
### Market:
#####################
# Target_audiance:
#   The demographic and player base the game is intended for (age, interests, gaming habits, etc.).
# Recepetion:
#   How you expect the game to be received by critics and players, including any potential challenges or expectations.
# Marketing:
#   The strategies you plan to use to market the game, such as trailers, social media, influencer partnerships, or events.
#####################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
### SWAT:
#####################
# Strengths:
#   The key advantages or unique features of your game that set it apart from others (e.g., engaging mechanics, strong art direction, etc.).
# Weaknesses:
#   Any potential weaknesses or challenges the game might face (e.g., lack of funding, competition, technical limitations).
# Advantages:
#   The factors that give your game an edge over competitors or position it for success (e.g., innovative gameplay, niche audience).
# Threats:
#   External factors that might affect the game’s success (e.g., market saturation, other high-profile releases, shifting trends).
#####################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
