"""
Project : Desktop Health Notifier

This project is about sending healty remainders to drink water and take food on time.

It will send notifications to take water breaks and take food on time like breakfast, lunch, 
snacks and dinner.

It will send water notifications for every 45 minutes and food notifications as per below timings.

Between 8:30AM and 9:00AM -  Breakfast 
Between 12:30PM and 1:00PM - Lunch
Between 4:30 PM and 5:00 PM - Snacks
Between 7:30 PM and 8:00 PM - Dinner

"""

#notify-py library is used to send notifications
from notifypy import Notify
import notifications as notifier
import time


def main():
    health_notifier()

def health_notifier():
    # It will get the current time
    current_time = get_time()

    # It will get the details of specific content for notification and type of notification
    # If water_icon is True then it is a water remainder else it will be a food remainder

    notification  , water_icon , break_type = get_remainder(current_time)

    # It will get customized notifications based on the above notification
    customized_notification = get_customized_notifier(notification)

    # icons will get image name either for water or for the food notifications from the list of images
    icons = get_icons(water_icon)

    # It will sets the path for the above icon images
    icons_path = f"images\{icons}"
   

    # It will send the notification to desktop
    send_notification(customized_notification,icons_path,break_type)


# It will return the current time in HH:MM format
def get_time():
    local_time = time.localtime()
    current_time = time.strftime("%H:%M", local_time)
    return current_time

# If will customize the given notification and returns the customized notification if possible  
def get_customized_notifier(customized_notification):

    if "[Your Name]" in customized_notification:
        name = notifier.customized_names()
        customized_notification = customized_notification.replace("[Your Name]",name)
        
    return customized_notification

# Based on time it will decide which type of notification should be send
def get_remainder(current_time):

    hour , minutes = current_time.split(":")
    hour = int(hour)
    minutes = int(minutes)
    
    # Initially it assumes it's a food remainder
    water_notifier = False

    if hour == 8 and minutes >= 30:
        remainder_type = notifier.breakfast_notifications()
        break_type = "Breakfast"

    elif hour == 12 and minutes >= 30:
        remainder_type = notifier.lunch_notifications()
        break_type = "Lunch"

    elif hour == 16 and minutes >= 30:
        remainder_type = notifier.snacks_notifications()
        break_type = "Snacks"

    elif hour == 19 and minutes >= 30:
        remainder_type = notifier.dinner_notifications()
        break_type = "Dinner"

    else:
        remainder_type = notifier.water_notifications()
        break_type = "Water"
        water_notifier = True
    
    return remainder_type,water_notifier,break_type


# It will return water icon if water_icons is True else it will return food icon image
def get_icons(water_icons):
    if water_icons:
        return notifier.water_icons()
    return notifier.food_icons()

# It will send a particular notification based on the passed parameters to the function.
def send_notification(custom_message,icons_path,break_type):
    notification = Notify()
    notification._notification_application_name = "Health Remainder"
    notification.title = f"Take a {break_type} Break"
    notification.message = custom_message
    notification.icon = icons_path
    notification.audio = r"ringtones\ringtone.wav"
    notification.send()
    
# It will call the main function
if __name__ == "__main__":
    main()