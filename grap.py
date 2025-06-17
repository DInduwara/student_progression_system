from graphics import*
total_count=30
progress_count=14
Trailer_count=10
Retriever_count=5
Excluded_count=1

progress_height=progress_count*8
Trailer_height=Trailer_count*8
Retriever_height=Retriever_count*8
Excluded_height=Excluded_count*8

win = GraphWin("histrogram",400 ,300)
win.setBackground("white")

line= Line(Point(20,250), Point(380,250))
line.draw(win)

label =Text(Point(80, 24), "Histogram Results.")
label.draw(win)

outcome= Text(Point(100,280), str(total_count)+" outcomes in total")
outcome.draw(win)

box= Rectangle(Point(24, 250), Point(96, 250-progress_height))
box.setFill("red")
box.draw(win)
text= Text(Point(24+35,260), "Progress")
text.draw(win)
count= Text(Point(24+6+30, 240-progress_height), str(progress_count))
count.draw(win)

box= Rectangle(Point(96+14, 250), Point(96+14+72, 250-Trailer_height))
box.setFill("green")
box.draw(win)
text= Text(Point(110+35,260), "Trailer")
text.draw(win)
count= Text(Point(96+14+6+30, 240-Trailer_height), str(Trailer_count))
count.draw(win)


box= Rectangle(Point(196, 250), Point(268, 250-Retriever_height))
box.setFill("red")
box.draw(win)
text= Text(Point(196+35,260), "Retriever")
text.draw(win)
count= Text(Point(202+30,240-Retriever_height), str(Retriever_count))
count.draw(win)

box= Rectangle(Point(282, 250), Point(354, 250-Excluded_height))
box.setFill("red")
box.draw(win)
text= Text(Point(282+35,260), "Excluded")
text.draw(win)
count= Text(Point(288+30, 240-Excluded_height), str(Excluded_count))
count.draw(win)


win.getMouse()
win.close

