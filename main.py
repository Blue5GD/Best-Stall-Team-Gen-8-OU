import itertools
"""
YOOOOO! What's up everyone!
Today we will be making the ultimate stall team using
PYTHON THREE.

Here's how it will work:


LETS GO

Part 1 the list setup

"""

#It looks better without comments

#S tier

tank_landorus_t = 0
sd_landorus_t = 1

#S- tier

specs_dragapult = 2 
darts_dragapult = 3
heatran = 4
weavile = 5 

#A+ tier

corviknight = 6 
tank_garchomp = 7
sweep_garchomp = 8
slowking_g = 9
whirlpool_tapu_fini = 10
cm_tapu_fini = 11
tank_tapu_fini = 12
tapu_koko = 13
other_tornadus_t = 14
np_tornadus_t = 15
toxapex = 16
urshifu_r = 17

#A tier

arctozolt = 18 
clefable = 19
ferrothorn = 20
sd_kartana = 21
other_kartana = 22
other_kyurem = 23
specs_kyurem = 24
specs_magnezone = 25
id_magnezone = 26
melmetal = 27
ninetales_alola = 28
scizor = 29
tapu_lele = 30
zeraora = 31

#A- tier

buzzwole = 32
dragonite = 33
hippowdon = 34
hydreigon = 35
rillaboom = 36
skarmory = 37
slowking = 38
volcarona = 39

#B+ tier

bisharp = 40
blacephalon = 41
blissey = 42
nidoking = 43
rotom_wash = 44
slowbro = 45
tangrowth = 46
tapu_bulu = 47
tyranitar = 48
victini = 49
zapdos = 50

#B tier

aegislash = 51
barraskewda = 52
dracozolt = 53
excadrill = 54
gastrodon = 55
hawlucha = 56
kommo_o = 57
ho_mew = 58
other_mew = 59
pelipper = 60
reuniclus = 61
swampert = 62
volcanion = 63

#B- tier

blaziken = 64
mandibuzz = 65
moltres_galar = 66
zapdos_galar = 67

#C+ tier

azumarill = 68
crawdaunt = 69
cresselia = 70
gengar = 71
glastrier = 72
grimmsnarl = 73
jirachi = 74
kingdra = 75
latias = 76
latios = 77
mamoswine = 78
band_mamoswine = 79
primarina = 80
rotom_heat = 81
suicune = 82
terrakion = 83
thundurus_t = 84
toxtricity = 85
zarude = 86

#C tier

amoonguss = 87
ditto = 88
hatterene = 89
keldeo = 90
marowak_alola = 91
porygon2 = 92
quagsire = 93
regieleki = 94
seismitoad = 95
shuckle = 96
togekiss = 97
torkoal = 98
venusaur = 99

#C-

alakazam = 100
celesteela = 101
charizard = 102
conkeldurr = 103
haxorus = 104
moltres = 105
necrozma = 106
ribombee = 107
shedinja = 108
slowbro_g = 109
uxie = 110
weezing_galar = 111
xatu = 112


list_all = [425.6, 31.05, 128.64, 85.76, 213.1, 152.8, 215.5, 116.87, 62.93, 81.5, 29.46, 36.83, 81.02, 97.6, 80.62, 26.88, 135.3, 144, 54.6, 139.5, 179.9, 43.74, 77.76, 63.24, 42.16, 23.83, 71.48, 146.7, 73.6, 70.4, 166, 88.4, 51.4, 114.2, 55.5, 37.7, 100.5, 37.6, 45.6, 85.2, 70.9, 66.1, 84.7, 32.4, 23.4, 57.6, 20.9, 14.9, 51.3, 56.7, 92, 30.4, 62.7, 13.6, 42.5, 13.2, 35.4, 16.3, 37.26, 24.84, 77.5, 12.8, 42.4, 41.4, 31.8, 41.4, 19.8, 31.6, 15.7, 34.3, 15, 19.4, 2.3, 8.9, 13.9, 13.1, 8.9, 23.1, 32, 2.4, 10, 9.3, 7.2, 9.6, 9.9, 11.4, 6.6, 7.6, 11.9, 29.8, 17.3, 20.3, 19.9, 8.6, 45.3, 26.4, 8.5, 6.7, 36.9, 22.4, 8.8, 20.5, 3.3, 10, 4.2, 8.2, 3.9, 4.4, 6.5, 3.8, 0.6, 2.8, 5.6]

#Part 2
#The functions
#SECTION 1     
def no0 ():
    global list_all
    for i, name in enumerate (list_all):
        if name < 0:
            list_all[i] = 0


def stall_blissey ():
    global list_all

    list_all[specs_dragapult] = 0        
    list_all[tank_tapu_fini] = 0
    list_all[tapu_koko] = list_all[tapu_koko]-88
    list_all[slowking_g] = 0
    list_all[other_tornadus_t]= list_all[other_tornadus_t]-60
    list_all[clefable] = list_all[clefable]-88.5
    list_all[specs_kyurem] = list_all[specs_kyurem]-20
    list_all[other_kyurem] = list_all[other_kyurem]-60
    list_all[ninetales_alola] = 0
    list_all[hydreigon] = list_all[hydreigon]-36
    list_all[slowking] = 0
    list_all[volcarona] = list_all[volcarona]-78
    list_all[blacephalon] = list_all[blacephalon]-54
    list_all[blissey] = list_all[blissey]-57
    list_all[nidoking] = list_all[nidoking]-31
    list_all[rotom_wash] = 0
    list_all[zapdos] = 0
    list_all[aegislash] = list_all[aegislash]-13
    list_all[gastrodon] = 0
    list_all[ho_mew] = list_all[ho_mew]-5
    list_all[pelipper] = 0
    list_all[volcanion] = list_all[volcanion]-27
    list_all[moltres_galar] =  list_all[moltres_galar]-15
    list_all[cresselia] = list_all[cresselia]-12
    list_all[latias] = 0
    list_all[latios] = list_all[latios]-16
    list_all[primarina] = 0
    list_all[rotom_heat] = 0 
    list_all[toxtricity] = list_all[toxtricity]-4
    list_all[togekiss] = 0
    list_all[amoonguss] = 0
    list_all[quagsire] = 0
    list_all[porygon2] = 0
    list_all[venusaur] = list_all[venusaur]-11
    list_all[celesteela] = list_all[celesteela]-18 
    list_all[charizard] = 0
    list_all[moltres] = 0
    list_all[shedinja] = 0
    list_all[xatu] = list_all[xatu]-5
    list_all[slowbro_g] = slowbro_g-1
    list_all[ribombee]=0

    no0()

def stall_clefable (): 
    global list_all

    list_all[sd_landorus_t] = list_all[sd_landorus_t]-10
    list_all[darts_dragapult] = 0
    list_all[weavile] =  list_all[weavile]-100
    list_all[sweep_garchomp] = 0
    list_all[corviknight] = list_all[corviknight]-35
    list_all[cm_tapu_fini] = list_all[cm_tapu_fini]-14
    list_all[clefable] = list_all[clefable]-55
    list_all[other_kyurem] = list_all[other_kyurem]-8
    list_all[id_magnezone] = list_all[id_magnezone]-30
    list_all[zeraora] = list_all[zeraora]-60
    list_all[dragonite] = list_all[dragonite]-105
    list_all[buzzwole] = 0
    list_all[hydreigon] = list_all[hydreigon]-28
    list_all[rillaboom] = list_all[rillaboom]-50
    list_all[volcarona] = list_all[volcarona]-70
    list_all[tapu_bulu] = list_all[tapu_bulu]-10
    list_all[hawlucha] = 0
    list_all[kommo_o] = 0
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[other_mew] = list_all[other_mew]-11
    list_all[reuniclus] = 0
    list_all[blaziken] = list_all[blaziken]-20
    list_all[moltres_galar] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-20
    list_all[azumarill] = list_all[azumarill]-12
    list_all[glastrier] = 0
    list_all[grimmsnarl] = 0
    list_all[latias] = 0
    list_all[latios] = list_all[latios]-20
    list_all[mamoswine] = list_all[mamoswine]-20
    list_all[primarina] = list_all[primarina]-5
    list_all[suicune] = list_all[suicune]-3.5
    list_all[thundurus_t] = list_all[thundurus_t]-3
    list_all[zarude] = list_all[zarude]-2
    list_all[hatterene] = 0
    list_all[keldeo] = list_all[keldeo]-12
    list_all[shuckle] = 0
    list_all[venusaur] = list_all[venusaur]-7
    list_all[celesteela] = list_all[celesteela]-13
    list_all[moltres] = 0
    list_all[ribombee] = 0

    no0 ()



def stall_corviknight (): 
    global list_all

    list_all[tank_landorus_t] = 0
    list_all[darts_dragapult] = 0
    list_all[corviknight] = list_all[corviknight]-161.63
    list_all[tank_garchomp] = 0
    list_all[sweep_garchomp] = list_all[sweep_garchomp]-80
    list_all[toxapex] = list_all[toxapex]-60
    list_all[clefable] = list_all[clefable]-35 
    list_all[ferrothorn] = 0
    list_all[other_kartana] = list_all[other_kartana]-67
    list_all[melmetal] = list_all[melmetal]-124.7
    list_all[scizor] = 0
    list_all[buzzwole] = 0
    list_all[dragonite] = 0
    list_all[hippowdon] = 0
    list_all[rillaboom] = 0
    list_all[skarmory] = list_all[skarmory]-28
    list_all[bisharp] = list_all[bisharp]-50
    list_all[blissey] = list_all[blissey]-65
    list_all[tangrowth] = list_all[tangrowth]-18
    list_all[tapu_bulu] = list_all[tapu_bulu]-8
    list_all[tyranitar] = list_all[tyranitar]-25
    list_all[excadrill] = 0
    list_all[hawlucha] = list_all[hawlucha]-20
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[swampert] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-15
    list_all[mandibuzz] = 0
    list_all[cresselia] = 0
    list_all[jirachi] = list_all[jirachi]-9
    list_all[mamoswine] = 0
    list_all[amoonguss] = 0
    list_all[venusaur] = list_all[venusaur]-7
    list_all[shuckle] = 0
    list_all[haxorus] = 0
    list_all[xatu] = 0

    no0()

def stall_spdef_corviknight ():
    global list_all

    list_all[tank_landorus_t] = 0
    list_all[corviknight] = list_all[corviknight]-161.63
    list_all[tank_garchomp] = 0
    list_all[other_tornadus_t] = 0
    list_all[toxapex] = list_all[toxapex]-60
    list_all[ferrothorn] = 0
    list_all[clefable] = list_all[clefable]-36
    list_all[other_kyurem] = list_all[other_kyurem]-45
    list_all[scizor] = 0
    list_all[tapu_lele] = list_all[tapu_lele]-125
    list_all[dragonite] = 0
    list_all[hippowdon] = 0
    list_all[rillaboom] = list_all[rillaboom]-75
    list_all[skarmory] = 0
    list_all[blissey] = list_all[blissey]-65
    list_all[tyranitar] = list_all[tyranitar]-12
    list_all[tangrowth] = list_all[tangrowth]-18
    list_all[aegislash] = list_all[aegislash]-22
    list_all[excadrill] = 0
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[swampert] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-10
    list_all[cresselia] = 0
    list_all[amoonguss] = 0
    list_all[porygon2] = 0
    list_all[shuckle] = 0
    list_all[venusaur] = list_all[venusaur]-7

    no0()


def stall_dragonite ():
    global list_all

    list_all[tank_landorus_t] = list_all[tank_landorus_t]-40
    list_all[heatran] = 0
    list_all[corviknight] = list_all[corviknight]-53.88
    list_all[other_tornadus_t]= list_all[other_tornadus_t]-60
    list_all[urshifu_r] = 0
    list_all[ferrothorn] = list_all[ferrothorn]-89.95
    list_all[sd_kartana] = 0
    list_all[other_kartana] = list_all[other_kartana]-65
    list_all[id_magnezone] = 0
    list_all[scizor] = list_all[scizor]-35
    list_all[zeraora] = 0
    list_all[rillaboom] = list_all[rillaboom]-60
    list_all[hippowdon] = list_all[hippowdon]-20
    list_all[skarmory] = list_all[skarmory]-13
    list_all[bisharp] = list_all[bisharp]-30
    list_all[victini] = list_all[victini]-48
    list_all[barraskewda] = list_all[barraskewda]-20
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[swampert] = list_all[swampert]-16
    list_all[volcanion] = 0
    list_all[blaziken] = 0
    list_all[thundurus_t] = list_all[thundurus_t]-4
    list_all[marowak_alola] = list_all[marowak_alola]-9
    list_all[seismitoad] = 0
    list_all[torkoal] = 0
    list_all[venusaur] = 0
    list_all[slowbro_g] = 0

    no0()

def stall_garchomp ():
    global list_all

    list_all[heatran] = list_all[heatran]-190
    list_all[zeraora] = 0
    list_all[specs_magnezone] = list_all[specs_magnezone]-15
    list_all[bisharp] = list_all[bisharp]-10
    list_all[blissey] = list_all[blissey]-45
    list_all[rotom_wash] = 0
    list_all[victini] = list_all[victini]-48
    list_all[zapdos] = list_all[zapdos]-8
    list_all[tyranitar] = list_all[tyranitar]-25
    list_all[gastrodon] = 0
    list_all[mandibuzz] = 0
    list_all[gengar] = list_all[gengar]-19
    list_all[rotom_heat] = 0
    list_all[amoonguss] = 0
    list_all[marowak_alola] = list_all[marowak_alola]-11
    list_all[regieleki] = 0
    list_all[torkoal] = 0
    list_all[shedinja] = 0
    list_all[slowbro_g] = 0

    no0 ()


def stall_hippowdon ():
    global list_all

    list_all[specs_dragapult] = list_all[specs_dragapult]-90
    list_all[heatran] = list_all[heatran]-125
    list_all[slowking_g] = list_all[slowking_g]-80
    list_all[other_tornadus_t]=list_all[other_tornadus_t]-60
    list_all[tapu_koko] = 0
    list_all[arctozolt] = 0
    list_all[ninetales_alola] = 0
    list_all[specs_magnezone] = list_all[specs_magnezone]-13
    list_all[melmetal] = list_all[melmetal]-45
    list_all[zeraora] = 0
    list_all[victini] = 0
    list_all[zapdos] = list_all[zapdos]-90
    list_all[dracozolt] = 0
    list_all[aegislash] = list_all[aegislash]-10
    list_all[mandibuzz] = list_all[mandibuzz]-35
    list_all[gengar] = list_all[gengar]-9
    list_all[rotom_heat] = list_all[rotom_heat]-7
    list_all[jirachi] = list_all[jirachi]-6
    list_all[grimmsnarl] = list_all[grimmsnarl]-80
    list_all[thundurus_t] = 0
    list_all[marowak_alola] = list_all[marowak_alola]-8
    list_all[regieleki] = 0
    list_all[torkoal] = 0
    list_all[seismitoad] = list_all[seismitoad]-20
    list_all[charizard] = 0
    list_all[slowbro_g] = 0
    list_all[shedinja] = 0
    list_all[moltres] = 0

    no0()
#SECTION 2
def stall_hydreigon ():
    global list_all

    list_all[heatran] = 0
    list_all[corviknight] = list_all[corviknight]-53.88
    list_all[slowking_g] = 0
    list_all[toxapex] = list_all[toxapex]-55
    list_all[hippowdon] = list_all[hippowdon]-25
    list_all[slowking] = 0
    list_all[blacephalon] = 0
    list_all[rotom_wash] = 0
    list_all[bisharp] = list_all[bisharp]-20
    list_all[slowbro] = 0
    list_all[victini] = list_all[victini]-20
    list_all[zapdos] = list_all[zapdos]-90
    list_all[aegislash] = list_all[aegislash]-12
    list_all[volcanion] = 0
    list_all[swampert] = list_all[swampert]-18
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[crawdaunt] = 0
    list_all[gengar] = list_all[gengar]-9
    list_all[rotom_heat] = 0
    list_all[marowak_alola] = 0
    list_all[seismitoad] = list_all[seismitoad]-18
    list_all[venusaur] = 0
    list_all[xatu] = 0
    list_all[shedinja] = 0
    list_all[slowbro_g] = list_all[slowbro_g]-1.5
    list_all[necrozma] = 0
    list_all[torkoal] = list_all[torkoal]-24

    no0()

def stall_kyurem ():
    global list_all

    list_all[heatran] = list_all[heatran]-180
    list_all[tank_garchomp] = list_all[tank_garchomp]-20
    list_all[tank_landorus_t] = list_all[tank_landorus_t]-40
    list_all[slowking_g] = list_all[slowking_g]-70
    list_all[other_tornadus_t] = list_all[other_tornadus_t]-70
    list_all[toxapex] = list_all[toxapex]-35
    list_all[urshifu_r] = list_all[urshifu_r]-40
    list_all[hippowdon] = list_all[hippowdon]-10
    list_all[dragonite] = list_all[dragonite]-25
    list_all[slowking] = 0
    list_all[other_kyurem] = 0
    list_all[rotom_wash] = list_all[rotom_wash]-20
    list_all[slowbro] = 0
    list_all[nidoking] = list_all[nidoking]-22
    list_all[zapdos] = list_all[zapdos]-90
    list_all[gastrodon] = 0
    list_all[pelipper] = 0
    list_all[mandibuzz] = 0
    list_all[crawdaunt] = list_all[crawdaunt]-12
    list_all[suicune] = list_all[suicune]-3
    list_all[marowak_alola] = list_all[marowak_alola]-9
    list_all[quagsire] = 0
    list_all[torkoal] = list_all[torkoal]-10
    list_all[xatu] = 0
    list_all[slowbro_g] = list_all[slowbro_g]-1

    no0()

def stall_landorus_t ():
    global list_all

    list_all[tank_landorus_t] = list_all[tank_landorus_t]-235
    list_all[sd_landorus_t]= list_all[sd_landorus_t]-16
    list_all[heatran] = list_all[heatran]-50
    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[tank_garchomp] = 0
    list_all[tapu_koko] = list_all[tapu_koko]-50
    list_all[id_magnezone] = list_all[id_magnezone]-50
    list_all[zeraora] = 0
    list_all[dragonite] = list_all[dragonite]-55
    list_all[hippowdon] = 0
    list_all[rillaboom] = list_all[rillaboom]-30
    list_all[skarmory] = list_all[skarmory]-17
    list_all[tapu_bulu] = list_all[tapu_bulu]-11
    list_all[victini] = list_all[victini]-47
    list_all[excadrill] = 0
    list_all[hawlucha] = list_all[hawlucha]-22
    list_all[blaziken] = list_all[blaziken]-20
    list_all[mandibuzz] = list_all[mandibuzz]-30
    list_all[grimmsnarl] = 0
    list_all[jirachi] = list_all[jirachi]-12
    list_all[terrakion] = list_all[terrakion]-6.5
    list_all[marowak_alola] = list_all[marowak_alola]-10
    list_all[regieleki] = 0
    list_all[shuckle] = 0
    list_all[torkoal] = list_all[torkoal]-24
    list_all[haxorus] = list_all[haxorus]-3

    no0()

def stall_mandibuzz ():
    global list_all

    list_all[tank_landorus_t] = list_all[tank_landorus_t]-200
    list_all[specs_dragapult] = list_all[specs_dragapult]-150
    list_all[darts_dragapult] = list_all[darts_dragapult]-85
    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[sweep_garchomp] = list_all[sweep_garchomp]-65
    list_all[urshifu_r] = list_all[urshifu_r]-40
    list_all[ferrothorn] = list_all[ferrothorn]-89.55
    list_all[sd_kartana] = 0
    list_all[other_kartana]=0
    list_all[scizor] = list_all[scizor]-65
    list_all[buzzwole] = 0
    list_all[dragonite] = list_all[dragonite]-60
    list_all[rillaboom] = 0
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[victini] = list_all[victini]-48
    list_all[aegislash] = list_all[aegislash]-18
    list_all[excadrill] = 0
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[gengar] = list_all[gengar]-15
    list_all[jirachi] = list_all[jirachi]-12
    list_all[marowak_alola] = list_all[marowak_alola]-10
    list_all[torkoal] = 0
    list_all[xatu] = 0
    list_all[haxorus] = 0

    no0()

def stall_mew ():
    global list_all

    list_all[tank_landorus_t] = list_all[tank_landorus_t]-100
    list_all[corviknight] = list_all[corviknight]-68.33
    list_all[tank_garchomp] = list_all[tank_garchomp]-55
    list_all[ferrothorn] = list_all[ferrothorn]-70
    list_all[clefable] = list_all[clefable]-45
    list_all[other_kyurem] = list_all[other_kyurem]-30
    list_all[ninetales_alola] = 0
    list_all[hippowdon] = list_all[hippowdon]-20
    list_all[slowking] = 0
    list_all[buzzwole] = list_all[buzzwole]-38
    list_all[bisharp] = list_all[bisharp]-20
    list_all[rotom_wash] = list_all[rotom_wash]-19
    list_all[tyranitar] = list_all[tyranitar]-10
    list_all[slowbro] = 0
    list_all[nidoking] = list_all[nidoking]-24
    list_all[tangrowth] = list_all[tangrowth]-10
    list_all[gastrodon] = list_all[gastrodon]-6
    list_all[ho_mew] = list_all[ho_mew]-6
    list_all[swampert] = list_all[swampert]-15
    list_all[crawdaunt] = list_all[crawdaunt]-7
    list_all[glastrier] = 0
    list_all[seismitoad] = 0
    list_all[xatu] = 0
    list_all[celesteela] = 0

    no0()
#Section 3

def stall_scizor ():
    global list_all

    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[id_magnezone] = list_all[id_magnezone]+8
    list_all[toxapex] = list_all[toxapex]-40
    list_all[ninetales_alola] = 0
    list_all[other_kyurem] = 0
    list_all[specs_kyurem] =  list_all[specs_kyurem] - 30
    list_all[tapu_lele] = 0
    list_all[tangrowth] = 0
    list_all[blissey] = list_all[blissey]-34
    list_all[aegislash] = list_all[aegislash]-13
    list_all[amoonguss] = 0
    list_all[shuckle] = 0
    list_all[alakazam] = 0

    no0()

def stall_skarmory ():
    global list_all

    list_all[tank_landorus_t] = 0
    list_all[corviknight] = list_all[corviknight]-110
    list_all[darts_dragapult] = 0
    list_all[sweep_garchomp] = 0
    list_all[tank_garchomp]= 0
    list_all[ferrothorn] = 0
    list_all[other_kartana] = list_all[other_kartana]-67
    list_all[melmetal] = list_all[melmetal]-124.3
    list_all[scizor] = 0
    list_all[buzzwole] = 0
    list_all[dragonite] = 0
    list_all[hippowdon] = 0
    list_all[rillaboom] = 0
    list_all[skarmory] = list_all[skarmory]-22
    list_all[bisharp] = list_all[bisharp]-55
    list_all[blissey] = list_all[blissey]-60
    list_all[tyranitar] = 0
    list_all[excadrill] = 0
    list_all[hawlucha] = list_all[hawlucha]-22
    list_all[swampert] = 0
    list_all[ho_mew] = 0
    list_all[mandibuzz] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-14
    list_all[glastrier] = 0
    list_all[jirachi] = list_all[jirachi]-9
    list_all[mamoswine] = 0
    list_all[amoonguss] = 0
    list_all[shuckle] = 0
    list_all[haxorus] = 0

    no0()

def stall_slowbro ():
    global list_all

    list_all[sd_landorus_t] =  list_all[sd_landorus_t]-18
    list_all[heatran] = list_all[heatran]-120
    list_all[sweep_garchomp] = list_all[sweep_garchomp]-30
    list_all[urshifu_r] = list_all[urshifu_r]-130
    list_all[toxapex] = list_all[toxapex]-30
    list_all[melmetal] = 0
    list_all[buzzwole] = list_all[buzzwole]-45
    list_all[tyranitar] = list_all[tyranitar]-10
    list_all[barraskewda] = 0
    list_all[excadrill] = 0
    list_all[hawlucha] = list_all[hawlucha]-17
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[blaziken] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-16
    list_all[jirachi] = list_all[jirachi]-9
    list_all[terrakion] = 0
    list_all[haxorus] = 0

    no0()

def stall_slowking_g ():
    global list_all

    list_all[heatran] = list_all[heatran]-80
    list_all[slowking_g] = list_all[slowking_g]-65
    list_all[tank_tapu_fini] = 0
    list_all[cm_tapu_fini] = 0
    list_all[whirlpool_tapu_fini] = 0
    list_all[tapu_koko] = 0
    list_all[clefable] = list_all[clefable]-75
    list_all[other_kyurem] = list_all[other_kyurem]-45
    list_all[specs_magnezone] = 0
    list_all[ninetales_alola] = 0
    list_all[rotom_wash] = 0
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[zapdos] = 0
    list_all[volcanion] = list_all[volcanion]-11
    list_all[cresselia] = 0
    list_all[primarina] = 0
    list_all[toxtricity] = 0
    list_all[thundurus_t] = list_all[thundurus_t]-2
    list_all[rotom_heat] = 0
    list_all[amoonguss] = 0
    list_all[hatterene] = 0
    list_all[keldeo] = list_all[keldeo] - 12
    list_all[togekiss] = 0
    list_all[celesteela] = list_all[celesteela]-11
    list_all[ribombee] = 0
    list_all[xatu] = 0
    list_all[moltres] = 0

    no0()

def stall_slowking ():
    global list_all

    list_all[heatran] = list_all[heatran]-165
    list_all[slowking_g] = 0
    list_all[other_kyurem] = list_all[other_kyurem]-35
    list_all[ninetales_alola] = 0
    list_all[tapu_lele] = 0
    list_all[slowking] = 0
    list_all[nidoking] = 0
    list_all[rotom_wash] = list_all[rotom_wash]-10
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[pelipper] = 0
    list_all[volcanion] = 0
    list_all[cresselia] = 0
    list_all[kingdra] = 0
    list_all[latios] = list_all[latios]-11
    list_all[latias] = list_all[latias]-5
    list_all[suicune] = list_all[suicune]-3.5
    list_all[seismitoad] = 0
    list_all[charizard] = 0
    list_all[moltres] = 0
    list_all[xatu] = 0

    no0()
#section 4    

def stall_tapu_koko ():
    global list_all

    list_all[heatran] = list_all[heatran]-30
    list_all[tank_tapu_fini] = list_all[tank_tapu_fini]-67
    list_all[whirlpool_tapu_fini]=0
    list_all[np_tornadus_t] = 0
    list_all[other_tornadus_t] = list_all[other_tornadus_t]-65
    list_all[toxapex] = list_all[toxapex]-50
    list_all[sd_kartana] = list_all[sd_kartana]-30
    list_all[buzzwole] = list_all[buzzwole]-27
    list_all[skarmory] = list_all[skarmory]-16
    list_all[slowbro] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-16
    list_all[mandibuzz] = 0
    list_all[moltres_galar] = 0
    list_all[togekiss] = 0
    list_all[specs_kyurem] = list_all[specs_kyurem]-14

    no0()

def stall_tornadus_t ():
    global list_all

    list_all[heatran] = list_all[heatran]-50
    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[ferrothorn] = list_all[ferrothorn]-50
    list_all[sd_kartana] = 0
    list_all[tank_tapu_fini] = list_all[tank_tapu_fini]-50
    list_all[whirlpool_tapu_fini] = list_all[whirlpool_tapu_fini] - 13
    list_all[skarmory] = 0
    list_all[toxapex] =  list_all[toxapex]-60
    list_all[rillaboom] = list_all[rillaboom]-40
    list_all[tapu_bulu] = list_all[tapu_bulu]-14
    list_all[gengar] = list_all[gengar]-9
    list_all[amoonguss] = 0
    list_all[slowking] = 0
    list_all[slowbro] = 0

    no0()

def stall_def_toxapex ():
    global list_all

    list_all[specs_dragapult] = list_all[specs_dragapult]-50
    list_all[heatran] = list_all[heatran]-70
    list_all[weavile] = list_all[weavile]-120
    list_all[cm_tapu_fini] = list_all[cm_tapu_fini]-10
    list_all[whirlpool_tapu_fini] = 0
    list_all[tank_tapu_fini] = 0
    list_all[urshifu_r] = 0
    list_all[other_tornadus_t] = 0
    list_all[toxapex] = list_all[toxapex]-70
    list_all[melmetal] = list_all[melmetal]-70
    list_all[scizor] = list_all[scizor]-35
    list_all[buzzwole] = list_all[buzzwole]-50
    list_all[slowking] = list_all[slowking]-30
    list_all[slowking_g] = list_all[slowking_g]-60
    list_all[slowbro] = list_all[slowbro]-40
    list_all[blissey] = list_all[blissey]-55
    list_all[tangrowth] = list_all[tangrowth]-16
    list_all[victini] = list_all[victini]-40
    list_all[aegislash] = list_all[aegislash]-17
    list_all[barraskewda] = 0
    list_all[pelipper] = list_all[pelipper]-55
    list_all[mandibuzz] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-14
    list_all[cresselia] = 0
    list_all[jirachi] = list_all[jirachi]-9
    list_all[primarina] = list_all[primarina]-5
    list_all[amoonguss] = 0
    list_all[keldeo] = list_all[keldeo]-9
    list_all[marowak_alola] = 0
    list_all[porygon2] = 0
    list_all[moltres] = 0
    list_all[shedinja] = 0

    no0()

def stall_spdef_toxapex ():
    global list_all

    list_all[specs_dragapult] = list_all[specs_dragapult]-90
    list_all[heatran] = list_all[heatran]-80
    list_all[weavile] = list_all[weavile]-110
    list_all[cm_tapu_fini] = list_all[cm_tapu_fini]-10
    list_all[whirlpool_tapu_fini] = 0
    list_all[tank_tapu_fini] = 0
    list_all[urshifu_r] = 0
    list_all[other_tornadus_t] = 0
    list_all[toxapex] = list_all[toxapex]-70
    list_all[melmetal] = list_all[melmetal]-70
    list_all[scizor] = list_all[scizor]-35
    list_all[buzzwole] = list_all[buzzwole]-47
    list_all[volcarona] = list_all[volcarona]-35
    list_all[slowking] = list_all[slowking]-35
    list_all[slowking_g] = list_all[slowking_g]-70
    list_all[slowbro] = list_all[slowbro]-45
    list_all[blissey] = list_all[blissey]-55
    list_all[tangrowth] = list_all[tangrowth]-16
    list_all[victini] = list_all[victini]-40
    list_all[aegislash] = list_all[aegislash]-17
    list_all[barraskewda] = 0
    list_all[pelipper] = list_all[pelipper]-60
    list_all[mandibuzz] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-13
    list_all[cresselia] = 0
    list_all[jirachi] = list_all[jirachi]-9
    list_all[primarina] = list_all[primarina]-5
    list_all[amoonguss] = 0
    list_all[keldeo] = list_all[keldeo]-11
    list_all[marowak_alola] = 0
    list_all[porygon2] = 0
    list_all[moltres] = 0
    list_all[shedinja] = 0

    no0()

def stall_zapdos ():
    global list_all

    list_all[corviknight] = list_all[corviknight]-170
    list_all[tank_tapu_fini] = list_all[tank_tapu_fini]-65
    list_all[np_tornadus_t] = 0
    list_all[other_tornadus_t] = 0
    list_all[ferrothorn] = 0
    list_all[sd_kartana] = 0
    list_all[other_kartana] = 0
    list_all[melmetal] = 0
    list_all[id_magnezone] = 0
    list_all[hippowdon] = list_all[hippowdon]-20
    list_all[skarmory] = 0
    list_all[scizor] = 0
    list_all[buzzwole] = 0
    list_all[rillaboom] = 0
    list_all[bisharp] = list_all[bisharp]-50
    list_all[blissey] = list_all[blissey]-30
    list_all[excadrill] = 0
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[zapdos_galar] = list_all[zapdos_galar]-20
    list_all[mandibuzz] = 0
    list_all[jirachi] = list_all[jirachi]-9

    no0()

def stall_ditto ():
    global list_all

    list_all[sweep_garchomp] = 0
    list_all[toxapex] = list_all[toxapex]-80
    list_all[sd_kartana] = 0
    list_all[np_tornadus_t] = 0
    list_all[dragonite] = list_all[dragonite]-80
    list_all[rillaboom] = list_all[rillaboom]-35
    list_all[blissey] = 0
    list_all[blacephalon] = list_all[blacephalon]-50
    list_all[blaziken] = 0
    list_all[zapdos_galar] = list_all[zapdos_galar]-24
    list_all[moltres_galar] = 0
    list_all[gengar] = 0
    list_all[terrakion] = 0
    list_all[togekiss] = 0
    list_all[venusaur] = list_all[venusaur]-10
    list_all[alakazam] = list_all[alakazam]-6
    list_all[celesteela] = list_all[celesteela]-10
    list_all[haxorus] = 0
    list_all[necrozma] = 0

    no0()

def stall_volcarona ():
    global list_all

    list_all[weavile] = 0
    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[arctozolt] = list_all[arctozolt] - 16
    list_all[ferrothorn] = 0
    list_all[sd_kartana] = 0
    list_all[id_magnezone] = 0
    list_all[melmetal] = list_all[melmetal] - 110
    list_all[ninetales_alola] = 0
    list_all[zeraora] = list_all[zeraora] - 78
    list_all[scizor] = 0
    list_all[buzzwole] = 0
    list_all[rillaboom] = list_all[rillaboom]-70
    list_all[skarmory] = 0
    list_all[tangrowth] = list_all[tangrowth]-10
    list_all[aegislash] = list_all[aegislash]-15
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[jirachi] = list_all[jirachi]-9

    no0()

 #section 5

def stall_aegislash ():
    global list_all

    list_all[tapu_lele] = 0
    list_all[slowking_g] = list_all[slowking_g]-60
    list_all[toxapex] = list_all[toxapex]-45
    list_all[ninetales_alola] = 0
    list_all[buzzwole] = list_all[buzzwole]-40
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[blissey] = list_all[blissey]-60
    list_all[tapu_bulu] = 0
    list_all[other_mew] = list_all[other_mew]-25
    list_all[zapdos_galar] = list_all[zapdos_galar]-20
    list_all[gengar] = list_all[gengar]-7
    list_all[jirachi] = list_all[jirachi]-9
    list_all[latios] = 0
    list_all[latias] = 0
    list_all[thundurus_t] = list_all[thundurus_t]
    list_all[amoonguss] = 0
    list_all[alakazam] = list_all[alakazam]-6

    no0()

def stall_buzzwole ():
    global list_all

    list_all[sd_landorus_t] = 0
    list_all[darts_dragapult] = list_all[darts_dragapult]-44
    list_all[weavile] = 0
    list_all[arctozolt] = 0
    list_all[melmetal] = list_all[melmetal]-100
    list_all[sd_kartana] = 0
    list_all[other_kartana] = 0
    list_all[scizor] = list_all[scizor]-35
    list_all[zeraora] = 0
    list_all[buzzwole] = list_all[buzzwole]-38
    list_all[rillaboom] = 0
    list_all[bisharp] = 0
    list_all[tapu_bulu] = 0
    list_all[tyranitar] = 0
    list_all[excadrill] = 0
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[crawdaunt] = 0
    list_all[glastrier] = 0
    list_all[mamoswine] = 0
    list_all[terrakion] = 0
    list_all[zarude] = 0
    list_all[conkeldurr] = 0

    no0()

def stall_azumarill ():
    global list_all

    list_all[weavile] = list_all[weavile]-70
    list_all[toxapex] = 0
    list_all[ferrothorn] = list_all[ferrothorn]-100
    list_all[id_magnezone] = 0
    list_all[rillaboom] = list_all[rillaboom]-75
    list_all[buzzwole] = 0
    list_all[blissey] = list_all[blissey]-30
    list_all[tapu_bulu] = 0
    list_all[tangrowth] = list_all[tangrowth]-15
    list_all[crawdaunt] = 0
    list_all[zarude] = 0
    list_all[hatterene] = 0
    list_all[venusaur] = 0
    list_all[torkoal] = 0

    no0()

def stall_moltres ():
    global list_all

    list_all[heatran] = list_all[heatran]-200
    list_all[corviknight] = list_all[corviknight]-178.55
    list_all[clefable] = list_all[clefable]-40
    list_all[ferrothorn] = 0
    list_all[sd_kartana] = 0
    list_all[other_kartana] = 0
    list_all[melmetal] = list_all[melmetal]-70
    list_all[id_magnezone] =  0
    list_all[other_kyurem] = 0
    list_all[ninetales_alola] = 0
    list_all[scizor] = 0
    list_all[buzzwole] = list_all[buzzwole]-47
    list_all[rillaboom] = 0
    list_all[skarmory] = 0
    list_all[bisharp] = list_all[bisharp]-50
    list_all[blissey] = list_all[blissey]-60
    list_all[tangrowth] = 0
    list_all[aegislash] = list_all[aegislash]-15
    list_all[excadrill] = list_all[excadrill]-35
    list_all[mamoswine] = list_all[mamoswine]-30
    list_all[jirachi] = list_all[jirachi]-9
    list_all[torkoal] = 0
    list_all[venusaur] = 0
    list_all[charizard] = 0

    no0()

def stall_jirachi ():
    global list_all

    list_all[slowking_g] = list_all[slowking_g]-30
    list_all[tapu_koko] = list_all[tapu_koko]-45
    list_all[toxapex] = list_all[toxapex]-65
    list_all[clefable] = list_all[clefable]-80
    list_all[other_kyurem] = list_all[other_kyurem]-30
    list_all[ninetales_alola] = 0
    list_all[tapu_lele] = 0
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[latias] = 0
    list_all[latios] = 0
    list_all[amoonguss] = 0
    list_all[alakazam] = 0

    no0()

def stall_cresselia():
    global list_all

    list_all[tapu_lele] = list_all[tapu_lele]-120
    list_all[toxapex] = list_all[toxapex]-65
    list_all[other_kyurem] = list_all[other_kyurem]-45
    list_all[ninetales_alola] = 0
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[nidoking] = 0
    list_all[zapdos] = list_all[zapdos]-65
    list_all[tangrowth] = list_all[tangrowth]-10
    list_all[rotom_wash] = list_all[rotom_wash]-15
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[latios] = 0
    list_all[latias] = 0
    list_all[rotom_heat] = list_all[rotom_heat]-5
    list_all[mamoswine] = list_all[mamoswine]-10
    list_all[seismitoad] = 0
    list_all[venusaur] = 0
    list_all[alakazam] = 0

    no0()
#section 6

def stall_tangrowth():
    global list_all

    list_all[other_kartana] = 0
    list_all[sd_kartana] = 0
    list_all[toxapex] = list_all[toxapex]-65
    list_all[urshifu_r] = list_all[urshifu_r]-12
    list_all[melmetal] = list_all[melmetal]-65
    list_all[id_magnezone] = 0
    list_all[zeraora] = 0
    list_all[buzzwole] = list_all[buzzwole]-45
    list_all[rillaboom] = 0
    list_all[bisharp] = 0
    list_all[tapu_bulu] = list_all[tapu_bulu]-14
    list_all[rotom_wash] = 0
    list_all[tyranitar] = list_all[tyranitar]-23
    list_all[tangrowth] = list_all[tangrowth]-15
    list_all[barraskewda] = 0
    list_all[excadrill] = 0
    list_all[ho_mew] = list_all[ho_mew]-8
    list_all[crawdaunt] = 0
    list_all[terrakion] = 0
    list_all[zarude] = list_all[zarude]-3
    list_all[conkeldurr] = 0

    no0()

def stall_gastrodon():
    global list_all

    list_all[heatran] = list_all[heatran]-200
    list_all[specs_dragapult] = list_all[specs_dragapult]-100
    list_all[tapu_koko] = list_all[tapu_koko]-90
    list_all[slowking_g] = list_all[slowking_g]-87
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[tank_tapu_fini] = list_all[tank_tapu_fini]-60
    list_all[arctozolt] = list_all[arctozolt]-26
    list_all[specs_magnezone] = 0
    list_all[zeraora] = 0
    list_all[blacephalon] = list_all[blacephalon]-35
    list_all[nidoking] = 0
    list_all[rotom_wash] = list_all[rotom_wash]-20
    list_all[victini] = 0
    list_all[zapdos] = 0
    list_all[dracozolt] = 0
    list_all[volcanion] = 0
    list_all[pelipper] = list_all[pelipper]-50
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[aegislash] = list_all[aegislash]-11
    list_all[gengar] = 0
    list_all[jirachi] = list_all[jirachi]-9
    list_all[thundurus_t] = list_all[thundurus_t]-8
    list_all[suicune] = list_all[suicune]-5
    list_all[regieleki] = 0
    list_all[marowak_alola] = list_all[marowak_alola]-7
    list_all[moltres]=0

    no0()

def stall_tapu_bulu():
    global list_all

    list_all[cm_tapu_fini] = 0
    list_all[tank_tapu_fini] = 0
    list_all[whirlpool_tapu_fini] = 0
    list_all[tapu_koko] = list_all[tapu_koko]-80
    list_all[tapu_lele] = list_all[tapu_lele]-90
    list_all[zeraora] = list_all[zeraora]-75
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[rotom_wash] = list_all[rotom_wash]-15
    list_all[tyranitar] = list_all[tyranitar]-23
    list_all[barraskewda] = list_all[barraskewda]-60
    list_all[crawdaunt] = 0
    list_all[azumarill] = 0
    list_all[terrakion] = 0
    list_all[suicune] = 0
    list_all[keldeo] = 0
    list_all[alakazam] = 0

    no0()

def stall_flygon():
    global list_all

    list_all[heatran] = 0
    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[other_tornadus_t] = list_all[other_tornadus_t]-65
    list_all[zeraora] = 0
    list_all[zapdos] = 0
    list_all[victini] = list_all[victini]-47
    list_all[tyranitar] = list_all[tyranitar]-40
    list_all[aegislash] = list_all[aegislash]-15
    list_all[ho_mew] = list_all[ho_mew]-11
    list_all[gengar] = 0
    list_all[rotom_heat] = 0
    list_all[regieleki] = 0
    list_all[marowak_alola] = list_all[marowak_alola]-6
    list_all[moltres] = 0

    no0()

def stall_marowak_alola():
    global list_all

    list_all[tapu_koko] = 0
    list_all[arctozolt] = 0
    list_all[specs_magnezone] = 0
    list_all[ninetales_alola] = 0
    list_all[buzzwole] = list_all[buzzwole]-45
    list_all[volcarona] = list_all[volcarona]-40
    list_all[victini] = 0
    list_all[regieleki] = 0
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[jirachi] = list_all[jirachi]-9
    list_all[rotom_heat] = 0
    list_all[amoonguss] = 0
    list_all[torkoal] = 0
    list_all[necrozma] = 0
    list_all[slowbro_g] = list_all[slowbro_g]-1
    list_all[ribombee] = 0

    no0()

def stall_reuniclus():
    global list_all

    list_all[specs_dragapult] = list_all[specs_dragapult]-50
    list_all[slowking_g] = list_all[slowking_g]-55
    list_all[cm_tapu_fini] = 0
    list_all[specs_kyurem] = 0
    list_all[other_kyurem] = list_all[other_kyurem]-50
    list_all[specs_magnezone] = 0
    list_all[ninetales_alola] = 0
    list_all[tapu_lele] = 0
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[nidoking] = 0
    list_all[rotom_wash] = 0
    list_all[zapdos] = 0
    list_all[pelipper] = 0
    list_all[volcanion] = list_all[volcanion]-20
    list_all[rotom_heat] = 0
    list_all[thundurus_t] = 0
    list_all[toxtricity] = 0
    list_all[primarina] = 0
    list_all[hatterene] = 0
    list_all[keldeo] = 0
    list_all[seismitoad] = 0
    list_all[venusaur] = 0
    list_all[alakazam] = 0
    list_all[celesteela] = 0
    list_all[necrozma] = 0
    list_all[moltres] = 0

    no0()

#section 7

def stall_togekiss():
    global list_all

    list_all[specs_dragapult] = list_all[specs_dragapult]-120
    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[sweep_garchomp] = 0
    list_all[other_tornadus_t] = 0
    list_all[sd_kartana] = 0
    list_all[rillaboom] = 0
    list_all[buzzwole] = 0
    list_all[hydreigon] = list_all[hydreigon]-70
    list_all[ho_mew] = list_all[ho_mew]-9
    list_all[mandibuzz] = list_all[mandibuzz]-22
    list_all[zapdos_galar] = list_all[zapdos_galar]-15
    list_all[latios] = list_all[latios]-5
    list_all[latias] = list_all[latias]-2
    list_all[zarude] = 0
    list_all[torkoal] = list_all[torkoal]-2

    no0()


def stall_xatu():
    global list_all

    list_all[heatran] = list_all[heatran]-200
    list_all[corviknight] = list_all[corviknight]-128
    list_all[toxapex] = list_all[toxapex]-65
    list_all[ferrothorn] = 0
    list_all[hippowdon] = 0
    list_all[skarmory] = 0
    list_all[tangrowth] = 0
    list_all[ho_mew] = 0
    list_all[swampert] = 0
    list_all[torkoal] = 0

    no0()

def stall_umbreon():
    global list_all

    list_all[sd_landorus_t] = list_all[sd_landorus_t]-20
    list_all[darts_dragapult] = 0
    list_all[weavile] = list_all[weavile]-60
    list_all[sweep_garchomp] = 0
    list_all[zeraora] = 0
    list_all[slowking] = 0
    list_all[slowbro] = 0
    list_all[victini] = 0
    list_all[aegislash] = list_all[aegislash]-15
    list_all[excadrill] = 0
    list_all[other_mew] = list_all[other_mew]-12
    list_all[mamoswine] = 0
    list_all[jirachi] = 0
    list_all[marowak_alola] = list_all[marowak_alola]-10
    list_all[haxorus] = 0

    no0()

def stall_avalugg():
    global list_all

    list_all[tank_landorus_t] = list_all[tank_landorus_t]-220
    list_all[sd_landorus_t] = list_all[sd_landorus_t]-15
    list_all[weavile] = list_all[weavile]-120
    list_all[darts_dragapult] = 0
    list_all[sweep_garchomp] = 0
    list_all[corviknight] = list_all[corviknight]-58.33
    list_all[arctozolt] = 0
    list_all[sd_kartana] = list_all[sd_kartana]-30
    list_all[zeraora] = list_all[zeraora]-50
    list_all[dragonite] =0
    list_all[tapu_bulu] = 0
    list_all[tyranitar] = list_all[tyranitar] - 23
    list_all[ho_mew] = list_all[ho_mew]-13
    list_all[crawdaunt] = 0
    list_all[mamoswine] = 0
    list_all[haxorus] = 0

    no0()

def stall_quagsire():
    global list_all

    list_all[darts_dragapult] = 0
    list_all[sd_landorus_t] = 0
    list_all[weavile] = list_all[weavile]-110
    list_all[heatran] = list_all[heatran]-50
    list_all[sweep_garchomp] = 0
    list_all[tapu_koko] = list_all[tapu_koko]-50
    list_all[arctozolt] = list_all[arctozolt]-1
    list_all[specs_magnezone] = 0
    list_all[melmetal] = list_all[melmetal]-100
    list_all[scizor] = 0
    list_all[zeraora] = 0
    list_all[buzzwole] = list_all[buzzwole]-45
    list_all[dragonite] = 0
    list_all[bisharp] = 0
    list_all[victini] = 0
    list_all[dracozolt] = 0
    list_all[excadrill] = 0
    list_all[hawlucha] = 0
    list_all[blaziken] = 0
    list_all[jirachi] = 0
    list_all[azumarill] = 0
    list_all[mamoswine] = 0
    list_all[rotom_heat] = list_all[rotom_heat]-11
    list_all[regieleki] = 0
    list_all[marowak_alola] = list_all[marowak_alola]-13
    list_all[haxorus] = 0

    no0()

def stall_shedinja():
    global list_all

    list_all[tank_tapu_fini] = list_all[tank_tapu_fini]-40
    list_all[whirlpool_tapu_fini] = list_all[whirlpool_tapu_fini]-20
    list_all[tapu_koko] = 0
    list_all[urshifu_r] = 0
    list_all[specs_kyurem] = 0
    list_all[other_kyurem] = list_all[other_kyurem]-32
    list_all[melmetal] = list_all[melmetal]-120
    list_all[tapu_lele] = 0
    list_all[buzzwole] = list_all[buzzwole]-47
    list_all[slowking] = 0
    list_all[reuniclus] = list_all[reuniclus]-7
    list_all[jirachi] = list_all[jirachi]-8
    list_all[primarina] = list_all[primarina]-5
    list_all[toxtricity] = list_all[toxtricity]-6
    list_all[thundurus_t] = 0
    list_all[suicune] = list_all[suicune]-6
    list_all[venusaur] = list_all[venusaur]-5
    list_all[keldeo] = list_all[keldeo]-9
    list_all[alakazam] = list_all[alakazam]-3

    no0()

def stall_goggles_shedinja():
    global list_all

    list_all[tank_tapu_fini] = list_all[tank_tapu_fini]-40
    list_all[whirlpool_tapu_fini] = list_all[whirlpool_tapu_fini]-20
    list_all[tapu_koko] = 0
    list_all[urshifu_r] = 0
    list_all[specs_kyurem] = 0
    list_all[other_kyurem] = list_all[other_kyurem]-32
    list_all[melmetal] = list_all[melmetal]-120
    list_all[tapu_lele] = 0
    list_all[buzzwole] = list_all[buzzwole]-47
    list_all[slowking] = 0
    list_all[reuniclus] = list_all[reuniclus]-7
    list_all[jirachi] = list_all[jirachi]-8
    list_all[primarina] = list_all[primarina]-5
    list_all[toxtricity] = list_all[toxtricity]-6
    list_all[thundurus_t] = 0
    list_all[suicune] = list_all[suicune]-6
    list_all[venusaur] = list_all[venusaur]-5
    list_all[keldeo] = list_all[keldeo]-9
    list_all[alakazam] = list_all[alakazam]-3
    list_all[corviknight]= list_all[corviknight]+55
    list_all[arctozolt] = 0
    list_all[ninetales_alola] = 0

    no0()
"""
Now we will get all of the possible combinations After the function:

First we will make a list
Do a fancy itertools import
Make something that prints it with the function name.
"""

def calculate (choice1="", choice2="", choice3="", choice4="", choice5="", choice6=""):
    global list_all

    if choice1 == "blissey":
        stall_blissey()
    elif choice1 == "clefable":
        stall_clefable()
    elif choice1 == "corviknight":
        stall_corviknight()
    elif choice1 == "spdef corviknight":
        stall_spdef_corviknight()
    elif choice1 == "garchomp":
        stall_garchomp()
    elif choice1 == "dragonite":
        stall_dragonite()
    elif choice1 == "hippowdon":
        stall_hippowdon()

    elif choice1 == "hydreigon":
        stall_hydreigon()
    elif choice1 == "kyurem":
        stall_kyurem()
    elif choice1 == "landorus t":
        stall_landorus_t()
    elif choice1 == "mandibuzz":
        stall_mandibuzz()
    elif choice1 == "mew":
        stall_mew()

    elif choice1 == "scizor":
        stall_scizor()
    elif choice1 == "skarmory":
        stall_skarmory()
    elif choice1 == "slowbro":
        stall_slowbro()
    elif choice1 == "slowking":
        stall_slowking()
    elif choice1 == "slowking g":
        stall_slowking_g()

    elif choice1 == "tapu koko":
        stall_tapu_koko()
    elif choice1 == "tornadus t":
        stall_tornadus_t()
    elif choice1 == "def toxapex":
        stall_def_toxapex()
    elif choice1 == "spdef toxapex":
        stall_spdef_toxapex()
    elif choice1 == "volcarona":
        stall_volcarona()
    elif choice1 == "zapdos":
        stall_zapdos()
    elif choice1 == "ditto":
        stall_ditto()

    elif choice1 == "aegislash":
        stall_aegislash()
    elif choice1 == "azumarill":
        stall_azumarill()
    elif choice1 == "buzzwole":
        stall_buzzwole()
    elif choice1 == "jirachi":
        stall_jirachi()
    elif choice1 == "moltres":
        stall_moltres()
    elif choice1 == "cresselia":
        stall_cresselia()

    elif choice1 == "tangrowth":
        stall_tangrowth()
    elif choice1 == "tapu bulu":
        stall_tapu_bulu()
    elif choice1 == "gastrodon":
        stall_gastrodon()
    elif choice1 == "flygon":
        stall_flygon()
    elif choice1 == "marowak alola":
        stall_marowak_alola()
    elif choice1 == "reuniclus":
        stall_reuniclus()

    elif choice1 == "togekiss":
        stall_togekiss()
    elif choice1 == "umbreon":
        stall_umbreon()
    elif choice1 == "xatu":
        stall_xatu()
    elif choice1 == "shedinja":
        stall_shedinja()
    elif choice1 == "goggles shedinja":
        stall_goggles_shedinja()
    elif choice1 == "quagsire":
        stall_quagsire()
    elif choice1 == "avalugg":
        stall_avalugg()


    if choice2 == "blissey":
        stall_blissey()
    elif choice2 == "clefable":
        stall_clefable()
    elif choice2 == "corviknight":
        stall_corviknight()
    elif choice2 == "spdef corviknight":
        stall_spdef_corviknight()
    elif choice2 == "garchomp":
        stall_garchomp()
    elif choice2 == "dragonite":
        stall_dragonite()
    elif choice2 == "hippowdon":
        stall_hippowdon()

    elif choice2 == "hydreigon":
        stall_hydreigon()
    elif choice2 == "kyurem":
        stall_kyurem()
    elif choice2 == "landorus t":
        stall_landorus_t()
    elif choice2 == "mandibuzz":
        stall_mandibuzz()
    elif choice2 == "mew":
        stall_mew()

    elif choice2 == "scizor":
        stall_scizor()
    elif choice2 == "skarmory":
        stall_skarmory()
    elif choice2 == "slowbro":
        stall_slowbro()
    elif choice2 == "slowking":
        stall_slowking()
    elif choice2 == "slowking g":
        stall_slowking_g()

    elif choice2 == "tapu koko":
        stall_tapu_koko()
    elif choice2 == "tornadus t":
        stall_tornadus_t()
    elif choice2 == "def toxapex":
        stall_def_toxapex()
    elif choice2 == "spdef toxapex":
        stall_spdef_toxapex()
    elif choice2 == "volcarona":
        stall_volcarona()
    elif choice2 == "zapdos":
        stall_zapdos()
    elif choice2 == "ditto":
        stall_ditto()

    elif choice2 == "aegislash":
        stall_aegislash()
    elif choice2 == "azumarill":
        stall_azumarill()
    elif choice2 == "buzzwole":
        stall_buzzwole()
    elif choice2 == "jirachi":
        stall_jirachi()
    elif choice2 == "moltres":
        stall_moltres()
    elif choice2 == "cresselia":
        stall_cresselia()

    elif choice2 == "tangrowth":
        stall_tangrowth()
    elif choice2 == "tapu bulu":
        stall_tapu_bulu()
    elif choice2 == "gastrodon":
        stall_gastrodon()
    elif choice2 == "flygon":
        stall_flygon()
    elif choice2 == "marowak alola":
        stall_marowak_alola()
    elif choice2 == "reuniclus":
        stall_reuniclus()

    elif choice2 == "togekiss":
        stall_togekiss()
    elif choice2 == "umbreon":
        stall_umbreon()
    elif choice2 == "xatu":
        stall_xatu()
    elif choice2 == "shedinja":
        stall_shedinja()
    elif choice2 == "goggles shedinja":
        stall_goggles_shedinja()
    elif choice2 == "quagsire":
        stall_quagsire()
    elif choice2 == "avalugg":
        stall_avalugg()

    if choice3 == "blissey":
        stall_blissey()
    elif choice3 == "clefable":
        stall_clefable()
    elif choice3 == "corviknight":
        stall_corviknight()
    elif choice3 == "spdef corviknight":
        stall_spdef_corviknight()
    elif choice3 == "garchomp":
        stall_garchomp()
    elif choice3 == "dragonite":
        stall_dragonite()
    elif choice3 == "hippowdon":
        stall_hippowdon()

    elif choice3 == "hydreigon":
        stall_hydreigon()
    elif choice3 == "kyurem":
        stall_kyurem()
    elif choice3 == "landorus t":
        stall_landorus_t()
    elif choice3 == "mandibuzz":
        stall_mandibuzz()
    elif choice3 == "mew":
        stall_mew()

    elif choice3 == "scizor":
        stall_scizor()
    elif choice3 == "skarmory":
        stall_skarmory()
    elif choice3 == "slowbro":
        stall_slowbro()
    elif choice3 == "slowking":
        stall_slowking()
    elif choice3 == "slowking g":
        stall_slowking_g()

    elif choice3 == "tapu koko":
        stall_tapu_koko()
    elif choice3 == "tornadus t":
        stall_tornadus_t()
    elif choice3 == "def toxapex":
        stall_def_toxapex()
    elif choice3 == "spdef toxapex":
        stall_spdef_toxapex()
    elif choice3 == "volcarona":
        stall_volcarona()
    elif choice3 == "zapdos":
        stall_zapdos()
    elif choice3 == "ditto":
        stall_ditto()

    elif choice3 == "aegislash":
        stall_aegislash()
    elif choice3 == "azumarill":
        stall_azumarill()
    elif choice3 == "buzzwole":
        stall_buzzwole()
    elif choice3 == "jirachi":
        stall_jirachi()
    elif choice3 == "moltres":
        stall_moltres()
    elif choice3 == "cresselia":
        stall_cresselia()

    elif choice3 == "tangrowth":
        stall_tangrowth()
    elif choice3 == "tapu bulu":
        stall_tapu_bulu()
    elif choice3 == "gastrodon":
        stall_gastrodon()
    elif choice3 == "flygon":
        stall_flygon()
    elif choice3 == "marowak alola":
        stall_marowak_alola()
    elif choice3 == "reuniclus":
        stall_reuniclus()

    elif choice3 == "togekiss":
        stall_togekiss()
    elif choice3 == "umbreon":
        stall_umbreon()
    elif choice3 == "xatu":
        stall_xatu()
    elif choice3 == "shedinja":
        stall_shedinja()
    elif choice3 == "goggles shedinja":
        stall_goggles_shedinja()
    elif choice3 == "quagsire":
        stall_quagsire()
    elif choice3 == "avalugg":
        stall_avalugg()

    if choice4 == "blissey":
        stall_blissey()
    elif choice4 == "clefable":
        stall_clefable()
    elif choice4 == "corviknight":
        stall_corviknight()
    elif choice4 == "spdef corviknight":
        stall_spdef_corviknight()
    elif choice4 == "garchomp":
        stall_garchomp()
    elif choice4 == "dragonite":
        stall_dragonite()
    elif choice4 == "hippowdon":
        stall_hippowdon()

    elif choice4 == "hydreigon":
        stall_hydreigon()
    elif choice4 == "kyurem":
        stall_kyurem()
    elif choice4 == "landorus t":
        stall_landorus_t()
    elif choice4 == "mandibuzz":
        stall_mandibuzz()
    elif choice4 == "mew":
        stall_mew()

    elif choice4 == "scizor":
        stall_scizor()
    elif choice4 == "skarmory":
        stall_skarmory()
    elif choice4 == "slowbro":
        stall_slowbro()
    elif choice4 == "slowking":
        stall_slowking()
    elif choice4 == "slowking g":
        stall_slowking_g()

    elif choice4 == "tapu koko":
        stall_tapu_koko()
    elif choice4 == "tornadus t":
        stall_tornadus_t()
    elif choice4 == "def toxapex":
        stall_def_toxapex()
    elif choice4 == "spdef toxapex":
        stall_spdef_toxapex()
    elif choice4 == "volcarona":
        stall_volcarona()
    elif choice4 == "zapdos":
        stall_zapdos()
    elif choice4 == "ditto":
        stall_ditto()

    elif choice4 == "aegislash":
        stall_aegislash()
    elif choice4 == "azumarill":
        stall_azumarill()
    elif choice4 == "buzzwole":
        stall_buzzwole()
    elif choice4 == "jirachi":
        stall_jirachi()
    elif choice4 == "moltres":
        stall_moltres()
    elif choice4 == "cresselia":
        stall_cresselia()

    elif choice4 == "tangrowth":
        stall_tangrowth()
    elif choice4 == "tapu bulu":
        stall_tapu_bulu()
    elif choice4 == "gastrodon":
        stall_gastrodon()
    elif choice4 == "flygon":
        stall_flygon()
    elif choice4 == "marowak alola":
        stall_marowak_alola()
    elif choice4 == "reuniclus":
        stall_reuniclus()

    elif choice4 == "togekiss":
        stall_togekiss()
    elif choice4 == "umbreon":
        stall_umbreon()
    elif choice4 == "xatu":
        stall_xatu()
    elif choice4 == "shedinja":
        stall_shedinja()
    elif choice4 == "goggles shedinja":
        stall_goggles_shedinja()
    elif choice4 == "quagsire":
        stall_quagsire()
    elif choice4 == "avalugg":
        stall_avalugg()

    if choice5 == "blissey":
        stall_blissey()
    elif choice5 == "clefable":
        stall_clefable()
    elif choice5 == "corviknight":
        stall_corviknight()
    elif choice5 == "spdef corviknight":
        stall_spdef_corviknight()
    elif choice5 == "garchomp":
        stall_garchomp()
    elif choice5 == "dragonite":
        stall_dragonite()
    elif choice5 == "hippowdon":
        stall_hippowdon()

    elif choice5 == "hydreigon":
        stall_hydreigon()
    elif choice5 == "kyurem":
        stall_kyurem()
    elif choice5 == "landorus t":
        stall_landorus_t()
    elif choice5 == "mandibuzz":
        stall_mandibuzz()
    elif choice5 == "mew":
        stall_mew()

    elif choice5 == "scizor":
        stall_scizor()
    elif choice5 == "skarmory":
        stall_skarmory()
    elif choice5 == "slowbro":
        stall_slowbro()
    elif choice5 == "slowking":
        stall_slowking()
    elif choice5 == "slowking g":
        stall_slowking_g()

    elif choice5 == "tapu koko":
        stall_tapu_koko()
    elif choice5 == "tornadus t":
        stall_tornadus_t()
    elif choice5 == "def toxapex":
        stall_def_toxapex()
    elif choice5 == "spdef toxapex":
        stall_spdef_toxapex()
    elif choice5 == "volcarona":
        stall_volcarona()
    elif choice5 == "zapdos":
        stall_zapdos()
    elif choice5 == "ditto":
        stall_ditto()

    elif choice5 == "aegislash":
        stall_aegislash()
    elif choice5 == "azumarill":
        stall_azumarill()
    elif choice5 == "buzzwole":
        stall_buzzwole()
    elif choice5 == "jirachi":
        stall_jirachi()
    elif choice5 == "moltres":
        stall_moltres()
    elif choice5 == "cresselia":
        stall_cresselia()

    elif choice5 == "tangrowth":
        stall_tangrowth()
    elif choice5 == "tapu bulu":
        stall_tapu_bulu()
    elif choice5 == "gastrodon":
        stall_gastrodon()
    elif choice5 == "flygon":
        stall_flygon()
    elif choice5 == "marowak alola":
        stall_marowak_alola()
    elif choice5 == "reuniclus":
        stall_reuniclus()

    elif choice5 == "togekiss":
        stall_togekiss()
    elif choice5 == "umbreon":
        stall_umbreon()
    elif choice5 == "xatu":
        stall_xatu()
    elif choice5 == "shedinja":
        stall_shedinja()
    elif choice5 == "goggles shedinja":
        stall_goggles_shedinja()
    elif choice5 == "quagsire":
        stall_quagsire()
    elif choice5 == "avalugg":
        stall_avalugg()

    if choice6 == "blissey":
        stall_blissey()
    elif choice6 == "clefable":
        stall_clefable()
    elif choice6 == "corviknight":
        stall_corviknight()
    elif choice6 == "spdef corviknight":
        stall_spdef_corviknight()
    elif choice6 == "garchomp":
        stall_garchomp()
    elif choice6 == "dragonite":
        stall_dragonite()
    elif choice6 == "hippowdon":
        stall_hippowdon()

    elif choice6 == "hydreigon":
        stall_hydreigon()
    elif choice6 == "kyurem":
        stall_kyurem()
    elif choice6 == "landorus t":
        stall_landorus_t()
    elif choice6 == "mandibuzz":
        stall_mandibuzz()
    elif choice6 == "mew":
        stall_mew()

    elif choice6 == "scizor":
        stall_scizor()
    elif choice6 == "skarmory":
        stall_skarmory()
    elif choice6 == "slowbro":
        stall_slowbro()
    elif choice6 == "slowking":
        stall_slowking()
    elif choice6 == "slowking g":
        stall_slowking_g()

    elif choice6 == "tapu koko":
        stall_tapu_koko()
    elif choice6 == "tornadus t":
        stall_tornadus_t()
    elif choice6 == "def toxapex":
        stall_def_toxapex()
    elif choice6 == "spdef toxapex":
        stall_spdef_toxapex()
    elif choice6 == "volcarona":
        stall_volcarona()
    elif choice6 == "zapdos":
        stall_zapdos()
    elif choice6 == "ditto":
        stall_ditto()

    elif choice6 == "aegislash":
        stall_aegislash()
    elif choice6 == "azumarill":
        stall_azumarill()
    elif choice6 == "buzzwole":
        stall_buzzwole()
    elif choice6 == "jirachi":
        stall_jirachi()
    elif choice6 == "moltres":
        stall_moltres()
    elif choice6 == "cresselia":
        stall_cresselia()

    elif choice6 == "tangrowth":
        stall_tangrowth()
    elif choice6 == "tapu bulu":
        stall_tapu_bulu()
    elif choice6 == "gastrodon":
        stall_gastrodon()
    elif choice6 == "flygon":
        stall_flygon()
    elif choice6 == "marowak alola":
        stall_marowak_alola()
    elif choice6 == "reuniclus":
        stall_reuniclus()

    elif choice6 == "togekiss":
        stall_togekiss()
    elif choice6 == "umbreon":
        stall_umbreon()
    elif choice6 == "xatu":
        stall_xatu()
    elif choice6 == "shedinja":
        stall_shedinja()
    elif choice6 == "goggles shedinja":
        stall_goggles_shedinja()
    elif choice6 == "quagsire":
        stall_quagsire()
    elif choice6 == "avalugg":
        stall_avalugg()




    if sum(list_all) < 300:
        total = sum(list_all)
        print (total)
        print (choice1+choice2+choice3+choice4+choice5+choice6)


    list_all = [425.6, 31.05, 128.64, 85.76, 213.1, 152.8, 215.5, 116.87, 62.93, 81.5, 29.46, 36.83, 81.02, 97.6, 80.62, 26.88, 135.3, 144, 54.6, 139.5, 179.9, 43.74, 77.76, 63.24, 42.16, 23.83, 71.48, 146.7, 73.6, 70.4, 166, 88.4, 51.4, 114.2, 55.5, 37.7, 100.5, 37.6, 45.6, 85.2, 70.9, 66.1, 84.7, 32.4, 23.4, 57.6, 20.9, 14.9, 51.3, 56.7, 92, 30.4, 62.7, 13.6, 42.5, 13.2, 35.4, 16.3, 37.26, 24.84, 77.5, 12.8, 42.4, 41.4, 31.8, 41.4, 19.8, 31.6, 15.7, 34.3, 15, 19.4, 2.3, 8.9, 13.9, 13.1, 8.9, 23.1, 32, 2.4, 10, 9.3, 7.2, 9.6, 9.9, 11.4, 6.6, 7.6, 11.9, 29.8, 17.3, 20.3, 19.9, 8.6, 45.3, 26.4, 8.5, 6.7, 36.9, 22.4, 8.8, 20.5, 3.3, 10, 4.2, 8.2, 3.9, 4.4, 6.5, 3.8, 0.6, 2.8, 5.6]






stuff = ["blissey","clefable", "corviknight", "spdef corviknight", "garchomp", "dragonite", "hippowdon", "hydreigon", "kyurem", "landorus t", "mandibuzz", "mew", "scizor", "skarmory", "slowbro", "slowking", "slowking g", "tapu koko", "tornadus t", "def toxapex", "spdef toxapex", "volcarona", "zapdos", "ditto", "aegislash", "azumarill", "buzzwole", "jirachi", "moltres", "cresselia", "tangrowth", "tapu bulu", "gastrodon", "flygon", "marowak alola", "reuniclus", "togekiss", "umbreon", "xatu", "shedinja", "goggles shedinja", "goggles shedinja", "quagsire", "avalugg"]

for i in range(6,7):
    for subset in itertools.combinations(stuff, i):
        param1 = subset[0] 
        param2 = subset[1]
        param3 = subset[2]
        param4 = subset[3]
        param5 = subset[4]
        param6 = subset[5]

        calculate (param1,param2,param3,param4,param5,param6)
