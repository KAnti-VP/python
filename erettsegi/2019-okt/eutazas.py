class Jegy:
  def __init__(self, megallo, felszallas, kartyaszam, jegy_tipus, ervenyes):
    self.megallo: int = megallo
    self.felszallas: str = felszallas
    self.kartyaszam: int = kartyaszam
    self.jegy_tipus: str = jegy_tipus
    self.ervenyes: str | int = ervenyes

    
def beolvasas():
  tickets = []
  with open('utasadat.txt', 'r') as f:
    for row in f:
      data = row.strip().split(' ')
      tickets.append(Jegy(int(data[0]), data[1], int(data[2]), data[3], data[4] if data[3] == 'JGY' else int(data[4])))
    return tickets

def is_ticket_valid(ticket: Jegy):
  if ticket.jegy_tipus == 'JGY':
    return int(ticket.ervenyes) > 0
  felszallas_datuma = ticket.felszallas.split('-')[0]
  return int(felszallas_datuma) <= int(ticket.ervenyes)

def nemszallhatott_fel(tickets: list[Jegy]):
  not_valid_tickets = []
  for ticket in tickets:
    if not is_ticket_valid(ticket):
      not_valid_tickets.append(ticket)
  return len(not_valid_tickets)

def legtobb_utas_megalloban(tickets: list[Jegy]):
  megallok = {}
  for ticket in tickets:
    if ticket.megallo in megallok:
      megallok[ticket.megallo] += 1
    else:
      megallok[ticket.megallo] = 1
  utas = max(megallok.values())
  allomasok = []
  for key in megallok.keys():
    if megallok[key] == utas:
      allomasok.append(key)
  megallo = min(allomasok)
  print(f'A legtöbb utas ({utas} fő) a {megallo}. megállóban próbált felszállni.')

def kedvezmenyes_utasok(tickets: list[Jegy]):
  ingyenes_utas, kedvezmenyes_utas = 0, 0
  for ticket in tickets:
    if is_ticket_valid(ticket):
      if ticket.jegy_tipus in ('TAB', 'NYB'):
        kedvezmenyes_utas += 1
      if ticket.jegy_tipus in ('NYP', 'RVS', 'GYK'):
        ingyenes_utas += 1
  print(f'Ingyenesen utazók száma: {ingyenes_utas} fő')
  print(f'A kedvezményesen utazók száma: {kedvezmenyes_utas} fő')

def napokszama(e1, h1, n1, e2, h2, n2):
  h1 = (h1 + 9) % 12
  e1 = e1 - h1 // 10
  d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
  h2 = (h2 + 9) % 12
  e2 = e2 - h2 // 10
  d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
  return d2-d1

def ev_ho_nap(datum):
  ev = int(datum[:4])
  ho = int(datum[4: 6])
  nap = int(datum[6:])
  return (ev, ho, nap)

def figyelmeztetes(tickets: list[Jegy]):
  rows = []
  for ticket in tickets:
    if ticket.jegy_tipus != 'JGY' and is_ticket_valid(ticket):
      felszallas_ev, felszallas_ho, felszallas_nap = ev_ho_nap(ticket.felszallas.split('-')[0])
      ervenyes_ev, ervenyes_ho, ervenyes_nap = ev_ho_nap(str(ticket.ervenyes))
      if napokszama(felszallas_ev, felszallas_ho, felszallas_nap, ervenyes_ev, ervenyes_ho, ervenyes_nap) <= 3:
        rows.append(f'{ticket.kartyaszam} {ervenyes_ev}-{str(ervenyes_ho).zfill(2)}-{ervenyes_nap}')
  with open ('figyelmeztetes.txt', 'w') as f:
    f.write('\n'.join(rows))


print('1. feladat')
jegyek = beolvasas()

print('2. feladat')
print(f'A buszra {len(jegyek)} utas akart felszállni.')

print('3. feladat')
print(f'A buszra {nemszallhatott_fel(jegyek)} utas nem szállhatott fel.')

print('4. feladat')
legtobb_utas_megalloban(jegyek)

print('5. feladat')
kedvezmenyes_utasok(jegyek)

print('6. feladat')
print('7. feladat')

figyelmeztetes(jegyek)
