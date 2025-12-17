hetek = int(input('Hetek száma='))
cel = float(input('Elérni kívánt testtömeg (kg)='))
heti_suly = []
elerte_a_sulyt = 0
for i in range(1, hetek + 1):
    suly = float(input(f'{i}. héten='))
    heti_suly.append(suly)
    if suly <= cel and elerte_a_sulyt == 0:
        elerte_a_sulyt = i
    
if elerte_a_sulyt > 0:
    print(f'Mari néni a(z) {elerte_a_sulyt}. héten érte el a célt.')
else:
    print('Sajnos Mari néni nem érte el a célját.')

elozo_suly = heti_suly[0]
szamlalo = 0
for suly in heti_suly:
    if suly > elozo_suly:
        szamlalo += 1
    elozo_suly = suly
print(f'A tömege {szamlalo} esetben nőtt egyik hétről a másikra.')