# coding: UTF-8
from LanguageKnock_30 import makeMecabPattern
import numpy as np
import matplotlib.pyplot as plt
# matplotlib用日本語フォントのセット
from matplotlib.font_manager import FontProperties
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()


class extractVersMethods:

    def checkNovel(self, novelListS):
        wordCounter = {}
        for sentenseList in novelListS:
            for word in sentenseList:
                if word["surface"] != "。" and word["surface"] != "、" and word["surface"] != "「" and word["surface"] != "」" and word["surface"] != "…":
                    if word["surface"] in wordCounter.keys():
                        wordCounter[word["surface"]] = wordCounter[word["surface"]] + 1
                    else:
                        wordCounter.setdefault(word["surface"], 1)
        sortedWordCounter = sorted(wordCounter.items(), key=lambda x:x[1], reverse=True)
        
        return sortedWordCounter
    
    def countAllWord(self, sortedWordCounter):
        allWord=0
        for value in sortedWordCounter:
            allWord = allWord + value[1]
        return allWord

if __name__ == '__main__':
    x = []
    y = []
    cal = extractVersMethods()
    novelListS = makeMecabPattern()
    ans = cal.checkNovel(novelListS)
    allWord = cal.countAllWord(ans)
    for i in range(0, len(ans)):
        x.append(i)
        y.append(ans[i][1]/allWord)
    plt.plot(x, y)
    ax = plt.gca()
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show()
    
