def chayotes(n_min, pack):
    if n_min % pack == 0:
        num_packs = n_min // pack

        return num_packs * pack
    else:
        num_packs = (n_min // pack) + 1
        return num_packs * pack
  

n = int(input())
k = int(input())

print(chayotes(n, k))