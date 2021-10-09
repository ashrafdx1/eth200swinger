# eth200swinger
offline half-random brute force script for Ethereum private keys, goes from the beginning to end of range and vice versa, saves any found address that happens to be in your provided list in a txt file
# Required:
-web3
-random
- its offline, so you need to provide your list of addresses as eth_list.txt
## SkipDups:
- shortly, skipdups func skips three duplications whenever it happens in the private key hex..
- example:
- input: 0x1112232fff######################################################
- output: 0x1122334001######################################################
- I added no skipdups edition, for those who doesn't like it but like other ideas 
## Swinging:
- it just means it goes from start of range to end of range and vice versa
## 200:
- four basis keys that generates in total 200 keys each time
- 2 base keys is random
- 1 is somewhat sequential
- 1 is a mix
## 128 keys version:
- three basis keys that generates in total 128 keys each time
- 1 base keys is random
- 1 is somewhat sequential
- 1 is a mix
- should be faster
# Important Note:
* The goal of this script is to test unusual ideas, not for anything else..
* This is by no mean a bug-free script,expect an error anytime.. so unless you can fix it, post an issue..
* This is not for casual users who just needs a script to run from time to time, some of the ideas applied here differ from other scripts, also this is not really a "User-friendly" aka no input taken from user.. you would need some python knowledge to edit it its parameters 
* The script currently is too slow, no threading nor multi-processing
* I appreciate any help..
# Disclaimer:
* I don't provide this script for malicious intentions and can't be held accountable for anything done by anyone who uses this script.
