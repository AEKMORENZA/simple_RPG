from random import randint
 
class Item:
    def __init__(self):
      self.name = name
      self.description = description
      self.value = value
    def __str__(self):
      return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
	
class Character:
  def __init__(self):
    self.name = ""
    self.health = 1
    self.level = 0
    self.health_max = 1
    self.experience = 0
    self.max_experience = 5
    self.classe = ""	
    self.profession = ""	
  def do_damage(self, enemy):
    damage = min(
        max(randint(0, self.health) - randint(0, enemy.health), 0),
        enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0: print "%s esquiva el ataque de %s." % (enemy.name, self.name)
    else: print "%s hiere a %s!" % (self.name, enemy.name)
    return enemy.health <= 0

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.health = randint(1, player.health)	

class Goblin(Enemy):
  def __init__(self, enemy):
    Enemy.__init__(self)
    self.name = 'Un Goblin'
    self.health = randint(1, player.helath)	
 
class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
    self.experience = 0
  def quit(self):
    print "%s no puede encontrar el camino de vuelta a casa y muere de inanicion.\nR.I.P." % self.name
    self.health = 0
  def help(self): print Commands.keys()
  def status(self): print "Salud de %s: %d/%d  Experiencia: %d/%d  Nivel: %d" % (self.name, self.health, self.health_max, self.experience, self.max_experience, self.level)
  def tired(self):
    print "%s se siente cansado." % self.name
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print "%s no puede descansar ahora!" % self.name; self.enemy_attacks()
    else:
      print "%s descansa." % self.name
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s es despertado subitamente por %s!" % (self.name, self.enemy.name)
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print "%s ha dormido demasiado." % self.name; self.health = self.health - 1
  def explore(self):
    if self.state != 'normal':
      print "%s esta demasiado ocupado ahora mismo!" % self.name
      self.enemy_attacks()
    else:
      print "%s explora un sinuoso pasadizo." % self.name
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s encuentra %s!" % (self.name, self.enemy.name)
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def flee(self):
    if self.state != 'fight': print "%s corre en circulos durante un rato." % self.name; self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print "%s huye de %s." % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
      else: print "%s no puede escapar de %s!" % (self.name, self.enemy.name); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print "%s corta el aire sin resultados aparentes." % self.name; self.tired()
    else:
      if self.do_damage(self.enemy):
        print "%s ejecuta %s!" % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
        self.experience += 1
        #TBW si experiencia >= experiencia maxima por nivel: nivel += 1
        if self.experience >= self.max_experience:
          self.level += 1
          self.max_experience *= 3
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print "%s se siente mas fuerte!" % self.name
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print "%s fue asesinado por %s!!!\nR.I.P." %(self.name, self.enemy.name)
 
Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  }
 
p = Player()
p.name = raw_input("Cual es el nombre de tu personaje? ")
p.classe = raw_input("Cual es tu clase " + str(p.name) + "? " )
p.profession = raw_input("Y cual es tu oficio?")
print "(escribe help para ver una lista de acciones)\n"
print "%s entra en una cueva oscura, buscando aventuras." % p.name
 
while(p.health > 0):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print "%s no entiende la sugerencia." % p.name
 
"""
Copyright 2010 Francesco Balducci
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
See <http://www.gnu.org/licenses/> for a copy of the GNU General Public License.
"""
