
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv


def generateWordCloud():

    r = open(r"PATH")
    r_ob = csv.reader(r)
    contents = list(r_ob)

    #Adding to a text string
    text = ""

    for row in contents:
        for word in row:
            text = text + " " + word

    #Size of image and number of words
    wordcloud = WordCloud(width=480, height=480, max_words=15).generate(text)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()


if __name__ == '__main__':
    generateWordCloud()

