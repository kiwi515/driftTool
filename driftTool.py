import os
import sys

os.system('cls')
print('Drift Color Tool\n')

# misinput handling
if len(sys.argv) != 4:
    print('Invalid usage!\nValid usage: driftTool.py myBreff.breff COLOR1 COLOR2\n')
    quit()
elif len(sys.argv[2]) != 6:
    print('Invalid color #1!\nColors should be AABBCC (no hashtag prefix),\nno alpha value can be included as they vary in Mario Kart Wii.\n')
    quit()
elif len(sys.argv[3]) != 6:
    print('Invalid color #2!\nColors should be AABBCC (no hashtag prefix),\nno alpha value can be included as they vary in Mario Kart Wii.\n')
    quit()


subfileList = ['rk_blueChip00', 'rk_blueSpark00', 'rk_blueSpark01', 'rk_blueSpark02', 'rk_driftSpark1L_Chip00', 'rk_driftSpark1L_Spark00',
               'rk_driftSpark1L_Spark01', 'rk_driftSpark1R_Chip00', 'rk_driftSpark1R_Spark00', 'rk_driftSpark1R_Spark01', 'rk_blueChip00_1T',
               'rk_blueSpark02_1T', 'rk_blueSpark01_1T', 'rk_blueSpark00_1T', 'rk_driftSpark1L1T_Chip00', 'rk_driftSpark1L1T_Spark00',
               'rk_driftSpark1L1T_Spark01', 'rk_driftSpark1R1T_Chip00', 'rk_driftSpark1R1T_Spark00', 'rk_driftSpark1R1T_Spark01',
               'rk_driftSpark1LB_Chip00', 'rk_driftSpark1LB_Spark00', 'rk_driftSpark1LB_Spark01', 'rk_driftSpark1RB_Chip00',
               'rk_driftSpark1RB_Spark00', 'rk_driftSpark1RB_Spark01', 'rk_driftSpark1LB1T_Chip00', 'rk_driftSpark1LB1T_Spark00',
               'rk_driftSpark1LB1T_Spark01', 'rk_driftSpark1RB1T_Chip00', 'rk_driftSpark1RB1T_Spark00', 'rk_driftSpark1RB1T_Spark01',
               'rk_driftSpark1CB1T_Chip00', 'rk_driftSpark1CB1T_Spark00', 'rk_driftSpark1CB1T_Spark01', 'rk_driftSpark1CB_Spark00',
               'rk_driftSpark1CB_Spark01', 'rk_driftSpark2L_Spark01', 'rk_driftSpark2R_Chip00', 'rk_driftSpark2L1T_Chip00',
               'rk_driftSpark2L1T_Spark00', 'rk_driftSpark2L1T_Spark01', 'rk_driftSpark2R1T_Chip00', 'rk_driftSpark2R1T_Spark00',
               'rk_driftSpark2R1T_Spark01', 'rk_driftSpark1LB_Chip00M', 'rk_driftSpark1LB_Spark00M', 'rk_driftSpark1LB_Spark01M',
               'rk_driftSpark1RB_Chip00M', 'rk_driftSpark1RB_Spark00M', 'rk_driftSpark1RB_Spark01M', 'rk_driftSpark1LB1T_Chip00M',
               'rk_driftSpark1LB1T_Spark00M', 'rk_driftSpark1LB1T_Spark01M', 'rk_driftSpark1RB1T_Chip00M', 'rk_driftSpark1RB1T_Spark00M',
               'rk_driftSpark1RB1T_Spark01M', 'rk_driftSpark1CB1T_Chip00M', 'rk_driftSpark1CB1T_Spark00M', 'rk_driftSpark1CB1T_Spark01M',
               'rk_driftSpark1CB_Spark00M', 'rk_driftSpark1CB_Spark01M', 'rk_driftSpark1L_Chip00M', 'rk_driftSpark1L_Spark00M',
               'rk_driftSpark1L_Spark01M', 'rk_driftSpark1R_Chip00M', 'rk_driftSpark1R_Spark00M', 'rk_driftSpark1R_Spark01M',
               'rk_driftSpark1L1T_Chip00M', 'rk_driftSpark1L1T_Spark00M', 'rk_driftSpark1L1T_Spark01M', 'rk_driftSpark1R1T_Chip00M',
               'rk_driftSpark1R1T_Spark00M', 'rk_driftSpark1R1T_Spark01M', 'rk_driftSpark2L_Spark01M', 'rk_driftSpark2R_Chip00M',
               'rk_driftSpark2R_Spark01M', 'rk_driftSpark2L1T_Chip00M', 'rk_driftSpark2R1T_Chip00M']

primaryColorExceptions = ['rk_driftSpark1RB_Spark00', 'rk_driftSpark1R_Spark00']

color1aSet = set()
color1bSet = set()

primColorStr = sys.argv[2]

primColor = sys.argv[2]
secColor  = sys.argv[3]

primColorBytes = bytes.fromhex(primColor)
secColorBytes  = bytes.fromhex(secColor)


rkInput = open(os.path.join(sys.path[0], sys.argv[1]), 'rb') # open BREFF

# RKRace check
rkInput.seek(40, 0)

if rkInput.read(6) != b'RKRace':
    print('Object in section 1 does not match RKRace. Are you sure this is the right file? y/n')
    x = input()
    
    if x.lower() == 'y':
        confirm = True
        
    else:
        quit()

else:
    confirm = True
    
if confirm == True:
    rkInput.seek(0, 0)
    s = rkInput.read()
    totalCount = 1
    for subfile in subfileList:
        ('Gathering info from RKRace...') # update progress bar
        rkInput.seek(24, 0) # seek to subfile list pointer
        
        subfileListOffList = (int.from_bytes(rkInput.read(4), byteorder = 'big') + (rkInput.tell() - 4)) # calculate subfile list's offset from beginning
        rkInput.seek(s.find(subfile.encode('utf-8')) + (len(subfile) + 1), 0) # seek to end of subfile item's name
        distanceFromSubList = int.from_bytes(rkInput.read(4), byteorder = 'big') # distance between current subfile's data and the subfile list
        rkInput.seek((subfileListOffList + distanceFromSubList) + 4, 0) # seek to current subfile's emitter size
        
        
        emitterDataSize = int.from_bytes(rkInput.read(4), byteorder = 'big') # size of subfile item's emitter data
        rkInput.seek(emitterDataSize + 4, 1) # seek to particle colors
        if subfile not in primaryColorExceptions:
            color1aSet.add(rkInput.tell()) # add current location to list of primary color addresses
            
        color1bSet.add(rkInput.tell() + 4) # add next color to list of secondary color addresses
        totalCount+=1 # iterate totalCount (for progress bar)

    rkInput.close() # close input stream
    newBREFF = os.path.join( sys.path[0] , sys.argv[1][0 : (len(sys.argv[1]) - 6)] ) + '(' + primColor + ').breff' # path for output BREFF
    rkOut = open(newBREFF, 'wb+') # create + open output BREFF
    s2 = bytearray(s) # create bytearray of RKRace
    
    
    print('Replacing primary colors.....')
    for pColorAddr in color1aSet:
        totalCount = 0

        for itr in range (0, 3):
            s2.pop(pColorAddr)
        
        s2[pColorAddr:3] = primColorBytes
            
            
    print('Replacing secondary colors...')       
    for sColorAddr in color1bSet:
        totalCount = 0
        
        
        for itr in range (0, 3):
            s2.pop(sColorAddr)
            
        s2[sColorAddr:3] = secColorBytes
        
        
    rkOut.write(s2) # write new BREFF contents to local file
    print('Wrote new contents to', newBREFF)
    rkOut.close() # close output stream
    quit()
    
else:
    quit()

quit()