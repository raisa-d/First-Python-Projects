# Welcome to the Area Calculator!
from time import sleep

print("The calculator is powering up...")
sleep(1) # wait one second before the prompt to enter shape

#user chooses circle or triangle
option = input("Enter C for circle or T for triangle: ").upper()

# if they choose circle
if option == "C":
    radius = float(input("Enter radius: ")) #convert string to a float since it will be a radius
    area = 3.14159 * (radius*2) #area caclulation
    print("The area of the circle is", area)

elif option == "T":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5*base*height
    print("The area of the triangle is ", area)

else:
    print("Oops, you entered an invalid shape. Please try again.")

print("Thank you for using our calculator. Good morrow!")