import requests
import tkinter as tk
from PIL import Image, ImageTk

def getNews():
    api_key = "f3c829222e4d4942ab16b0334746bb2c"
    url = "https://newsapi.org/v2/top-headlines?country=gb&category=health&apiKey=f3c829222e4d4942ab16b0334746bb2c"
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = []
    my_news = ""
    links = ""

    for article in articles:
        my_articles.append(article["title"])
        #my_articles.append(article["url"])

    for i in range(20):
        my_news = my_news +  str(i+1) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)

root = tk.Tk()
# Everything between this and canvas.mainloop will be in the UI window.
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)
root.title("Healthcare News App")

# Logo
logo = Image.open('FL463_Explore_industries_-_Healthcare_blog_header-606x303.jpeg')
# convert to tkinter image
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=10)

button = tk.Button(canvas, font=24, text= "Reload", command=getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)


getNews()

canvas.mainloop()