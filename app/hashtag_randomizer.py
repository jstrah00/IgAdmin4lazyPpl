import random

small_ht = ['#hotcars','#omgcars ','#amazingcar247','#luxurycarlife','#luxuryvehicle','#supercarlife','#carswhitoutlimits','#caranddriver','#trackaddicts','#autounlimited','#carbooty','#racecarlife','#thecardrawer','#superexoticscars','#carporn101','#supercarsbuzz']
medium_ht = ['#bestcar','#carsoftheday','#carthrottle','#motor_head_','#dreamcar','#cars247','#projectcar','#dailydriver','#carmeets','#carsovereverything']

small_choices = random.sample(small_ht, 6)
medium_choices = random.sample(medium_ht,4)

hashtags = small_choices + medium_choices 
random.shuffle(hashtags)
separator = ' '
hashtags_joined = separator.join(hashtags)
final_string = ".\n.\n.\n.\nPicture: @unknown (DM FOR CREDITS)\n"
final_string = final_string + hashtags_joined

print(final_string)
