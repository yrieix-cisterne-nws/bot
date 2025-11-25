from PIL import Image, ImageDraw, ImageFont
import datetime as dt
#

# Font used
timer = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 150, )
texte = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 70)
image = Image.open("s18splashart.png")

# Date of new season and date of now
endofseason = dt.datetime(2025, 10, 14, 20, 0)
actualtime = dt.datetime.now()

# Calculation of the time left between actualtime and endofseason
timebeforeseason = endofseason - actualtime
days, seconds = timebeforeseason.days, timebeforeseason.seconds # We get the seconds to then transform it into hours and minutes
hours, minutes = seconds // 3600, (seconds % 3600) // 60 
endofseason = f"{days:02d}:{hours:02d}:{minutes:02d}" #:02d is here to include a 0 if the timer goes for example at {1:5:9} with the use of :02d, it will become {01:05:09}

# Put the text in the middle of the image
image_width, image_height = image.size
x = image_width / 2
y = image_height / 2

draw = ImageDraw.Draw(image)
draw.text((x, y), endofseason, font=timer, anchor="mm", fill="black")
draw.text((x, 50), "Season 18", font=texte, anchor="mm")
draw.text((x, image_height-50), "14 October 2025", font=texte, anchor="mm")

image.show()
image.save("s18timer.png")

