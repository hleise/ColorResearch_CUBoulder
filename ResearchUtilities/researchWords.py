def main():
    rounded = [
        ########## CVCV ##########
        # Varying Vowel (a & i)
        ["babi", "biba"],
        ["gagi", "giga"],
        # Varying Vowel (a & o)
        ["babo", "boba"],
        ["gago", "goga"],
        ["lalo", "lola"],
        # Varying Vowel (a & u)
        ["babu", "buba"],
        ["dadu", "duda"],
        ["gagu", "guga"],
        ["lalu", "lula"],
        ["mamu", "muma"],
        ["nanu", "nuna"],
        ["sasu", "susa"],
        # Varying Vowel (i & o)
        ["bibo", "bobi"],
        ["gigo", "gogi"],
        ["siso", "sosi"],
        # Varying Vowel (i & u)
        ["gigu", "gugi"],
        ["lilu", "luli"],
        ["mimu", "mumi"],
        ["ninu", "nuni"],
        # Varying Vowel (o & u)
        ["dodu", "dudo"],
        ["gogu", "gugo"],
        ["lolu", "lulo"],
        ["nonu", "nuno"],
        ["popu", "pupo"],
        ["sosu", "suso"],

        # Varying Consonant (b & d)
        ["bodo", "dobo"],
        ["budu", "dubu"],
        # Varying Consonant (b & g)
        ["bugu", "gubu"],
        # Varying Consonant (b & l)
        ["bala", "laba"],
        ["bulu", "lubu"],
        # Varying Consonant (b & m)
        ["bimi", "mibi"],
        ["bomo", "mobo"],
        ["bumu", "mubu"],
        # Varying Consonant (b & n)
        ["bini", "nibi"],
        ["bunu", "nubu"],
        # Varying Consonant (b & p)
        ["bapa", "paba"],
        ["bopo", "pobo"],
        ["bupu", "pubu"],
        # Varying Consonant (b & s)
        ["basa", "saba"],
        ["boso", "sobo"],
        ["busu", "subu"],
        # Varying Consonant (d & l)
        ["dala", "lada"],
        ["dili", "lidi"],
        ["dolo", "lodo"],
        ["dulu", "ludu"],
        # Varying Consonant (d & m)
        ["dumu", "mudu"],
        # Varying Consonant (d & n)
        ["dono", "nodo"],
        ["dunu", "nudu"],
        # Varying Consonant (d & p)
        ["dopo", "podo"],
        ["dupu", "pudu"],
        # Varying Consonant (d & s)
        ["dasa", "sada"],
        ["dusu", "sudu"],
        # Varying Consonant (g & l)
        ["gulu", "lugu"],
        # Varying Consonant (g & m)
        ["gimi", "migi"],
        ["gomo", "mogo"],
        ["gumu", "mugu"],
        # Varying Consonant (g & n)
        ["gono", "nogo"],
        ["gunu", "nugu"],
        # Varying Consonant (g & p)
        ["gapa", "paga"],
        ["gupu", "pugu"],
        # Varying Consonant (g & s)
        ["goso", "sogo"],
        ["gusu", "sugu"],
        # Varying Consonant (l & m)
        ["lomo", "molo"],
        ["lumu", "mulu"],
        # Varying Consonant (l & n)
        ["lini", "nili"],
        ["lono", "nolo"],
        ["lunu", "nulu"],
        # Varying Consonant (l & p)
        ["lupu", "pulu"],
        # Varying Consonant (l & s)
        ["lasa", "sala"],
        ["lusu", "sulu"],
        # Varying Consonant (m & n)
        ["munu", "numu"],
        # Varying Consonant (m & p)
        ["mipi", "pimi"],
        ["mopo", "pomo"],
        ["mupu", "pumu"],
        # Varying Consonant (m & s)
        ["moso", "somo"],
        ["musu", "sumu"],
        # Varying Consonant (n & p)
        ["nopo", "pono"],
        ["nupu", "punu"],
        # Varying Consonant (n & s)
        ["noso", "sono"],
        ["nusu", "sunu"],
        # Varying Consonant (p & s)
        ["pasa", "sapa"],
        ["poso", "sopo"],
        ["pusu", "supu"],

        ########## Other ##########
        # ma_uma & ma_oma
        ["maluma", "maloma"],
        ["manuma", "manoma"],
        ["mabuma", "maboma"],
        ["masuma", "masoma"],
        ["maduma", "madoma"],
        # ba_uba & ba_oba
        ["baduba", "badoba"],
        ["baguba", "bagoba"],
        ["baluba", "baloba"],
        # masu_i & maso_i
        ["masumi", "masomi"],
        ["masuni", "masoni"],
        ["masugi", "masogi"],
        ["masubi", "masobi"],
        ["masusi", "masosi"],
        # ba_ota & ba_uta
        ["balota", "baluta"],
        ["bamota", "bamuta"],
        ["badota", "baduta"],
        ["babota", "babuta"],
        # ba_oma & ba_uma
        ["baloma", "baluma"],
        ["bagoma", "babuma"],
        ["bapoma", "bapuma"],
        ["basoma", "basuma"],
        # da_ola & da_ula
        ["dabola", "dabula"],
        ["dadola", "dadula"],
        ["damola", "damula"],
        ["dagola", "dagula"],
        ["dapola", "dapula"],
        # de_olo & da_olo
        ["depolo", "dapolo"],
        ["desolo", "dasolo"],
        ["degolo", "dagolo"],
        ["demono", "damono"],
        ["denono", "danono"],
        # li_ubi & la_ubi
        ["lidubi", "ladubi"],
        ["limubi", "lamubi"],
        ["linubi", "lanubi"],
        ["lisubi", "lasubi"],
        # pa_umo & pa_omo
        ["panumo", "panomo"],
        ["pamumo", "pamomo"],
        ["pasumo", "pasomo"],
        ["pagumo", "pagomo"],
        ["padumo", "padomo"],
        ["pabumo", "pabomo"],
        #  me_udo & ma_udo
        ["meludo", "maludo"],
        ["mesudo", "masudo"],
        ["megudo", "magudo"],
        ["mebudo", "mabudo"],
        ["mepudo", "mapudo"],
        # mo_ubi & ma_ubi
        ["momubi", "mamubi"],
        ["molubi", "malubi"],
        ["mogubi", "bagubi"],
        # no_egi & na_egi
        ["nodegi", "nadegi"],
        ["nobegi", "nabegi"],
        ["nogegi", "nagegi"],
        ["nopegi", "napegi"],
        ["nosegi", "nasegi"],
        # ga_umi & ga_omi
        ["gagumi", "gagomi"],
        ["gasumi", "gasomi"],
        ["gadumi", "gadomi"],
        ["gapumi", "gapomi"],
        ["gamumi", "gamomi"],
        ["ganumi", "ganomi"],
        ["galumi", "galomi"],
        # ga_ana & ge_ana
        ["gabana", "gebana"],
        ["gamana", "gemana"],
        ["ganana", "genana"],
        ["gapana", "gepana"],
        ["gadana", "gedana"],
        ["galana", "gelana"]
    ]

    spiky = [
        ########## CVCV ##########
        # Varying Vowel (a & i)
        ["kaki", "kika"],
        ["tati", "tita"],
        ["zazi", "ziza"],
        # Varying Vowel (a & o)
        ["kako", "koka"],
        ["tato", "tota"],
        ["vavo", "vova"],
        ["zazo", "zoza"],
        # Varying Vowel (a & u)
        ["kaku", "kuka"],
        ["tatu", "tuta"],
        ["vavu", "vuva"],
        ["zazu", "zuza"],
        # Varying Vowel (i & o)
        ["kiko", "koki"],
        ["tito", "toti"],
        ["zizo", "zozi"],
        # Varying Vowel (i & u)
        ["kiku", "kuki"],
        ["titu", "tuti"],
        ["vivu", "vuvi"],
        ["zizu", "zuzi"],
        # Varying Vowel (o & u)
        ["koku", "kuko"],
        ["totu", "tuto"],
        ["vovu", "vuvo"],
        ["zozu", "zuzo"],

        # Varying Consonant (k & t)
        ["kete", "teke"],
        ["koto", "toko"],
        ["kutu", "tuku"],
        # Varying Consonant (k & v)
        ["kava", "vaka"],
        ["keve", "veke"],
        ["kivi", "viki"],
        ["kovo", "voko"],
        ["kuvu", "vuku"],
        # Varying Consonant (k & z)
        ["kaza", "zaka"],
        ["keze", "zeke"],
        ["kizi", "ziki"],
        ["kozo", "zoko"],
        ["kuzu", "zuku"],
        # Varying Consonant (t & v)
        ["tava", "vata"],
        ["teve", "vete"],
        ["tovo", "voto"],
        ["tuvu", "vutu"],
        # Varying Consonant (t & z)
        ["taza", "zata"],
        ["teze", "zete"],
        ["tizi", "ziti"],
        ["tozo", "zoto"],
        ["tuzu", "zutu"],
        # Varying Consonant (v & z)
        ["vaza", "zava"],
        ["veze", "zeve"],
        ["vizi", "zivi"],
        ["vozo", "zovo"],
        ["vuzu", "zuvu"],

        ########## Other ##########
        # ke_eke & ka_eke
        ["keteke", "kateke"],
        ["kekeke", "kakeke"],
        ["keveke", "kaveke"],
        ["kezeke", "kazeke"],
        # te_ete & ta_ete
        ["tekete", "takete"],
        ["tevete", "tavete"],
        ["tezete", "tazete"],
        # kik_vu & kik_vo
        ["kikivu", "kikivo"],
        ["kikavu", "kikavo"],
        # ziza_o & ziza_u
        ["zizazo", "zizazu"],
        ["zizavo", "zizavu"],
        ["zizako", "zizaku"],
        ["zizato", "zizatu"],
        # ta_ea & ta_ia
        ["tazea", "tazia"],
        ["tatea", "tatia"],
        ["tavea", "tavia"],
        ["takea", "takia"],
        # ti_aku & ti_ako
        ["titaku", "titako"],
        ["tikaku", "tikako"],
        ["tivaku", "tivako"],
        ["tizaku", "tizako"],
        # kika_u & kika_o
        ["kikaku", "kikako"],
        ["kikazu", "kikazo"],
        ["kikatu", "kikato"],
        # kaki_u & kaki_o
        ["kakivu", "kakivo"],
        ["kakitu", "kakito"],
        ["kakizu", "kakizo"],
        ["kakiku", "kakiko"],
        # aki_u & aki_o
        ["akiku", "akiko"],
        ["akitu", "akito"],
        ["akizu", "akizo"],
        ["akivu", "akivo"],
        # za_azu & za_azo
        ["zavazu", "zavazo"],
        ["zazazu", "zazazo"],
        ["zatazu", "zatazo"],
        ["zakazu", "zakazo"],
        # vi_u & vi_o
        ["vizu", "vizo"],
        ["viku", "viko"],
        # ka_io & ke_io
        ["kakio", "kekio"],
        ["kazio", "kezio"],
        # kiki_u & kiki_o
        ["kikibu", "kikibo"],
        ["kikizu", "kikizo"],
        ["kikitu", "kikito"],
        ["kikiku", "kikiko"],
        # ti_aki & ta_aki
        ["tivaki", "taviki"],
        ["tizaki", "tazaki"],
        ["tikazi", "takazi"],
        # ki_azi & ka_azi
        ["kitazi", "katazi"],
        ["kivazi", "kavazi"],
        ["kizazi", "kazazi"],
        # te_azi & te_azi
        ["terazi", "tarazi"],
        ["tevazi", "tezazi"],
        # ka_iti & ke_iti
        ["kaziti", "keziti"],
        ["kaviti", "keviti"],
        ["kakiti", "kekiti"],
        # ti_kaza
        ["tikaza", "tekaza"],
        ["tivaza", "tevaza"],
        ["titaza", "tetaza"],
        ["tizaza", "tezaza"],
        # vi_iki & ve_iki
        ["vitiki", "vetiki"],
        ["viviki", "veviki"],
        ["vikiki", "vekiki"],
        ["viziki", "veziki"]
    ]

    print(getWordList(spiky))

# Prints an array of repeated words if any exist
def printRepeats(wordList):
    wordList2 = []
    repeatList = []

    for wordPair in wordList:
        for word in wordPair:
            if word in wordList2:
                repeatList.append(word)
            wordList2.append(word)

    if len(repeatList):
        print(repeatList)
    else:
        print("No repeats")

def printList(wordList):
    for wordPair in wordList:
        for word in wordPair:
            print(word)

# Prints the number of words in the list
def numWords(wordList):
    numWords = 0
    for wordPair in wordList:
        numWords += 1
    print("%s words in list" %(numWords))

def getWordList(wordList):
    return wordList

main()