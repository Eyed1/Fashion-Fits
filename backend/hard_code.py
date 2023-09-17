def find_match_pair(c1, c2):

    #DOUBLE (NO JACKET)
    #idk names of these variables yet or how they coded
    isFormal=False
    colorsMatch=False
    matchWeather=True

    isMulticolor=[False,False]

    p=[c1,c2]

    hsl=[rgb_to_hsl(p[0][3],p[0][4],p[0][5]),rgb_to_hsl(p[1][3],p[1][4],p[1][5])]

    if isMulticolor[0]:
        if isNeutral(hsl[1]) and (not isMulticolor[1]):
            colorsMatch=True
    elif isMulticolor[1]:
        if isNeutral(hsl[0]) and (not isMulticolor[0]):
            colorsMatch=True
    elif (not isMulticolor[0]) and (not isMulticolor[1]):
        complementaryShades=False
        analogousMatching=False
        triadicColor=False
        goodNeutral=False

        hueD1=hueDist(hsl[0][0],hsl[1][0])
        satD1=satDist(hsl[0][1],hsl[1][1])
        lightD1=lightDist(hsl[0][2],hsl[1][2])

        notClose1=(hueD1+0.6*satD1+0.6*lightD1>=42)

        if hueD1>=160:
            complementaryShades=True
        if notClose1 and hueD1<=60:
            analogousMatching=True
        if notClose1 and (isNeutral(hsl[0]) or isNeutral(hsl[1])):
            goodNeutral=True

        if complementaryShades or analogousMatching or triadicColor or goodNeutral:
            colorsMatch=True
    
    if colorsMatch and matchWeather:
        if isFormal:
            if p[0]=='formal shirt' and p[1]=='formal pant':
                return True
        else:
            return True
    return False

def find_match_triple(c1, c2, c3):
    #TRIPLE (JACKET)
    #idk names of these variables yet or how they coded
    isFormal=False
    colorsMatch=False
    matchWeather=True
    
    isMulticolor=[False,False,False]

    c=[c1, c2, c3]
    hsl=[rgb_to_hsl(c[0][3],c[0][4],c[0][5]),rgb_to_hsl(c[1][3],c[1][4],c[1][5]),rgb_to_hsl(c[2][3],c[2][4],c[2][5])]

    if isMulticolor[0]:
        if isNeutral(hsl[1]) and isNeutral(hsl[2]) and (not isMulticolor[1]) and (not isMulticolor[2]):
            colorsMatch=True
    elif isMulticolor[1]:
        if isNeutral(hsl[0]) and isNeutral(hsl[2]) and (not isMulticolor[0]) and (not isMulticolor[2]):
            colorsMatch=True
    elif isMulticolor[2]:
        if isNeutral(hsl[0]) and isNeutral(hsl[1]) and (not isMulticolor[0]) and (not isMulticolor[1]):
            colorsMatch=True
    elif (not isMulticolor[0]) and (not isMulticolor[1]) and (not isMulticolor[2]):
        complementaryShades=False
        analogousMatching=False
        triadicColor=False
        goodNeutral=False

        hueD1=hueDist(hsl[0][0],hsl[1][0])
        hueD2=hueDist(hsl[0][0],hsl[2][0])
        hueD3=hueDist(hsl[1][0],hsl[2][0])
        satD1=hueDist(hsl[0][1],hsl[1][1])
        satD2=hueDist(hsl[0][1],hsl[2][1])
        satD3=hueDist(hsl[1][1],hsl[2][1])
        lightD1=hueDist(hsl[0][2],hsl[1][2])
        lightD2=hueDist(hsl[0][2],hsl[2][2])
        lightD3=hueDist(hsl[1][2],hsl[2][2])

        notClose1=(hueD1+0.6*satD1+0.6*lightD1>=42)
        notClose2=(hueD2+0.6*satD2+0.6*lightD2>=42)
        notClose3=(hueD3+0.6*satD3+0.6*lightD3>=42)

        if ((hueD2<=42 or hueD3<=42) and hueD1>=160) or ((hueD3<=42 or hueD1<=42) and hueD2>=160) or ((hueD1<=42 or hueD2<=42) and hueD3>=160):
            complementaryShades=True
        if (hueD1<=60 and hueD2<=60 and hueD3<=60) and (notClose1 or notClose2 or notClose3):
            analogousMatching=True
        if (hueD1>=120-25 and hueD1<=120+25) and (hueD2>=120-25 and hueD2<=120+25) and (hueD3>=120-25 and hueD3<=120+25):
            triadicColor=True
        if (notClose1 or notClose2 or notClose3) and ((isNeutral(hsl[0]) and isNeutral(hsl[1])) or (isNeutral(hsl[0]) and isNeutral(hsl[1])) or (isNeutral(hsl[0]) and isNeutral(hsl[1]))):
            goodNeutral=True
        if complementaryShades or analogousMatching or triadicColor or goodNeutral:
            colorsMatch=True

    if colorsMatch and matchWeather:
        if isFormal:
            if c[0]=='formal shirt' and c[2]=='formal pant':
                return True
        else:
            return True

    return False

def hueDist(h1, h2):
    return min(abs(h2-h1),abs(360+h2-h1),abs(360+h1-h2))

def satDist(s1,s2):
    return abs(s2-s1)

def lightDist(l1,l2):
    return abs(l2-l1)

def isNeutral(hsl):
    if hsl[1]<=50 or hsl[2]<=25:
        return True
    else:
        return False


def rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    max_color = max(r, g, b)
    min_color = min(r, g, b)
    
    # Calculate lightness
    l = (max_color + min_color) / 2.0
    
    if max_color == min_color:
        h = s = 0
    else:
        # Calculate saturation
        if l < 0.5:
            s = (max_color - min_color) / (max_color + min_color)
        else:
            s = (max_color - min_color) / (2.0 - max_color - min_color)
        
        # Calculate hue
        delta = max_color - min_color
        if max_color == r:
            h = (g - b) / delta + (6 if g < b else 0)
        elif max_color == g:
            h = (b - r) / delta + 2
        else:
            h = (r - g) / delta + 4
        
        h = h * 60
        
    return [round(h), round(s * 100), round(l * 100)]
