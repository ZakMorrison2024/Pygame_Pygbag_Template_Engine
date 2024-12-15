############################################################################################################################################
############################################################################################################################################
##################################################--The Pygame Template Engine--############################################################
######################################################-- by Zak Morrison --#################################################################
############################################################################################################################################
############################################################################################################################################
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
#   "asyncio",
#   "time",
#   "heapq"
# ]
# ///
#####################################################
## Authors notes:
##################################################
## Features:

# Coder/Business model review system
# Dynamic Camera/View System
# Command and talk based M-Network system (Multiplayer)
# Procedual Room Generation - World builder/background generation? (to implament)
# Sound/Audio system (to implament)
# Character customisation (to implament)
# G.O.A.T NPC AI (to implament)
# Basic Pathfinding (to implament)
# Game UI (to implament)
# Engine UI and drag and drop (to implament)
# Asset management (to implament)
# GPT/ML features? (to implament)
# 3D engine? (to implament)
# added peripherials (xbox gamepad) (to impliment)
# Actors needs (to implemnt)

# Sophisticated Debug System! 

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
import time # time
import select # select
import asyncio # async
import heapq #pathing
##################################################
##################################################
#Debug System
#######################################
DEBUG_MODE = False

keys = pygame.key.get_pressed()

if keys[pygame.K_LCTRL] and DEBUG_MODE == False:
    DEBUG_MODE = True
elif keys[pygame.K_LCTRL] and DEBUG_MODE == True:
    DEBUG_MODE = False

def draw_debug_info(surface, info_dict, x=10, y=10, line_height=20):
    font = pygame.font.Font(None, 36) # Font #1
    for p in info_dict:
        text_surface = font.render(p, True, GREEN)
        surface.blit(text_surface, (x, y + p * line_height))
        selection = input("Please write the menu you wish to see.")
        if selection == Object_0:
            num = input("Type the number of the instance you want to view.")   
            for i, (key, value) in enumerate(selection[num].items()):
             text = f"{key}: {value}"
        if selection != Object_0:
            for i, (key, value) in enumerate(selection.items()):
             text = f"{key}: {value}"
        text_surface = font.render(text, True, GREEN)
        surface.blit(text_surface, (x, y + i * line_height))
##################################################
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
FONT = pygame.font.Font(None, 36) # Font #2
splash_trigger = False # trigger for splash screen
actors = [] # list for all NPCs and Players
list_of_all_objects = [] # catalog of all active item, objects, actors and entities
## In-game time:
day_length = 20
hour_len = 60
hours_past = random.random(20)
date = 0
year_length = 90
night_True_day_False = False
# In-game time mechanism:
if ROOM == True:
    if hours_past > day_length:
        hours_past = 0
        date += 1
    if hours_past > 14 and hours_past < 20:
        night_True_day_False = True
    else:
        night_True_day_False = False
    if date > year_length:
        date = 0
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
no_of_clients = 0 # How many clients are active
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
        self.target = "" # focus target
        self.setting = 0 # camera control setting
        keys = pygame.key.get_pressed() # check keyboard

        # camera control select:
        #setting 1:
        if keys[pygame.K_1] and self.setting != 1: # key no.1
            self.setting = 1 # freemouse - control using mouse
        elif keys[pygame.K_1] and self.setting == 1:
            self.setting = 0
            #setting 2:
        if keys[pygame.K_2] and self.setting != 2: # key no.2
            self.setting = 2 # freehand - control using keys
        elif keys[pygame.K_2] and self.setting == 2:
            self.setting = 0
            #setting 3:
        if keys[pygame.K_3] and self.setting != 3: # key no.3
            self.setting = 3 # Focus_target - view stays on target
        elif keys[pygame.K_3] and self.setting == 3:
            self.setting = 0
           #setting 4:
        if keys[pygame.K_4] and self.setting != 4: # key no.4
            self.setting = 4 # cycle_actors(incremental)
        elif keys[pygame.K_4] and self.setting == 4:
            self.setting = 0
            #setting 5:
        if keys[pygame.K_5] and self.setting != 5: # key no.5
            self.setting = 5 # cycle_actors(decremental)
        elif keys[pygame.K_5] and self.setting == 5:
            self.setting = 0
            #setting 6:
        if keys[pygame.K_6] and self.setting != 6: # key no.6
            self.setting = 6 # cycle_actors(decremental)
        elif keys[pygame.K_6] and self.setting == 6:
            self.setting = 0
            #setting 7:
        if keys[pygame.K_7] and self.setting != 7: # key no.7
            self.setting = 7 # split-screen (to impliment)
        elif keys[pygame.K_7] and self.setting == 7:
            self.setting = 0
             #setting 8:
        if keys[pygame.K_8] and self.setting != 8: # key no.8
            self.setting = 8 # 3D camera
        elif keys[pygame.K_8] and self.setting == 8:
            self.setting = 0
              #setting 9:
        if keys[pygame.K_9] and self.setting != 9: # key no.9
            self.setting = 9 # splitscreen 3D
        elif keys[pygame.K_9] and self.setting == 9:
            self.setting = 0           

        # changing setting and view behaviour    
        if self.setting == 0:
           if self.target == actors[0]:
                self.focus_target(self.target) ## setting 0: Focus on Player
        if self.setting == 1:
            self.freemouse() ## setting 1: free mouse movement
        if self.setting == 2:
            self.freekey() ## setting 2: free key movement
        if self.setting == 3:
            self.find_target(self.rect.x,self.rect.y) ## setting 3: find closest living thing
            self.focus_target(self.target)
        if self.setting == 4:
            j += 1
            self.cycle_actors(j) ## setting 4: increment living things
        if self.setting == 5:
            j -= 1
            self.cycle_actors(j) ## setting 5: decrement living thing 
        if self.setting == 6:
            self.reset() ## setting 6: reset camera to top left

   def reset(self):
        return self.rect.move(self.camera.topleft) # Return Camera
   def find_target(self,x,y):
       potential_people = [] # potential people list
       distance = [] # distance measure list
       intial_scan = 1 # scanning everyone but player
       end_scan_former = 0 # end scan slow
       end_scan_later = 0 # end scan fast
       first_number_cycle = 1 # first index cycler
       second_number_cycle = 2 # second index cycle
       third_number_cycle = 3 # third index cycle
       while intial_scan < len(actors): # intial scan hasn't reached the end
         indiv = actors.index[intial_scan] # add actors to indiv 
         potential_people.append(indiv, indiv.rect.x - x, indiv.rect.y - y) # add indiv along with their coordinates, minus that of the cameras
         intial_scan += 1 ## increment intial scan
       if len(potential_people) > 5: ## potential people has atleast 6 indexes 
         if first_number_cycle % 3 and first_number_cycle <= len(potential_people): # first index cycler
            first_number_cycle += 3 # increase by three to skip unwanted entires
         if second_number_cycle % 2 and second_number_cycle <= len(potential_people): # second index cycler
            second_number_cycle += 3  # increase by three to skip unwanted entires
         if third_number_cycle % 3 and third_number_cycle <= len(potential_people): # third index cycler
            third_number_cycle += 3 # increase by three to skip unwanted entires
       distance.append(math.sqrt(potential_people[second_number_cycle]**2 + potential_people[third_number_cycle]**2))# list distances
       if first_number_cycle >= len(potential_people): # when the slowest cycler is above len
           end_scan_former += 1 # increment slow scan
           end_scan_later += 2 # increment fast scan
           if (distance[end_scan_former] > distance[end_scan_later] and distance[end_scan_former] != 0 and distance[end_scan_later] != 0) or  (distance[end_scan_later] > distance[end_scan_former] and distance[end_scan_former] != 0 and distance[end_scan_later] != 0) : # compare scans
                distance.pop(distance[end_scan_former]) # remove larger entries
           if len(distance) == 1: # when length of list is one
                self.target = distance[0] # make that actor the target  
   def freemouse(self): # free mouse look
            if pygame.mouse.get_pressed(3): #middle mouse button
                button += 1 #increment button
                mx,my = pygame.mouse.get_pos() # click coordinates
                time.sleep(1) # wait 1 milisecond
                if button < 2: # if no second press
                    nx,ny = pygame.mouse.get_pos() # new mouse coordinates
                    dif_x = nx - mx # find x difference
                    dif_y = ny - my # find y difference
                    self.rect.y + dif_x # move x
                    self.rect.y + dif_y # move y
   def freekey(self): # free key
            keys = pygame.key.get_pressed() # assign keys
            if keys[pygame.K_w] or keys[pygame.K_UP]: # if up or W
                 if self.rect.y < room_height and self.rect.y > 0: # if within restriction
                           self.rect.y -= 2 # move up
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # if right or D
                 if self.rect.x < room_width and self.rect.x > 0: # if within restriction
                           self.rect.x += 2 # move right
            if keys[pygame.K_a] or keys[pygame.K_LEFT]: # if left or A
                 if self.rect.x < room_width and self.rect.x > 0: # if within restriction
                           self.rect.x -= 2 # move left
            if keys[pygame.K_s] or keys[pygame.K_DOWN]: # if down or S
                 if self.rect.y < room_height and self.rect.y > 0: # if within restriction
                           self.rect.y += 2 # move down
   def focus_target(self, target_rect):
        x = -target_rect.centerx + int(self.camera.width / 2) # Move Camera along X axis, following target
        y = -target_rect.centery + int(self.camera.height / 2) # Move Camera along Y axis, following target
        x = min(0, x) # Limit Camera along X axis, min
        y = min(0, y) # Limit Camera along Y axis, min
        x = max(-(self.room_width - self.camera.width), x) # Limit Camera along X axis, max
        y = max(-(self.room_height - self.camera.height), y) # Limit Camera along Y axis, max
        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)  # Set boundary
   def cycle_actors(self,j): # cycle actors
       self.focus_target(actors[j]) # focus target to next increment or decremented actor   
   def set_room_size(self, width, height):
        self.room_width = width # Set room width
        self.room_height = height # Set room height
camera = Camera(width,height) # intiate camera, set resolusion to default game resolution
##################################################
### Engine UI
##################################################
def Engine():
    pass
##################################################
### Room: ROOM_0. defintions: (Room/Level #0) -- (2D)
##################################################
def room_0(): # Level_0 (2D)
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
### Room: ROOM_1. defintions: (Room/Level #1) -- (2D)
##################################################
def room_1(): # Level_1 (2D)
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
### Room: ROOM_2. defintions: (Room/Level #2) -- (3D)
##################################################
def room_2(): ## 3D room
 pass
##################################################
### GAME MECHANICAL:
##################################################
dt = 0 # Delta Time/Step-Up Clock
PAUSE = False # For the Pause menu
interacted = False # Variable to know if a pointer had pressed
game_levels = [room_0(),room_1()] # List of all avalible levels
current_room = ("splash_room", width(960), height(540)) # To know which stage we're on
room_width = current_room[1] # Change Room Dimension
room_height = current_room[2] # Change Room Dimension
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
            global MENU, ROOM
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
##################################################
################### Narrator_AI_Story_driver
class Narrator(pygame.sprite.Sprite): ### Narrator
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      self.difficulty = random.random(1)
      self.personality = "Welcoming"
      self.intelligence = "Low"
      self.disposition = [] # Actors disposition to those they meet
   def tasks(self):
       pass
   def events(self):
       pass 
   def dialog(self):
       pass
   def update(self, dt):
       pass
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
      # Image Loading: (init)
      self.image = self.img_org[0] # Set Default image
      self.img_pre_render = self.img_org[0]
      # Animation Mechanics 
      self.max_frames = len(self.img_pre_render)
      self.current_frame = 0 ## current frame for animation
      self.animation_time = 0.1 ## threshold for next frame (time)
      self.current_time = 0 ## current timing for animation
      # Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y
      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      self.fleeing = False # flee
      # Needs:
      self.hunger = random.random(100) # hunger 
      self.thirst = random.random(100) # thirsty
      self.toilet = random.random(100) # toilet need  
      self.hygiene = random.random(100) # clean
      self.social = random.random(100) # social need  
      self.sex = random.random (100) # loneiness
      self.sleep = random.random(100) # sleepy
      # Locals:
      self.task = ""
      self.hand_left = "Empty" # left hand item
      self.hand_right = "Empty" # right hand item
      self.carry_threat_value = 0 # determine how much a threat someone is by what they're holding
      self.target = 0 # Player target
      self.speed = 3 # object speed
      self.value = random.random(2000) # object market value
      self.inventory = [] # object invetory
      self.hostile = False # object temperament
      self.damage = 5 # base damage
      self.debuff = 2 # base draw back
      self.damage_calc = 0 # varaible for calculation
      self.mutations = [] # potential mutations
      # Psychological
      self.mood = "Sad"
      self.brain_state = "Healthy"
      self.mind_activity = "Pondering"
      self.congition_perdinance = "High"
      self.emotions = "Low"
      self.personality = "Welcoming"
      self.intelligence = "Low"
      self.disposition = [] # Actors disposition to those they meet
      # globals
      self.job_career = "" 
      self.deposit = "£0" # bank
      self.friends = [] # social
      self.address = "Quite close" # address
      self.transport = "Car - Toyota" # transport
      # Health
      self.health = 100 # object life
      self.head = 100 # head vital
      self.body = 100 # body vital
      self.shoulders = 100 # shoulders vital
      self.chest = 100 # chest vital
      self.left_arm = 100 # left_arm vital
      self.right_arm = 100 # right_arm vital
      self.left_leg = 100 # left_leg vital
      self.right_leg = 100 # right_leg vital
      self.right_eye = 100 # right_eye vital  
      self.left_eye = 100 # left_eye vital
      self.immunity = 0 # immunity
      self.Lympathic = 0 # infections
      self.heart = 100 # heart vital
      self.brain = 100 # brain vital
      self.liver = 100 # liver
      self.kidneys = 100 # kidneys
      # Pathfinding
   def pathfinding(self,start, goal):
       self.start = start
       self.goal = goal
       self.path = 0
       self.obstacles = []
       ##
   def destination(self,tx,ty,grid):    
       pass
   
   def GOAT(self):
       self.objective = ""
       pass
       ##
   def update(self, dt): # Main behaviour loop
     ## Drains/needs:
     if dt % 2:
        self.hunger -= random.random(1)
        self.thirst -= random.random(1)
        self.toilet += random.random(2)
        self.hygiene -= random.random(2) # clean
        self.social -= random.random(0.5) # social need  
        self.sex -= random.random (0.3) # loneiness
        self.sleep -= random.random(2)
     if night_True_day_False == True:
        self.sleep -= random.random(6)
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
      # Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      self.fleeing = False # flee
      # Needs:
      self.hunger = random.random(100) # hunger 
      self.thirst = random.random(100) # thirsty
      self.toilet = random.random(100) # toilet need  
      self.hygiene = random.random(100) # clean
      self.social = random.random(100) # social need  
      self.sex = random.random (100) # loneiness
      # Locals:
      self.task = ""
      self.hand_left = "Empty" # left hand item
      self.hand_right = "Empty" # right hand item
      self.carry_threat_value = 0 # determine how much a threat someone is by what they're holding
      self.target = 0 # Player target
      self.speed = 3 # object speed
      self.value = random.random(2000) # object market value
      self.inventory = [] # object invetory
      self.hostile = False # object temperament
      self.damage = 5 # base damage
      self.debuff = 2 # base draw back
      self.damage_calc = 0 # varaible for calculation
      self.mutations = [] # potential mutations
      # Psychological
      self.mood = "Sad"
      self.brain_state = "Healthy"
      self.mind_activity = "Pondering"
      self.congition_perdinance = "High"
      self.emotions = "Low"
      self.personality = "Welcoming"
      self.intelligence = "Low"
      # globals
      self.job_career = "" 
      self.deposit = "£0" # bank
      self.friends = [] # social
      self.address = "Quite close" # address
      self.transport = "Car - Toyota" # transport
      # Health
      self.health = 100 # object life
      self.head = 100 # head vital
      self.body = 100 # body vital
      self.shoulders = 100 # shoulders vital
      self.chest = 100 # chest vital
      self.left_arm = 100 # left_arm vital
      self.right_arm = 100 # right_arm vital
      self.left_leg = 100 # left_leg vital
      self.right_leg = 100 # right_leg vital
      self.right_eye = 100 # right_eye vital  
      self.left_eye = 100 # left_eye vital
      self.immunity = 0 # immunity
      self.Lympathic = 0 # infections
      self.heart = 100 # heart vital
      self.brain = 100 # brain vital
      self.liver = 100 # liver
      self.kidneys = 100 # kidneys
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
def handle_client(client_socket, client_address, logs):
   message = client_socket.recv(1024).decode() # recieved 1024 bit socket/buffer
   start_client_timer(dt+120,client_socket,client_address) # reset users in-activity timer
   print(f"Player {client_address} said: {message}") # print message
   logs[client_address].append(message) # add to logs
   tot_log = len(list(logs.keys())) # find total logs size
   if tot_log > 0: # if logs greater than nothing
      key_value_log = logs[list(logs.keys())[tot_log]] # use latest log
   else:
      key_value_log = logs[list(logs.keys())[0]] # else use the 0th one
# Send result back to all players
   for client_address in logs.keys():
      client_socket.send(key_value_log.encode()) # Send data to other clients
      print("sent to: " + client_address)
   if message.read == int: # of int 
       network_action(int(message)) # action the command
 #####################
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # establish connection
    server.bind((My_IP, PORT)) # combine ip + port
    print(My_IP +":"+ PORT)  # print it 
    server.listen(max_clients) # start server
    print("Server now listening on port: " +str(PORT)) # ping port
    while True:
        client_socket, client_address = server.accept() # if joined
        print(f"Player connected from {client_address}") # establish connection
        if client_address not in logs:
            no_of_clients += 1
        client_socket.setblocking(0) # turn off blocking
        threading.Thread(target=handle_client, args=(client_socket, client_address, logs)).start() # thread for game
        pass
 #####################
def start_client_timer(duration,client_socket, client_address):
   if dt > duration: # if delta time greater than timer
      check_client_timeout(client_socket, client_address) # probe user
#####################
def check_client_timeout(client_socket, client_address): # Test for time out
      try:
         for client_address in logs.keys(): # if client in logs
          client_socket.send(b"PING") # ping them
          return True # if good, leave to enjoy game
      except socket.error:
         client_socket.close() # else close connection
         no_of_clients -= 1
         return False
      if True:
            start_client_timer(dt+120,client_socket, client_address)
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
                message = s.recv(1024).decode() # read message
                if message == str:
                    return see_message(message) # read message
                elif message == int:
                    network_action(int(message))
    except Exception as e:
       send_message(My_IP +" | "+ temporal_measurements +" : "+"| 404: Didn't get last message.")
       return "Error: Unable to recieve data from server."
    except BlockingIOError:
       s.setblocking(0)# stop blocking
 #####################
   ##################################################
   # Client and Server:
   ##################################################
def network_action(message):
    if message == int:
        if message == 1:
           pass
        if message == 2:
           pass 
##################
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
            send_message(My_IP +" | "+ temporal_measurements +" : "+"| 200: I have connected! Thanks for having me.") # connect
################### Server_side
   if Server == True: # if server
      PORT = input("Please pick a port number i.e. 8080 or 5050, etc etc...") # ask for port
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
   ### DEBUG Main Loop
##################################################
##################################################
   # Debug display
    if DEBUG_MODE:
     debug_info = [debug_NPC,debug_PLAYER,debug_GAME,debug_ROOM,debug_CAMERA,debug_Multiplayer,debug_Audio,debug_NARRATOR,debug_GAMEINFO]
     NPC = Object_0
     Player = Object_1
     Narra = Narrator
     Audio = 0
     ROOMS = current_room
     CAMERA = Camera
     
     debug_GAMEINFO = [
         "GAME SERIAL INFORMATION: ",
         "Title :", Title,
         "Author: ", Author,
         "Co-Author: ", Co_Author,
         "Company: ", Company,
         "Genre: ", Genre,
         "Date oF Release: ", Date_of_Release,
         "Contact: ", Contact,
         "Description: ", Decription]  

        
     debug_Audio = ["To be included."]


     debug_NARRATOR = [ "Narrator: ",
                        "Difficulty: ", Narra.difficulty,
                        "Personality: ", Narra.personality,
                        "Intelligence: ", Narra.intelligence,
                        "Disposition: ", Narra.disposition]



     debug_ROOM = [
         "Room Info: ",
         "Current Room: ", current_room,
         "Width: ", ROOMS.width,
         "Height: ", ROOMS.height,
         "Max # of Spawn points: ", ROOMS.max_spawns,
         "# of Entities: ", ROOMS.Current_Entities,
         "Max # of Entities: ", ROOMS.Max_Entities,
         "Total Entities in Game: ", ROOMS.Total_Entities,
         "Enitities Difficulty Multiplier: ". ROOMS.Entities_difficulty,
         "Room Delta Time: ", ROOMS.IN_GAME_TIME]      


     debug_CAMERA = [
         "Camera: ",
         "Rect: ", CAMERA.rect,
         "Rect X: ", CAMERA.rect.x,
         "Rect Y: ", CAMERA.rect.y,
         "Target: ", CAMERA.target,
         "Setting: ", CAMERA.setting,
         "Keys: ", CAMERA.keys]



     debug_Multiplayer = [
         
        "Multiplayer Debug: ",
        "Multiplayer Setting: ", Multiplayer,
        "My IP Address: ", My_IP,
        "My Port: ", PORT,
        "MP Name: ", player_name,
        "Client Mode: ", Client,
        "Connected Address: ", online_host_address,
        "Connected Port: ", online_host_port,
        "Server Mode: ", Server,
        "Max Clients: ", max_clients,
        "Last Message: ", see_message(logs[len(logs)]),
        "Current Clients: ", no_of_clients,
        "Logs :", logs.readline]

     
     debug_GAME = [
         "Game: ",
         "Delta Time: ", dt,
         "Time + Date", temporal_measurements,
         "Pause: ", PAUSE,
         "Splash :", splash_trigger,
         "Mouse Click: ", interacted,
         "Touch Taps: ", fingers,
         "Current Room: ", current_room,
         "Room Width: ", room_width,
         "Room Height: ", room_height,
         "View Dimiensions: ", "Width: ", width, "Height: ", height,
         "In-Game Clock: ",
         "Year Length :", year_length,
         "Day Length (Mins): ", day_length,
         "Hour Length (Mins): ", hour_len,
         "In-Game Time: ", hours_past,
         "In-Game Date: ", date,
         "Day (False), Night (True): ",night_True_day_False,
         "Actors: ", actors
         ]


     debug_NPC = [
               
                "Biography: "
                "First Name: ",NPC.fname,
                "Middle Names: ",NPC.mname,
                "Surname :", NPC.surname,
                "D.O.B: ",NPC.DOB,
                "Age: ", NPC.age,
                "Ethnicity: ", NPC.Enth,

                "States: ", 
                "Alert: ", NPC.alert,
                "Moving: ", NPC.moving,
                "Attacking: ",NPC.attacking,
                "Dead: ", NPC.dead,
                "Fleeing: ", NPC.fleeing,

                "Needs: ",
                "Hunger: ", NPC.hunger,
                "Thirst: ", NPC.thirst,
                "Toilet: ", NPC.toilet,
                "Hygiene: ", NPC.hygiene,
                "Social: ", NPC.social,
                "Sex: ", NPC.sex,

                "Physical Health: ",
                "Health: ",NPC.health,
                "Infection: ", NPC.Lympathic, 
                "Immunity: ", NPC.immunity,

                "Psychology: ",
                "Mood: ", NPC.mood,
                "Brain State: ",NPC.brain_state,
                "Mind/Thoughts: ", NPC.mind_activity,
                "Cognition: ", NPC.congition_perdinance,
                "Emotions: ", NPC.emotions,
                "Personality: ",NPC.personality,
                "Intelligence: ",NPC.intelligence,

                 "Body Parts:",
                 "Head: ",NPC.head,
                 "Heart: ",NPC.heart,
                 "Brain: ",NPC.brain,
                 "Liver: ",NPC.liver,
                 "Kidney: ",NPC.kidneys,
                 "Body: ", NPC.body,
                 "Shoulders: ", NPC.shoulders,
                 "Chest: ",NPC.chest,
                 "Left Eye: ",NPC.left_eye,
                 "Left Arm: ",NPC.left_arm,
                 "Left Leg: ",NPC.left_leg,
                 "Right Eye: ",NPC.right_eye,
                 "Right Arm: ",NPC.right_arm,
                 "Right Leg: ",NPC.right_leg,

                "Collision :",
                "rect : ", NPC.rect,
                "rect_x : ", NPC.rect.x,
                "rect_y : ", NPC.rect.y,
                "Collided: ", 
                 
                "Attack: ",
                "Damage: ", NPC.damage,
                "Debuff: ",NPC.debuff,
                "Damage Calculation: ", NPC.damage_calc,

                "Local Variables: ",
                "Task: ", NPC.task,
                "Left Hand: ", NPC.hand_left,
                "Right Hand: ", NPC.hand_right,
                "Carry Threat Value: ", NPC.carry_threat_value,
                "Target: ", NPC.target,
                "Speed: ", NPC.speed,
                "Value: ", NPC.value,
                "Inventory: ", NPC.inventory,
                "Hostile: ", NPC.hostile,
                "Mutations: ", NPC.mutations,

                "Global Variables: ",
                "Job/Career: ",NPC.job_career,
                "Bank: ",NPC.deposit,
                "Friends: ",NPC.friends,
                "Address: ", NPC.address,
                "Transport: ", NPC.transport,

               "Sprites_Loaded: ",
               "Original Sprites: ", NPC.img_org,
               "Attack Sprites: ", NPC.img_attack,
               "Death Sprite: ", NPC.image_death,
               "Current Sprite: ", NPC.image,
                "Next Sprite: ", NPC.img_pre_render,

                "Animation: ",
                "Max Frames: ", NPC.max_frames,
                "Current Frame: ", NPC.current_frame,
                "Animation Threshold Time :", NPC.animation_time,
                "Current Animation Step: ", NPC.current_time ]
     
     
     
     debug_PLAYER = [
               
                "Biography: "
                "First Name: ",Player.fname,
                "Middle Names: ",Player.mname,
                "Surname :", Player.surname,
                "D.O.B: ",Player.DOB,
                "Age: ", Player.age,
                "Ethnicity: ", Player.Enth,

               
                "States: ", 
                "Alert: ", Player.alert,
                "Moving: ", Player.moving,
                "Attacking: ",Player.attacking,
                "Dead: ", Player.dead,
                "Fleeing: ", Player.fleeing,

                "Needs: ",
                "Hunger: ", Player.hunger,
                "Thirst: ", Player.thirst,
                "Toilet: ", Player.toilet,
                "Hygiene: ", Player.hygiene,
                "Social: ", Player.social,
                "Sex: ", Player.sex,

                "Physical Health: ",
                "Health: ",Player.health,
                "Infection: ", Player.Lympathic, 
                 "Immunity: ", Player.immunity,

                "Psychology: ",
                "Mood: ", Player.mood,
                "Brain State: ",Player.brain_state,
                "Mind/Thoughts: ", Player.mind_activity,
                "Cognition: ",Player.congition_perdinance,
                "Emotions: ", Player.emotions,
                "Personality: ",Player.personality,
                "Intelligence: ",Player.intelligence, 

                 "Body Parts:",
                 "Head: ",Player.head,
                 "Heart: ",Player.heart,
                 "Brain: ",Player.brain,
                 "Liver: ",Player.liver,
                 "Kidney: ",Player.kidneys,
                 "Body: ", Player.body,
                 "Shoulders: ", Player.shoulders,
                 "Chest: ",Player.chest,
                 "Left Eye: ",Player.left_eye,
                 "Left Arm: ",Player.left_arm,
                 "Left Leg: ",Player.left_leg,
                 "Right Eye: ",Player.right_eye,
                 "Right Arm: ",Player.right_arm,
                 "Right Leg: ",Player.right_leg,

                "Attack: ",
                "Damage: ", Player.damage,
                "Debuff: ",Player.debuff,
                "Damage Calculation: ", Player.damage_calc,
                 
             "Local Variables: ",
                "Task: ", Player.task,
                "Left Hand: ", Player.hand_left,
                "Right Hand: ", Player.hand_right,
                "Carry Threat Value: ", Player.carry_threat_value,
                "Target: ", Player.target,
                "Speed: ", Player.speed,
                "Value: ", Player.value,
                "Inventory: ", Player.inventory,
                "Hostile: ", Player.hostile,
                "Mutations: ", Player.mutations,

                "Global Variables: ",
                "Job/Career: ",Player.job_career,
                "Bank: ",Player.deposit,
                "Friends: ",Player.friends,
                "Address: ", Player.address,
                "Transport: ", Player.transport,

                 "Sprites_Loaded: ",
               "Original Sprites: ", Player.img_org,
               "Attack Sprites: ", Player.img_attack,
               "Death Sprite: ", Player.image_death,
               "Current Sprite: ", Player.image,
                "Next Sprite: ", Player.img_pre_render,

                "Animation: ",
                "Max Frames: ", Player.max_frames,
                "Current Frame: ", Player.current_frame,
                "Animation Threshold Time :", Player.animation_time,
                "Current Animation Step: ", Player.current_time,

                "Collision :",
                "rect : ", Player.rect,
                "rect_x : ", Player.rect.x,
                "rect_y : ", Player.rect.y,
                "Collided: ", 
 ]          
  
     
       
    
   

    draw_debug_info(screen, debug_info)



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
           splash_trigger = True # cancel trigger
       if dt > timer: # if timer runs out
         MENU = True # Change Scene
         current_room = ("menu_room",960,540) # change current_room
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
