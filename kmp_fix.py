from datetime import datetime

start = 0
running = 0

# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    colored_text = txt
    global jum
    global loc_found # kata ke-
    global found # index string ke-
    global space # jumlah spasi
    global move # bantuan colored text
    global start
    global running

    jum = space = move = 0
    loc_found = []
    found = []

    lenT = len(txt)
    lenP = len(pat)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    start = datetime.now()
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:

        if (text[i] == " "):
            space+=1

        if (pat[j] == txt[i]): # or (pat[j] == "*" and txt[i] != " "
            i += 1
            j += 1

        if j == M:      
            found_tmp = i - lenP
            loc_found.append(space+1)
            found.append(found_tmp)
            jum=jum+1    
            colored_text = colored_text[:found_tmp+move] + '\033[33m' + pattern + '\033[39m' + colored_text[found_tmp+lenP+move:]
            move+=10
            j = lps[j-1]
        # mismatch after j matches
        elif (i < N and pat[j] != txt[i]): # and pat[j] != "*"
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    running = datetime.now() - start
    return colored_text
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
  
  
# This code is contributed by Bhavya Jain

file = open("text.txt")

text = file.read().replace("\n", " ")

pattern = input("Masukkan pattern: ")
lower_pattern = pattern.lower()
lower_text = text.lower()

colored_text = KMPSearch(lower_pattern, lower_text)

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

    replace_idx = input("Masukkan urutan kata yang ingin diganti: ")
    
    replace_idx = int(replace_idx)

    while ( replace_idx > len(found) or replace_idx < 0):
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




