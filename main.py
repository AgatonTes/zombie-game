# gra o zombie, tekstówka

#random () losuje floata miedzy 0 a 1 i ustawiam sobie parametr, że jesli
# - np. w supermarkecie szansa na spotkanie zombie jest duża, czyli jesli wylosuje floata miedzy 0 a np. 0.75
# to trafia na zombie
# - na stacji szansa jest mniejsza, więc jesli wyosluje floata miedzy 0 a 0.25 to trafia na zombie
# gdzie 0.75 i 0.25 sa parametrami stałymi dla tych wybranych miejsc

#dodanie grafiki - pygame, później
#dodanie zombie w zależności kilometrów np. 1 zombie na km i liczenie szansy na zombie na każdy km
#dodanie przejścia wybranej lokacji do kolejnej lokacji - kolejna petla
#dodanie różnego terenu i wyszukiwania najlepsziej sciezki A*

import math
import random
import time


class Spot:
#konstruktor,metoda _init_
	def __init__(self,coordinate_x, coordinate_y,chance):
		self.x = coordinate_x
		self.y = coordinate_y
		self.chance = chance

#metoda licząca odległośc między miejscami
	def road (self,m2):
		distance = math.sqrt((self.x-m2.x)**2+(self.y-m2.y)**2)
		print ("Odleglosc wynosi: " + str(distance) + "km")
		
#metoda mówiąca jaka jest szansa na spotkanie zombie i licząca czy się je spotkało czy nie w danym miejscu
	def zombie (self):
		global live
		fate = random.random()
		print("Szansa", fate)
		if fate < self.chance:
			print ("Spotkałeś bandę zombiaków i teraz jesteś jednym z nich.")
			print ("Game (as you know it) over.")
			live = False
		else:
			print ("Lucky you!")
			print ("Zero zombie i kilka przydatnych drobiazgów, które pozwolą Ci przetrwac jeszcze jakiś czas.")


home = Spot(0,0,0)
supermarket = Spot(3,3,0.75)
gas_station = Spot(1,2,0.30)
live = True

# historia

def Intro():
	print ("Świat stał się piekłem, świat jest w rękach wściekłych już-nie-ludzi, ")
	print ("którym marzy sie Twój świeży, lekko zblazowany mózg.")
	time.sleep(1)
	print ("Czy odważysz sie wyjść z domu?")
	print()
	
#pytanie - dlaczego w spotselector nie potrzebowałam uzyc global statment?
# bo zienna globalna moge odczytać bez globalna
#ale nie moge zapisac/zmianic, - wtedy wpada jako zmienna lokalna

#nowa funkcja wyboru miejsca, zapętlająca akcję - petla glupcze
def SpotSelector():
	spot = home
	while live == True:
		print ("Wybierz gdzie chcesz sie teraz udać:")
		if spot == home:
			print ("Supermarket - > 1")
			print ("Stacja benzynowa -> 2")
			print ()
			selectSpot = input("1 czy 2")
			if selectSpot == "1":
				spot = supermarket
				home.road(supermarket)
				supermarket.zombie()
			elif selectSpot == "2":
				spot = gas_station
				home.road(gas_station)
				gas_station.zombie()
		elif spot == supermarket:
			print ("Dom - > 1")
			print ("Stacja benzynowa -> 2")
			print ()
			selectSpot = input("1 czy 2")
			if selectSpot == "1":
				spot = home
				supermarket.road(home)
				home.zombie()
				StayAtHome()
			elif selectSpot == "2":
				spot = gas_station
				supermarket.road(gas_station)
				gas_station.zombie()
		else:
			print ("Dom - > 1")
			print ("Supermarket -> 2")
			print ()
			selectSpot = input("1 czy 2")
			if selectSpot == "1":
				spot = home
				gas_station.road(home)
				home.zombie()
				StayAtHome()
			elif selectSpot == "2":
				spot = supermarket
				gas_station.road(supermarket)
				supermarket.zombie()


#def - zostajesz w domy, raz za razem
def StayAtHome():
	global live
	print ("Mijają dni, jesteś już bardzo głodny.")
	time.sleep (1)
	print ("Czy odważysz się wyjść i poszukać jedzenia?")
	print ()
	reply = input("y or n")
	print ()
	if reply == "y":
		SpotSelector()
	else:
		print ("Ledwo się ruszasz, umierasz z głodu.")
		print (" To Twoja ostatnia szansa by wyjść i zdobyć pożywienie. Wychodzisz?")
		print ()
		reply = input("y or n")
		print ()
		if reply == "y":
			SpotSelector()
		else:
			print ("Umarłeś i... obudziłeś się... ")
			time.sleep (1)
			print ("Z nieposkromioną ochotą na świeży mózg.")
			live = False
			

playAgain = "yes"

while playAgain == "yes" or playAgain == "y":
	live = True
	print ("Gra o zombie")
	print ()
	Intro()
	act = input("y or n")
	if act == "y":
		SpotSelector()
	else:
		StayAtHome()
	
	print("Czy chcesz spróbowac jeszcze raz? yes/y lub no/n")
	playAgain = input()
		
  


