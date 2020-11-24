from html5print import HTMLBeautifier

with open('test.html', 'rb') as f:
    html_string = f.read()

# write output to html
prettyHTML = HTMLBeautifier.beautify(html_string, 4)

fout = open("test.html", "w")
fout.write(prettyHTML)
fout.close()
