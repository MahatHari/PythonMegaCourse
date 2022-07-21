import justpy as jp
from matplotlib.pyplot import text


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course Reviews",
                 classes="text-h2 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These grapsh represent course review analysis")
    return wp


jp.justpy(app)
