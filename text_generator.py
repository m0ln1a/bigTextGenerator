#      TTTTT  EEEEE  X   X  TTTTT       GGGGG  EEEEE  N   N  EEEEE  RRR     AAA   TTTTT  OOOOO  RRR
#       T    E       X X     T         G      E      NN  N  E      R  R   A   A    T    O   O  R  R
#      T    EEEEE    X      T         G      EEEEE  N N N  EEEEE  R  R   A   A    T    O   O  R  R
#     T    E       X X     T         G  GG  E      N  NN  E      RRR    AAAAA    T    O   O  RRR
#    T    E      X   X    T         G   G  E      N   N  E      R  R   A   A    T    O   O  R  R
#   T    EEEEE  X   X    T         GGGGG  EEEEE  N   N  EEEEE  R   R  A   A    T    OOOOO  R   R

#   @   @  @@@@       @@@@@
#   @   @ @   @       @   @
#   @   @    @        @   @
#   @   @   @         @   @
#    @ @   @    @@    @   @
#     @   @@@@@ @@    @@@@@


import sys

wordIn = ""
simbol = ""
masterMode = False
alphabetEng = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
alphabetRus = 'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'
alphabetSpecial = ' ', '.', ',', '?', '!', '-', '+', '=', '*', '/', '<', '>'
alphabetNumbers = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','|'
alphabet = alphabetEng + alphabetRus + alphabetSpecial + alphabetNumbers
wordOut = ""
wordOutForPrint = ""
curve = ""
lenS = 0
A = " ### ", "#   #", "#   #", "#####", "#   #", "#   #"
B = "#### ", "#   #", "#### ", "#   #", "#   #", "#### "
C = "#####", "#    ", "#    ", "#    ", "#    ", "#####"
D = "#### ", "#   #", "#   #", "#   #", "#   #", "#### "
E = "#####", "#    ", "#####", "#    ", "#    ", "#####"
F = "#####", "#    ", "#####", "#    ", "#    ", "#    "
G = "#####", "#    ", "#    ", "#  ##", "#   #", "#####"
H = "#   #", "#   #", "#####", "#   #", "#   #", "#   #"
I = "#####", "  #  ", "  #  ", "  #  ", "  #  ", "#####"
J = "    #", "    #", "    #", "    #", "#   #", " ### "
K = "#   #", "# ## ", "##   ", "# #  ", "#  # ", "#   #"
L = "#    ", "#    ", "#    ", "#    ", "#    ", "#####"
M = "#   #", "## ##", "# # #", "#   #", "#   #", "#   #"
N = "#   #", "##  #", "# # #", "#  ##", "#   #", "#   #"
O = "#####", "#   #", "#   #", "#   #", "#   #", "#####"
P = "#####", "#   #", "#####", "#    ", "#    ", "#    "
Q = "#### ", "#  # ", "#  # ", "# ## ", "#  # ", "#####"
R = "###  ", "#  # ", "#  # ", "###  ", "#  # ", "#   #"
S = "#####", "#    ", "#####", "    #", "    #", "#####"
T = "#####", "  #  ", "  #  ", "  #  ", "  #  ", "  #  "
U = "#   #", "#   #", "#   #", "#   #", "#   #", "#####"
V = "#   #", "#   #", "#   #", "#   #", " # # ", "  #  "
W = "#   #", "#   #", "#   #", "# # #", "# # #", " # # "
X = "#   #", " # # ", "  #  ", " # # ", "#   #", "#   #"
Y = "#   #", " # # ", "  #  ", "  #  ", "  #  ", "  #  "
Z = "#####", "   # ", "  #  ", " #   ", "#    ", "#####"
А = " ### ", "#   #", "#   #", "#####", "#   #", "#   #"
Б = "#####", "#    ", "#### ", "#   #", "#   #", "#####"
В = "#### ", "#   #", "#### ", "#   #", "#   #", "#### "
Г = "#####", "#    ", "#    ", "#    ", "#    ", "#    "
Д = " ### ", " # # ", " # # ", " # # ", "#####", "#   #"
Е = "#####", "#    ", "#####", "#    ", "#    ", "#####"
Ё = " # # ", "#####", "#    ", "#####", "#    ", "#####"
Ж = "# # #", " # # ", "  #  ", " # # ", "# # #", "#   #"
З = "#### ", "    #", "#### ", "    #", "    #", "#### "
И = "#   #", "#  ##", "# # #", "##  #", "#   #", "#   #"
Й = " ### ", "#   #", "#  ##", "# # #", "##  #", "#   #"
К = "#   #", "# ## ", "##   ", "# #  ", "#  # ", "#   #"
Л = "  #  ", " # # ", "#   #", "#   #", "#   #", "#   #"
М = "#   #", "## ##", "# # #", "#   #", "#   #", "#   #"
Н = "#   #", "#   #", "#####", "#   #", "#   #", "#   #"
О = "#####", "#   #", "#   #", "#   #", "#   #", "#####"
П = "#####", "#   #", "#   #", "#   #", "#   #", "#   #"
Р = "#####", "#   #", "#####", "#    ", "#    ", "#    "
С = "#####", "#    ", "#    ", "#    ", "#    ", "#####"
Т = "#####", "  #  ", "  #  ", "  #  ", "  #  ", "  #  "
У = "#   #", "#   #", " # # ", "  #  ", " #   ", "#    "
Ф = "#####", "# # #", "# # #", "#####", "  #  ", "  #  "
Х = "#   #", " # # ", "  #  ", " # # ", "#   #", "#   #"
Ц = "#  # ", "#  # ", "#  # ", "#  # ", "#### ", "    #"
Ч = "#   #", "#   #", "#   #", "#####", "    #", "    #"
Ш = "# # #", "# # #", "# # #", "# # #", "# # #", "#####"
Щ = "# # #", "# # #", "# # #", "# # #", "#####", "    #"
Ъ = "##   ", " #   ", " ### ", " #  #", " #  #", " ### "
Ы = "#   #", "#   #", "##  #", "# # #", "# # #", "##  #"
Ь = "#    ", "#    ", "#### ", "#   #", "#   #", "#### "
Э = "#### ", "    #", "#####", "    #", "    #", "#### "
Ю = "# ###", "# # #", "### #", "# # #", "# # #", "# ###"
Я = "  ###", " #  #", " #  #", "  ###", " #  #", "#   #"
space = "     ", "     ", "     ", "     ", "     ", "     "
tochka = "     ", "     ", "     ", "     ", "##   ", "##   "
zapyat = "     ", "     ", "     ", "     ", " #   ", "#    "
vopros = " ### ", "#   #", "   # ", "  #  ", "     ", "  #  "
voskl = "  #  ", "  #  ", "  #  ", "  #  ", "     ", "  #  "
tire = "     ", "     ", " ### ", "     ", "     ", "     "
plus = "     ", "  #  ", " ### ", "  #  ", "     ", "     "
ravno = "     ", "     ", " ### ", " ### ", "     ", "     "
umnog = "     ", " # # ", "  #  ", " # # ", "     ", "     "
delit = "   # ", "   # ", "  #  ", "  #  ", " #   ", " #   "
strLeft = "   # ", "  #  ", " #   ", "  #  ", "   # ", "     "
strRight = " #   ", "  #  ", "   # ", "  #  ", " #   ", "     "
zero =  "#####", "#   #", "#   #", "#   #", "#   #", "#####"
one = "    #", "   ##", "  # #", "    #", "    #", "    #"
two = " ####", "#   #", "   # ", "  #  ", " #   ", "#####"
three = "#### ", "    #", "#### ", "    #", "    #", "#### "
four = "  ## ", " # # ", "#  # ", "#### ", "   # ", "   # "
five = "#####", "#    ", "#### ", "    #", "    #", "#####"
six = "#####", "#    ", "#####", "#   #", "#   #", "#####"
seven = "#####", "    #", "   # ", "   # ", "  #  ", "  #  "
eight = "#####", "#   #", "#####", "#   #", "#   #", "#####"
nine = "#####", "#   #", "#####", "    #", "    #", "#####"
i_small = "  #  ", "     ", "  #  ", "  #  ", "  #  ", "  #  "

alp = A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я,space,tochka,zapyat,vopros,voskl,tire,plus,ravno,umnog,delit, strLeft, strRight,zero, one, two, three, four, five, six, seven, eight, nine, i_small


def generate_text(wordIn, curve, simbol):
    wordOut = ""
    wordOutForPrint = "" # used for generate text in print command
    for letterWeight in range(6):
        if curve == "<1>":
            wordOut = wordOut + " " * (6 - letterWeight)
            wordOutForPrint = wordOutForPrint + " " * (6 - letterWeight)
        elif curve == "<2>":
            wordOut = wordOut + " " * letterWeight
            wordOutForPrint = wordOutForPrint + " " * letterWeight

        for letterCount in range(len(wordIn)):
            wordOut = wordOut + alp[alphabet.index(wordIn[letterCount])][letterWeight] + " "
            wordOutForPrint = wordOutForPrint + alp[alphabet.index(wordIn[letterCount])][letterWeight] + " "
            if simbol == "<simbol>":
                wordOut = wordOut.replace('#', wordIn[letterCount].upper())
                wordOutForPrint = wordOutForPrint.replace('#', wordIn[letterCount].upper())

        # change simbols
        wordOut = wordOut.replace('#', simbol) + "\n"
        wordOutForPrint = wordOutForPrint.replace('#', simbol) + "\\n"
    return wordOut

def main():
    while True:
        wordIn = str(input("Write your text: \n>>> ")).lower()
        if wordIn == "":
            sys.exit()
        simbol = str(input("Simbol for write (write \"<simbol>\" for use default simbols):  \n>>> "))
        curve = str(input("Curve? (none, \'<1>\' or \'<2>\') \n>>> "))
        text_for_print = generate_text(wordIn, curve, simbol)
        print(text_for_print)

# main process
main()
