def main():
    def top():
        return """
                <html>
                    <head></head>
                    <title>Hello world!</title>
                    <body>
                        <h1>hi there</h1>
                """
    file = open("blogPost01.txt", "r")
    for i in file:
        print(i)
    file.close()
    return """
                </body>
            </html>
            """


if __name__ == '__main__':
    print(main())
