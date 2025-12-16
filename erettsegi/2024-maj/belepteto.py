class Card:
  def __init__(self, id, time, code):
    self.id = id
    self.time = self.set_time(time)
    self.code = code
  
  def set_time(self, time: str):
    hours, minutes = time.strip().split(':')
    return int(hours) * 60 + int(minutes)

  def time_to_str(self, time: int):
    return f'{str(time // 60).zfill(2)}:{str(time % 60).zfill(2)}'
  
  def get_time(self):
    return self.time_to_str(self.time)
  
  def duration(self, other):
    difference = abs(self.time - other.time)
    return {'hours': difference // 60, 'minutes' : difference % 60}
  
  def __str__(self):
    return f'{self.id} {self.get_time()} {self.code}'

##########################################


def printCards(cards: list[Card]):
  for card in cards:
    print(card)


def readFile():
  data = []
  with open('bedat.txt', 'r') as f:
    for row in f:
      card = row.strip().split(' ')
      data.append(Card(card[0], card[1], int(card[2])))
  return data


def first_last_students(cards: list[Card]):
  print(f'Az első tanuló {cards[0].get_time()}-kor lépett be a főkapun.')
  print(f'Az utolsó tanuló {cards[-1].get_time()}-kor lépett ki a főkapun')


def they_are_late(cards: list[Card]):
  start_time = 7 * 60 + 50
  end_time = 8 * 60 + 15
  entries = []
  for card in cards:
    if card.code == 1 and start_time < card.time <= end_time:
      entries.append(f'{card.id} {card.get_time()}')
    if card.time > end_time:
      break
  with open('kesok.txt', 'w') as f:
    f.write('\n'.join(entries))


def get_amount_of(cards: list[Card], place):
  visitors = set()
  for card in cards:
    if card.code == place:
      visitors.add(card.id)
  return len(visitors)


def back_door(cards: list[Card]):
  students_in = set()
  leavers = []
  entered, left = 1, 2
  end_time = 11 * 60
  for card in cards:
    if card.code == entered and card.id in students_in:
      leavers.append(card.id)
    if card.code == entered and card.id not in students_in:
      students_in.add(card.id)
    if card.code == left and card.id in students_in:
      students_in.remove(card.id)
    if card.time >= end_time:
      break
  print('Az érintett tanulók: ')
  print(' '.join(leavers))
    

def duration_time(cards: list[Card]):
  student_id = input('Egy tanuló azonosítója= ')
  entered = ''
  left = ''
  for card in cards:
    if card.id == student_id:
      if entered == '':
        entered = card
      left = card
  if entered == '':
    print('Ilyen azonosítójú tanuló aznap nem volt az iskolában.')
    return
  duration = entered.duration(left)
  print(f'A tanuló érkezése és távozása között {duration['hours']} óra {duration['minutes']} perc telt el.')


print('1. feladat')
cards_data = readFile()
# printCards(cards_data)
print('Adatok beolvasása a fájlból.')

print('2. feladat')
first_last_students(cards_data)

print('3. feladat')
# they_are_late(cards_data)

print('4. feladat')
lunch_visitors = get_amount_of(cards_data, 3)
print(f'A menzán aznap {lunch_visitors} tanuló ebédelt.')

print('5. feladat')
library_visitors = get_amount_of(cards_data, 4)
print(f'Aznap {library_visitors} tanuló kölcsönzött a könyvtárban.')
if library_visitors > lunch_visitors:
  print('Többen voltak, mint a menzán.')
else: 
  print('Nem voltak többen, mint a menzán.')

print('6. feladat')
back_door(cards_data)

print('7. feladat')
duration_time(cards_data)

