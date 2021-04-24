import random

class Player:

    def __init__(self, nm):
        self.name=nm
        self.points=0
        self.desk = []
        self.opdesk = []
        self.tozdik = 9
        self.optozdik = 9
        for i in range(9):
            self.desk.append(9)
            self.opdesk.append(9)

    def reprint(self):
        s = ''
        for i in range(9):
            s = s + str(self.desk[8 - i])
            s = s + ' '
        s = s + '<= ' + self.name
        return s

    def print(self):
        s = ''
        for i in range(9):
            s = s + str(self.desk[i])
            s = s + ' '
        s = s + '<= ' + self.name
        return s

    def move(self):
        l = True
        for i in range(9):
            if self.optozdik != i and self.desk[i] > 0 :
                l=False
                break
        if l:
            return 9
        else:
            print(self.name + ', please make a move:')
            mv=int(input())
            while self.optozdik == mv - 1 or mv < 1 or mv > 9 or self.desk[mv - 1] == 0:
                print('This move is incorrect:')
                print('Please make a move:')
                mv=int(input())
            return mv - 1


class Bot(Player):
    
    def __init__(self, lv):
        while lv < 0 or lv > 4:
            print('Level cannot be less than 0 or bigger than 4, please input correct data:')
            lv=int(input())
        Player.__init__(self, 'Bob')
        self.level=lv

    def __move0(self):
        r=random.randint(0, 8)
        while self.optozdik == r or self.desk[r]==0:
            r=random.randint(0, 8)
        return r

    def __move1(self):
        sav = self.tozdik
        sac = self.optozdik
        deff = 163
        attc = 0
        position = 0
        cattc = 0
        cdeff = 0
        if self.tozdik == 9:
            mak = False
        else:
            mak =True
        if self.optozdik == 9:
            ak = False
        else:
            ak = True
        changes = []
        maket = False
        akm = False
        maxk = 0
        for i in range(18):
            changes.append(0)
        for i in range(9):
            self.tozdik = sav
            self.optozdik = sac 
            if i != self.optozdik and self.desk[i] > 0:
                cattc = 0
                cdeff = 0
                crattc = 0
                crdeff = 0
                if self.tozdik == 9:
                    maket = False
                else:
                    maket =True
                if self.optozdik == 9:
                    akm = False
                else:
                    akm = True
                cmaxk = self.desk[i]
                for j in range(18):
                    changes[j] = 0
                if self.desk[i] == 1:
                    changes[i] = -1
                    changes[i + 1] = 1
                    if i == 8 :
                        if self.tozdik == 0:
                            cattc = 1
                        elif self.opdesk[0] % 2 == 1:
                            cattc = self.opdesk[0] + 1
                            changes[9] = 0 - self.opdesk[0]
                        elif self.opdesk[0] == 2:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                cattc = cattc + 3
                                changes[9] = 0 - self.opdesk[0]
                                maket = True
                                
                else:
                    changes[i] = 1 - self.desk[i]
                    moves = self.desk[i] - 1
                    cr = i + 1
                    while moves > 0:
                        while moves > 0 and cr < 9:
                            changes[cr] = changes[cr] + 1
                            if cr == self.optozdik:
                                cdeff = cdeff + 1
                            moves = moves - 1
                            cr = cr + 1
                        while moves > 0 and cr < 18:
                            changes[cr] = changes[cr] + 1
                            if cr - 9 == self.tozdik:
                                cattc = cattc + 1
                            moves = moves - 1
                            cr = cr + 1
                        if moves == 0:
                            cr = cr - 1
                            break
                        cr = 0
                    if cr > 8 and cr - 9 != self.tozdik:
                        if (self.opdesk[cr - 9] + changes[cr]) % 2 == 0:
                            cattc = cattc + self.opdesk[cr - 9] + changes[cr]
                            changes[cr] = 0 - self.opdesk[cr - 9]
                        elif (self.opdesk[cr - 9] + changes[cr]) == 3:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                maket = True
                                cattc = cattc + 3
                                changes[cr] = 0 - self.opdesk[cr - 9]
                                self.tozdik = cr - 9
                crattc = cattc
                crdeff = cdeff
                for j in range(9):
                    if j != self.tozdik and self.opdesk[j] > 0:
                        if self.opdesk[j] == 1:
                            if j == 8:
                                if self.optozdik == 0:
                                    cdeff = cdeff + 1
                                elif (changes[0]+self.desk[0]) % 2 == 0:
                                    cdeff = cdeff + changes[0]+self.desk[0]
                                elif (changes[0]+self.desk[0]) == 3:
                                    akm = True
                                    cdeff = cdeff + 3
                        else:
                            changes[j + 9] = 1 - self.opdesk[j]
                            moves = self.opdesk[j] - 1
                            cr = j + 10
                            while moves > 0:
                                while moves > 0 and cr < 18:
                                    changes[cr] = changes[cr] + 1
                                    if cr - 9 == self.tozdik:
                                        cattc = cattc + 1
                                    moves = moves - 1
                                    cr = cr + 1
                                if moves == 0:
                                    cr = cr - 1
                                    break
                                cr = 0
                                while moves > 0 and cr < 9:
                                    changes[cr] = changes[cr] + 1
                                    if cr == self.optozdik:
                                        cdeff = cdeff + 1
                                    moves = moves - 1
                                    cr = cr + 1
                            if cr <= 8 and cr != self.optozdik:
                                if (self.desk[cr] + changes[cr]) % 2 == 0:
                                    cdeff = cdeff + self.desk[cr] + changes[cr]
                                elif (self.desk[cr] + changes[cr]) == 3:
                                    if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                        akm = True
                                        cdeff = cdeff + 3
                        if cdeff < deff:
                            deff = cdeff
                            attc = cattc
                            mak = maket
                            ak = akm
                            position = i
                            maxk = cmaxk
                        elif cdeff == deff:
                            if cattc > attc:
                                deff = cdeff
                                attc = cattc
                                mak = maket
                                ak = akm
                                position = i
                                maxk = cmaxk
                            elif cattc == attc:
                                if maket == True and mak == False:
                                    deff = cdeff
                                    attc = cattc
                                    mak = maket
                                    ak = akm
                                    position = i
                                    maxk = cmaxk
                                elif maket == mak:
                                    if ak == True and akm == False:
                                        deff = cdeff
                                        attc = cattc
                                        mak = maket
                                        ak = akm
                                        position = i
                                        maxk = cmaxk
                                    elif ak == akm:
                                        if cmaxk > maxk:
                                            deff = cdeff
                                            attc = cattc
                                            mak = maket
                                            ak = akm
                                            position = i
                                            maxk =cmaxk
                        cattc = crattc
                        cdeff = crdeff 
        return position

    def __move2(self):
        sav = self.tozdik
        sac = self.optozdik
        deff = 163
        attc = 0
        position = 0
        cattc = 0
        cdeff = 0
        if self.tozdik == 9:
            mak = False
        else:
            mak =True
        if self.optozdik == 9:
            ak = False
        else:
            ak = True
        changes = []
        maket = False
        akm = False
        maxk = 0
        for i in range(18):
            changes.append(0)
        for i in range(9):
            self.tozdik = sav
            self.optozdik = sac 
            if i != self.optozdik and self.desk[i] > 0:
                cattc = 0
                cdeff = 0
                crattc = 0
                crdeff = 0
                if self.tozdik == 9:
                    maket = False
                else:
                    maket =True
                if self.optozdik == 9:
                    akm = False
                else:
                    akm = True
                cmaxk = self.desk[i]
                for j in range(18):
                    changes[j] = 0
                if self.desk[i] == 1:
                    changes[i] = -1
                    changes[i + 1] = 1
                    if i == 8 :
                        if self.tozdik == 0:
                            cattc = 1
                        elif self.opdesk[0] % 2 == 1:
                            cattc = self.opdesk[0] + 1
                            changes[9] = 0 - self.opdesk[0]
                        elif self.opdesk[0] == 2:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                cattc = cattc + 3
                                changes[9] = 0 - self.opdesk[0]
                                maket = True
                                
                else:
                    changes[i] = 1 - self.desk[i]
                    moves = self.desk[i] - 1
                    cr = i + 1
                    while moves > 0:
                        while moves > 0 and cr < 9:
                            changes[cr] = changes[cr] + 1
                            if cr == self.optozdik:
                                cdeff = cdeff + 1
                            moves = moves - 1
                            cr = cr + 1
                        while moves > 0 and cr < 18:
                            changes[cr] = changes[cr] + 1
                            if cr - 9 == self.tozdik:
                                cattc = cattc + 1
                            moves = moves - 1
                            cr = cr + 1
                        if moves == 0:
                            cr = cr - 1
                            break
                        cr = 0
                    if cr > 8 and cr - 9 != self.tozdik:
                        if (self.opdesk[cr - 9] + changes[cr]) % 2 == 0:
                            cattc = cattc + self.opdesk[cr - 9] + changes[cr]
                            changes[cr] = 0 - self.opdesk[cr - 9]
                        elif (self.opdesk[cr - 9] + changes[cr]) == 3:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                maket = True
                                cattc = cattc + 3
                                changes[cr] = 0 - self.opdesk[cr - 9]
                                self.tozdik = cr - 9
                crattc = cattc
                crdeff = cdeff
                for j in range(9):
                    if j != self.tozdik and self.opdesk[j] > 0:
                        if self.opdesk[j] == 1:
                            if j == 8:
                                if self.optozdik == 0:
                                    cdeff = cdeff + 1
                                elif (changes[0]+self.desk[0]) % 2 == 0:
                                    cdeff = cdeff + changes[0]+self.desk[0]
                                elif (changes[0]+self.desk[0]) == 3:
                                    akm = True
                                    cdeff = cdeff + 3
                        else:
                            changes[j + 9] = 1 - self.opdesk[j]
                            moves = self.opdesk[j] - 1
                            cr = j + 10
                            while moves > 0:
                                while moves > 0 and cr < 18:
                                    changes[cr] = changes[cr] + 1
                                    if cr - 9 == self.tozdik:
                                        cattc = cattc + 1
                                    moves = moves - 1
                                    cr = cr + 1
                                if moves == 0:
                                    cr = cr - 1
                                    break
                                cr = 0
                                while moves > 0 and cr < 9:
                                    changes[cr] = changes[cr] + 1
                                    if cr == self.optozdik:
                                        cdeff = cdeff + 1
                                    moves = moves - 1
                                    cr = cr + 1
                            if cr <= 8 and cr != self.optozdik:
                                if (self.desk[cr] + changes[cr]) % 2 == 0:
                                    cdeff = cdeff + self.desk[cr] + changes[cr]
                                elif (self.desk[cr] + changes[cr]) == 3:
                                    if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                        akm = True
                                        cdeff = cdeff + 3
                        if cattc - cdeff > attc - deff:
                            deff = cdeff
                            attc = cattc
                            mak = maket
                            ak = akm
                            position = i
                            maxk = cmaxk
                        elif cattc - cdeff == attc - deff:
                            if cdeff < deff:
                                deff = cdeff
                                attc = cattc
                                mak = maket
                                ak = akm
                                position = i
                                maxk = cmaxk
                            elif cdeff == deff:
                                if cattc > attc:
                                    deff = cdeff
                                    attc = cattc
                                    mak = maket
                                    ak = akm
                                    position = i
                                    maxk = cmaxk
                                elif cattc == attc:
                                    if maket == True and mak == False:
                                        deff = cdeff
                                        attc = cattc
                                        mak = maket
                                        ak = akm
                                        position = i
                                        maxk = cmaxk
                                    elif maket == mak:
                                        if ak == True and akm == False:
                                            deff = cdeff
                                            attc = cattc
                                            mak = maket
                                            ak = akm
                                            position = i
                                            maxk = cmaxk
                                        elif ak == akm:
                                            if cmaxk > maxk:
                                                deff = cdeff
                                                attc = cattc
                                                mak = maket
                                                ak = akm
                                                position = i
                                                maxk =cmaxk
                        cattc = crattc
                        cdeff = crdeff 
        return position

    def __move4(self):
        sav = self.tozdik
        sac = self.optozdik
        deff = 163
        attc = 0
        position = 0
        cattc = 0
        cdeff = 0
        if self.tozdik == 9:
            mak = False
        else:
            mak =True
        if self.optozdik == 9:
            ak = False
        else:
            ak = True
        changes = []
        maket = False
        akm = False
        maxk = 0
        for i in range(18):
            changes.append(0)
        for i in range(9):
            self.tozdik = sav
            self.optozdik = sac 
            if i != self.optozdik and self.desk[i] > 0:
                cattc = 0
                cdeff = 0
                crattc = 0
                crdeff = 0
                if self.tozdik == 9:
                    maket = False
                else:
                    maket =True
                if self.optozdik == 9:
                    akm = False
                else:
                    akm = True
                cmaxk = self.desk[i]
                for j in range(18):
                    changes[j] = 0
                if self.desk[i] == 1:
                    changes[i] = -1
                    changes[i + 1] = 1
                    if i == 8 :
                        if self.tozdik == 0:
                            cattc = 1
                        elif self.opdesk[0] % 2 == 1:
                            cattc = self.opdesk[0] + 1
                            changes[9] = 0 - self.opdesk[0]
                        elif self.opdesk[0] == 2:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                cattc = cattc + 3
                                changes[9] = 0 - self.opdesk[0]
                                maket = True
                                
                else:
                    changes[i] = 1 - self.desk[i]
                    moves = self.desk[i] - 1
                    cr = i + 1
                    while moves > 0:
                        while moves > 0 and cr < 9:
                            changes[cr] = changes[cr] + 1
                            if cr == self.optozdik:
                                cdeff = cdeff + 1
                            moves = moves - 1
                            cr = cr + 1
                        while moves > 0 and cr < 18:
                            changes[cr] = changes[cr] + 1
                            if cr - 9 == self.tozdik:
                                cattc = cattc + 1
                            moves = moves - 1
                            cr = cr + 1
                        if moves == 0:
                            cr = cr - 1
                            break
                        cr = 0
                    if cr > 8 and cr - 9 != self.tozdik:
                        if (self.opdesk[cr - 9] + changes[cr]) % 2 == 0:
                            cattc = cattc + self.opdesk[cr - 9] + changes[cr]
                            changes[cr] = 0 - self.opdesk[cr - 9]
                        elif (self.opdesk[cr - 9] + changes[cr]) == 3:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                maket = True
                                cattc = cattc + 3
                                changes[cr] = 0 - self.opdesk[cr - 9]
                                self.tozdik = cr - 9
                crattc = cattc
                crdeff = cdeff
                for j in range(9):
                    if j != self.tozdik and self.opdesk[j] > 0:
                        if self.opdesk[j] == 1:
                            if j == 8:
                                if self.optozdik == 0:
                                    cdeff = cdeff + 1
                                elif (changes[0]+self.desk[0]) % 2 == 0:
                                    cdeff = cdeff + changes[0]+self.desk[0]
                                elif (changes[0]+self.desk[0]) == 3:
                                    akm = True
                                    cdeff = cdeff + 3
                        else:
                            changes[j + 9] = 1 - self.opdesk[j]
                            moves = self.opdesk[j] - 1
                            cr = j + 10
                            while moves > 0:
                                while moves > 0 and cr < 18:
                                    changes[cr] = changes[cr] + 1
                                    if cr - 9 == self.tozdik:
                                        cattc = cattc + 1
                                    moves = moves - 1
                                    cr = cr + 1
                                if moves == 0:
                                    cr = cr - 1
                                    break
                                cr = 0
                                while moves > 0 and cr < 9:
                                    changes[cr] = changes[cr] + 1
                                    if cr == self.optozdik:
                                        cdeff = cdeff + 1
                                    moves = moves - 1
                                    cr = cr + 1
                            if cr <= 8 and cr != self.optozdik:
                                if (self.desk[cr] + changes[cr]) % 2 == 0:
                                    cdeff = cdeff + self.desk[cr] + changes[cr]
                                elif (self.desk[cr] + changes[cr]) == 3:
                                    if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                        akm = True
                                        cdeff = cdeff + 3
                        if cattc - cdeff > attc - deff:
                            deff = cdeff
                            attc = cattc
                            mak = maket
                            ak = akm
                            position = i
                            maxk = cmaxk
                        elif cattc - cdeff == attc - deff:
                            if cattc > attc:
                                deff = cdeff
                                attc = cattc
                                mak = maket
                                ak = akm
                                position = i
                                maxk = cmaxk
                            elif cattc == attc:
                                if cdeff < deff:
                                    deff = cdeff
                                    attc = cattc
                                    mak = maket
                                    ak = akm
                                    position = i
                                    maxk = cmaxk
                                elif cdeff == deff:
                                    if maket == True and mak == False:
                                        deff = cdeff
                                        attc = cattc
                                        mak = maket
                                        ak = akm
                                        position = i
                                        maxk = cmaxk
                                    elif maket == mak:
                                        if ak == True and akm == False:
                                            deff = cdeff
                                            attc = cattc
                                            mak = maket
                                            ak = akm
                                            position = i
                                            maxk = cmaxk
                                        elif ak == akm:
                                            if cmaxk > maxk:
                                                deff = cdeff
                                                attc = cattc
                                                mak = maket
                                                ak = akm
                                                position = i
                                                maxk =cmaxk
                        cattc = crattc
                        cdeff = crdeff 
        return position

    def __move3(self):
        sav = self.tozdik
        sac = self.optozdik
        deff = 163
        attc = 0
        position = 0
        cattc = 0
        cdeff = 0
        if self.tozdik == 9:
            mak = False
        else:
            mak =True
        if self.optozdik == 9:
            ak = False
        else:
            ak = True
        changes = []
        maket = False
        akm = False
        maxk = 0
        for i in range(18):
            changes.append(0)
        for i in range(9):
            self.tozdik = sav
            self.optozdik = sac 
            if i != self.optozdik and self.desk[i] > 0:
                cattc = 0
                cdeff = 0
                crattc = 0
                crdeff = 0
                if self.tozdik == 9:
                    maket = False
                else:
                    maket =True
                if self.optozdik == 9:
                    akm = False
                else:
                    akm = True
                cmaxk = self.desk[i]
                for j in range(18):
                    changes[j] = 0
                if self.desk[i] == 1:
                    changes[i] = -1
                    changes[i + 1] = 1
                    if i == 8 :
                        if self.tozdik == 0:
                            cattc = 1
                        elif self.opdesk[0] % 2 == 1:
                            cattc = self.opdesk[0] + 1
                            changes[9] = 0 - self.opdesk[0]
                        elif self.opdesk[0] == 2:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                cattc = cattc + 3
                                changes[9] = 0 - self.opdesk[0]
                                maket = True
                                
                else:
                    changes[i] = 1 - self.desk[i]
                    moves = self.desk[i] - 1
                    cr = i + 1
                    while moves > 0:
                        while moves > 0 and cr < 9:
                            changes[cr] = changes[cr] + 1
                            if cr == self.optozdik:
                                cdeff = cdeff + 1
                            moves = moves - 1
                            cr = cr + 1
                        while moves > 0 and cr < 18:
                            changes[cr] = changes[cr] + 1
                            if cr - 9 == self.tozdik:
                                cattc = cattc + 1
                            moves = moves - 1
                            cr = cr + 1
                        if moves == 0:
                            cr = cr - 1
                            break
                        cr = 0
                    if cr > 8 and cr - 9 != self.tozdik:
                        if (self.opdesk[cr - 9] + changes[cr]) % 2 == 0:
                            cattc = cattc + self.opdesk[cr - 9] + changes[cr]
                            changes[cr] = 0 - self.opdesk[cr - 9]
                        elif (self.opdesk[cr - 9] + changes[cr]) == 3:
                            if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                maket = True
                                cattc = cattc + 3
                                changes[cr] = 0 - self.opdesk[cr - 9]
                                self.tozdik = cr - 9
                crattc = cattc
                crdeff = cdeff
                for j in range(9):
                    if j != self.tozdik and self.opdesk[j] > 0:
                        if self.opdesk[j] == 1:
                            if j == 8:
                                if self.optozdik == 0:
                                    cdeff = cdeff + 1
                                elif (changes[0]+self.desk[0]) % 2 == 0:
                                    cdeff = cdeff + changes[0]+self.desk[0]
                                elif (changes[0]+self.desk[0]) == 3:
                                    akm = True
                                    cdeff = cdeff + 3
                        else:
                            changes[j + 9] = 1 - self.opdesk[j]
                            moves = self.opdesk[j] - 1
                            cr = j + 10
                            while moves > 0:
                                while moves > 0 and cr < 18:
                                    changes[cr] = changes[cr] + 1
                                    if cr - 9 == self.tozdik:
                                        cattc = cattc + 1
                                    moves = moves - 1
                                    cr = cr + 1
                                if moves == 0:
                                    cr = cr - 1
                                    break
                                cr = 0
                                while moves > 0 and cr < 9:
                                    changes[cr] = changes[cr] + 1
                                    if cr == self.optozdik:
                                        cdeff = cdeff + 1
                                    moves = moves - 1
                                    cr = cr + 1
                            if cr <= 8 and cr != self.optozdik:
                                if (self.desk[cr] + changes[cr]) % 2 == 0:
                                    cdeff = cdeff + self.desk[cr] + changes[cr]
                                elif (self.desk[cr] + changes[cr]) == 3:
                                    if self.tozdik == 9 and cr - 9 != 8 and cr - 9 != self.optozdik:
                                        akm = True
                                        cdeff = cdeff + 3
                        if cattc > attc:
                            deff = cdeff
                            attc = cattc
                            mak = maket
                            ak = akm
                            position = i
                            maxk = cmaxk
                        elif cattc == attc:
                            if cdeff < deff:
                                deff = cdeff
                                attc = cattc
                                mak = maket
                                ak = akm
                                position = i
                                maxk = cmaxk
                            elif cdeff == deff:
                                if maket == True and mak == False:
                                    deff = cdeff
                                    attc = cattc
                                    mak = maket
                                    ak = akm
                                    position = i
                                    maxk = cmaxk
                                elif maket == mak:
                                    if ak == True and akm == False:
                                        deff = cdeff
                                        attc = cattc
                                        mak = maket
                                        ak = akm
                                        position = i
                                        maxk = cmaxk
                                    elif ak == akm:
                                        if cmaxk > maxk:
                                            deff = cdeff
                                            attc = cattc
                                            mak = maket
                                            ak = akm
                                            position = i
                                            maxk =cmaxk
                        cattc = crattc
                        cdeff = crdeff 
        return position

    def move(self):
        l = True
        for i in range(9):
            if self.optozdik != i and self.desk[i] > 0:
                l = False
                break
        if l:
            return 9
        if self.level == 0:
            return self.__move0()
        elif self.level == 1:
            return self.__move1()
        elif self.level == 2:
            return self.__move2()
        elif self.level == 3:
            return self.__move3()
        else:
            return self.__move4()

class Game:
    def __init__(self, a):
        self.tyzdikplo = 9
        self.tyzdikplt = 9
        while a > 2 or a < 1:
            print('Please input correct data:')
            print('1 or 2 players?')
            a=int(input())
        if a == 1:
            print('Please input name:')
            nm=input()
            self.plo=Player(nm)
            print('Please input level of bot x (0 <= x <= 4)')
            lv=int(input())
            self.plt=Bot(lv)
        else:
            print('Player 1,please input name:')
            nm=input()
            self.plo=Player(nm)
            print('Player 2,please input name:')
            nm=input()
            self.plt=Player(nm)

    def start(self):
        while True:
            print(self.plo.name + ': ' + str(self.plo.points))
            print(self.plt.name + ': ' + str(self.plt.points))
            print(self.plt.reprint())
            print()
            print(self.plo.print())
            mv=self.plo.move()
            cr = 0
            if mv == 9:
                self.plt.points = 162 - self.plo.points
                break
            moves=self.plo.desk[mv]
            if moves > 1:
                cr = mv
            else :
                cr = mv + 1
            self.plo.desk[mv] = 0
            self.plt.opdesk[mv] = 0
            while moves > 0:
                while moves > 0 and cr < 9:
                    if self.tyzdikplt == cr :
                        self.plt.points = self.plt.points + 1
                    else :
                        self.plo.desk[cr] = self.plo.desk[cr] + 1
                        self.plt.opdesk[cr] = self.plt.opdesk[cr] + 1
                    cr = cr + 1
                    moves = moves - 1
                while moves > 0 and cr < 18:
                    if self.tyzdikplo == cr - 9:
                        self.plo.points = self.plo.points + 1
                    else :
                        self.plt.desk[cr - 9] = self.plt.desk[cr - 9] + 1
                        self.plo.opdesk[cr - 9] = self.plo.opdesk[cr - 9] + 1
                    cr = cr + 1
                    moves = moves - 1
                if moves == 0:
                    cr = cr - 1
                    break
                cr = 0
            if cr > 8 and cr - 9 != self.plo.tozdik:
                if self.plo.opdesk[cr - 9] % 2 == 0:
                    self.plo.points = self.plo.points + self.plo.opdesk[cr - 9]
                    self.plo.opdesk[cr - 9] = 0
                    self.plt.desk[cr - 9] = 0
                elif self.plo.opdesk[cr - 9] == 3 and self.tyzdikplo == 9 and cr - 9 != 8 and cr - 9 != self.tyzdikplt:
                    self.plo.points = self.plo.points + self.plo.opdesk[cr - 9]
                    self.plo.opdesk[cr - 9] = '*'
                    self.plt.desk[cr - 9] = '*'
                    self.tyzdikplo = cr - 9
                    self.plo.tozdik = cr - 9
                    self.plt.optozdik = cr - 9
            print(self.plo.name + ': ' + str(self.plo.points))
            print(self.plt.name + ': ' + str(self.plt.points))
            print(self.plo.reprint())
            print()
            print(self.plt.print())
            if self.plo.points > 81 or self.plt.points > 81:
                break
            mv=self.plt.move()
            if mv == 9:
                self.plo.points = 162 - self.plt.points
                break
            moves=self.plt.desk[mv]
            if moves > 1:
                cr = mv
            else :
                cr = mv + 1
            self.plt.desk[mv] = 0
            self.plo.opdesk[mv] = 0
            while moves > 0:
                while moves > 0 and cr < 9:
                    if self.tyzdikplo == cr :
                        self.plo.points = self.plo.points + 1
                    else :
                        self.plo.opdesk[cr] = self.plo.opdesk[cr] + 1
                        self.plt.desk[cr] = self.plt.desk[cr] + 1
                    cr = cr + 1
                    moves = moves - 1
                while moves > 0 and cr < 18:
                    if self.tyzdikplt == cr - 9:
                        self.plt.points = self.plt.points + 1
                    else :
                        self.plt.opdesk[cr - 9] = self.plt.opdesk[cr - 9] + 1
                        self.plo.desk[cr - 9] = self.plo.desk[cr - 9] + 1
                    cr = cr + 1
                    moves = moves - 1
                if moves == 0:
                    cr = cr - 1
                    break
                cr = 0
            if cr > 8 and cr - 9 != self.plt.tozdik:
                if self.plt.opdesk[cr - 9] % 2 == 0:
                    self.plt.points = self.plt.points + self.plt.opdesk[cr - 9]
                    self.plt.opdesk[cr - 9] = 0
                    self.plo.desk[cr - 9] = 0
                elif self.plt.opdesk[cr - 9] == 3 and self.tyzdikplt == 9 and cr - 9 != 8 and cr - 9 != self.tyzdikplo:
                    self.plt.points = self.plt.points + self.plt.opdesk[cr - 9]
                    self.plt.opdesk[cr - 9] = '*'
                    self.plo.desk[cr - 9] = '*'
                    self.tyzdikplt = cr - 9
                    self.plt.tozdik = cr - 9
                    self.plo.optozdik = cr - 9
            if self.plo.points > 81 or self.plt.points > 81:
                break
            print()
        print(self.plo.name + ': ' + str(self.plo.points))
        print(self.plt.name + ': ' + str(self.plt.points))
        if self.plo.points > 81:
            print('Player 1 is winner!')
        elif self.plt.points > 81:
            print('Player 2 is winner!')
        else:
            print('Tie')
            

print('1 or 2 players?')
pl=int(input())
r=Game(pl)
r.start()
