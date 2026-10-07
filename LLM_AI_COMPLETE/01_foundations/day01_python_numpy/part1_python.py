sentence = "the cat sat on the mat"
tokens = sentence.split()
print(tokens)

vocab = {}
for tok in tokens:
    if tok not in vocab:
        vocab[tok] = len(vocab)
print(vocab)

ids = [vocab[t] for t in tokens]
print(ids)


def encode(text, vocab):
    return [vocab[w] for w in text.split()]


def decode(ids, vocab):
    id_to_word = {i: w for w, i in vocab.items()}
    return " ".join(id_to_word[i] for i in ids)


print(encode("the cat sat", vocab))
print(decode([0, 4, 2], vocab))