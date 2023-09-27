from datetime import datetime

print()
print("================================================ Teks ================================================")

file = open("text.txt")

text = file.read().replace("\n", " ")

print(text,"\n")
lower_text = text.lower()
colored_text = text

pattern = input("Masukkan pattern: ")
lower_pattern = pattern.lower()

lenT = len(text)
lenP = len(pattern)


jum = 0
loc_found = [] # kata ke-
found = [] #index string ke-
space = 0 #jumlah spasi
move = 0 #bantuan colored text

start = datetime.now()
for i in range(lenT-lenP):
    j = 0
    if (text[i] == " "):
        space+=1
    while (j<lenP and (lower_text[i+j] == lower_pattern[j] or (lower_pattern[j] == "*" and lower_text[i+j] != " "))):
        j=j+1
    if (j>=lenP):
        
        found_tmp = i
        loc_found.append(space+1)
        found.append(found_tmp)
        jum=jum+1    
        colored_text = colored_text[:found_tmp+move] + '\033[33m' + pattern + '\033[39m' + colored_text[found_tmp+lenP+move:]
        move+=10
running = datetime.now()-start

i = 1

if (len(found) == 0):
    print("Pattern tidak ditemukan di dalam teks.")
else:
    print(colored_text)
    print("Jumlah pattern (", pattern,") yang ditemukan adalah sebanyak", jum,"pattern")
    tmp = input("Lihat semua indeks . . .")
    for j in range(len(loc_found)):
        print(i, ".kata ke - ", loc_found[j], ",indeks ke-", found[j])
        i+=1

    replace_idx = int(input("Masukkan urutan kata yang ingin diganti: "))
    while (replace_idx > len(found) or replace_idx < 0):
        replace_idx = int(input("Urutan tidak tepat. Masukkan kembali urutan kata yang ingin diganti: "))
    replace_word = input("Masukkan kata pengganti yang diinginkan: ")
    if (replace_idx == 0):
        move = 0
        for i in range(len(loc_found)):
            if(i == 0):
                text = text[:found[i]+move] + '\033[33m' + replace_word + '\033[39m' + text[found[i]+len(pattern)+move:]
            else:
                text = text[:found[i]+move] + '\033[33m' + replace_word + '\033[39m' + text[found[i]+(len(replace_word)*i)+move:]
            move+=13
    else:
        text = text[:found[replace_idx-1]] + '\033[33m' + replace_word + '\033[39m' + text[found[replace_idx-1]+len(pattern):]

    print()
    print()
    print(text)
print ("Total Running time: ", running)
