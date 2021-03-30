import time

COST = 0
cnt = 0
PROFIT = 0
T_PROFIT = 0
NoORDER = 0
UNIT = 600
ONHAND = 0
for each_line in open('PTT.txt','r').readlines():
    PROFIT = 0
    NAV = float(each_line)
    if COST == 0:
        COST = NAV
        NoORDER = 1
    GAIN =  (NAV - COST)/COST*100
    if GAIN > 3:  ## Take Profit & open 1 
        NoORDER = 0
        PROFIT = NAV - COST
        T_PROFIT += PROFIT*UNIT
        print("################################ Accumulate Profit = ",T_PROFIT)
        NoORDER = 1
        COST = NAV
##        break
    elif GAIN < -3:
##        break
        NoORDER += 1
##        COST = (COST+NoORDER*NAV)/(NoORDER+1)
        COST = (COST+ NAV)/2
##        PROFIT = 99
        
        ONHAND += NoORDER*UNIT
        print("################################ Number of Order  = ",NoORDER)
##        if NoORDER > 15:
##            break
##    print("{:.4f} : {:.4f} : {:.2f} % : {:.4f}".format(NAV, COST, GAIN, PROFIT*UNIT))
    
    cnt += 1
    if cnt == 4000:
        break
          
