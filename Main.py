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
#   "datetime"
# ]
# ///

#####################################################
## Libraries:
##################################################
import pygame
from pygame.locals import QUIT
import os
import random
import math
import sys
import socket
import threading
import datetime

###################################################
##################################################

#Pre-defintions: (remove if unwanted, added for consideration.)

###################################################
# Colours:
##################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
################################################
# GAME:
################################################
abs_cwd_path_ts = os.path.abspath(os.getcwd())
################################################

###################################################
# GLOBAL VARIABLES:
##################################################
### GAME DESCRIPTIVE:
##################################################
Author = ""
Co_Author = []
Company = ""
Title = ""
Genre = ""
Decription = ""
Date_of_Release = "--/--/----"
Contact = []
Rating_Age = ""
##################################################
### GAME NETWORK:
##################################################
Multiplayer = False
player_name = ""
hostname = socket.gethostname()
My_IP = socket.gethostbyname(hostname)
PORT = 8080
Server = False
Client = False
max_clients = 8
online_host_address = ""
online_host_port = ""
##################################################
### GAME SCENES/MAPS:
##################################################
SPLASH = True # Splash Window
MENU = False # Menu Window
ROOM = False # Room Placeholder
##################################################
### Room: ROOM_0. defintions: (Room #0)
##################################################
def room_0():
   width = 1920
   height = 1080
   Max_Entities = 50
   IN_GAME_TIME = "00:00"
##################################################
### Room: ROOM_1. defintions: (Room #1)
##################################################
def room_1():
   width = 1920
   height = 1080
   Max_Entities = 20
   IN_GAME_TIME = "00:00"
##################################################
### GAME MECHANICAL:
##################################################
dt = 0 # Delta Time/Step-Up Clock
PAUSE = False
game_levels = [room_0(),room_1()]
current_room = game_levels[0]
room_width = current_room.width
room_height = current_room.height
temporal_measurements = datetime.datetime.now()
################################################






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

      self.dt = 0 # Life Timer, used to destroy and continue progression.

   def update(self): # Behaviour loop
         self.dt + 1 # Life timer
         if self.dt > 3: # After 3 ticks 
            global SPLASH, MENU # access in game Variables
            MENU = True # Change Scene
            SPLASH = False # End Scene
         pass

###########################################################################################################################################
##################################################
### Classes/Objects (in-Game):
##################################################

class Object_0(pygame.sprite.Sprite): ### Object Template, showing features one can add to object to define the objects nature and interactions (Non-playable Character Ver.)
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 

      ## Primary image placeholder:
      self.img_org =[pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE_2-####.png")))] # - List Placeholder for second (or more) images for animation # All With Pre-Defined PATH Variable

      ## Secondary image placeholders:
      self.img_attack = [pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_0-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_1-####.png"))),
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_2-####.png")))]
     
      self.image_death = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-CORPSE-####.png")))

     ## Image Loading: (init)
      self.image = self.img_org[0] # Set Default image
      self.img_pre_render = 0
     
     ## Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y

      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      
      # Animation Mechanics 
      self.max_frames = len(self.img_pre_render)
      self.current_frame = 0 ## current frame for animation
      self.animation_time = 0.1 ## threshold for next frame (time)
      self.current_time = 0 ## current timing for animation

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
      
      self.rect = self.image.get_rect(center=self.rect.center) # set new boundary

     
      if self.current_frame >= self.max_frame: # Animation Frame loop
          self.current_frame = 0
      
     
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
    ## i.e.:
    if self.target != 0:
      if self.attacking == True:
        if self.current_frame = 3: # Placeholder number, edit for your needs.
          self.debuff = self.debuff + (self.debuff*self.target.damage)
          self.damage_calc = self.damage/self.debuff
          self.target.life -= self.damage_calc
  
  pass

##################################################
##################################################
##################################################

class Object_1(pygame.sprite.Sprite): ### Object Template, showing features one can add to object to define the objects nature and interactions (playable Character Ver.)
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 

      ## Primary image placeholder:
      self.img_org =[pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE_2-####.png")))] # - List Placeholder for second (or more) images for animation # All With Pre-Defined PATH Variable

      ## Secondary image placeholders:
      self.img_attack = [pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_0-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_1-####.png"))),
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_2-####.png")))]
     
      self.image_death = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-CORPSE-####.png")))

     ## Image Loading: (init)
      self.image = self.img_org[0] # Set Default image
      self.img_pre_render = 0
     
     ## Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y

      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      
      # Animation Mechanics 
      self.max_frames = len(self.img_pre_render)
      self.current_frame = 0 ## current frame for animation
      self.animation_time = 0.1 ## threshold for next frame (time)
      self.current_time = 0 ## current timing for animation

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
      self.image = self.img_pre_render
    
   ## LIFE 
   if self.health <= 0:
        self.death = True

  if self.death == False: # Check if Alive/Active

      keys = pygame.key.get_pressed()
      if keys[pygame.K_w] or keys[pygame.K_UP]:
        if player.rect.y < room_height and player.rect.y >= 0:
                           self.rect.y -= 2
     elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player.rect.x < room_width and player.rect.y >= 0:
                           self.rect.x += 2
     elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player.rect.x < room_width and player.rect.y >= 0
                           self.rect.x -= 2
     elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if player.rect.y < room_height and player.rect.y >= 0:
                           self.rect.y += 2
       
      # Make instance rotate around point (define point by px,py)
      mx,my = = pygame.mouse.get_pos() # center point of mouse (assuming this game is a top-down or requires the player to face the mouse)
      rel_x, rel_y = round(mx - self.rect.x), round(my - self.rect.y) # find difference between mouse and rect coordinates
      angle = round((180/math.pi)*+math.atan2(rel_x,rel_y)) # Trignometery for rotation
      self.image = pygame.transform.rotate(self.image_clean,angle) # rotate image
      
      self.rect = self.image.get_rect(center=self.rect.center) # set new boundary

     
      if self.current_frame >= self.max_frame: # Animation Frame loop
          self.current_frame = 0
      
     
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
    ## i.e.:
    if self.target != 0:
      if self.attacking == True:
        if self.current_frame = 3: # Placeholder number, edit for your needs.
          self.debuff = self.debuff + (self.debuff*self.target.attack)
          self.damage_calc = self.damage/self.debuff
          self.target.life -= self.damage_calc
  
  pass

##################################################
##################################################
##################################################


#
# ... add more OBJECTS
#

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

# Initialize Pygame
pygame.init()
#pygame.mixer.init() # uncomment to use audio engine.

# Pygame/Game intialisation
width, height = 960, 540 # Default APR: 16:9 1.777, RESO DIMEN: 960 x 540 px (1920 x 1080 % 2), scale resolution by 2.
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME_NAME") ## Change Game title name here
clock = pygame.time.Clock()
running = True

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
def check_client_timeout(client_socket):
       try:
         for client in log.keys():
          client_socket.send(b"PING")
        return True
    except socket.error:
         client_socket.close()
        return False

def start_client_timer(dt,duration, clinet_socket):
   if dt > duration:
      check_client_timeout(client_socket)

def handle_client(client_socket, client_address, client_message, dt):
   message = client_socket.recv(1024).decode()
   client[client_address].start_client_timer(dt+120, client_socket)
   print(f"Player {client_address} said: {message}")
   log[client_address].append(message)
   tot_log = len(list(log.keys()))
   if tot_log > 0:
      key_value_log = log[list(log.keys())[tot_log]] 
   else:
      key_value_log = log[list(log.keys())[0]] 
   
# Send result back to all players
   for client in log.keys():
      client_socket.send(key_value_log.encode())

   except Exception as e:
        print(f"Error: {e}")
     finally:
        client_socket.close()

 #####################
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((My_IP, PORT))
    server.listen(max_clients)
    print("Server listening on port: " +str(PORT))

      log = {}

    while True:
        client_socket, client_address = server.accept()
        print(f"Player connected from {client_address}")
        client_socket.setblocking(0)
        threading.Thread(target=handle_client, args=(client_socket, client_address, client_message)).start()
        pass
#####################
   ##################################################
   # Client:
   ##################################################
def send_message(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setblocking(0)
            s.connect((online_host_address, online_host_port))
            if s:
               readable, writable, errored = select.select([], [s], [], 0)
               if writable:
               s.send(message.encode())
               print("message sent!")
            try:
               data = s.recv(1024)
               if data:
                  recv_message(data)
                  return print("message recieved!")
               else:
                   print("No data received.")
                except BlockingIOError:
                 s.setblocking(0)
                 print("No data available (BlockingIOError).")
                except Exception as e:
                 print(f"An error occurred: {e}")
                   pass
       except Exception as e:
         print (f"Error: Unable to connect to server. {e}")
                  pass
 #####################
def recv_message(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setblocking(0)
            readable, writable, errored = select.select([s], [], [], 0)
            if readable:
            recv_message = s.recv(1024).decode()
            return see_message(recv_message)
    except Exception as e:
       return "Error: Unable to recieve data from server."
    except BlockingIOError:
       s.setblocking(0)
       send_message(My_IP +" | "+ temporal_measurements +" : "+"404, didn't get last message.")

 #####################
   ##################################################
   # Client and Server:
   ##################################################
def see_message(message):
   if message:
            result_text = FONT.render(message, True, RED)
      #####################

def multiplayer():
   if Client == True:
      online_host_address = input("Type in IP of HOST")
      online_host_port = input("Type in PORT of HOST")
      if online_host_address, online_host_host:
         send_message(My_IP +" | "+ temporal_measurements +" : "+"I have connected! Thanks for having me.")

   if Server == True:
      PORT = input("Please pick a port number i.e. 8080 or 5050")
      start_server()
      print(My_IP)
      print(PORT)
     #####################
##################################################
####################################################################################################
####################################################################################################
#Visual intialisation
####################################################################################################
####################################################################################################
#Groups:
Splash = pygame.sprite.Group()
Player = pygame.sprite.Group()
Enemy = pygame.sprite.Group()
# Branding Objects:
Company_branding = splash(0,0,Splash)
# Game Objects:
obj_NPC = Object_0(rand_random(room_ROOM_width),rand_random(room_ROOM_width),Enemy) # Spawns ONE enemy at random location
obj_Player = Object_1(10,10,Player) # Spawns player at x:10, y:10 
# Multi-Spawner
i ++
if i < Max_Entities:
  NPC_MULTI.append(Object_0(rand_random(room_ROOM_width),rand_random(room_ROOM_width),Enemy))

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
#fingers = [] # Touch Register

##################################################
# Primary Game Loop:
##################################################
##################################################
##################################################
async def main():
    #Globals (to reach inside game loop):
    global dt
   ##################################################
    #Event System/Control System:
   ##################################################
    while running:
     for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
      # ...
      # ...
      ## For device touch mechaninics:
      #  if event.type == pygame.FINGERDOWN:
      #      x = event.x * screen.get_height()
      #      y = event.y * screen.get_width()
      #      fingers[event.finger_id] = x, y
      #  if event.type == pygame.FINGERUP:
      #      fingers.pop(event.finger_id, None)  


##################################################
   ##################################################
      ##################################################
    ## Scene Hyirachy:
    if SPLASH == True:
        screen.blit(Company_branding,(0,0)) # Small image for publicity 
        Splash.draw(screen)
      pass # Splash screen for Branding
    if MENU == True:
       pass # Menu to select features
    if ROOM == True:
      screen.blit(obj_NPC) # Render NPC
      screen.blit(obj_Player) # Render Player
      screen.blit(NPC_MULTI) # Render Multi-spawned NPCs
      Enemy.draw(screen) # Draw Enemy
      Player.draw(screen) # Draw Player
      # ...
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
    print(dt)
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
