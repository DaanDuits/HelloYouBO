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
Tekst10 = "Jullie besluiten om de bergen te reiden, na een lange reis van een ongeveer dag komen jullie aan bij de grens."
Tekst11 = "Jullie besluiten om over de bergen te lopen na een lange reis van ongeveer een paar dagen komen jullie bij de grens aan"
Tekst12 = "Jullie besluiten om om de bergen heen te lopen na een lange reis van ongeveer een paar dagen komen jullie bij de grens aan"
Tekst13 = "In de bergen worden jullie staande gehouden door een stel soldaten van de taliban ze herkennen sommige van jullie van de dreigbriefen en jullie worden opgepakt en meegenomen."
Tekst14 = "Bij de grens zien jullie 2 mensen bij een auto staan, mischien kun je met hun mee? Maar jullie kunnen ook zelf de grens over vluchten op de voet."
Tekst15 = "Jullie besluiten door te reiden over de grens en richting europa te reiden. Maar welk land?"
Tekst16 = "Jullie besluiten de grens over telopen totdat jullie geschreeuw achter jullie horen het zij een paar soldaten van de taliban en ze weten precies wat jullie proberen."
Tekst17 = "Jullie lopen richting de mensen en begint met hun te praten ze helpen mensen de grens over. Je voeld je blij je ben gevlugd maar waar ga je nu naartoe?"
Tekst18 = "In Nederland aangekomen worden jullie naar een vluchtelingen asiel gestuurd na een paar maanden zijn jullie vrij in Nederland."
Tekst19 = "In Griekeland aangekomen worden jullie naar een vluchtelingen asiel gestuurd maar naar een paar weken worden jullie terug gestuurd."
Tekst20 = "In de toekomst wil jij ook jouw vrouw en andere kinderen naar Nederkland krijgen maar dat gaat nog wel een paar jaar duren."

end =0
vn = 0
v = 0
while end == 1:
    print("Je ben opgepakt en meegenomen door de taliban jouw en jouw kind's lot worden in hun handen gelegd.")
    v = 1
while end == 2:
    print("Bij de grens wordt je neergeschoten door de soldaten van de taliban en jouw kind word meegenomen.")
    v = 1
while end == 3:
    print("Je bent terug gestuurd naar Afghanistan waar je nu in de gaten word gehouden door de taliban")
    v = 1
while end == 4:
    print("Je bent gevlucht en vrij in Nederland wat je wilt wat er in de toekomst gaat gebeuren gaat nog even duren maar het komt vas goed.")
    v = 1
while v == 1:
    print("Wil je mijn verhaal nog een keer volgen? Y/N")
    ant = input()
    if ant == "Y":
        end =0
        vn = 0
        v = 0
    if ant == "N":
        break
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
        vn = 11
while vn == 9:
    print(Tekst9)
    print(Tekst9n2)
    vn = 13
while vn == 10:
    print(Tekst10)
    vn = 15
while vn == 11:
    print(Tekst11)
    vn = 14
while vn == 12:
    print(Tekst12)
    vn = 14
while vn == 13:
    print(Tekst13)
    end = 1
while vn == 14:
    print(Tekst14)
    print("A. Op de voet de grens over")
    print("B. Naar de mensen met de auto toe gaan")
    ant = input()
    if ant == "A":
        vn = 16
    elif ant == "B":
        vn = 17
while vn == 15:
    print(Tekst15)
    print("A. Nederland")
    print("B. Griekeland")
    ant = input()
    if ant == "A":
        vn = 18
    elif ant == "B":
        vn = 19
while vn == 16:
    print(Tekst16)
    end = 2
while vn == 17:
    print(Tekst17)
    print("A. Nederland")
    print("B. Griekeland")
    ant = input()
    if ant == "A":
        vn = 18
    elif ant == "B":
        vn = 19
while vn == 18:
    print(Tekst18)
    vn = 20
while vn == 19:
    print(Tekst19)
    end = 3
while vn == 20:
    print(Tekst20)
    end = 4