
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']
class GraphVisuzalization:
    def __init__(self):

        self.visual = []

    def addEdge(self,a,b):
        temp = [a,b]
        self.visual.append(temp)
        
    def visuzalize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

KanjiList =["日本", "本日", "先日", "学校", "学生", "先生", "会社", "本人", "社会", "先人", "語学", "本学", "学会", "本社", "日学", "日生", "学語", "語生", "先学", "生会", "人会", "人学", "会生", "先社", "社生", "本語", "語本", "人社", "学人", "校人"]
G = GraphVisuzalization()

for word in KanjiList:
    G.addEdge(word[0],word[1])

G.visuzalize()
