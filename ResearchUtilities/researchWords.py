import random

rounded_short = [
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
    ["pusu", "supu"]
]

rounded_long = [
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
mixed_rounded = [
    ########## Short ##########
    ['babi', 'giga'],
    ['gagi', 'muma'],
    ['babo', 'nubu'],
    ['gago', 'mumi'],
    ['lalo', 'gubu'],
    ['babu', 'biba'],
    ['dadu', 'suso'],
    ['gagu', 'sunu'],
    ['lalu', 'sosi'],
    ['mamu', 'dubu'],
    ['nanu', 'laba'],
    ['sasu', 'dudo'],
    ['bibo', 'mobo'],
    ['gigo', 'lada'],
    ['siso', 'nolo'],
    ['gigu', 'lulo'],
    ['lilu', 'pubu'],
    ['mimu', 'ludu'],
    ['ninu', 'nulu'],
    ['dodu', 'saba'],
    ['gogu', 'bobi'],
    ['lolu', 'gugo'],
    ['nonu', 'goga'],
    ['popu', 'dobo'],
    ['sosu', 'pobo'],
    ['bodo', 'sulu'],
    ['budu', 'podo'],
    ['bugu', 'buba'],
    ['bala', 'paba'],
    ['bulu', 'nili'],
    ['bimi', 'nodo'],
    ['bomo', 'luli'],
    ['bumu', 'gugi'],
    ['bini', 'mubu'],
    ['bunu', 'nudu'],
    ['bapa', 'lula'],
    ['bopo', 'lugu'],
    ['bupu', 'nuno'],
    ['basa', 'lola'],
    ['boso', 'pudu'],
    ['busu', 'duda'],
    ['dala', 'mudu'],
    ['dili', 'mogo'],
    ['dolo', 'nogo'],
    ['dulu', 'sada'],
    ['dumu', 'nibi'],
    ['dono', 'pono'],
    ['dunu', 'subu'],
    ['dopo', 'mulu'],
    ['dupu', 'sono'],
    ['dasa', 'susa'],
    ['dusu', 'pomo'],
    ['gulu', 'boba'],
    ['gimi', 'lidi'],
    ['gomo', 'mibi'],
    ['gumu', 'pumu'],
    ['gono', 'sudu'],
    ['gunu', 'migi'],
    ['gapa', 'molo'],
    ['gupu', 'sobo'],
    ['goso', 'lubu'],
    ['gusu', 'punu'],
    ['lomo', 'guga'],
    ['lumu', 'sapa'],
    ['lini', 'numu'],
    ['lono', 'gogi'],
    ['lunu', 'sala'],
    ['lupu', 'sumu'],
    ['lasa', 'mugu'],
    ['lusu', 'nugu'],
    ['munu', 'pimi'],
    ['mipi', 'pulu'],
    ['mopo', 'sopo'],
    ['mupu', 'sugu'],
    ['moso', 'paga'],
    ['musu', 'nuni'],
    ['nopo', 'lodo'],
    ['nupu', 'pugu'],
    ['noso', 'supu'],
    ['nusu', 'somo'],
    ['pasa', 'nuna'],
    ['poso', 'sogo'],
    ['pusu', 'pupo'],

    ########## Long ##########
    ['maluma', 'baluma'],
    ['manuma', 'nadegi'],
    ['mabuma', 'baduta'],
    ['masuma', 'manoma'],
    ['maduma', 'masoni'],
    ['baduba', 'damono'],
    ['baguba', 'babuta'],
    ['baluba', 'damula'],
    ['masumi', 'baluta'],
    ['masuni', 'nabegi'],
    ['masugi', 'bamuta'],
    ['masubi', 'mamubi'],
    ['masusi', 'masoma'],
    ['balota', 'bapuma'],
    ['bamota', 'maboma'],
    ['badota', 'pamomo'],
    ['babota', 'madoma'],
    ['baloma', 'lanubi'],
    ['bagoma', 'dagula'],
    ['bapoma', 'lasubi'],
    ['basoma', 'pagomo'],
    ['dabola', 'dagolo'],
    ['dadola', 'gemana'],
    ['damola', 'dapolo'],
    ['dagola', 'genana'],
    ['dapola', 'dadula'],
    ['depolo', 'baloba'],
    ['desolo', 'gapomi'],
    ['degolo', 'magudo'],
    ['demono', 'gamomi'],
    ['denono', 'galomi'],
    ['lidubi', 'nagegi'],
    ['limubi', 'napegi'],
    ['linubi', 'masosi'],
    ['lisubi', 'mapudo'],
    ['panumo', 'maludo'],
    ['pamumo', 'bagoba'],
    ['pasumo', 'masudo'],
    ['pagumo', 'gagomi'],
    ['padumo', 'pabomo'],
    ['pabumo', 'danono'],
    ['meludo', 'nasegi'],
    ['mesudo', 'gelana'],
    ['megudo', 'bagubi'],
    ['mebudo', 'mabudo'],
    ['mepudo', 'masomi'],
    ['momubi', 'babuma'],
    ['molubi', 'lamubi'],
    ['mogubi', 'badoba'],
    ['nodegi', 'gadomi'],
    ['nobegi', 'masogi'],
    ['nogegi', 'pasomo'],
    ['nopegi', 'malubi'],
    ['nosegi', 'gasomi'],
    ['gagumi', 'ganomi'],
    ['gasumi', 'gepana'],
    ['gadumi', 'maloma'],
    ['gapumi', 'padomo'],
    ['gamumi', 'gedana'],
    ['ganumi', 'panomo'],
    ['galumi', 'basuma'],
    ['gabana', 'dasolo'],
    ['gamana', 'dapula'],
    ['ganana', 'masobi'],
    ['gapana', 'gebana'],
    ['gadana', 'dabula'],
    ['galana', 'ladubi']
]

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

spiky_short = [
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
    ["vuzu", "zuvu"]
]

spiky_long = [
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

mixed_spiky = [
    ########## Short ##########
    ['kaki', 'vuku'],
    ['tati', 'zoko'],
    ['zazi', 'zozi'],
    ['kako', 'kuka'],
    ['tato', 'koka'],
    ['vavo', 'zeke'],
    ['zazo', 'tuto'],
    ['kaku', 'zuzi'],
    ['tatu', 'zuza'],
    ['vavu', 'tota'],
    ['zazu', 'koki'],
    ['kiko', 'vuvo'],
    ['tito', 'zuvu'],
    ['zizo', 'tita'],
    ['kiku', 'veke'],
    ['titu', 'viki'],
    ['vivu', 'tuti'],
    ['zizu', 'vuva'],
    ['koku', 'zoto'],
    ['totu', 'tuku'],
    ['vovu', 'zuzo'],
    ['zozu', 'tuta'],
    ['kete', 'ziti'],
    ['koto', 'zovo'],
    ['kutu', 'voko'],
    ['kava', 'zata'],
    ['keve', 'zuku'],
    ['kivi', 'vata'],
    ['kovo', 'zeve'],
    ['kuvu', 'kika'],
    ['kaza', 'kuko'],
    ['keze', 'zete'],
    ['kizi', 'toko'],
    ['kozo', 'vuvi'],
    ['kuzu', 'zava'],
    ['tava', 'vutu'],
    ['teve', 'zaka'],
    ['tovo', 'toti'],
    ['tuvu', 'ziza'],
    ['taza', 'ziki'],
    ['teze', 'vova'],
    ['tizi', 'teke'],
    ['tozo', 'zivi'],
    ['tuzu', 'zutu'],
    ['vaza', 'voto'],
    ['veze', 'vete'],
    ['vizi', 'zoza'],
    ['vozo', 'vaka'],
    ['vuzu', 'kuki'],

    ########## Long ##########
    ['keteke', 'takete'],
    ['kekeke', 'kakito'],
    ['keveke', 'tivako'],
    ['kezeke', 'tikako'],
    ['tekete', 'tatia'],
    ['tevete', 'tavete'],
    ['tezete', 'kekio'],
    ['kikivu', 'titako'],
    ['kikavu', 'tazete'],
    ['zizazo', 'zizavu'],
    ['zizavo', 'kikivo'],
    ['zizako', 'keziti'],
    ['zizato', 'zizatu'],
    ['tazea', 'tezaza'],
    ['tatea', 'kakivo'],
    ['tavea', 'zavazo'],
    ['takea', 'viko'],
    ['titaku', 'kakeke'],
    ['tikaku', 'akito'],
    ['tivaku', 'tevaza'],
    ['tizaku', 'kazeke'],
    ['kikaku', 'zizazu'],
    ['kikazu', 'kikazo'],
    ['kikatu', 'kikiko'],
    ['kakivu', 'kavazi'],
    ['kakitu', 'kakizo'],
    ['kakizu', 'kaveke'],
    ['kakiku', 'keviti'],
    ['akiku', 'tekaza'],
    ['akitu', 'taviki'],
    ['akizu', 'akizo'],
    ['akivu', 'kekiti'],
    ['zavazu', 'kateke'],
    ['zazazu', 'vekiki'],
    ['zatazu', 'tavia'],
    ['zakazu', 'tezazi'],
    ['vizu', 'vizo'],
    ['viku', 'zakazo'],
    ['kakio', 'kezio'],
    ['kazio', 'tizako'],
    ['kikibu', 'zizaku'],
    ['kikizu', 'kazazi'],
    ['kikitu', 'akiko'],
    ['kikiku', 'kikizo'],
    ['tivaki', 'zatazo'],
    ['tizaki', 'kikibo'],
    ['tikazi', 'zazazo'],
    ['kitazi', 'kakiko'],
    ['kivazi', 'kikako'],
    ['kizazi', 'tazia'],
    ['terazi', 'tarazi'],
    ['tevazi', 'veviki'],
    ['kaziti', 'kikato'],
    ['kaviti', 'tetaza'],
    ['kakiti', 'takia'],
    ['tikaza', 'takazi'],
    ['tivaza', 'kikavo'],
    ['titaza', 'akivo'],
    ['tizaza', 'vetiki'],
    ['vitiki', 'veziki'],
    ['viviki', 'tazaki'],
    ['vikiki', 'katazi'],
    ['viziki', 'kikito']
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

# Prints the given wordList
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

# Returns the given wordList
def getWordList(wordList):
    if wordList == "spiky":
        return spiky
    elif wordList == "mixed_spiky":
        return mixed_spiky
    elif wordList == "rounded":
        return rounded
    elif wordList == "mixed_rounded":
        return mixed_rounded
    else:
        print("Invalid parameter passed to getWordList")

# Randomizes the word pairs in the given list
def randomizeList(wordList):
    rand_indices = list(range(0, len(wordList)))
    random.shuffle(rand_indices)

    for i in range(0, len(wordList)):
        temp = wordList[rand_indices[i]][1]
        wordList[rand_indices[i]][1] = wordList[i][1]
        wordList[i][1] = temp

    return(wordList)