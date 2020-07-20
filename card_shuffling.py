import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class Deck:

    def __init__(self, size=52):
        self.size = size
        self.cards = np.arange(size)

    def random_shuffle(self):
        np.random.shuffle(self.cards)

    def pemantle_overhand_shuffle(self,k=1):
        while not k == 0:
            start = 0
            end = 0
            packages = []
            while start < len(self.cards) - 1:
                end = start + np.random.geometric(p=0.5, size = 1)[0]
                if end >= len(self.cards)-1:
                    end = len(self.cards)
                package = self.cards[start:end]
                packages.append(package)
                start = end
            self.cards = np.array(np.concatenate(packages[::-1]))
            k = k-1

    def rss(self):
        differences = self.cards - np.arange(self.size)
        return np.sqrt(np.sum(np.square(differences)))

    def rms(self):
        differences = self.cards - np.arange(self.size)
        return np.sqrt(np.sum(np.square(differences))/self.size)


def plt_rms_or_rss(n,shuffles=1,rms=False,rss=True,pemantle=False,random=True):
    rss_values = []
    for _ in range(n):
        deck = Deck()
        if rss:
            if random:
                deck.random_shuffle(n)
                rss_values.append(deck.rss())
            elif pemantle:
                deck.pemantle_overhand_shuffle(k=shuffles)
                rss_values.append(deck.rss())
        elif rms:
            if random:
                deck.random_shuffle(n)
                rss_values.append(deck.rss())
            elif pemantle:
                deck.pemantle_overhand_shuffle(k=shuffles)
                rss_values.append(deck.rss())
    sns.distplot(rss_values)
    plt.show()


plt_rms_or_rss(10000,rms=False,rss=True,pemantle=True,random=True)