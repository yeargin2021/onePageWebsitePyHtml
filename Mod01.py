#def main():
def top():
    print ("""
            <html>
                <head></head>
                <title>Hello world!</title>
                <body>
                    <h1>hi there</h1>
            """)
def body():
    file = open("blogPost01.txt", "r")
    for i in file:
        print(i)
    file.close()
def bottom():
    print ("""
                </body>
            </html>
            """)


if __name__ == '__main__':
    top()
    body()
    bottom()
