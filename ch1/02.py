s1 = "パトカー"
s2 = "タクシー"
conc = list(zip(s1 , s2))
conc = "".join([item[0]+item[1] for item in conc])
print(conc)