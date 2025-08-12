'''
Every 20 minutes, look at something 20 feet away for 20 seconds. Then close your eyes for 5 sec.
'''
from winotify import Notification, audio
import pyttsx3
import time
import os

# Setup speech engine once
engine = pyttsx3.init()
# Icon path
icon_path = os.path.abspath("eye_icon.ico")
if not os.path.exists(icon_path):
    print("Warning: Icon not found. Notifications will show without an icon.")

repeat_interval = 1200   # every 20 min

try:
    while True:
        title = "Reminder!"
        message = "20-20-20 rule time!!"
        message_say = "Hey, it's 20 20 20 rule time!"
        
        # Show toast
        toast = Notification(app_id="EyeCare Reminder",
                            title=title,
                            msg=message,
                            duration="long",
                            icon=icon_path)  # "long"== 25 sec, 20 sec for watching outside
        toast.set_audio(audio.Default, loop=False)
        toast.show()

        # Speak message
        engine.say(message_say)
        engine.runAndWait()

        time.sleep(repeat_interval)

except KeyboardInterrupt:
    print("Code stopped by user.")

except Exception as e:
    print(e)

    
