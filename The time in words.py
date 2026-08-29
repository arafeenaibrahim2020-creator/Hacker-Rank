def timeInWords(h, m):
    words=[" ","one","two","three","four","five","six","seven","eight","nine",
        "ten","eleven","twovelve","thirteen","fourteen","fifteen","sixteen",
        "seventeen","eighteen","nineteen","twenty","twenty one","twenty two",
        "twenty three","twenty four","twenty five","twenty six","twenty seven",
        "twenty eight","twenty nine"]
    if m==0:
        return words[h]+" o' clock"
    elif m==1:
        return words[m]+ " minute past " + words[h]
    elif m==15:
        return "quarter past " + words[h]
    elif m==30:
        return "half past " + words[h]
    elif m<30:
        return words[m]+ " minutes past " + words[h]
    elif m==45:
        return "quarter to " + words[h+1]
    else:
        return words[60-m]+" minutes to " + words[h+1]
