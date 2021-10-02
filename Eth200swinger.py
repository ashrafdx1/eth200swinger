import time
import os
moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
import web3
from web3 import Web3
import random
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
lmda = 0x5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72
lmda2 = 0xac9c52b33fa3cf1f5ad9e3fd77ed9ba4a880b9fc8ec739c2e0cfc810b51283ce
s1 = 0x1034B8370E64CC000
s2 = 0x309E28A52B2E640000
s729 = 0x64656D6F
one = 0x00000000000001
maxN = 0xFFFeFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
minN =  0x0010000000000000000000000000000000000000000000000000000000000000
eth_address_list = set([line.split('\n')[0].lower()for line in open("eth143m19Sept21.txt",'r')])#eth_addressR.txt
totalAddresses = 0


def checkPK(prefix,PK):
    global totalAddresses
    try:
            acct = web3.eth.Account.privateKeyToAccount(PK)
            eth_addr = acct.address.lower()
            #print(f' success, {prefix}, {PK} is vaild pk')
            if eth_addr[:] in eth_address_list:
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
        if PK[2:] < hex(one):
            checkPK(prefix,hex(int(os.urandom(32).hex(),16))[2:].zfill(64))
        else:
            checkPK(prefix,PK[1:])
        pass


def extractHex(anyhex):
    size = str(anyhex[2:])
    #print(len(size))
    counter = 2
    i = len(size)
    #print(anyhex)
    #print(i)
    #item = i - (i - counter)
    a = [anyhex[i - (i - counter):][:3]]
    while counter < len(size)-1:
        counter += 1
        a.append(anyhex[i - (i - counter):][:3])
    #print(a)
    return a

def skipdups(prefixes):
    sizeOfList = len(prefixes)
    #print(sizeOfList)
    counter = 0
    hasDups = 'False'
    for i in prefixes:
        a = i[0]
        b = i[1]
        c = i[2]
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
                    if prefixes[counter-2][0] != prefixes[counter-2][1]:
                        prefixes[counter-3] = prefixes[counter-3][0]+prefixes[counter-3][1] + prefixes[counter-2][1]
                    else:
                        if prefixes[counter-3][0] == prefixes[counter-2][0]:
                            d = hex(int(prefixes[counter-3][2],16)+2)[2:]
                            if counter > 3 and prefixes[counter-3][0] == 'f':
                                prefixes[counter-3] = hex(int(prefixes[counter-3][0],16)-15)[2:] + hex(int(prefixes[counter-3][1],16)-15)[2:] + hex(int(prefixes[counter-3][2],16)-13)[2:]
                                prefixes[counter-2] = prefixes[counter-3][1] + prefixes[counter-3][2] + prefixes[counter-2][2]
                                prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-2][2] + prefixes[counter-1][2]
                                prefixes[counter-4] = hex(int(prefixes[counter-4][0],16)+1)[2:] +  prefixes[counter-3][0] + prefixes[counter-3][1]
                                prefixes[counter-5] = prefixes[counter-5][0] + prefixes[counter-4][0] + prefixes[counter-4][1]
                                prefixes[counter-6] = prefixes[counter-6][0] + prefixes[counter-5][0] + prefixes[counter-5][1]
                                #print(prefixes[counter-6])
                                #print(prefixes[counter-5])
                                #print(prefixes[counter-4])
                                #print(prefixes[counter-3])
#                            print(f'd = {d}')
                            else:
                                prefixes[counter-3] = prefixes[counter-3][0] + prefixes[counter-3][1]+d
                                prefixes[counter-2] = prefixes[counter-2][0] + prefixes[counter-3][2] + prefixes[counter-2][2]
                                prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-1][1] + prefixes[counter-1][2]
                        else:
                            d = hex(int(prefixes[counter-3][2],16)+1)[2:]
                            prefixes[counter-3] = prefixes[counter-3][0] + prefixes[counter-3][1]+d
                            prefixes[counter-2] = prefixes[counter-2][0] + prefixes[counter-3][2] + prefixes[counter-2][2]
                            prefixes[counter-1] = prefixes[counter-2][1] + prefixes[counter-1][1] + prefixes[counter-1][2]
            else:
                c = hex(int(c,16)+1)[2:]
            if counter < (sizeOfList-2):
                prefixes[counter+1] = prefixes[counter+1][0]+c+prefixes[counter+1][2]
                prefixes[counter+2] = c+prefixes[counter+2][1]+prefixes[counter+2][2]
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
add1hex = '-251084069415467230553431576928306656644094217778561380515840'
def main():
    global privatekeyStart,add1hex,reverse
    counter = 0
    print('Starting Script...')
    while True:
        if reverse == 0:
            prefixes = extractHex(hex(privatekeyStart))
            privatekeyStart = int(skipdups(prefixes),16)
            #print(f'key after skip:{hex(privatekeyStart)}')
        counter += 200
        #i=input('enter anything')
        #privateKey = os.urandom(32)
        pvkr = int(os.urandom(32).hex(),16)
        pvkrr = int(os.urandom(32).hex(),16)
        pvk = int(hex(privatekeyStart)[2:].zfill(64),16)
        pvk1 = int(os.urandom(32).hex(),16) + int(pvk/44) +int(pvkrr/52) + int(pvkr/63)
        #pvk1 = pvk + pvkr - pvkrr
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        checkPK(1,hex(pvk)[2:].zfill(64))
        checkPK(2,hex(pvk1)[2:].zfill(64))
        checkPK(3,hex(pvkr)[2:].zfill(64))
        checkPK(4,hex(pvkrr)[2:].zfill(64))
        #4
        checkPK(5,hex(pvk*lmda%N)[2:].zfill(64))
        checkPK(6,hex(pvk1*lmda%N)[2:].zfill(64))
        checkPK(7,hex(pvkr*lmda%N)[2:].zfill(64))
        checkPK(8,hex(pvkrr*lmda%N)[2:].zfill(64))
        #8
        checkPK(9,hex(pvk*lmda2%N)[2:].zfill(64))
        checkPK(10,hex(pvk1*lmda2%N)[2:].zfill(64))
        checkPK(11,hex(pvkr*lmda2%N)[2:].zfill(64))
        checkPK(12,hex(pvkrr*lmda2%N)[2:].zfill(64))
        #12
        checkPK(13,hex(N-pvk)[2:].zfill(64))
        checkPK(14,hex(N-pvk1)[2:].zfill(64))
        checkPK(15,hex(N-pvkr)[2:].zfill(64))
        checkPK(16,hex(N-pvkrr)[2:].zfill(64))
        #16
        checkPK(17,hex(N-pvk*lmda%N)[2:].zfill(64))
        checkPK(18,hex(N-pvk1*lmda%N)[2:].zfill(64))
        checkPK(19,hex(N-pvkr*lmda%N)[2:].zfill(64))
        checkPK(20,hex(N-pvkrr*lmda%N)[2:].zfill(64))
        #20
        checkPK(21,hex(N-pvk*lmda2%N)[2:].zfill(64))
        checkPK(22,hex(N-pvk1*lmda2%N)[2:].zfill(64))
        checkPK(23,hex(N-pvkr*lmda2%N)[2:].zfill(64))
        checkPK(24,hex(N-pvkrr*lmda2%N)[2:].zfill(64))
        #24
        checkPK(25,hex(N-s1-pvk)[2:].zfill(64))
        checkPK(26,hex(N-s1-pvk1)[2:].zfill(64))
        checkPK(27,hex(N-s1-pvkr)[2:].zfill(64))
        checkPK(28,hex(N-s1-pvkrr)[2:].zfill(64))
        #28
        checkPK(29,hex(N-s2-pvk)[2:].zfill(64))
        checkPK(30,hex(N-s2-pvk1)[2:].zfill(64))
        checkPK(31,hex(N-s2-pvkr)[2:].zfill(64))
        checkPK(32,hex(N-s2-pvkrr)[2:].zfill(64))
        #32
        checkPK(33,hex(N-s729-pvk)[2:].zfill(64))
        checkPK(34,hex(N-s729-pvk1)[2:].zfill(64))
        checkPK(35,hex(N-s729-pvkr)[2:].zfill(64))
        checkPK(36,hex(N-s729-pvkrr)[2:].zfill(64))
        #36
        checkPK(37,hex(s1+pvk)[2:].zfill(64))
        checkPK(38,hex(s1+pvk1)[2:].zfill(64))
        checkPK(39,hex(s1+pvkr)[2:].zfill(64))
        checkPK(40,hex(s1+pvkrr)[2:].zfill(64))
        #40
        checkPK(41,hex(s2+pvk)[2:].zfill(64))
        checkPK(42,hex(s2+pvk1)[2:].zfill(64))
        checkPK(43,hex(s2+pvkr)[2:].zfill(64))
        checkPK(44,hex(s2+pvkrr)[2:].zfill(64))
        #44
        checkPK(45,hex(s729+pvk)[2:].zfill(64))
        checkPK(46,hex(s729+pvk1)[2:].zfill(64))
        checkPK(47,hex(s729+pvkr)[2:].zfill(64))
        checkPK(48,hex(s729+pvkrr)[2:].zfill(64))
        #48
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        """from 49 to  108 , format : hex(int(N/16)*x-y"""
        checkPK(49,hex(int(N/16)*1-pvk)[2:].zfill(64))
        checkPK(50,hex(int(N/16)*2-pvk)[2:].zfill(64))
        checkPK(51,hex(int(N/16)*3-pvk)[2:].zfill(64))
        checkPK(52,hex(int(N/16)*4-pvk)[2:].zfill(64))
        checkPK(53,hex(int(N/16)*5-pvk)[2:].zfill(64))
        checkPK(54,hex(int(N/16)*6-pvk)[2:].zfill(64))
        checkPK(55,hex(int(N/16)*7-pvk)[2:].zfill(64))
        checkPK(56,hex(int(N/16)*8-pvk)[2:].zfill(64))
        checkPK(57,hex(int(N/16)*9-pvk)[2:].zfill(64))
        checkPK(58,hex(int(N/16)*10-pvk)[2:].zfill(64))
        checkPK(59,hex(int(N/16)*11-pvk)[2:].zfill(64))
        checkPK(60,hex(int(N/16)*12-pvk)[2:].zfill(64))
        checkPK(61,hex(int(N/16)*13-pvk)[2:].zfill(64))
        checkPK(62,hex(int(N/16)*14-pvk)[2:].zfill(64))
        checkPK(63,hex(int(N/16)*15-pvk)[2:].zfill(64))
        #63
        checkPK(64,hex(int(N/16)*1-pvk1)[2:].zfill(64))
        checkPK(65,hex(int(N/16)*2-pvk1)[2:].zfill(64))
        checkPK(66,hex(int(N/16)*3-pvk1)[2:].zfill(64))
        checkPK(67,hex(int(N/16)*4-pvk1)[2:].zfill(64))
        checkPK(68,hex(int(N/16)*5-pvk1)[2:].zfill(64))
        checkPK(69,hex(int(N/16)*6-pvk1)[2:].zfill(64))
        checkPK(70,hex(int(N/16)*7-pvk1)[2:].zfill(64))
        checkPK(71,hex(int(N/16)*8-pvk1)[2:].zfill(64))
        checkPK(72,hex(int(N/16)*9-pvk1)[2:].zfill(64))
        checkPK(73,hex(int(N/16)*10-pvk1)[2:].zfill(64))
        checkPK(74,hex(int(N/16)*11-pvk1)[2:].zfill(64))
        checkPK(75,hex(int(N/16)*12-pvk1)[2:].zfill(64))
        checkPK(76,hex(int(N/16)*13-pvk1)[2:].zfill(64))
        checkPK(77,hex(int(N/16)*14-pvk1)[2:].zfill(64))
        checkPK(78,hex(int(N/16)*15-pvk1)[2:].zfill(64))
        #78
        checkPK(79,hex(int(N/16)*1-pvkr)[2:].zfill(64))
        checkPK(80,hex(int(N/16)*2-pvkr)[2:].zfill(64))
        checkPK(81,hex(int(N/16)*3-pvkr)[2:].zfill(64))
        checkPK(82,hex(int(N/16)*4-pvkr)[2:].zfill(64))
        checkPK(83,hex(int(N/16)*5-pvkr)[2:].zfill(64))
        checkPK(84,hex(int(N/16)*6-pvkr)[2:].zfill(64))
        checkPK(85,hex(int(N/16)*7-pvkr)[2:].zfill(64))
        checkPK(86,hex(int(N/16)*8-pvkr)[2:].zfill(64))
        checkPK(87,hex(int(N/16)*9-pvkr)[2:].zfill(64))
        checkPK(88,hex(int(N/16)*10-pvkr)[2:].zfill(64))
        checkPK(89,hex(int(N/16)*11-pvkr)[2:].zfill(64))
        checkPK(90,hex(int(N/16)*12-pvkr)[2:].zfill(64))
        checkPK(91,hex(int(N/16)*13-pvkr)[2:].zfill(64))
        checkPK(92,hex(int(N/16)*14-pvkr)[2:].zfill(64))
        checkPK(93,hex(int(N/16)*15-pvkr)[2:].zfill(64))
        #93
        checkPK(94,hex(int(N/16)*1-pvkrr)[2:].zfill(64))
        checkPK(95,hex(int(N/16)*2-pvkrr)[2:].zfill(64))
        checkPK(96,hex(int(N/16)*3-pvkrr)[2:].zfill(64))
        checkPK(97,hex(int(N/16)*4-pvkrr)[2:].zfill(64))
        checkPK(98,hex(int(N/16)*5-pvkrr)[2:].zfill(64))
        checkPK(99,hex(int(N/16)*6-pvkrr)[2:].zfill(64))
        checkPK(100,hex(int(N/16)*7-pvkrr)[2:].zfill(64))
        checkPK(101,hex(int(N/16)*8-pvkrr)[2:].zfill(64))
        checkPK(102,hex(int(N/16)*9-pvkrr)[2:].zfill(64))
        checkPK(103,hex(int(N/16)*10-pvkrr)[2:].zfill(64))
        checkPK(104,hex(int(N/16)*11-pvkrr)[2:].zfill(64))
        checkPK(105,hex(int(N/16)*12-pvkrr)[2:].zfill(64))
        checkPK(106,hex(int(N/16)*13-pvkrr)[2:].zfill(64))
        checkPK(107,hex(int(N/16)*14-pvkrr)[2:].zfill(64))
        checkPK(108,hex(int(N/16)*15-pvkrr)[2:].zfill(64))
        #108
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        """from 109 to 138, format : hex(int(N/16)*x-y-z"""
        checkPK(109,hex(int(N/16)*1-pvkr-pvk)[2:].zfill(64))
        checkPK(110,hex(int(N/16)*2-pvkr-pvk)[2:].zfill(64))
        checkPK(111,hex(int(N/16)*3-pvkr-pvk)[2:].zfill(64))
        checkPK(112,hex(int(N/16)*4-pvkr-pvk)[2:].zfill(64))
        checkPK(113,hex(int(N/16)*5-pvkr-pvk)[2:].zfill(64))
        checkPK(114,hex(int(N/16)*6-pvkr-pvk)[2:].zfill(64))
        checkPK(115,hex(int(N/16)*7-pvkr-pvk)[2:].zfill(64))
        checkPK(116,hex(int(N/16)*8-pvkr-pvk)[2:].zfill(64))
        checkPK(117,hex(int(N/16)*9-pvkr-pvk)[2:].zfill(64))
        checkPK(118,hex(int(N/16)*10-pvkr-pvk)[2:].zfill(64))
        checkPK(119,hex(int(N/16)*11-pvkr-pvk)[2:].zfill(64))
        checkPK(120,hex(int(N/16)*12-pvkr-pvk)[2:].zfill(64))
        checkPK(121,hex(int(N/16)*13-pvkr-pvk)[2:].zfill(64))
        checkPK(122,hex(int(N/16)*14-pvkr-pvk)[2:].zfill(64))
        checkPK(123,hex(int(N/16)*15-pvkr-pvk)[2:].zfill(64))
        #123
        checkPK(124,hex(int(N/16)*1-pvkr-pvk1)[2:].zfill(64))
        checkPK(125,hex(int(N/16)*2-pvkr-pvk1)[2:].zfill(64))
        checkPK(126,hex(int(N/16)*3-pvkr-pvk1)[2:].zfill(64))
        checkPK(127,hex(int(N/16)*4-pvkr-pvk1)[2:].zfill(64))
        checkPK(128,hex(int(N/16)*5-pvkr-pvk1)[2:].zfill(64))
        checkPK(129,hex(int(N/16)*6-pvkr-pvk1)[2:].zfill(64))
        checkPK(130,hex(int(N/16)*7-pvkr-pvk1)[2:].zfill(64))
        checkPK(131,hex(int(N/16)*8-pvkr-pvk1)[2:].zfill(64))
        checkPK(132,hex(int(N/16)*9-pvkr-pvk1)[2:].zfill(64))
        checkPK(133,hex(int(N/16)*10-pvkr-pvk1)[2:].zfill(64))
        checkPK(134,hex(int(N/16)*11-pvkr-pvk1)[2:].zfill(64))
        checkPK(135,hex(int(N/16)*12-pvkr-pvk1)[2:].zfill(64))
        checkPK(136,hex(int(N/16)*13-pvkr-pvk1)[2:].zfill(64))
        checkPK(137,hex(int(N/16)*14-pvkr-pvk1)[2:].zfill(64))
        checkPK(138,hex(int(N/16)*15-pvkr-pvk1)[2:].zfill(64))
        #138
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        """from 139 to 168, format : hex(int(N/16)*x-y-z+g"""
        checkPK(139,hex(int(N/16)*1-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(140,hex(int(N/16)*2-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(141,hex(int(N/16)*3-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(142,hex(int(N/16)*4-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(143,hex(int(N/16)*5-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(144,hex(int(N/16)*6-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(145,hex(int(N/16)*7-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(146,hex(int(N/16)*8-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(147,hex(int(N/16)*9-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(148,hex(int(N/16)*10-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(149,hex(int(N/16)*11-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(150,hex(int(N/16)*12-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(151,hex(int(N/16)*13-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(152,hex(int(N/16)*14-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(153,hex(int(N/16)*15-pvkr-pvk+pvkrr)[2:].zfill(64))
        #153
        checkPK(154,hex(int(N/16)*1-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(155,hex(int(N/16)*2-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(156,hex(int(N/16)*3-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(157,hex(int(N/16)*4-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(158,hex(int(N/16)*5-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(159,hex(int(N/16)*6-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(160,hex(int(N/16)*7-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(161,hex(int(N/16)*8-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(162,hex(int(N/16)*9-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(163,hex(int(N/16)*10-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(164,hex(int(N/16)*11-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(165,hex(int(N/16)*12-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(166,hex(int(N/16)*13-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(167,hex(int(N/16)*14-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(168,hex(int(N/16)*15-pvkr-pvk1+pvkrr)[2:].zfill(64))
        #168
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        checkPK(169,hex(N-pvkr-s1-pvk)[2:].zfill(64))
        checkPK(170,hex(N-pvkr-s2-pvk)[2:].zfill(64))
        checkPK(171,hex(N-pvkr-s729-pvk)[2:].zfill(64))
        checkPK(172,hex(N-pvkr-pvk)[2:].zfill(64))
        checkPK(173,hex(N-pvkr+pvk)[2:].zfill(64))
        checkPK(174,hex(pvkr+pvk)[2:].zfill(64))
        checkPK(175,hex(pvkr-pvk)[2:].zfill(64))
        checkPK(176,hex(N-pvkr-s1-pvk+pvkrr)[2:].zfill(64))
        checkPK(177,hex(N-pvkr-s2-pvk+pvkrr)[2:].zfill(64))
        checkPK(178,hex(N-pvkr-s729-pvk+pvkrr)[2:].zfill(64))
        checkPK(179,hex(N-pvkr-pvk+pvkrr)[2:].zfill(64))
        checkPK(180,hex(N-pvkr+pvk-pvkrr)[2:].zfill(64))
        checkPK(181,hex(pvkr+pvk-pvkrr)[2:].zfill(64))
        checkPK(182,hex(pvkr-pvk+pvkrr)[2:].zfill(64))
        #182
        checkPK(183,hex(N-pvkr-s1-pvk1)[2:].zfill(64))
        checkPK(184,hex(N-pvkr-s2-pvk1)[2:].zfill(64))
        checkPK(185,hex(N-pvkr-s729-pvk1)[2:].zfill(64))
        checkPK(186,hex(N-pvkr-pvk1)[2:].zfill(64))
        checkPK(187,hex(N-pvkr+pvk1)[2:].zfill(64))
        checkPK(188,hex(pvkr+pvk1)[2:].zfill(64))
        checkPK(189,hex(pvkr-pvk1)[2:].zfill(64))
        checkPK(190,hex(N-pvkr-s1-pvk1+pvkrr)[2:].zfill(64))
        checkPK(191,hex(N-pvkr-s2-pvk1+pvkrr)[2:].zfill(64))
        checkPK(192,hex(N-pvkr-s729-pvk1+pvkrr)[2:].zfill(64))
        checkPK(193,hex(N-pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(194,hex(N-pvkr+pvk1-pvkrr)[2:].zfill(64))
        checkPK(195,hex(pvkr+pvk1-pvkrr)[2:].zfill(64))
        checkPK(196,hex(pvkr-pvk1+pvkrr)[2:].zfill(64))
        checkPK(197,hex(pvk+pvk1)[2:].zfill(64))
        checkPK(198,hex(pvk1-pvk)[2:].zfill(64))
        checkPK(199,hex(int(pvk1%pvk))[2:].zfill(64))
        checkPK(200,hex(int(pvk%pvkr+pvk1%pvkrr))[2:].zfill(64))
        #200
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        """-----------------------------------------------------------------------------------------------------------"""
        if counter % 100000 ==0:
            add1hex = str(int(add1hex)*random.randint(3, 333))
            print(f'  total scanned {counter}, add1hex = {add1hex}, total found {totalAddresses}, digits {len(hex(pvk)[2:])}, current pvk = '+
                  f'\n\t\t\t{hex(pvk)[2:].zfill(64)}\n\t\t\t{hex(pvk1)[2:].zfill(64)}\n\t\t\t{hex(pvkr)[2:].zfill(64)}\n\t\t\t{hex(pvkrr)[2:].zfill(64)}\n')
        if  privatekeyStart> maxN:
            add1hex = str(-1*random.randint(1, 1000))
            privatekeyStart = int(os.urandom(32).hex(),16)
            print(f'pks bigger than maxN, add1hex = {add1hex},reversing, key = {hex(privatekeyStart)}')
            reverse = 1
            #i=input('enter anything')
            continue

        privatekeyStart= pvk+ int(add1hex, 16)
        if  privatekeyStart< minN:
            add1hex = str(random.randint(1, 1000))
            privatekeyStart = int(os.urandom(32).hex(),16)
            print(f'pks smaller than start, add1hex = {add1hex},no reverse, key = {hex(privatekeyStart)}')
            reverse = 0
            #i=input('enter anything')
            continue

reverse = 0
if __name__ == '__main__':
    main()
