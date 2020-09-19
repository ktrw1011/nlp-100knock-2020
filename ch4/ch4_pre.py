import MeCab
import pickle
tagger = MeCab.Tagger('')
tagger.parse('')

lines = []

with open("./neko.txt") as f:
    for line in f:
        parsed = tagger.parse(line)
        item_list = []
        for item in parsed.split('\n'):
            if item == 'EOS':
                break

            items = {'surface':'', 'base':'', 'pos':'', 'pos1':''}

            surface, feature = item.split('\t')
            features = feature.split(',')

            items['surface'] = surface
            items['base'] = features[6]
            items['pos'] = features[0]
            items['pos1'] = features[1]

            item_list.append(items)
        
        if item_list != []:
            lines.append(item_list)

with open('./neko.txt.mecab', 'wb') as f:
    pickle.dump(lines, f)

