def read_data(file_path, feature=1):
    """
    (1) This function will read the given file
    (2) Arguments: an input file
    (3) The returned value: a dictionary {label:data}
    """
    data = {}
    lable = []
    value = []
    lines = open(file_path, 'r').readlines()
    print("Content: \n")
    print(lines)
    print("Data for drawing: \n")
    for i in range(0, len(lines), 3):
        lable = lines[i].rstrip()
        data[lable] = int(lines[i+feature])
    print(data)
    return data

def count_observations(file_path):
    """
    (1) This function will calculate the number of observations from the file
    (2) Arguments: an input file
    (3) The returned value: number of observations
    """
    lines = open(file_path).readlines()
    return len(lines) // 3

def get_max_value(file_path, feature=1):
    """
    (1) This function will compute the maximum value of the feature of interest
    (2) Arguments: an input file, feature
        (with default =1 which will consider feature 1 is the interest)
    (3) The returned value: maximum value of the feature of interest
    """
    lines = open(file_path).readlines()
    max_label = lines[0]
    max_value = lines[feature]
    for i in range(0, len(lines), 3):
        label = lines[i]
        value = lines[i + feature]
        if value > max_value:
            max_label = label
            max_value = value
    #print('largest:', (max_label, max_value))
    return max_value

### Create and Setup the Window ###
def setup_screen(turtle, data):
    """
    (1) This function will get turtle to set up the window of the chart
    (2) Arguments: turtle, and an input file
    (3) No returned value
    """
    title = input("what is your chart title? \n")
    #title = "Bar chart"
    num = len(data)
    ymax = max(list(data.values()))
    window = turtle.Screen()
    width = 200 + 120 * num #the space between each bar is 20, the width of each bar is 100
    window.setworldcoordinates(-300, -300, 300, 300)
    window.setup(width,600,0,0) #specify window size (height is 800)
    window.title(title) #give it the input title

def draw_axes(turtle, data):
    """
    (1) This function will get turtle to draw x-axis and y-axis and y-ticks
    (2) Arguments: turtle, and an input file
    (3) No returned value
    """
    #draw y-axis
    num = len(data)
    ymax = max(list(data.values()))
    y_tick = 400/10
    i = 1
    turtle.left(90)
    while i <= 10:
        turtle.forward(y_tick)
        yv1 = float(ymax/10*i)
        yv = '%.1f' % yv1
        turtle.write(yv, move=False, align="right", font=("Arial", 14, "normal"))
        turtle.right(90)
        turtle.forward(10)
        turtle.backward(10)
        turtle.left(90)
        i += 1
    turtle.backward(400) #back to start point
    turtle.right(90) 
    #draw x-axis
    turtle.forward(70*num)
    turtle.backward(70*num) #back to start point


def draw_rectangle(turtle, rec_height, rec_width, c):
    """
    (1) This function will get turtle to draw a rectangle
    (2) Arguments: 
    turtle for drawing, 
    rec_height is the height of rectangle, 
    rec_width is the width of rectangle, 
    and c is the color of the rectangle
    (3) No returned value
    """
    turtle.forward(10) #the space between each bar is 10
    turtle.left(90)
    turtle.pencolor('black')
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.forward(rec_height) # height of bar
    turtle.right(90)
    turtle.forward(rec_width)
    turtle.right(90)
    turtle.forward(rec_height)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(10)

def choose_color(number):
    """
    (1) This function will help to choose the color for the chart
    (2) Arguments: an int value
    (3) Return the chosen color 
    """
    colors = ['#DAF7A6', '#FFC300', '#FF5733', '#C70039',
              '#900C3F', '#581845', '#117a65', '#d68910',
              '#DAF7A6', '#FFC300', '#FF5733', '#C70039'
              '#009933','#996699','#CCFFFF','#FFCC33',
              '#FF33CC','#336600','#CCCC44','#990033',
              '#FFFF99','#9999CC','#FFCC33','#333333',
              '#9999FF','#993399','#CC99CC','#CC9966',
              '#FF99CC','#CCCC66','#990033','#458b74'
              '#999900','#00CC00','#333399','#993333',
              '#F00000','#999933','#CCCC99','#FF9933',
              '#006699','#CC3366', '#0099CC','#9999CC',
              '#999999','#66CC66','#996699','#FF6600',
              '#006600','#CCFF66','#3366CC','#666666']
    color = colors[number]
    return color

def draw_bars(turtle, data):
    """
    (1) This function determine the size and position of rectangles that need to be drawn, and then draw bars
    (2) Arguments: turtle and data input
    (3) No returned value
    """
    num = len(data)
    ymax = max(list(data.values()))
    width = 50 + 60 * num #width of the chart
    rec_width = width/(num+4) #width of the rectangle
    pixel = ymax/400 
    i = 0

    for a,b in data.items():
        #z = int(input('Choose your color by type a number (0-50)'))
        z = random.randint(0,49) # value of colors
        print(z)
        c = choose_color(z)
        rec_height = b/pixel
        turtle.color('black')
        turtle.forward(5)
        turtle.up()
        turtle.right(90)
        turtle.forward(rec_width)
        turtle.left(90)
        turtle.forward(40)
        turtle.write(a, move=False, align="center", font=("Arial", 14, "normal"))
        turtle.backward(40)
        turtle.left(90)
        turtle.forward(rec_width)
        turtle.right(90)
        turtle.pendown()
        draw_rectangle(turtle, rec_height, rec_width, c)
        turtle.forward(5)
        i += 1
    turtle.color('black')
    turtle.backward(rec_width*num+10) #back to start point
    turtle.forward(rec_width*num+20)

if __name__ == "__main__":
    import turtle
    import os
    import random
    current_dir = os.getcwd()

    print("Welcome to the Turtle Charter!")
    ### Prompt for input ###
    #file_name = input("Please type your file name: (eg:sample_data.txt) \n ")
    #file_name = "sample_data.txt"
    #file_name = "huskies2016.txt"
    #file_path = current_dir + "/data/" + file_name
    path = input("Please type the path to your file: (eg:data/sample_data.txt) \n ")
    file_path = current_dir + "/" + path
    # Read data
    data = read_data(file_path)
    # See observations
    print(count_observations(file_path))
    # Get max value
    print(get_max_value(file_path))

    # Set up screen & chart position in the screen
    setup_screen(turtle, data)
    
    tur = turtle.Turtle()
    
    width=50+20*(count_observations(file_path)+1)
    tur.speed(0)
    tur.up()
    tur.setpos(-(width/2+350),-225)
    tur.pendown()

    # Draw chart
    draw_axes(tur, data)
    draw_bars(tur, data)
    
    
    # User will close the window
    turtle.mainloop()
