words = open('names.txt', 'r', encoding='utf-8').read().splitlines()

# print(words[:10])
# print(len(words))

import torch
N = torch.zeros((27, 27), dtype=torch.int32) # matrix of the first char to second char. 26 chars + 1 special char = 27

chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
# stoi['<S>'] = 26
# stoi['<E>'] = 27
stoi['.'] = 0 # . means the start of the end
itos = {i:s for s,i in stoi.items()}

for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1, ix2] += 1

# notice row of <E> is all 0, and col of <S> is all zero
def visualize_N():
    import matplotlib.pyplot as plt
    plt.figure(figsize=(16,16))
    plt.imshow(N, cmap='Blues')
    plt.axis('off')
    for i in range(27):
        for j in range(27):
            chstr = itos[i] + itos[j]
            plt.text(j, i, chstr, ha="center", va="bottom", color="gray")
            plt.text(j, i, N[i, j].item(), ha="center", va="top", color="gray")
    plt.savefig("test.png")


