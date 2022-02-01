import matplotlib.pylab as plt
from bs4 import BeautifulSoup
import requests
import japanize_matplotlib

url = "********************************"

count = 0
katakana_list = [chr(i) for i in range(ord("ァ"), ord("ヴ"))]
katakana_list.append("ー")

exclude_list = ["♀", "♂", "２", "Ｚ", "："]

katakana_init_list = [0 for i in range(len(katakana_list))]
name_char_dict = dict(zip(katakana_list, katakana_init_list))
name_file = open('FiveLengthPokemon.txt', 'w')

for i in range(1, 900):
    dest_url = url + str(i).zfill(3)
    html = requests.get(dest_url)
    soup = BeautifulSoup(html.content, "html.parser")
    pokemon_name = soup.find("title").encode("utf-8").decode("utf-8").replace("<title>", "").replace("｜ポケモンずかん</title>", "")
    if " " in pokemon_name:
        tmp_pokemon_name_list = pokemon_name.split()
        pokemon_name = tmp_pokemon_name_list[0]

    flg = 0
    for j in exclude_list:
        if j in pokemon_name:
            flg = 1

    if flg == 1:
        continue
    if (len(pokemon_name) == 5):
        name_file.write(pokemon_name + "\n")
        count += 1
        for i in range(0, 5):
            name_char_dict[pokemon_name[i]] += 1

print(name_char_dict)

name_sorted = sorted(name_char_dict.items(), key=lambda x:x[1], reverse = True)
x, y = zip(*name_sorted)

plt.xticks(fontsize = 14)
plt.yticks(fontsize = 20)

plt.title("5文字のポケモン限定で、各文字の登場回数数えてみた")
plt.bar(x, y)
plt.show()

