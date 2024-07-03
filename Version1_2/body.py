def body():
    print("     <body>")
    file = open("posts/blogPost01.txt", "r")
    for i in file:
        print(i, "<br>")
    file.close()
    print("     </body>")
