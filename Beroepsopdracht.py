Intro = "Hallo ik ben Ahmet Abdu"
Intro2 = "Wil je mijn Verhaal horen?"
Intro3 = "Oke stel je voor dat"
Begin = "Jij en jouw kind zijn samen thuis terwijl jij een bedreigende brief van de taliban hebt ontvangen."
Begin2 = "Je zegt meteen dat jullie moeten vluchten zonder je vrouw en andere kinderen."
Begin3 = "Het enige wat jouw kind nog mee kan nemen is een van jouw kind's favoriete knuffels."
Tekst1 = "je  besluit eerst met Je eigen auto/op de voet te vertrekken"
Tekst2 = "Het is druk op straat ga je naar de meest drukke kant of de minst drukke kant."
Tekst3 = "Jullie stappen snel de auto in maar dan moet je snel beslissen waar je naartoe gaat ga je richting de bergen of richting de steden."
Tekst4 = "Jullie lopen richting de menigde en horen dat ze ook willen vluchten door een dreigbrief die zij hebben ontvangen Helaas gaan zij een ander kant op dan jij snel had gepland jullie lopen verder richting de bergen verderop."
Tekst5 = "Jullie lopen naar de kleine groep mensen op straat sommige van hun hebben ook een dreigbrief ontvangen en willen ook zo snel mogelijk weg."
Tekst5n2 = "ga je met ze mee of blijven jullie met z'n tweeen door reizen?"
Tekst6 = "Julie rijden nu richting de grote stad maar onderweg kom je erachter dat je je beter laag kan houden en niet naar te drukke plekken moet gaan dus je keert om terug naar de bergen."
Tekst7 = "Bij de bergen aangekomen moeten je beslissen of je om de bergen heen gaat reiden of over de berg op de voet"
Tekst8 = "Bij de bergen aangekomen moet je kiezen of je er omheen gaat lopen of over de bergen heen gaat."
Tekst9 = "Je besluit met de groep mee te gaan en je volgt ze richting de bergen."
Tekst9n2 = "Bij de bergen aangekomen moeten jullie als groep kiezen of jullie over de bergen gaan of om de bergen heen jullie keizen om over de bergen te gaan."
Tekst10 = "In de bergen worden jullie staande gehouden door een stel mensen van de taliban ze herkennen sommige van jullie van de dreigbriefen en jullie worden opgepakt en meegenomen."
end =0
vn = 0
while end == 1:
    print("Je ben opgepakt en meegenomen door de taliban jouw en jouw kinds lot worden in hun handen gelegd.")
while vn == 0:
    print(Intro)
    print(Intro2)
    ant = input()
    if ant == "ja":
        print(Intro3)
        print(Begin)
        print(Begin2)
        print(Begin3)
        vn = 1
    elif ant == "nee":
        print("Jammer hoor.")
        break
while vn == 1:
    print(Tekst1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    print("A. Met de auto")
    print("B. Op de voet")
    ant = input()
    if ant == "A":
        vn = 3
    elif ant == "B":
        vn = 2
while vn == 2:
    print(Tekst2)
    print("A. Meest drukke kant")
    print("B. Minst drukke kant")
    ant = input()
    if ant == "A":
        vn = 4
    elif ant == "B":
        vn = 5
while vn == 3:
    print(Tekst3)
    print("A. De stad")
    print("B. De bergen")
    ant = input()
    if ant == "A":
        vn = 6
    elif ant == "B":
        vn = 7
while vn == 4:
    print(Tekst4)
    vn = 8
while vn == 5:
    print(Tekst5)
    print(Tekst5n2)
    print("A. Ga mee")
    print("B. Ga niet mee")
    ant = input()
    if ant == "A":
        vn = 9
    elif ant == "B":
        vn = 8   
while vn == 6:
    print(Tekst6)
    vn = 7
while vn == 7:
    print(Tekst7)
    print("A. Om de bergen heen reiden")
    print("B. Over de bergen lopen")
    ant = input()
    if ant == "A":
        vn = 10
    elif ant == "B":
        vn = 11
while vn == 8:
    print(Tekst8)
    print("A. Om de bergen heen lopen")
    print("B. Over de bergen lopen")
    ant = input()
    if ant == "A":
        vn = 12
    elif ant == "B":
        vn = 13
while vn == 9:
    print(Tekst9)
    print(Tekst9n2)
    print("B. Over de bergen lopen")
    ant = input()
    if ant == "A":
        vn = 14
    elif ant == "B":
        vn = 15
while vn == 10:
    print(Tekst10)
    end = 1