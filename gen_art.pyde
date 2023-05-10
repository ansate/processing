import csv

csvfile =  open('/Users/msantos/Documents/Processing/sketch_230509b/data/librarything_ansate-2.csv')
csvreader = csv.DictReader(csvfile)

border = 10
xstep = 2
ystep = border

#brewer.pal(7, 'Dark2')
#"#1B9E77" "#D95F02" "#7570B3" "#E7298A" "#66A61E" "#E6AB02" "#A6761D"
colorMap = dict()
colorMap["fantasy"] ="0x1B9E77"
colorMap["scifi"]= "0xD95F02"
colorMap["memoir"]= "0x7570B3"
colorMap["romance"]= "0xE7298A"
colorMap["historical"]= "0x66A61E"
colorMap["mystery"]= "0xE6AB02"
colorMap["ya"]= "0xA6761D"

def setup():
    background("0xFFFFFF")
    size(800, 600)

def draw():
    lastx = 0
    lasty = 0 
    #line(30, 20, 85, 20)
    j = 0
    for row in csvreader:
        j = j+1
        i = ystep/2 + j*ystep
        #print(row)
        rating = row["Rating"]
            
        tagsString = row["Tags"]
        tags = tagsString.split(",")
        tags = [trim(x) for x in tags]
        #print(tags)
        ebook = "ebook" in tags
        genre = tags[-1]
        
        pages = row["Page Count"]

        if pages.isdigit():
            pages = int(pages)
        else:
            pages = random(300,500)
        
        mycolor = "0x000000"
        if genre in colorMap.keys():
            #print("Getcolor")
            mycolor = colorMap[genre]

        x = border
        while(x < (pages - border)):
            y = noise(random(border, border+ystep))
            if ebook:
                y = noise(random(border, border+ystep))*15 

            if (x == border):
                #print("here")
                lastx = 0
            if (lastx > 0):
                #print("there")
                stroke(mycolor)
                #stroke("0x00FF9F")
                #print(int(rating))
                strokeWeight(int(rating) + 1)
                line(x, y+i, lastx, lasty+i)
            
            #print("end")
            x = x + xstep
            lastx = x
            lasty = y
            #print(lastx)

    
