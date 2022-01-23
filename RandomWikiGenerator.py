import wikipedia

print("Welcome to the Random Wiki Generator!\n"
+"Type start to look at your first article")

#Get user input to start application
usr_input = ""
while usr_input.lower() != "start":
    usr_input = input()

usr_input = "yes"

import re

#Loop while the user answers yes to "[Read Another Article? (type yes)"
while usr_input == "yes":
    print("[Loading article...]\n")
    #Get random wiki article
    wiki = wikipedia.page(wikipedia.random())
    
    #Print title
    print("\n" + wiki.title,"\n\n") 

    #Get wiki page content
    text = wiki.content

    #Split paragraphs into array
    content = re.split(r"\n\n\n==.*==", text) #Returns array of each wikipedia section inclusing the introduction
    #Get article headings
    headings = re.findall(r"==.*==", text) #Returns array of each wikipedia heading after the introduction
    
    print(content[0],"\n")
    if len(content) > 1:
        print("[Read More? (type yes)]")
        usr_input2 = input().lower()
        print("\n")
        i = 1
        #Loop (print next paragraph of article) while the user doesn't enter "no"
        while usr_input2 != "no" and i < len(content) - 2:
            print(headings[i - 1].replace("=", "")[1:])
            print(content[i],"\n")
            i += 1
            print("[Read More? (type yes)]")
            usr_input2 = input().lower()
            print("\n")
        #Print last section
        if usr_input2 == "yes":
            print(headings[i - 1].replace("=", "")[1:])
            print(content[i],"\n")
            print("\n")
    print("[Read Another Article? (type yes)")
    usr_input = input().lower()
    print("\n")
print("Thanks for reading. Goodbye")