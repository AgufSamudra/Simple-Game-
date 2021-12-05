# SIMPLE GAME
class Hero:
    # INIT SELALU DI JALANKAN DULUAN/ SEPERTI MAIN DARI CLASS HERO
    def __init__(self, inputName, inputHealth, inputAttack):
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack

    def attackEnemy(self, enemy):
        print(self.name + ' Menyerang ' + enemy.name)
        print("Serangan yang di terima:", self.attack)
        enemy.reHealth(self)

    def reHealth(self, enemy):
         print(self.name + " Di Serang " + enemy.name)
         sisa_darah = self.health - enemy.attack
         print("Sisa darah " + self.name + ":", sisa_darah)

KillJoy = Hero('Kill Joy', 150, 50)
Reyna = Hero("Reyna", 150, 40)

print("\n")
KillJoy.attackEnemy(Reyna)
print("\n")
Reyna.attackEnemy(KillJoy)
print("\n")