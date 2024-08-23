import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
        title = "Please Drink water",
        message ="Women should have about 2 litres (8 cups) of fluids a day, and men about 2.6 litres (10 cups). People who are pregnant or breastfeeding need more fluid each day than usual. Dehydration can happen when the body's fluids are low.",
        app_icon ="C:/Users/fateh/OneDrive/Desktop/Rupinder/PYTHON PROJECT 1/icon.ico",
        timeout=5
        
    )
    time.sleep(60*60)
    