'''
6. You have a list of daily temperatures recorded over a month. Write code to:

 Calculate and print the average temperature for the month.
 Find and print the highest and lowest temperatures.
 Sort the temperatures in ascending order.
 Remove the temperature record for a specific day
Given Temperature list in °C = [22, 24, 30, 35, 29, 22, 20, 19]


'''
temperature_list= [22, 24, 30, 35, 29, 22, 20, 19]
average = (sum(temperature_list))/(len(temperature_list))

highest_temp = max(temperature_list)
lowest_temp = min(temperature_list)

soreted_list = sorted(temperature_list)

try:
    index_to_remove = int(input("ENTER THE INDEX/DAY (0-7) YOU WANT TO REMOVE FROM THE LIST: "))
    if 0 <= index_to_remove < len(temperature_list):
        removed_temp = temperature_list[index_to_remove]
        del temperature_list[index_to_remove]
        print(f"Removed temperature: {removed_temp}°C")
        print(f"LIST AFTER REMOVING {temperature_list}")
    else:
        print("Invalid index. Please enter a number between 0 and 7.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

print(f"THE AVERAGE TEMERATURE IS {average:.2f}")
print(f"HIGHEST TEMPERATURE IS {highest_temp}")
print(f"LOWEST  TEMPERATURE IS {lowest_temp}")
print(f"SORTED LIS IN ASCENDING ORDER IS {soreted_list}")
 
