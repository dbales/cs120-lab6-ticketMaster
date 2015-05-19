#variables for how much tickets cost dependent on age. 
adultTicket = float(7.50)
studentTicket = float(5.00)
childTicket = float(2.00)
#introduction


#get the amount of tickets needed and age of buyer
numberOfTickets = int(raw_input('How many tickets would you like to buy today?:'))
age = int(raw_input('How old are you?:'))
netPriceAdult = float(numberOfTickets) * adultTicket
netPriceStudent = float(numberOfTickets) * studentTicket
netPriceChild = float(numberOfTickets) * childTicket

# adult and with or without military service
if(age >= 19):
    while True: 
        vetDiscount = raw_input('Type \'yes\' if you are a Veteran, if not press return:')
        if vetDiscount.strip() == str('yes') or str('Yes') or ('YES'): 
            vetDiscount = adultTicket *.80
            print'Yaass! You\'re a Barrel Chested Freedom Fighter and because of that we took 20 percent off so your total today comes to: $%d.00' % (vetDiscount)
            break
        else:
            print '%d Adult tickets will be $%d.00' % (adultTicket, netPriceAdult)
#for student and community service discount
if(age <= 18) and ( age >= 6):
    while True:
        comServiceDiscount = raw_input('Type \'yes\' if you are involved in commmunity service, if not press return:')
        if comServiceDiscount.strip() == str('yes') or str('Yes') or ('YES'):
         comServiceDiscount = netPriceStudent * .50
         print 'Your community reconignizes your hard work, so we took 50\% off. That makes today\'s total: $%.00' % (comServiceDiscount)
         break
        else:
            print 'Your total for %d student tickets are %d' % (numberOfTickets, netPriceStudent)
         

#price when age is < 5 
if(age <= 5):
    netPriceChild = childTicket * numberOfTickets
    print '%d children\'s tickets will be $%d.00' % (childTicket, netPriceChil
