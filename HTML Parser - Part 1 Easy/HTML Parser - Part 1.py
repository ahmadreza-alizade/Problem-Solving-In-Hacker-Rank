from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if len(list(attrs)) != 0:
            for kaj in attrs:
                print("-> " + kaj[0], end="")
                if kaj[1] != "None":
                    print(" > " + str(kaj[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for kaj in attrs:
            if len(list(attrs)) != 0:
                print("-> " + kaj[0], end="")
                if kaj[1] != "None":
                    print(" > " + str(kaj[1]))

    # def handle_data(self, data):
    #     print(data)


n_lines = int(input())
my_string = "<html><head><title>HTML Parser - I</title></head>"

lines = []
for l in range(0, n_lines):
    lines.append(input())

parser = MyHTMLParser()

for line in lines:
    parser.feed(line)
