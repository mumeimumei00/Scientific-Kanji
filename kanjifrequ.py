import MeCab

tagger = MeCab.Tagger("-Owakati")

text = "はじめまして、アリと申します"

print(tagger.parse(text))
