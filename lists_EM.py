import webbrowser
name = "Ella"

subjects = ["Math", "Latin", "English", "Science", "History"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)
    
tvshows = ["Grey's Anatomy", "Glee", "The Good Place", "New Girl", "Stranger Things"]

for i in tvshows:
    if i == "Grey's Anatomy":
        print(i + " is my favorite show.")
    elif i == "Glee":
        print(i + " is about a highschool Glee club.")
    elif i == "Stranger Things":
        print(i + " only has two seasons so far.")
    else:
        print("one of my favorite shows is " + i)
    
    
movies = []

while True:
    print("What is a movie you like? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)


for i in movies:
    print("One of your favorites is " + i)
    webbrowser.open(i)
