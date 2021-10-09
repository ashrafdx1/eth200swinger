"""
* swing after 1m ^^
* 128 keys , 3 base keys
* skipdups edition
* almost double the speed, at least for me using 6GB list lol
* still testing it, code is really messy, expect bugs to happen /:
* have fun!
"""
import time
import os
moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
import web3
from web3 import Web3
import random
from multiprocessing import Manager, Event, Process, Queue, Value, cpu_count
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
lmda = 0x5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72
lmda2 = 0xac9c52b33fa3cf1f5ad9e3fd77ed9ba4a880b9fc8ec739c2e0cfc810b51283ce
s1 = 0x1034B8370E64CC000
s2 = 0x309E28A52B2E640000
s729 = 0x64656D6F
one = 0x00000000000001
maxN = 0xFFFeFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
minN =  0x0010000000000000000000000000000000000000000000000000000000000000
eth_address_list = set([line.split('\n')[0].lower()for line in open("eth143m19Sept21.txt",'r')])#
#eth_address_list = set([line.split('\n')[0].lower()for line in open("eth_addressR.txt",'r')])#
totalAddresses = 0
n161 = int(N/16)
n162 = n161*2
n163 = n161*3
n164 = n161*4
n165 = n161*5
n166 = n161*6
n167 = n161*7
n168 = n161*8
n169 = n161*9
n1610 = n161*10
n1611 = n161*11
n1612 = n161*12
n1613 = n161*13
n1614 = n161*14
n1615 = n161*15

def checkPK(prefix,PK):
    global totalAddresses
    try:
            #if prefix < 49 or prefix > 63:
                #return
            #if prefix < 154 or prefix > 168:
                #return
            #acct = web3.eth.Account.privateKeyToAccount(PK)#*
            #eth_addr = acct.address.lower()
            #print(f' success, {prefix}, {PK} is vaild pk,{len(PK)}')#*
            #print(web3.eth.Account.privateKeyToAccount(PK).address.lower()[:])      
            if web3.eth.Account.privateKeyToAccount(PK).address.lower()[:] in eth_address_list:
                acct = web3.eth.Account.privateKeyToAccount(PK)
                eth_addr = acct.address.lower()
                totalAddresses += 1
                print(f'#Found Address\n')
                print(eth_addr + '\n')
                print(PK + '\n')
                print(f'total addresses found = {totalAddresses}')
                with open(f'ETH_found_143m_200KEYs.txt','a') as fw:
                    fw.write(eth_addr + '\n')
                    fw.write(PK + '\n')
                return
    except:
        #print(f' faild, {prefix}, {PK[1:]} is not vaild pk, {len(PK[1:])}')
        #print(f' faild, {prefix}, {PK} is not vaild pk, {len(PK[1:])}')#*
        if PK[2:] < hex(one):
            #print(f'{prefix} hex smaller than one')
            checkPK(prefix,hex(int(os.urandom(32).hex(),16))[2:].zfill(64))
        else:
            checkPK(prefix,PK[1:])
            #print(f'{prefix} hex bigger than range')
        pass



def checkPKoo(prefix,PK,pko):
    global totalAddresses
    totalpk = 15
    try:
            #if prefix < 49 or prefix > 63:
                #return
            #if prefix < 154 or prefix > 168:
                #return
            #print('this is the oo fun')
            #print(pko)
            #print(PK)
            #print(f'{PK[1:]}, {len(PK[1:])},{PK[1:2]}')
            #print(PK[1:])
            #print(len(PK[1:]))
            if len(PK[1:]) ==64 or len(PK[1:]) ==63 :
                checkPKo(prefix,PK,-pko)
                return
            firstDigit = 15
            
            #print(firstDigit)
            
            #print(PK[2:3])
            """
            if len(PK[1:]) ==64:
                firstDigit = int(PK[1:2],16)
            if len(PK[1:]) ==63:
                if int(PK[1:2],16) > 1:
                    print('skip')
                    firstDigit = -1
                else:
                    firstDigit = 1
                    print(f'calling check firstDigit = {firstDigit}')
                    ppp = f'{hex(firstDigit)[2:]}'+PK[2:]
                    #print('this is the o fun')
                    checkPK(prefix,ppp)
                    firstDigit = -1
                    prefix += 1
            """
            #if counter == 2:
                #if len(PK[1:]) ==63:
                    #print('hi')
                    #counter = 1
                    #ppp = f'{hex(counter)[2:]}'+PK[2:]
                    #checkPK(prefix,ppp)
                    #print('calling check 1')
                    #counter = 0
                    #prefix += 1
                #else:
                    #counter = 2
            #print(counter)
            #pcounter 
            #print(counter-1)
            while firstDigit >= 0:
                #print('hi0')
                #print(firstDigit)
                pp = f'{hex(firstDigit)[2:]}'+PK[3:]
                firstDigit -= 1
                #print(pp)
                #print('this is the o fun')
                #print('1st while')
                checkPK(prefix,pp)
                
                #print('calling check 2')
                prefix += 1
                totalpk -= 1
                
                
                #
            """
            counter = int(PK[1:2],16) + 2
            #print(counter)
            #print(f'this is counter outside while {counter}')
            #checkPK(prefix,hex(n161*counter - pko)[2:].zfill(64))
            ccounter = 0
            p = hex(n161*counter + pko)[2:].zfill(64)
            #print('before second while')
            #print(p[0:1])
            firstDigit2 = int(p[0:1],16)
            print(firstDigit2)
            if len(PK[1:]) ==63:
                firstDigit2 = 0
            while totalpk >= 1:
                #print('hi')
                #print(hex(firstDigit2)[2:])
                pp = f'{hex(firstDigit2)[2:]}'+p[5:]
                #print(pp)
                #print('this is the o fun')
                checkPK(prefix,pp)
                #print(hex(ccounter)[2:])
                #print(pp)
                firstDigit2 += 1
                
                #print('calling check 3')
                counter += 1
                
                prefix += 1
                totalpk -= 1
            """
            return
    except:
        #print(f' faild, {prefix}, {PK[1:]} is not vaild pk, {len(PK[1:])}')
        #print(f' faild in o, {prefix}, {PK} is not vaild pk, {len(PK[1:])}')#*
        if PK[2:] < hex(one):
            #print(f'{prefix} hex smaller than one')
            checkPK(prefix,hex(int(os.urandom(32).hex(),16))[2:].zfill(64))
        else:
            checkPK(prefix,PK[1:])
            #print(f'{prefix} hex bigger than range')
        pass

def checkPKo(prefix,PK,pko):
    global totalAddresses
    totalpk = 15
    try:
            #if prefix < 49 or prefix > 63:
                #return
            #if prefix < 154 or prefix > 168:
                #return
            #print('this is the o fun')
            #print(f'{PK[1:]}, {len(PK[1:])},{PK[1:2]}')
            #print(PK[1:])
            firstDigit = int(PK[1:2],16)
            
            #print(firstDigit)
            #print(len(PK[1:]))
            #print(PK[1:2])
            if len(PK[1:]) ==63:
                if int(PK[1:2],16) > 1:
                    #print('skip')
                    firstDigit = -1
                else:
                    firstDigit = 1
                    #print(f'calling check firstDigit = {firstDigit}')
                    ppp = f'{hex(firstDigit)[2:]}'+PK[2:]
                    #print('this is the o fun')
                    checkPK(prefix,ppp)
                    firstDigit = -1
                    prefix += 1
                
            #if counter == 2:
                #if len(PK[1:]) ==63:
                    #print('hi')
                    #counter = 1
                    #ppp = f'{hex(counter)[2:]}'+PK[2:]
                    #checkPK(prefix,ppp)
                    #print('calling check 1')
                    #counter = 0
                    #prefix += 1
                #else:
                    #counter = 2
            #print(counter)
            #pcounter 
            #print(counter-1)
            while firstDigit >= 0:
                #print('hi0')
                #print(firstDigit)
                pp = f'{hex(firstDigit)[2:]}'+PK[2:]
                firstDigit -= 1
                #print(pp)
                #print('this is the o fun')
                checkPK(prefix,pp)
                #print('1st while')
                #print('calling check 2')
                prefix += 1
                totalpk -= 1
                
                
                #
            counter = int(PK[1:2],16) + 2
            #print(counter)
            #print(f'this is counter outside while {counter}')
            #checkPK(prefix,hex(n161*counter - pko)[2:].zfill(64))
            ccounter = 0
            p = hex(n161*counter - pko)[2:].zfill(64)
            #print('before second while')
            #print(p[0:1])
            firstDigit2 = int(p[0:1],16)
            #print(firstDigit2)
            if len(PK[1:]) ==63:
                firstDigit2 = 0
            while totalpk >= 1:
                #print('hi')
                #print(hex(firstDigit2)[2:])
                pp = f'{hex(firstDigit2)[2:]}'+p[1:]
                #print(pp)
                #print('this is the o fun')
                checkPK(prefix,pp)
                #print(hex(ccounter)[2:])
                #print(pp)
                firstDigit2 += 1
                
                #print('calling check 3')
                counter += 1
                
                prefix += 1
                totalpk -= 1
            return
    except:
        #print(f' faild, {prefix}, {PK[1:]} is not vaild pk, {len(PK[1:])}')
        #print(f' faild in o, {prefix}, {PK} is not vaild pk, {len(PK[1:])}')#*
        if PK[2:] < hex(one):
            #print(f'{prefix} hex smaller than one')
            checkPK(prefix,hex(int(os.urandom(32).hex(),16))[2:].zfill(64))
        else:
            checkPK(prefix,PK[1:])
            #print(f'{prefix} hex bigger than range')
        pass
"""
from working script
['f3d', '3d7', 'd70', '70b', '0b9', 'b9f', '9fb', 'fb2', 'b27', '270', '70f', '0fa', 'fa9', 'a9a', '9ad', 'ad8', 'd8f', '8f3', 'f36', '360', '607', '07d', '7df', 'dfd', 'fd6', 'd6f', '6f7', 'f77',
'771', '710', '106', '06c', '6c3', 'c35', '354', '544', '444', '440', '407', '073', '736', '366', '66d', '6df', 'dfe', 'fe9','e9a', '9a7', 'a73', '730', '304', '049', '49f', '9f7', 'f78',
 '787', '87e', '7ea', 'eaa', 'aa1', 'a12', '124']
"""
"""
['f3d', '3d7', 'd70', '70b', '0b9', 'b9f', '9fb', 'fb2', 'b27', '270', '70f', '0fa', 'fa9', 'a9a', '9ad', 'ad8', 'd8f', '8f3', 'f36', '360', '607', '07d', '7df', 'dfd', 'fd6', 'd6f', '6f7', 'f77',
'771', '710', '106', '06c', '6c3', 'c35', '354', '544', '445', '450', '50', '073', '736', '366', '66d', '6df', 'dfe', 'fe9', 'e9a', '9a7', 'a73', '730', '304', '049', '49f', '9f7', 'f78',
'787', '87e', '7ea', 'eaa', 'aa1', 'a12', '124']
"""
def extractHex(anyhex):
    ##print(anyhex)
    size = str(anyhex[2:])
    #print(len(size))
    counter = 2
    i = len(size)
    ##print(i)
    #print(anyhex)
    #print(i)
    #item = i - (i - counter)
    a = [anyhex[i - (i - counter):][:3]]
    while counter < len(size)-1:
        counter += 1
        ##print(counter)
        a.append(anyhex[i - (i - counter):][:3])
        ##print(a)
    ##print(a)
    return a

def skipdups(prefixes):
    #print('skip')
    sizeOfList = len(prefixes)
    #print(sizeOfList)
    counter = 0
    hasDups = 'False'
    for i in prefixes:
        a = i[0]
        b = i[1]
        c = i[2]
        """
        try:
            c = i[2]
        except:
           print(prefixes)
           print(i)
           i=input()
        """
#        print(c)
        if a != b:
            Do='Nothing'
        elif b == c:
            hasDups = 'True'
#            print('dups found!!')
            if c == 'f':
                c = hex(int(c,16)-14)[2:]
                b = hex(int(b,16)-15)[2:]
                a = hex(int(a,16)-15)[2:]
                d = hex(int(prefixes[counter-1][0],16)+1)[2:]
                prefixes[counter-1] = d+a+b
                if counter > 2:
                    prefixes[counter-2] = prefixes[counter-2][0]+prefixes[counter-1][0] + prefixes[counter-1][1]
                    ##prefixes[counter-2] = prefixes[counter-2][0]+prefixes[counter-1][0:2]
                    if prefixes[counter-2][0] != prefixes[counter-2][1]:
                        prefixes[counter-3] = prefixes[counter-3][0]+prefixes[counter-3][1] + prefixes[counter-2][1]
                        ##prefixes[counter-3] = prefixes[counter-3][0:2]+ prefixes[counter-2][1]
                        #print(prefixes[counter-3][0]+prefixes[counter-3][1] + prefixes[counter-2][1])
                        #print(prefixes[counter-3][0:2]+ prefixes[counter-2][1])
                    else:
                        if prefixes[counter-3][0] == prefixes[counter-2][0]:
                            d = hex(int(prefixes[counter-3][2],16)+2)[2:]
                            if counter > 3 and prefixes[counter-3][0] == 'f':
                                prefixes[counter-3] = hex(int(prefixes[counter-3][0],16)-15)[2:] + hex(int(prefixes[counter-3][1],16)-15)[2:] + hex(int(prefixes[counter-3][2],16)-13)[2:]
                                prefixes[counter-2] = prefixes[counter-3][1] + prefixes[counter-3][2] + prefixes[counter-2][2]
                                ##prefixes[counter-2] = prefixes[counter-3][1:2] + prefixes[counter-2][2]
                                prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-2][2] + prefixes[counter-1][2]
                                ##prefixes[counter-1] = prefixes[counter-2][1:2] + prefixes[counter-1][2]
                                prefixes[counter-4] = hex(int(prefixes[counter-4][0],16)+1)[2:] +  prefixes[counter-3][0] + prefixes[counter-3][1]
                                ##prefixes[counter-4] = hex(int(prefixes[counter-4][0],16)+1)[2:] +  prefixes[counter-3][0:2]
                                prefixes[counter-5] = prefixes[counter-5][0] + prefixes[counter-4][0] + prefixes[counter-4][1]
                                ##prefixes[counter-5] = prefixes[counter-5][0] + prefixes[counter-4][0:2]
                                prefixes[counter-6] = prefixes[counter-6][0] + prefixes[counter-5][0] + prefixes[counter-5][1]
                                ##prefixes[counter-6] = prefixes[counter-6][0] + prefixes[counter-5][0:2]
                                #print(prefixes[counter-6])
                                #print(prefixes[counter-5])
                                #print(prefixes[counter-4])
                                #print(prefixes[counter-3])
#                            print(f'd = {d}')
                            else:
                                prefixes[counter-3] = prefixes[counter-3][0] + prefixes[counter-3][1]+d
                                ##prefixes[counter-3] = prefixes[counter-3][0:2]+d
                                prefixes[counter-2] = prefixes[counter-2][0] + prefixes[counter-3][2] + prefixes[counter-2][2]
                                prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-1][1] + prefixes[counter-1][2]
                                ##prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-1][1:2]
                        else:
                            d = hex(int(prefixes[counter-3][2],16)+1)[2:]
                            prefixes[counter-3] = prefixes[counter-3][0] + prefixes[counter-3][1]+d
                            ##prefixes[counter-3] = prefixes[counter-3][0:2] + d
                            ##prefixes[counter-3] = prefixes[counter-3][0:2] + hex(int(prefixes[counter-3][2],16)+1)[2:]
                            prefixes[counter-2] = prefixes[counter-2][0] + prefixes[counter-3][2] + prefixes[counter-2][2]
                            prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-1][1] + prefixes[counter-1][2]
                            ##prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-1][1:2]
            else:
                c = hex(int(c,16)+1)[2:]
            if counter < (sizeOfList-2):
                prefixes[counter+1] = prefixes[counter+1][0]+c+prefixes[counter+1][2]
                prefixes[counter+2] = c+prefixes[counter+2][1]+prefixes[counter+2][2]
                ##prefixes[counter+2] = c+prefixes[counter+2][1:2]
                """ this strangely makes an error when doing the short version!!!"""
            elif counter ==(sizeOfList-2):
                prefixes[counter+1] = prefixes[counter+1][0]+c+prefixes[counter+1][2]
            #print('modified to '+a+b+c
            prefixes[counter] = a+b+c
            #print(prefixes[1])
        else:
            Do='Nothing'
        counter += 1
    counter = 0
    nodups ='0x'+prefixes[counter]
    while counter < (sizeOfList-4)+3:
        counter += 1
        nodups =nodups + prefixes[counter][2]
        #print(counter)
    #print('0x'+nodups)
    #print(nodups)
    return nodups


start = 0x111

#privatekeyStart = 0x3a2256cb72a1fb4b72fdf7a933dddde3df9c2bc9a26d8e199b508dfb544990000
privatekeyStart = 0x000000000000111
#privatekeyStart = 0xf1269218cac52eab2344342c3ecff43082efd4f090fe3a6e1535ee426244d5aa
add1hex = '-251084069415467230553431576928306656644094217778561380515840'
#add1hex = '808'
def main():
    global privatekeyStart,add1hex,reverse
    print('Starting Script...')
    counterT = Value('L')
    st = time.time()
    while True:
        counterT.value += 200
        if reverse == 0:
            prefixes = extractHex(hex(privatekeyStart))
            ##print('before calling skipdups')
            ##print(prefixes)
            privatekeyStart = int(skipdups(prefixes),16)
            #print(f'key after skip:{hex(privatekeyStart)}')
        #i=input('enter anything')#*
        #privateKey = os.urandom(32)
        pvkr = int(os.urandom(32).hex(),16)
        #pvkrr = int(os.urandom(32).hex(),16)
        pvk = int(hex(privatekeyStart)[2:].zfill(64),16)
        #pvk1 = int(os.urandom(32).hex(),16) + int(pvk/44) +int(pvkrr/52) + int(pvkr/63)
        pvk1 = int(os.urandom(32).hex(),16) + int(pvk/44) + int(pvkr/63)
        #pvk1 = pvk + pvkr - pvkrr
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        checkPK(1,hex(pvk)[2:].zfill(64))
        checkPK(2,hex(pvk1)[2:].zfill(64))
        checkPK(3,hex(pvkr)[2:].zfill(64))
        #checkPK(4,hex(pvkrr)[2:].zfill(64))
        #4
        checkPK(5,hex(pvk*lmda%N)[2:].zfill(64))
        checkPK(6,hex(pvk1*lmda%N)[2:].zfill(64))
        checkPK(7,hex(pvkr*lmda%N)[2:].zfill(64))
        #checkPK(8,hex(pvkrr*lmda%N)[2:].zfill(64))
        #8
        checkPK(9,hex(pvk*lmda2%N)[2:].zfill(64))
        checkPK(10,hex(pvk1*lmda2%N)[2:].zfill(64))
        checkPK(11,hex(pvkr*lmda2%N)[2:].zfill(64))
        #checkPK(12,hex(pvkrr*lmda2%N)[2:].zfill(64))
        #12
        checkPK(13,hex(N-pvk)[2:].zfill(64))
        checkPK(14,hex(N-pvk1)[2:].zfill(64))
        checkPK(15,hex(N-pvkr)[2:].zfill(64))
        #checkPK(16,hex(N-pvkrr)[2:].zfill(64))
        #16
        checkPK(17,hex(N-pvk*lmda%N)[2:].zfill(64))
        checkPK(18,hex(N-pvk1*lmda%N)[2:].zfill(64))
        checkPK(19,hex(N-pvkr*lmda%N)[2:].zfill(64))
        #checkPK(20,hex(N-pvkrr*lmda%N)[2:].zfill(64))
        #20
        checkPK(21,hex(N-pvk*lmda2%N)[2:].zfill(64))
        checkPK(22,hex(N-pvk1*lmda2%N)[2:].zfill(64))
        checkPK(23,hex(N-pvkr*lmda2%N)[2:].zfill(64))
        #checkPK(24,hex(N-pvkrr*lmda2%N)[2:].zfill(64))
        #24
        checkPK(25,hex(N-s1-pvk)[2:].zfill(64))
        checkPK(26,hex(N-s1-pvk1)[2:].zfill(64))
        checkPK(27,hex(N-s1-pvkr)[2:].zfill(64))
        #checkPK(28,hex(N-s1-pvkrr)[2:].zfill(64))
        #28
        checkPK(29,hex(N-s2-pvk)[2:].zfill(64))
        checkPK(30,hex(N-s2-pvk1)[2:].zfill(64))
        checkPK(31,hex(N-s2-pvkr)[2:].zfill(64))
        #checkPK(32,hex(N-s2-pvkrr)[2:].zfill(64))
        #32
        checkPK(33,hex(N-s729-pvk)[2:].zfill(64))
        checkPK(34,hex(N-s729-pvk1)[2:].zfill(64))
        checkPK(35,hex(N-s729-pvkr)[2:].zfill(64))
        #checkPK(36,hex(N-s729-pvkrr)[2:].zfill(64))
        #36
        checkPK(37,hex(s1+pvk)[2:].zfill(64))
        checkPK(38,hex(s1+pvk1)[2:].zfill(64))
        checkPK(39,hex(s1+pvkr)[2:].zfill(64))
        #checkPK(40,hex(s1+pvkrr)[2:].zfill(64))
        #40
        checkPK(41,hex(s2+pvk)[2:].zfill(64))
        checkPK(42,hex(s2+pvk1)[2:].zfill(64))
        checkPK(43,hex(s2+pvkr)[2:].zfill(64))
        #checkPK(44,hex(s2+pvkrr)[2:].zfill(64))
        #44
        checkPK(45,hex(s729+pvk)[2:].zfill(64))
        checkPK(46,hex(s729+pvk1)[2:].zfill(64))
        checkPK(47,hex(s729+pvkr)[2:].zfill(64))
        #checkPK(48,hex(s729+pvkrr)[2:].zfill(64))
        #48
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        """from 49 to  108 , format : hex(int(N/16)*x-y"""
        #checkPK(49,hex(n161-pvk)[2:].zfill(64))#60
        #checkPK(50,hex(n162-pvk)[2:].zfill(64))#51
        #checkPK(51,hex(n163-pvk)[2:].zfill(64))#42
        #checkPK(52,hex(n164-pvk)[2:].zfill(64))#33
        #checkPK(53,hex(n165-pvk)[2:].zfill(64))#24
        #checkPK(54,hex(n166-pvk)[2:].zfill(64))#15
        #checkPK(55,hex(n167-pvk)[2:].zfill(64))#06
        #checkPK(56,hex(n168-pvk)[2:].zfill(64))
        #checkPK(57,hex(n169-pvk)[2:].zfill(64))
        #checkPK(58,hex(n1610-pvk)[2:].zfill(64))
        #checkPK(59,hex(n1611-pvk)[2:].zfill(64))
        #checkPK(60,hex(n1612-pvk)[2:].zfill(64))
        #checkPK(61,hex(n1613-pvk)[2:].zfill(64))
        #checkPK(62,hex(n1614-pvk)[2:].zfill(64))
        #checkPK(63,hex(n1615-pvk)[2:].zfill(64))
        #### from 49 to 63 , -14 
        checkPKo(49,hex(n161-pvk)[2:].zfill(64),pvk)
        #checkPKo(55,hex(n167-pvk)[2:].zfill(64),pvk)
        ####
        #63
        #checkPK(64,hex(n161-pvk1)[2:].zfill(64))
        #checkPK(65,hex(n162-pvk1)[2:].zfill(64))
        #checkPK(66,hex(n163-pvk1)[2:].zfill(64))
        #checkPK(67,hex(n164-pvk1)[2:].zfill(64))
        #checkPK(68,hex(n165-pvk1)[2:].zfill(64))
        #checkPK(69,hex(n166-pvk1)[2:].zfill(64))
        #checkPK(70,hex(n167-pvk1)[2:].zfill(64))
        #checkPK(71,hex(n168-pvk1)[2:].zfill(64))
        #checkPK(72,hex(n169-pvk1)[2:].zfill(64))
        #checkPK(73,hex(n1610-pvk1)[2:].zfill(64))
        #checkPK(74,hex(n1611-pvk1)[2:].zfill(64))
        #checkPK(75,hex(n1612-pvk1)[2:].zfill(64))
        #checkPK(76,hex(n1613-pvk1)[2:].zfill(64))
        #checkPK(77,hex(n1614-pvk1)[2:].zfill(64))
        #checkPK(78,hex(n1615-pvk1)[2:].zfill(64))
        #### from 64 to 78, - 28
        checkPKo(64,hex(n161-pvk1)[2:].zfill(64),pvk1)
        ####
        #78
        #checkPK(79,hex(n161-pvkr)[2:].zfill(64))
        #checkPK(80,hex(n162-pvkr)[2:].zfill(64))
        #checkPK(81,hex(n163-pvkr)[2:].zfill(64))
        #checkPK(82,hex(n164-pvkr)[2:].zfill(64))
        #checkPK(83,hex(n165-pvkr)[2:].zfill(64))
        #checkPK(84,hex(n166-pvkr)[2:].zfill(64))
        #checkPK(85,hex(n167-pvkr)[2:].zfill(64))
        #checkPK(86,hex(n168-pvkr)[2:].zfill(64))
        #checkPK(87,hex(n169-pvkr)[2:].zfill(64))
        #checkPK(88,hex(n1610-pvkr)[2:].zfill(64))
        #checkPK(89,hex(n1611-pvkr)[2:].zfill(64))
        #checkPK(90,hex(n1612-pvkr)[2:].zfill(64))
        #checkPK(91,hex(n1613-pvkr)[2:].zfill(64))
        #checkPK(92,hex(n1614-pvkr)[2:].zfill(64))
        #checkPK(93,hex(n1615-pvkr)[2:].zfill(64))
        #### from 79 to 93, - 42
        checkPKo(79,hex(n161-pvkr)[2:].zfill(64),pvkr)
        ####
        #93
        #checkPK(94,hex(n161-pvkrr)[2:].zfill(64))
        #checkPK(95,hex(n162-pvkrr)[2:].zfill(64))
        #checkPK(96,hex(n163-pvkrr)[2:].zfill(64))
        #checkPK(97,hex(n164-pvkrr)[2:].zfill(64))
        #checkPK(98,hex(n165-pvkrr)[2:].zfill(64))
        #checkPK(99,hex(n166-pvkrr)[2:].zfill(64))
        #checkPK(100,hex(n167-pvkrr)[2:].zfill(64))
        #"""
        #checkPK(101,hex(n168-pvkrr)[2:].zfill(64))
        #checkPK(102,hex(n169-pvkrr)[2:].zfill(64))
        #checkPK(103,hex(n1610-pvkrr)[2:].zfill(64))
        #checkPK(104,hex(n1611-pvkrr)[2:].zfill(64))
        #checkPK(105,hex(n1612-pvkrr)[2:].zfill(64))
        #checkPK(106,hex(n1613-pvkrr)[2:].zfill(64))
        #checkPK(107,hex(n1614-pvkrr)[2:].zfill(64))
        #checkPK(108,hex(n1615-pvkrr)[2:].zfill(64))
        #### from 94 to 108, -56
        #checkPKo(94,hex(n161-pvkrr)[2:].zfill(64),pvkrr)
        ####
        #108
        #""""-----------------------------------------------------------------------------------------------------------""""
        #""""-----------------------------------------------------------------------------------------------------------""""
        #""""from 109 to 138, format : hex(int(N/16)*x-y-z""""
        npvkrPnpvk = (-pvkr) + (-pvk)
        #print(n161 + npvkrPnpvk)+npvkrPnpvk
        #print(n161-pvkr-pvk)
        #i = input()
        #### - 70
        #print(npvkrPnpvk)
        #checkPK(109,hex(n161+npvkrPnpvk)[2:].zfill(64))
        #checkPK(110,hex(n162+npvkrPnpvk)[2:].zfill(64))
        #checkPK(111,hex(n163+npvkrPnpvk)[2:].zfill(64))
        #checkPK(112,hex(n164+npvkrPnpvk)[2:].zfill(64))
        #checkPK(113,hex(n165+npvkrPnpvk)[2:].zfill(64))
        #checkPK(114,hex(n166+npvkrPnpvk)[2:].zfill(64))
        #checkPK(115,hex(n167+npvkrPnpvk)[2:].zfill(64))
        #checkPK(116,hex(n168+npvkrPnpvk)[2:].zfill(64))
        #checkPK(117,hex(n169+npvkrPnpvk)[2:].zfill(64))
        #checkPK(118,hex(n1610+npvkrPnpvk)[2:].zfill(64))
        #checkPK(119,hex(n1611+npvkrPnpvk)[2:].zfill(64))
        #checkPK(120,hex(n1612+npvkrPnpvk)[2:].zfill(64))
        #checkPK(121,hex(n1613+npvkrPnpvk)[2:].zfill(64))
        #checkPK(122,hex(n1614+npvkrPnpvk)[2:].zfill(64))
        #checkPK(123,hex(n1615+npvkrPnpvk)[2:].zfill(64))
        #### from 94 to 108, -70
        checkPKoo(109,hex(n161+npvkrPnpvk)[2:].zfill(64),npvkrPnpvk)
        ####
        #123
        npvkrPnpvk1 = (-pvkr) + (-pvk1)#+npvkrPnpvk1
        #### - 84
        #checkPK(124,hex(n161+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(125,hex(n162+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(126,hex(n163+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(127,hex(n164+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(128,hex(n165+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(129,hex(n166+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(130,hex(n167+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(131,hex(n168+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(132,hex(n169+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(133,hex(n1610+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(134,hex(n1611+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(135,hex(n1612+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(136,hex(n1613+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(137,hex(n1614+npvkrPnpvk1)[2:].zfill(64))
        #checkPK(138,hex(n1615+npvkrPnpvk1)[2:].zfill(64))
        #### from 124 to 138, -84
        checkPKoo(124,hex(n161+npvkrPnpvk1)[2:].zfill(64),npvkrPnpvk1)
        ####
        #138
        #""""-----------------------------------------------------------------------------------------------------------""""
        #""""-----------------------------------------------------------------------------------------------------------""""
        #""""from 139 to 168, format : hex(int(N/16)*x-y-z+g""""
        #npvkrPnpvkPpvkrr = npvkrPnpvk+pvkrr
        #### - 98
        #checkPK(139,hex(n161+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(140,hex(n162+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(141,hex(n163+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(142,hex(n164+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(143,hex(n165+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(144,hex(n166+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(145,hex(n167+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(146,hex(n168+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(147,hex(n169+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(148,hex(n1610+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(149,hex(n1611+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(150,hex(n1612+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(151,hex(n1613+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(152,hex(n1614+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #checkPK(153,hex(n1615+npvkrPnpvkPpvkrr)[2:].zfill(64))
        #### from 139 to 153, -98
        #checkPKoo(139,hex(n161+npvkrPnpvkPpvkrr)[2:].zfill(64),npvkrPnpvkPpvkrr)
        ####
        #153
        #npvkrPnpvk1Ppvkrr = npvkrPnpvk1+pvkrr
        #### - 112
        #checkPK(154,hex(n161+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(155,hex(n162+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(156,hex(n163+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(157,hex(n164+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(158,hex(n165+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(159,hex(n166+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(160,hex(n167+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(161,hex(n168+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(162,hex(n169+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(163,hex(n1610+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(164,hex(n1611+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(165,hex(n1612+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(166,hex(n1613+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(167,hex(n1614+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #checkPK(168,hex(n1615+npvkrPnpvk1Ppvkrr)[2:].zfill(64))
        #### from 154 to 168, -112
        #checkPKoo(154,hex(n161+npvkrPnpvk1Ppvkrr)[2:].zfill(64),npvkrPnpvk1Ppvkrr)
        ####
        #168
        #""""-----------------------------------------------------------------------------------------------------------""""
        #""""-----------------------------------------------------------------------------------------------------------""""
        nPnpvkrPnpvk = N+npvkrPnpvk
        checkPK(169,hex(nPnpvkrPnpvk-s1)[2:].zfill(64))
        checkPK(170,hex(nPnpvkrPnpvk-s2)[2:].zfill(64))
        checkPK(171,hex(nPnpvkrPnpvk-s729)[2:].zfill(64))
        checkPK(172,hex(nPnpvkrPnpvk)[2:].zfill(64))
        checkPK(173,hex(N-pvkr+pvk)[2:].zfill(64))
        checkPK(174,hex(pvkr+pvk)[2:].zfill(64))
        checkPK(175,hex(pvkr-pvk)[2:].zfill(64))
        #checkPK(176,hex(nPnpvkrPnpvk-s1+pvkrr)[2:].zfill(64))
        #checkPK(177,hex(nPnpvkrPnpvk-s2+pvkrr)[2:].zfill(64))
        #checkPK(178,hex(nPnpvkrPnpvk-s729+pvkrr)[2:].zfill(64))
        #checkPK(179,hex(nPnpvkrPnpvk+pvkrr)[2:].zfill(64))
        #checkPK(180,hex(N-pvkr+pvk-pvkrr)[2:].zfill(64))
        #checkPK(181,hex(pvkr+pvk-pvkrr)[2:].zfill(64))
        #checkPK(182,hex(pvkr-pvk+pvkrr)[2:].zfill(64))
        #182
        nPnpvkrPnpvk1 = N+npvkrPnpvk1
        checkPK(183,hex(nPnpvkrPnpvk1-s1)[2:].zfill(64))
        checkPK(184,hex(nPnpvkrPnpvk1-s2)[2:].zfill(64))
        checkPK(185,hex(nPnpvkrPnpvk1-s729)[2:].zfill(64))
        checkPK(186,hex(nPnpvkrPnpvk1)[2:].zfill(64))
        checkPK(187,hex(N-pvkr+pvk1)[2:].zfill(64))
        checkPK(188,hex(pvkr+pvk1)[2:].zfill(64))
        checkPK(189,hex(pvkr-pvk1)[2:].zfill(64))
        #checkPK(190,hex(nPnpvkrPnpvk1-s1+pvkrr)[2:].zfill(64))
        #checkPK(191,hex(nPnpvkrPnpvk1-s2+pvkrr)[2:].zfill(64))
        #checkPK(192,hex(nPnpvkrPnpvk1-s729+pvkrr)[2:].zfill(64))
        #checkPK(193,hex(nPnpvkrPnpvk1+pvkrr)[2:].zfill(64))
        #checkPK(194,hex(N-pvkr+pvk1-pvkrr)[2:].zfill(64))
        #checkPK(195,hex(pvkr+pvk1-pvkrr)[2:].zfill(64))
        #checkPK(196,hex(pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(197,hex(pvk+pvk1)[2:].zfill(64))
        checkPK(198,hex(pvk1-pvk)[2:].zfill(64))
        checkPK(199,hex(int(pvk1%pvk))[2:].zfill(64))
        #checkPK(200,hex(int(pvk%pvkr+pvk1%pvkrr))[2:].zfill(64))
        #200
        #"""
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        if counterT.value % 100000 ==0:
            add1hex = str(int(add1hex)*random.randint(654321, 6543210))
            print('\n[ Speed : {1:.2f} Keys/s ]'.format(counterT.value, counterT.value/(time.time() - st)))
            #print(f'  total scanned {counterT.value}, add1hex = {add1hex}, total found {totalAddresses}, digits {len(hex(pvk)[2:])}, current pvk = '+
                  #f'\n\t\t\t{hex(pvk)[2:].zfill(64)}\n\t\t\t{hex(pvk1)[2:].zfill(64)}\n\t\t\t{hex(pvkr)[2:].zfill(64)}\n\t\t\t{hex(pvkrr)[2:].zfill(64)}\n')
            print(f'  total scanned {counterT.value}, add1hex = {add1hex}, total found {totalAddresses}, digits {len(hex(pvk)[2:])}, current pvk = '+
                  f'\n\t\t\t{hex(pvk)[2:].zfill(64)}\n\t\t\t{hex(pvk1)[2:].zfill(64)}\n\t\t\t{hex(pvkr)[2:].zfill(64)}\n')
        if  privatekeyStart> maxN:
            add1hex = str(-1*random.randint(1, 1000))
            privatekeyStart = int(os.urandom(32).hex(),16)
            print(f'pk bigger than maxN, add1hex = {add1hex},reversing, key = {hex(privatekeyStart)}')
            reverse = 1
            #i=input('enter anything')
            continue

        privatekeyStart= pvk+ int(add1hex, 16)
        if  privatekeyStart< minN:
            add1hex = str(random.randint(1, 1000))
            privatekeyStart = int(os.urandom(32).hex(),16)
            print(f'pk smaller than start, add1hex = {add1hex},no reverse, key = {hex(privatekeyStart)}')
            reverse = 0
            #i=input('enter anything')
            continue

reverse = 1
if __name__ == '__main__':
    main()
