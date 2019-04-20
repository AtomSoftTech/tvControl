from pynput.keyboard import Key, Listener, KeyCode
import requests

lnkMain = "http://192.168.1.2:8060/"
lnkHome = "keypress/home"
lnkPower = "keypress/Power"
lnkUp = "keypress/Up"
lnkDown = "keypress/Down"
lnkLeft = "keypress/Left"
lnkRight = "keypress/Right"
lnkSelect = "keypress/Select"
lnkEnter = "keypress/Enter"
lnkHBO = "launch/61322"
lnkHulu = "launch/2285"
lnkNetlix = "launch/12"
lnkSpotify = "launch/19977"
lnkYoutube = "launch/837"
lnkVolUp =  "keypress/VolumeUp"
lnkVolDown =  "keypress/VolumeDown"
lnkPlay =  "keypress/Play"
lnkMute =  "keypress/VolumeMute"
lnkFWD =  "keypress/Fwd"
lnkRev =  "keypress/Rev"
lnkBackSpace = "keypress/Backspace"
lnkText = "keypress/Lit_"
lnkNav = ""

class MyException (Exception) : pass

def on_press(key):
    print ("\r")
    #print('{0} pressed'.format(key))


def on_release(key):

  temp = format(key)

  isReady = 0

  if temp == "Key.shift":
    return

  print(temp)

  if temp.find("269025051") > 0 :
    lnkNav = lnkMain + lnkPower
    isReady = 1
  if temp.find("269025153") > 0 :
    lnkNav = lnkMain + lnkYoutube
    isReady = 1
  if temp.find("269025043") > 0 :
    lnkNav = lnkMain + lnkVolUp
    isReady = 1
  if temp.find("269025041") > 0:
    lnkNav = lnkMain + lnkVolDown
    isReady = 1  
  if temp.find("269025046") > 0 :
    lnkNav = lnkMain + lnkRev
    isReady = 1  
  if temp.find("269025047") > 0:
    lnkNav = lnkMain + lnkFwd
    isReady = 1  
  if temp.find("269025044") > 0:
    lnkNav = lnkMain + lnkPlay
    isReady = 1  
  if temp.find("269025042") > 0:
    lnkNav = lnkMain + lnkMute
    isReady = 1  
  if temp.find("269025117") > 0:
    lnkNav = lnkMain + lnkHome
    isReady = 1  
  if temp == "Key.up": 
    lnkNav = lnkMain + lnkUp
    isReady = 1
  if temp == "Key.down": 
    lnkNav = lnkMain + lnkDown
    isReady = 1
  if temp == "Key.left": 
    lnkNav = lnkMain + lnkLeft
    isReady = 1
  if temp == "Key.right": 
    lnkNav = lnkMain + lnkRight
    isReady = 1
  if temp == "Key.enter": 
    lnkNav = lnkMain + lnkSelect
    isReady = 1
  if temp == "Key.page_down": 
    lnkNav = lnkMain + lnkEnter
    isReady = 1
  if temp == "Key.f1": 
    lnkNav = lnkMain + lnkNetlix
    isReady = 1
  if temp == "Key.f2": 
    lnkNav = lnkMain + lnkHulu
    isReady = 1
  if temp == "Key.f3": 
    lnkNav = lnkMain + lnkHBO
    isReady = 1
  if temp == "Key.f4": 
    lnkNav = lnkMain + lnkSpotify
    isReady = 1
  if temp == "Key.f5": 
    lnkNav = lnkMain + lnkYoutube
    isReady = 1
  if temp == "Key.space": 
    lnkNav = lnkMain + lnkText + " "
    isReady = 1
  if temp == "Key.backspace": 
    lnkNav = lnkMain + lnkBackSpace
    isReady = 1

  if isReady == 0:
    if temp.find("a") > 0:
      lnkNav = lnkMain + lnkText + "a"
      isReady = 1  
    if temp.find("b") > 0:
      lnkNav = lnkMain + lnkText + "b"
      isReady = 1  
    if temp.find("c") > 0:
      lnkNav = lnkMain + lnkText + "c"
      isReady = 1  
    if temp.find("d") > 0:
      lnkNav = lnkMain + lnkText + "d"
      isReady = 1  
    if temp.find("e") > 0:
      lnkNav = lnkMain + lnkText + "e"
      isReady = 1  
    if temp.find("f") > 0:
      lnkNav = lnkMain + lnkText + "f"
      isReady = 1  
    if temp.find("g") > 0:
      lnkNav = lnkMain + lnkText + "g"
      isReady = 1  
    if temp.find("h") > 0:
      lnkNav = lnkMain + lnkText + "h"
      isReady = 1  
    if temp.find("i") > 0:
      lnkNav = lnkMain + lnkText + "i"
      isReady = 1  
    if temp.find("j") > 0:
      lnkNav = lnkMain + lnkText + "j"
      isReady = 1  
    if temp.find("k") > 0:
      lnkNav = lnkMain + lnkText + "k"
      isReady = 1  
    if temp.find("l") > 0:
      lnkNav = lnkMain + lnkText + "l"
      isReady = 1  
    if temp.find("m") > 0:
      lnkNav = lnkMain + lnkText + "m"
      isReady = 1  
    if temp.find("n") > 0:
      lnkNav = lnkMain + lnkText + "n"
      isReady = 1  
    if temp.find("o") > 0:
      lnkNav = lnkMain + lnkText + "o"
      isReady = 1  
    if temp.find("p") > 0:
      lnkNav = lnkMain + lnkText + "p"
      isReady = 1  
    if temp.find("q") > 0:
      lnkNav = lnkMain + lnkText + "q"
      isReady = 1  
    if temp.find("r") > 0:
      lnkNav = lnkMain + lnkText + "r"
      isReady = 1  
    if temp.find("s") > 0:
      lnkNav = lnkMain + lnkText + "s"
      isReady = 1  
    if temp.find("t") > 0:
      lnkNav = lnkMain + lnkText + "t"
      isReady = 1  
    if temp.find("u") > 0:
      lnkNav = lnkMain + lnkText + "u"
      isReady = 1  
    if temp.find("v") > 0:
      lnkNav = lnkMain + lnkText + "v"
      isReady = 1  
    if temp.find("w") > 0:
      lnkNav = lnkMain + lnkText + "w"
      isReady = 1  
    if temp.find("x") > 0:
      lnkNav = lnkMain + lnkText + "x"
      isReady = 1  
    if temp.find("y") > 0:
      lnkNav = lnkMain + lnkText + "y"
      isReady = 1  
    if temp.find("z") > 0:
      lnkNav = lnkMain + lnkText + "z"
      isReady = 1
      
  if isReady == 0:
    if temp.find("A") > 0:
      lnkNav = lnkMain + lnkText + "A"
      isReady = 1
    if temp.find("B") > 0:
      lnkNav = lnkMain + lnkText + "B"
      isReady = 1
    if temp.find("C") > 0:
      lnkNav = lnkMain + lnkText + "C"
      isReady = 1
    if temp.find("D") > 0:
      lnkNav = lnkMain + lnkText + "D"
      isReady = 1
    if temp.find("E") > 0:
      lnkNav = lnkMain + lnkText + "E"
      isReady = 1
    if temp.find("F") > 0:
      lnkNav = lnkMain + lnkText + "F"
      isReady = 1
    if temp.find("G") > 0:
      lnkNav = lnkMain + lnkText + "G"
      isReady = 1
    if temp.find("H") > 0:
      lnkNav = lnkMain + lnkText + "H"
      isReady = 1
    if temp.find("I") > 0:
      lnkNav = lnkMain + lnkText + "I"
      isReady = 1
    if temp.find("J") > 0:
      lnkNav = lnkMain + lnkText + "J"
      isReady = 1
    if temp.find("K") > 0:
      lnkNav = lnkMain + lnkText + "K"
      isReady = 1
    if temp.find("L") > 0:
      lnkNav = lnkMain + lnkText + "L"
      isReady = 1
    if temp.find("M") > 0:
      lnkNav = lnkMain + lnkText + "M"
      isReady = 1
    if temp.find("N") > 0:
      lnkNav = lnkMain + lnkText + "N"
      isReady = 1
    if temp.find("O") > 0:
      lnkNav = lnkMain + lnkText + "O"
      isReady = 1
    if temp.find("P") > 0:
      lnkNav = lnkMain + lnkText + "P"
      isReady = 1
    if temp.find("Q") > 0:
      lnkNav = lnkMain + lnkText + "Q"
      isReady = 1
    if temp.find("R") > 0:
      lnkNav = lnkMain + lnkText + "R"
      isReady = 1
    if temp.find("S") > 0:
      lnkNav = lnkMain + lnkText + "S"
      isReady = 1
    if temp.find("T") > 0:
      lnkNav = lnkMain + lnkText + "T"
      isReady = 1
    if temp.find("U") > 0:
      lnkNav = lnkMain + lnkText + "U"
      isReady = 1
    if temp.find("V") > 0:
      lnkNav = lnkMain + lnkText + "V"
      isReady = 1
    if temp.find("W") > 0:
      lnkNav = lnkMain + lnkText + "W"
      isReady = 1
    if temp.find("X") > 0:
      lnkNav = lnkMain + lnkText + "X"
      isReady = 1
    if temp.find("Y") > 0:
      lnkNav = lnkMain + lnkText + "Y"
      isReady = 1
    if temp.find("Z") > 0:
      lnkNav = lnkMain + lnkText + "Z"
      isReady = 1

  if isReady == 0:
    if temp.find(",") > 0:
      lnkNav = lnkMain + lnkText + ","
      isReady = 1
    if temp.find("<") > 0:
      lnkNav = lnkMain + lnkText + "<"
      isReady = 1
    if temp.find(".") > 0:
      lnkNav = lnkMain + lnkText + "."
      isReady = 1
    if temp.find(">") > 0:
      lnkNav = lnkMain + lnkText + ">"
      isReady = 1
    if temp.find("/") > 0:
      lnkNav = lnkMain + lnkText + "/"
      isReady = 1
    if temp.find("?") > 0:
      lnkNav = lnkMain + lnkText + "?"
      isReady = 1
    if temp.find(";") > 0:
      lnkNav = lnkMain + lnkText + ";"
      isReady = 1
    if temp.find(":") > 0:
      lnkNav = lnkMain + lnkText + ":"
      isReady = 1
    if temp.find("'") > 0:
      lnkNav = lnkMain + lnkText + "'"
      isReady = 1
    if temp.find('"') > 0:
      lnkNav = lnkMain + lnkText + '"'
      isReady = 1
    if temp.find("[") > 0:
      lnkNav = lnkMain + lnkText + "["
      isReady = 1
    if temp.find("{") > 0:
      lnkNav = lnkMain + lnkText + "{"
      isReady = 1
    if temp.find("]") > 0:
      lnkNav = lnkMain + lnkText + "]"
      isReady = 1
    if temp.find("}") > 0:
      lnkNav = lnkMain + lnkText + "}"
      isReady = 1
    if temp.find("\\") > 0:
      lnkNav = lnkMain + lnkText + "\\"
      isReady = 1
    if temp.find("|") > 0:
      lnkNav = lnkMain + lnkText + "|"
      isReady = 1
    if temp.find("`") > 0:
      lnkNav = lnkMain + lnkText + "`"
      isReady = 1
    if temp.find("~") > 0:
      lnkNav = lnkMain + lnkText + "~"
      isReady = 1
    if temp.find("!") > 0:
      lnkNav = lnkMain + lnkText + "!"
      isReady = 1
    if temp.find("@") > 0:
      lnkNav = lnkMain + lnkText + "@"
      isReady = 1
    if temp.find("#") > 0:
      lnkNav = lnkMain + lnkText + "#"
      isReady = 1
    if temp.find("$") > 0:
      lnkNav = lnkMain + lnkText + "$"
      isReady = 1
    if temp.find("%") > 0:
      lnkNav = lnkMain + lnkText + "%"
      isReady = 1
    if temp.find("^") > 0:
      lnkNav = lnkMain + lnkText + "^"
      isReady = 1
    if temp.find("&") > 0:
      lnkNav = lnkMain + lnkText + "&"
      isReady = 1
    if temp.find("*") > 0:
      lnkNav = lnkMain + lnkText + "*"
      isReady = 1
    if temp.find("(") > 0:
      lnkNav = lnkMain + lnkText + "("
      isReady = 1
    if temp.find(")") > 0:
      lnkNav = lnkMain + lnkText + ")"
      isReady = 1
    if temp.find("-") > 0:
      lnkNav = lnkMain + lnkText + "-"
      isReady = 1
    if temp.find("_") > 0:
      lnkNav = lnkMain + lnkText + "_"
      isReady = 1
    if temp.find("=") > 0:
      lnkNav = lnkMain + lnkText + "="
      isReady = 1
    if temp.find("+") > 0:
      lnkNav = lnkMain + lnkText + "+"
      isReady = 1

  #print('{0} is link'.format(lnkNav))
  if isReady == 1:
    r = requests.post(url = lnkNav, data = "")

  if temp == "Key.esc":
  # Stop listener
    return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    try:
      listener.join()
            
    except MyException as e:
      print('{0} was error'.format(e.args[0]))


    
