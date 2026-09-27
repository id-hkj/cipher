CORPUS = "Corpus.txt"
ALPHA = "ALPHA.txt"
FREQ = "FREQ.txt"
MONO = "MONO.txt"
TETRAS = "TetraSPACE.txt"
TETRAN = "TetraNO.txt"

def get_words(in_file, type):
	print("Opening word list")
	words = open(in_file, 'r', encoding='utf-8').read().split('\n')
	if type == 'a':
		return words
	elif type == 'f':
		for i in range(len(words)):
			words[i] = words[i].split(' ')
		return dict(words)


def get_monoF(in_file, space):
	print("Opening frequency data")
	data = open(in_file, 'r', encoding='utf-8').read().split('\n')
	freqs = []
	space = int(space)
	for i in range(26 + space):
		freqs.append(float(data[i].split(' ')[space]))
	return freqs


def get_tetraF(in_file):
	print("Opening frequency data")
	data = open(in_file, 'r', encoding='utf-8').read()
	data = data.split('\n')
	for i in range(len(data)):
		data[i] = [data[i][:4], float(data[i][5:])]
	return dict(data)
