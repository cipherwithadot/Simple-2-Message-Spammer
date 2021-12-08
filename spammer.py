import pyautogui
import time

msg1 = input("Enter the message: ")
msg2 = input("Enter the Second message: ")
n = input("How many times ?: ")
delay = int(input("How much delay do you want bettween messages ?: "))
print()
print("T Minus")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1
print()
print("Fire in the hole!!!")

for i in range(0,int(n)):
	pyautogui.typewrite(msg1 + '\n')
	pyautogui.typewrite(msg2 + '\n')
	time.sleep(delay)
