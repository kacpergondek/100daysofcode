print('''
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM `MM' VMMMMM
MMMMMV  MV  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  VM  MMMMMM
MMMMMM  M  mMMMMMMMMMMMMMMMMMMMV'"     "`VMMMMMMMMMMMMMM  MMMA `M  MM  MM
MM  VM  M  MMMMMMMMMMMMMMMV"                 "VMMMMMMMMM.  'MM  M  M' .MM
MM.  M  M  MV  VMMMMMMMV'                      "VMMMMMMMMM.  "  V  V .MMM
MMA  V  M  M' ,MMMMMMV'                          "VMMMMMMMM.  ..     mMMM
MMMA `     V  MMMMMM'                              `VMMMMMMm  "S"   mMMMM
MMMM  .,.,   AMMMMV                                 `VMMM"""   :   .MMMMM
MMMM  "B"   MMMMMV                                    M"      .'  .MMMMMM
MMMM   :   AV"  V                                     `   .mm.    MMMMMMM
MMMM.  `.                                              ..MMMMMm   MMMMMMM
MMMMM.. .  .mMMV  .                                   . VMMMMMMA   VMMMMM
MMMMMM  AMMMMMM'  *         <^@^>        <==>        .* 'MMMMMMm    MMMMM
MMMMM'  MMMMMMV  .I                                 .a@. V'"MMMMA    MMMM
MMMMM   MMMMMM(  a@:.                             .' @@! .   "MMMm    MMM
MMMM'   MMMV""'  !@a :.                         .';.a@@R ,             MM
MMMV    MV"   :  :@@@: :.                     .:  a@@@@! ..............mM
MMM'          .  `@@@@ : `...             ..:' : a@@@@@' MMMMMMMMMMMMMMMM
MMM  ..........   @@@@@a  :  :'`:`------':  :  a@@@@@@@  MMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMA   `@@@@@@@a  :  :   ::   :  a@@@@@@@@@' :MMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMM.   `@@@@@@@@@@aaA. .;|. .Aaa@@@@@@@@@' .AMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM.   `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   mMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMM.    @@@@@@@@@@@"oOo.oOOo"@@@@@@@'   mMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMm    `@@@@@@@"OOOOOOxOOOOO"@@@V    mMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMA.     `@@@"OOOOOOOOxOOOOO"@'   .AMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMA.     ""V@@AOOOOOOxOOOOO.  .AMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMm.       `OOOOOOOxXOOOo.mMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMAm..   `OOOOOOoxOOOO:MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMA`OOOOOOOxOOOO:MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMA`OOOOOOxOOOO;MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMA`OOOOOOOOO;AMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMA`OOOOOO;AMMMMMMMMMMMMMMMMMMMMMMMMMMM
WIZMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmmmmmMMMMMMMMMMMMMMMMMMMMMMMMM*MJJ
''')
print(
  'You see a spooky ghost in front of you, which seems hostile. What is your course of action?'
)
answer1 = input(
  'Do you either Fight[F], Run[R], or attempt to Talk to it[T]? \n').lower()

if answer1 == "f" or answer1 == "t":
  print("The moment you approach the ghost, it kills you. You have died.")

if answer1 == "r":
  print(
    'The ghost is right behind you, but you see an abandoned house in front of you.'
  )
  answer2 = input('Do you Enter[E] it, or do you Run[R] further?\n').lower()
  if answer2 == "r":
    print("You kept running, but the ghost caught up to you. You have died.")
  elif answer2 == "e":
    print(
      "You entered the house, \nand you see a vaccum cleaner, a gun, and a book."
    )
    answer3 = input(
      "Which one do you use to defend yourself? \nA vaccum cleaner[V], A gun [G] or a book [B]\n"
    ).lower()

    if answer3 == "b" or answer3 == "g":
      print(
        "Clearly, you have no self-preservation skills, as the ghost makes quick \nwork of you. You have died."
      )
    elif answer3 == "v":
      print(
        "Somehow, the vaccum cleaner sucks up the ghost, and you live to see another day. \n You have won."
      )
