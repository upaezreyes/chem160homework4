from cards import *
ntrials = 1000  # number of trials
awins = 0   # to keep track wins

for i in range(ntrials):
    adeck=deck()     # creates  a deck on adeck
    adeck.shuffle()   # shuffles the deck
    bdeck=deck()
    bdeck.shuffle()
    ascore = 0    # keep track of ascore
    bscore = 0    # keep track of bscore
    tied = 0 
    while adeck.cardsleft() > 0 and bdeck.cardsleft() > 4:     # the loop will break when 2 cards are left
        acard1 = adeck.dealcard()   # get a value for acard1
        bcard = bdeck.dealcard()    # get a value for acard2
       

        if acard1.value() > bcard.value(): 
            ascore += 1
        if acard1.value() == bcard.value():
            tied += 1
          
        if bcard.value() > acard1.value(): 
            bscore += 1
    if ascore > bscore:
        awins += 1
print("Player A win percentage=",awins/ntrials," tied games", tied)


 

    
