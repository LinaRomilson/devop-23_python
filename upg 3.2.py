namn = input('Ange ditt namn: ')
ålder = int(input('Ange din ålder: '))

print("-----")

if ålder == 1 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder ,'år ) sova minst 14 timmar per natt.')
elif ålder == 2 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 13 timmar per natt.')
elif ålder == 3 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 12 timmar per natt.')
elif ålder == 4 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 11,5 timmar per natt.')
elif ålder == 5 or ålder == 6 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 11 timmar per natt.')
elif ålder == 7 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 10,5 timmar per natt.')
elif ålder <= 10 and ålder >= 8 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 10 timmar per natt.')
elif ålder == 11 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 9,5 timmar per natt.')
elif ålder >= 12 and ålder <= 15 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 9 timmar per natt.')
elif ålder == 16 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 8,5 timmar per natt.')
elif ålder >= 17 :
    print('Hallå', namn, '! Enligt Vårdguidens rekommendationer behöver individer i din ålder (', ålder, 'år ) sova minst 8 timmar per natt.')
else :
    print("Felinmatning")