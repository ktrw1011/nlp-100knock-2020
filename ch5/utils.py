from typing import List
import ginza

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self._surface = surface
        self._base = base
        self._pos = pos
        self._pos1 = pos1

    @property
    def surface(self):
        return self._surface

    @property
    def base(self):
        return self._base

    @property
    def pos(self):
        return self._pos

    @property
    def pos1(self):
        return self._pos1

    def __str__(self):
        return f"surface:{self._surface}\tbase:{self._base}\tpos:{self._pos}\tpos1:{self._pos1}"


class Chunk:
    def __init__(self):
        # 形態素解析のリスト
        self.morphs: List[Morph]
        # 係り元文節インデックス番号
        self.srcs: List[int] = []
        # 係り先文節インデックス
        self.dst: int = None

    def __str__(self):
        chunk_surface = "".join([m.surface for m in self.morphs])
        ms = "\t"+"\n\t".join([str(m) for m in self.morphs])
        return f"surface: {chunk_surface}\nmorphs:\n{ms}\ndst: {self.dst}\nsrcs: {self.srcs}"

def get_morphs(doc) -> List[Morph]:
    """ginzaの解析結果からMorphクラスのリストを返す
    """
    morphs = []
    for token in doc:
        pos_info = token.tag_.split('-')
        morph = Morph(
            surface=token.orth_,
            base=token.lemma_,
            pos=pos_info[0],
            pos1=pos_info[1] if len(pos_info) >= 2 else '',
        )
        morphs.append(morph)
    return morphs

def analysis_bunsetu(doc):
    """ginzaの係り受け解析結果を受け取り、文節クラスのリスト(Chunk)を返す
    """
    chunks = []
    # 文節Head番号=(形態素解析した時のトークンindex)を取得
    bunsetu_head_list = ginza.bunsetu_head_list(doc)

    # 文節に分解
    for i, bunsetu in enumerate(ginza.bunsetu_spans(doc)):
        # 文節を表すChunkクラスをインスタンス化
        chunk = Chunk()
        # 文節を形態素解析
        morphs = get_morphs(bunsetu)
        # chunkのメンバ変数にappend
        chunk.morphs = morphs
        chunks.append(chunk)

        # 係り受け解析
        for token in bunsetu.lefts:
            # 文節トークンが係る元の文節indexを取得
            chunk_idx = get_bunsetu_head_list_index(bunsetu_head_list, token.i)
            chunks[chunk_idx].dst = i

            chunks[i].srcs.append(chunk_idx)

    return chunks



def get_bunsetu_head_list_index(bunsetu_head_list, i) -> int:
    """tokenが文節の先頭を係り受け先として示さない場合があるので、それを補正
    するためのヘルパ関数
    """

    while True:
        try:
            index = bunsetu_head_list.index(i)
            return index
        except:
            i -=1
            if i == 0:
                raise ValueError
            continue


def check_meishi(morhps):
    for m in morhps:
        if m.pos == "名詞":
            return True
    return False

def get_chunk_surface(chunk, exclude_kigou=True):
    if exclude_kigou:
        return "".join([m.surface for m in chunk.morphs if m.pos != "補助記号"])
    else:
        return "".join([m.surface for m in chunk.morphs])
    