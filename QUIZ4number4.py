def adventure_game():
    print("Maligayang pagdating sa adventure game!")
    print("Ikaw at ang iyong mga kaibigan (Bryan, Jay Rey, Lawrence, Ran, at Renz) ay nawala sa isang mahiwagang kagubatan.")

    choice1 = input("May nakita kayong dalawang landas. Aling daan ang pipiliin mo? (kaliwa/kanan): ").lower()

    if choice1 == "kaliwa":
        choice2 = input("Nakakita ka ng isang ilog. Tatawid ka ba o hahanap ng tulay? (tawid/tulay): ").lower()
        if choice2 == "tawid":
            choice3 = input("Ang agos ay malakas! Sinubukan kang sagipin ni Bryan. Hawakan mo ba ang kamay niya? (oo/hindi): ").lower()
            if choice3 == "oo":
                print("Salamat kay Bryan! Nakatawid ka nang ligtas.")
                choice4 = input("May nakita kang lumang bahay. Papasukin mo ba ito? (oo/hindi): ").lower()
                if choice4 == "oo":
                    print("Napansin ni Renz na may mapa sa loob! May pag-asa kayong makalabas.")
                else:
                    print("Nagsimula nang dumilim at nawala kayo sa kagubatan.")
            else:
                print("Nahulog ka sa ilog at natangay ng agos!")
        else:
            print("Habang naghahanap ng tulay, napansin ni Jay Rey na may ahas sa paligid!")
            choice5 = input("Tumakbo ba kayo o dahan-dahang lumayo? (takbo/dahan): ").lower()
            if choice5 == "takbo":
                print("Nadapa si Lawrence at kinagat ng ahas!")
            else:
                print("Matagumpay kayong nakalayo.")

    elif choice1 == "kanan":
        choice6 = input("May nakita kayong kuweba. Papasukin mo ba ito? (oo/hindi): ").lower()
        if choice6 == "oo":
            choice7 = input("Madilim sa loob. Gagamitin mo ba ang flashlight ni Ran? (oo/hindi): ").lower()
            if choice7 == "oo":
                print("Napansin ni Ran ang isang lumang kayamanan!")
                choice8 = input("Kukunin mo ba ito o iiwan? (kunin/iwan): ").lower()
                if choice8 == "kunin":
                    print("Biglang bumagsak ang lupa at na-trap kayo sa loob!")
                else:
                    print("Lumabas kayo ng kuweba at natagpuan ang daan pauwi.")
            else:
                print("Dahil madilim, nadulas si Lawrence at natumba!")
        else:
            choice9 = input("Napansin ni Renz ang isang mahiwagang puno. Susuriin mo ba ito? (oo/hindi): ").lower()
            if choice9 == "oo":
                print("Biglang may lumabas na diwata at binigyan kayo ng gabay pauwi!")
            else:
                print("Naglakad pa kayo ng matagal ngunit hindi pa rin nakita ang daan.")

    else:
        print("Hindi mo napili ang alinman sa dalawang landas at nanatili kang naliligaw sa kagubatan.")

    print("Salamat sa paglalaro!")

adventure_game()