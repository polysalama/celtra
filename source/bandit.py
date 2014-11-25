import urllib.request
from scipy.stats import beta
import sys


def bandit(url):
    #stevec zmag
    wins = 0
    #stevilo avtomatov in potegov
    num_of_machines = int(urllib.request.urlopen(url + '/machines').read())
    num_of_pulls = int(urllib.request.urlopen(url + '/pulls').read())
    #stevec zmag posameznega avtomata
    machines_wins = [0] * num_of_machines
    machines_fail = [0] *num_of_machines
    for j in range(num_of_pulls):
        samples = []
        #vzorcimo vsak avtomat iz njegove apriorne beta distribucije
        for k in range(num_of_machines):
            prior = beta(machines_wins[k] + 1, 1 + machines_fail[k] - machines_wins[k])
            samples += [prior.rvs()]
        #izberemo avtomat z najvecjo vrednosjo vzorca
        selected = samples.index(max(samples))
        #potegnemo izbran avtomat, poveca se stevec zmag avtomata in stevec skupnih uspesnih potegov
        pull = int(urllib.request.urlopen(url + "/" + str(selected + 1) + "/" + str(j + 1)).read())
        machines_wins[selected] += pull
        machines_fail[selected] += 1
        wins += pull
    return wins






if __name__ == '__main__':
    print(bandit(sys.argv[1]))