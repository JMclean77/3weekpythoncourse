"""
This is a script that checks if a citizens
speed has exceeded the speed limit
and issues a ticket if it is true
"""

def cal_ticket():
    """
    This function takes user input
    checks if the value is a numerical value, if true it proceeds
    if not it prompts the user to re-enter the value
    if input is below the max speed it prints as such
    if the input is above max speed it calculates the amount above speed limit
    and the ticket amount
    """
    while True:
        try:
#if value entered is a float breaks the while loop
            speed = float(input("Enter the speed in km/h: "))
            if speed == float(speed):
                break
#If value entered is not float displays error message
        except ValueError:
            print("Invalid input please input a numerical speed value")
#math to calculate if citizen exceeded speed
#if true calculates the value of the ticket and displays a message
#if false displays a message
    max_speed = float(60)
    ticket_amount = 17 * speed - max_speed
    above_speed_value= speed - max_speed
#Displays the false message of the math above
    if speed <= max_speed:
        print("\nNo ticket required, citizen is under or at the maximum speed")
#Displays the true message of the match above and the values of the output
    if speed > max_speed:
        print(f"\nCitizen is above the maximum speed at {speed} km/h")
        print(f"Citizen is {above_speed_value:,.2f} km/h above the speed limit")
        print(f"Citizen is to be ticketed at ${ticket_amount:,.2f}")
        print()

cal_ticket()
