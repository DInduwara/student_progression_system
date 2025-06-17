##student id:w2051597(20230231)
##Date: 14/ 12/ 2023
##I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion
##Any code taken from other sources is referenced within my code solution

from graphics import *

def histogram():
    global progress_count, Trailer_count, Retriever_count, Excluded_count, total_outcome
    progress_height = progress_count * 8
    Trailer_height = Trailer_count * 8
    Retriever_height = Retriever_count * 8
    Excluded_height = Excluded_count * 8

    win = GraphWin("histogram", 400, 300)
    win.setBackground("#edf2ec")

    line = Line(Point(20, 250), Point(380, 250))
    line.draw(win)

    label = Text(Point(80, 24), "Histogram Results.")
    label.setStyle("bold")
    label.draw(win)

    outcome = Text(Point(100, 280), str(total_outcome) + " outcomes in total")
    outcome.setStyle("bold")
    outcome.draw(win)

    # Define a list for different categories
    categories = [ {"name": "Progress", "count": progress_count, "colour": "#97fb97"},
        {"name": "Trailer", "count": Trailer_count, "colour": "#96c783"},
        {"name": "Retriever", "count": Retriever_count, "colour": "#a2bd6e"},
        {"name": "Excluded", "count": Excluded_count, "colour": "#d8b5b4"}]
       
    

    # Draw rectangles for each category
    for i, category in enumerate(categories):
        height = category["count"] * 8
        rect = Rectangle(Point(24 + i * 80, 250), Point(96 + i * 80, 250 - height))
        rect.setFill(category["colour"])
        rect.draw(win)
        text_count = Text(Point(24 + i * 80 +30, 240 - height), str(category["count"]))
        text_count.setStyle("bold")
        text_count.draw(win)
        text_name = Text(Point(24 + 35 + i * 80, 260), category["name"])
        text_name.setStyle("bold")
        text_name.draw(win)

    win.getMouse()
    win.close
        
# Variables 
total_outcome=0
progress_count=0
Trailer_count=0
Retriever_count=0
Excluded_count=0

progress_list = []
trailer_list = []
retriever_list = []
excluded_list = []

# Print the stored data in the list
def print_data():
    print("Part 2:")
    for entry in progress_list:
        print(f"Progress - {entry[0]}, {entry[1]}, {entry[2]}")

    for entry in trailer_list:
        print(f"Progress(module trailer) - {entry[0]}, {entry[1]}, {entry[2]}")

    for entry in retriever_list:
        print(f"Module retriever - {entry[0]}, {entry[1]}, {entry[2]}")

    for entry in excluded_list:
        print(f"Exclude - {entry[0]}, {entry[1]}, {entry[2]}")

# Save data to the text file
def save_data_text_file():
    with open("progression_data.txt", "w")as file:
        file.write("progression data:\n")
        for entry in progress_list:
            file.write(f"Progress - {entry[0]}, {entry[1]}, {entry[2]}\n")
        for entry in trailer_list:
            file.write(f"Progress(module trailer) - {entry[0]}, {entry[1]}, {entry[2]}\n")
        for entry in retriever_list:
            file.write(f"Module retriever - {entry[0]}, {entry[1]}, {entry[2]}\n")
        for entry in excluded_list:
            file.write(f"Exclude - {entry[0]}, {entry[1]}, {entry[2]}\n")

# Read data from a text file
def read_data_text_file():
    with open("progression_data.txt", "r")as file:
        print("part 3:")
        print(file.read())
# Determine progression outcome based on credits        
def progression_outcome(pass_credit, defer_credit, fail_credit):
    global progress_count, Trailer_count, Retriever_count, Excluded_count


    if pass_credit == 120:
        progress_count += 1
        progress_list.append([pass_credit, defer_credit, fail_credit])
        return "Progress"
    elif fail_credit >= 80:
        Excluded_count += 1
        excluded_list.append([pass_credit, defer_credit, fail_credit])
        return "Exclude"
    elif 80 < pass_credit <= 100:
        Trailer_count += 1
        trailer_list.append([pass_credit, defer_credit, fail_credit])
        return "Progress(module trailer)"
    elif pass_credit <= 80:
        Retriever_count += 1
        retriever_list.append([pass_credit, defer_credit, fail_credit])
        return "Module retriever"

# Validate user input within a specific range
def valid_input(prompt, valid_range):
    while True:
        try:
            credit_input = int(input(prompt))
            if credit_input not in valid_range:
                print("Out of range")
                continue
            return credit_input
        except ValueError:
            print("Integer required")
# Main program loop to input data and perform operations
while True:
    pass_credit = valid_input("Enter your PASS credits: ", range(0, 121, 20))
    defer_credit = valid_input("Enter your DEFER credits: ", range(0, 121, 20))
    fail_credit = valid_input("Enter your FAIL credits: ", range(0, 121, 20))

    total_credits = pass_credit + defer_credit + fail_credit
    if total_credits != 120:
        print( "Total incorrect")
        continue

    print( progression_outcome(pass_credit, defer_credit, fail_credit))
    total_outcome+=1

    
    while True:
        user_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to qiut and view results: ")
        if user_input.lower()=="q":
            break
        elif user_input.lower()=="y":
            break
        else:
            print("please enter 'q' or 'y'")
            
    if user_input.lower() == "q":
        save_data_text_file()
        break
    elif user_input.lower() == "y":
        continue
print_data()
histogram()
read_data_text_file()
