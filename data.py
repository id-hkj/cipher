from math import log, sqrt
import get


def clean(text):
	print("Cleaning Corpus")
	new_text = ""
	hav_space = True
	for letter in text:
		if 65 <= ord(letter) <= 90:
			new_text += letter
			hav_space = True
		elif 97 <= ord(letter) <= 122:
			new_text += letter.upper()
			hav_space = True
		elif (ord(letter) == 32 or ord(letter) == 10) and hav_space:
			new_text += ' '
			hav_space = False
	return new_text


def alphabetical(text):
	words = list(set(text.split(' ')))
	print("Sorting words")
	words.sort()
	return words


def frequency(text):
	words = text.split(' ')
	print("Counting words")
	freqs = {}
	for word in words:
		if word in freqs.keys():
			freqs[word] += 1
		else:
			freqs[word] = 1
	print("Sorting words")
	freqs = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[0])}
	return {k: v for k, v in sorted(freqs.items(), key=lambda item: -item[1])}
	

def mono(text, space):
	freqs = {chr(i): 0 for i in range(65,91)}
	freqs[' '] = 0
	for letter in text:
		freqs[letter] += 1
	
	total = len(text)
	if not space:
		total -= freqs[' ']
		del freqs[' ']
	
	return [i / total for i in freqs.values()]


def tetra(corpus, space): # -16 is the log of 0 for our purposes
	space = int(space)
	if not space:
		new_corp = corpus
		corpus = ""
		for letter in new_corp:
			if letter != ' ':
				corpus += letter
	freqs = {}
	for i in range(65,91 + space):
		if i < 91:
			a = chr(i)
		else:
			a = ' '
		for j in range(65,91 + space):
			if j < 91:
				b = chr(j)
			else:
				b = ' '
			for k in range(65,91 + space):
				if k < 91:
					c = chr(k)
				else:
					c = ' '
				for l in range(65,91):
					freqs[a + b + c + chr(l)] = 0
				if space:
					freqs[a + b + c + ' '] = 0
	
	total_count = 0
	for i in range(len(corpus) - 3):
		if ' ' in corpus[i:i + 4] and not space:
			continue
		freqs[corpus[i:i + 4]] += 1
		total_count += 1
	for i in range(65,91 + space):
		if i < 91:
			a = chr(i)
		else:
			a = ' '
		for j in range(65,91 + space):
			if j < 91:
				b = chr(j)
			else:
				b = ' '
			for k in range(65,91 + space):
				if k < 91:
					c = chr(k)
				else:
					c = ' '
				for l in range(65,91 + space):
					if l < 91:
						d = chr(l)
					else:
						d = ' '
					x = freqs[a + b + c + d]
					x = x / total_count
					if x == 0:
						freqs[a + b + c + d] = "-16"
					else:
						freqs[a + b + c + d] = str(log(x))
	return freqs


def inner(v1, v2):
	if len(v1) != len(v2):
		raise ValueError("Vectors of different lengths")
	total = 0
	for i in range(len(v1)):
		total += v1[i] * v2[i]
	return total


def angle(v1, v2):
	denom = inner(v1, v1) * inner(v2, v2)
	denom = sqrt(denom)
	num = inner(v1, v2)
	return num / denom


def angle_fit(text, space, norm=""):
	if not norm:
		norm = get.get_monoF("MONO.txt", space)
	this = mono(text, space)
	return angle(norm, this)


def tetra_fit(text, space, norm=""):
	if not norm:
		if space:
			norm = get.get_tetraF("TetraSPACE.txt")
		else:
			norm = get.get_tetraF("TetraNO.txt")
	total = 0
	count = 0
	for i in range(len(text) - 3):
		if ' ' in text[i:i + 4] and not space:
			continue
		total += norm[text[i:i + 4]]
		count += 1
	return total / count


def IndexCoin(text, space):
	text_f = mono(text, True)
	for i in range(27):
		text_f[i] = text_f[i] * len(text)
	if space:
		denom = len(text) * (len(text) - 1)
	else:
		denom = (len(text) - text_f[26]) * (len(text) - text_f[26] - 1)
	total = 0
	for value in text_f:
		total += value * (value - 1)
	total = (26) * total / denom
	return total
