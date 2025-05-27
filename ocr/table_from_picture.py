# pip install opencv-python pytesseract pandas openpyxl

import cv2
import pytesseract
import pandas as pd
import numpy as np

# Kép elérési útja
image_path = 'tablazat.jpg'  # Cseréld ki a saját képed nevére!

# Beolvassuk a képet
image = cv2.imread(image_path)

if image is None:
    print(f"HIBA: Nem található a kép: {image_path}")
    exit(1)

# Kép szürkeárnyalatossá alakítása
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invertálás és küszöbölés
_, binary = cv2.threshold(~gray, 150, 255, cv2.THRESH_BINARY)

# Függőleges és vízszintes vonalak detektálása morfológiai műveletekkel
def extract_lines(binary, axis='horizontal'):
    length = binary.shape[1 if axis == 'horizontal' else 0] // 100
    structure = cv2.getStructuringElement(cv2.MORPH_RECT, (length, 1) if axis == 'horizontal' else (1, length))
    lines = cv2.erode(binary, structure)
    lines = cv2.dilate(lines, structure)
    return lines

horizontal = extract_lines(binary, 'horizontal')
vertical = extract_lines(binary, 'vertical')

# Rács létrehozása
grid = cv2.add(horizontal, vertical)

# Kontúrok detektálása → cellák meghatározása
contours, _ = cv2.findContours(grid, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Cellák kivágása, OCR és rendezés
cells = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w < 30 or h < 20:  # kis zaj kiszűrése
        continue
    roi = image[y:y+h, x:x+w]
    text = pytesseract.image_to_string(roi, config='--psm 7').strip()
    cells.append((y, x, text))

# Cellák sorokba és oszlopokba rendezése
cells.sort()  # Y szerint

rows = []
current_row = []
prev_y = -100

for y, x, text in sorted(cells, key=lambda c: (c[0], c[1])):
    if abs(y - prev_y) > 20:
        if current_row:
            rows.append(current_row)
        current_row = [text]
        prev_y = y
    else:
        current_row.append(text)
if current_row:
    rows.append(current_row)

# DataFrame létrehozása
df = pd.DataFrame(rows)

# Mentés
df.to_csv('kimenet_grid.csv', index=False, header=False)
df.to_excel('kimenet_grid.xlsx', index=False, header=False)

print("Sikeresen elmentve rácsvonalas detektálással:")
print("- kimenet_grid.csv")
print("- kimenet_grid.xlsx")
