import mono, data, get
from itertools import product
from copy import deepcopy
from random import randint, shuffle

def encrypt(text, keys):
	new_t = ""
	keyNo = len(keys)
	for i in range(len(text)):
		new_t += mono.encrypt(text[i], keys[i % keyNo])
	return new_t


def decrypt(text, keys):
	new_k = []
	for key in keys:
		new_k.append(mono.invert(key))
	return encrypt(text, new_k)


def slicer(text, n):
	new_texts = []
	for i in range(n):
		new_texts.append(text[i::n])
	return new_texts


def get_key_len(text):
	coin = 0
	count = 0
	while not(1.7 <= coin <= 1.8):
		count += 1
		slices = slicer(text, count)
		total = 0
		for i in range(count):
			total += data.IndexCoin(slices[i], False)
		coin = total / count
		print(count, coin)
	return str(count), str(coin)


def signature(text):
	freqs = data.mono(text, False)
	freqs.sort()
	return freqs


def twist(a, b):
	twist = 0
	for i in range(13):
		twist += (a[i] - b[i])
	for i in range(13, 26):
		twist += (b[i] - a[i])
	return twist


def average_sigs(sigs):
	total = [0 for i in range(26)]
	for arg in sigs:
		for i in range(26):
			total[i] += arg[i]
	for i in range(26):
		total[i] = total[i] / len(sigs)
	return total


def getlentwist(text):
	monos = get.get_monoF("MONO.txt", False)
	last = 0
	twst = 0
	count = 0
	while twst >= last:
		count += 1
		last = twst
		slices = slicer(text, count)
		for j in range(count):
			slices[j] = signature(slices[j])
		avg = average_sigs(slices)
		twst = twist(monos, avg)
	return count - 1


def vigEn(text, word):
	total_len = len(text)
	word_len = len(word)
	text = slicer(text, word_len)
	for i in range(word_len):
		text[i] = mono.caeser(text[i], (ord(word[i]) - 65) % 26)
	final = ""
	for i in range(total_len):
		final += text[i % word_len][i // word_len]
	return final


def vigDe(text, word):
	total_len = len(text)
	word_len = len(word)
	text = slicer(text, word_len)
	for i in range(word_len):
		text[i] = mono.caeser(text[i], -(ord(word[i]) - 65) % 26)
	final = ""
	for i in range(total_len):
		final += text[i % word_len][i // word_len]
	return final


def vigAutoDe(text):
	best = -100
	tetragram_load = get.get_tetraF("TetraNO.txt")
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(1, 21):
		combos = list(product(letters, repeat=i))
		for combo in combos:
			decryption = vigDe(text, combo)
			fit = data.tetra_fit(decryption, False, tetragram_load)
			if fit >= best:
				best = fit
				print(combo, fit)
				print(decryption)


def vigAutoDict(text):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_result = -100
	best_word = words[0]
	for word in words:
		tempText = vigDe(text, word)
		fit = data.tetra_fit(tempText, False, tetragram_load)
		if fit > best_result:
			best_result, best_word = fit, word
			print("New high fitness", fit, word)
	return vigDe(text, best_word)


def vigAutoHill(text, m):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	key = ['A' for i in range(m)]
	best_key = deepcopy(key)
	fit_now = data.tetra_fit(text, False, tetragram_load)
	unfinished = True
	while unfinished:
		fit_then = fit_now
		for i in range(m):
			fit_max = fit_now
			for j in range(65, 91):
				key[i] = chr(j)
				tempText = vigDe(text, key)
				fit_now = data.tetra_fit(tempText, False, tetragram_load)
				if fit_now > fit_max:
					fit_max = fit_now
					best_key[i] = chr(j)
			key = deepcopy(best_key)
			fit_now = fit_max
		if fit_now == fit_then:
			unfinished = False
	print(key)
	return vigDe(text, key)


def vigMono(text, m):
	slices = slicer(text, m)
	for i in range(m):
		slices[i] = mono.caeserBruteMono(slices[i])
	final = ""
	for i in range(len(text)):
		final += slices[i % m][i // m]
	return final


def beaufort(text, let_key):
	new_text = ""
	key = []
	key_len = len(let_key)
	for item in let_key:
		key.append(ord(item)-65)
	for i in range(len(text)):
		new_text += chr((key[i%key_len] - ord(text[i]) + 65) % 26 + 65)
	return new_text


def beauAutoDe(text):
	best = -100
	tetragram_load = get.get_tetraF("TetraNO.txt")
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(1, 21):
		combos = list(product(letters, repeat=i))
		for combo in combos:
			decryption = beaufort(text, combo)
			fit = data.tetra_fit(decryption, False, tetragram_load)
			if fit >= best:
				best = fit
				print(combo, fit)
				print(decryption)


def beauAutoDict(text):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_result = -100
	best_word = words[0]
	for word in words:
		tempText = beaufort(text, word)
		fit = data.tetra_fit(tempText, False, tetragram_load)
		if fit > best_result:
			best_result, best_word = fit, word
			print("New high fitness", fit, word)
	return beaufort(text, best_word)


def beauAutoHill(text, m):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	key = ['A' for i in range(m)]
	best_key = deepcopy(key)
	fit_now = data.tetra_fit(text, False, tetragram_load)
	unfinished = True
	while unfinished:
		fit_then = fit_now
		for i in range(m):
			fit_max = fit_now
			for j in range(65, 91):
				key[i] = chr(j)
				tempText = beaufort(text, key)
				fit_now = data.tetra_fit(tempText, False, tetragram_load)
				if fit_now > fit_max:
					fit_max = fit_now
					best_key[i] = chr(j)
			key = deepcopy(best_key)
			fit_now = fit_max
		if fit_now == fit_then:
			unfinished = False
	print(key)
	return beaufort(text, key)


def beauMono(text, m):
	slices = slicer(text, m)
	monogram_load = get.get_monoF("MONO.txt", False)
	for i in range(m):
		best = (-1, 0)
		for j in range(26):
			tempText = mono.encrypt(slices[i], mono.atbash(mono.getCaeserKey(j)))
			fitnow = data.angle_fit(tempText, False, monogram_load)
			if fitnow > best[0]:
				best = (fitnow, j)
		slices[i] = mono.encrypt(slices[i], mono.atbash(mono.getCaeserKey(best[1])))
	final = ""
	for i in range(len(text)):
		final += slices[i % m][i // m]
	return final


def beauvarAutoDe(text):
	best = -100
	tetragram_load = get.get_tetraF("TetraNO.txt")
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(1, 21):
		combos = list(product(letters, repeat=i))
		for combo in combos:
			decryption = vigDe(text, combo)
			fit = data.tetra_fit(decryption, False, tetragram_load)
			if fit >= best:
				best = fit
				print(combo, fit)
				print(decryption)


def beauvarAutoDict(text):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_result = -100
	best_word = words[0]
	for word in words:
		tempText = vigEn(text, word)
		fit = data.tetra_fit(tempText, False, tetragram_load)
		if fit > best_result:
			best_result, best_word = fit, word
			print("New high fitness", fit, word)
	return vigEn(text, best_word)


def beauvarAutoHill(text, m):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	key = ['A' for i in range(m)]
	best_key = deepcopy(key)
	fit_now = data.tetra_fit(text, False, tetragram_load)
	unfinished = True
	while unfinished:
		fit_then = fit_now
		for i in range(m):
			fit_max = fit_now
			for j in range(65, 91):
				key[i] = chr(j)
				tempText = vigEn(text, key)
				fit_now = data.tetra_fit(tempText, False, tetragram_load)
				if fit_now > fit_max:
					fit_max = fit_now
					best_key[i] = chr(j)
			key = deepcopy(best_key)
			fit_now = fit_max
		if fit_now == fit_then:
			unfinished = False
	print(key)
	return vigEn(text, key)


def porta(text, key, style):
	keys = []
	total_len = len(text)
	key_len = len(key)
	if style == 0:
		for letter in key:
			keys.append((ord(letter) - 65) // 2)
	else:
		for letter in key:
			keys.append(((-ord(letter) - 64) % 26) // 2)
	text = slicer(text, key_len)
	for i in range(len(keys)):
		key = ""
		for j in range(13):
			key += chr(78 + ((j+keys[i]) % 13))
		for j in range(13):
			key += chr(65 + ((j-keys[i]) % 13))
		text[i] = mono.encrypt(text[i], key)
	final = ""
	for i in range(total_len):
		final += text[i % key_len][i // key_len]
	return final


def portaAutoDe(text):
	best = -100
	tetragram_load = get.get_tetraF("TetraNO.txt")
	letters = "ACEGIKMOQSUWY"
	for i in range(1, 21):
		combos = list(product(letters, repeat=i))
		for combo in combos:
			decryption = porta(text, combo, 0)
			fit = data.tetra_fit(decryption, False, tetragram_load)
			if fit >= best:
				best = fit
				print(combo, fit)
				print(decryption)


def find_eng(word):
	words = get.get_words("ALPHA.txt", 'a')
	poss1 = []
	poss2 = []
	alll = [0, 1]
	for letter in word:
		x = (ord(letter) - 65) // 2
		poss1.append([chr(x * 2 + 65), chr(x * 2 + 66)])
		poss2.append([chr((-x % 13) * 2 + 65), chr((-x % 13) * 2 + 66)])
	
	alll = list(product(alll, repeat = (len(word))))
	for poss in alll:
		w1, w2 = "", ""
		for i in range(len(word)):
			w1 += poss1[i][poss[i]]
			w2 += poss2[i][poss[i]]
		if w1 in words:
			print(w1)
		if w2 in words:
			print(w2)


def portaAutoDict(text):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_result = -100
	best_word = words[0]
	best_i = 0
	for word in words:
		for i in range(2):
			tempText = porta(text, word, i)
			fit = data.tetra_fit(tempText, False, tetragram_load)
			if fit > best_result:
				best_result, best_word, best_i = fit, word, i
				print("New high fitness", fit, word, i)
	return porta(text, best_word, best_i)


def portaAutoHill(text, m):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	key = ['A' for i in range(m)]
	best_key = deepcopy(key)
	fit_now = data.tetra_fit(text, False, tetragram_load)
	unfinished = True
	while unfinished:
		fit_then = fit_now
		for i in range(m):
			fit_max = fit_now
			for j in range(65, 91):
				key[i] = chr(j)
				tempText = porta(text, key, 0)
				fit_now = data.tetra_fit(tempText, False, tetragram_load)
				if fit_now > fit_max:
					fit_max = fit_now
					best_key[i] = chr(j)
			key = deepcopy(best_key)
			fit_now = fit_max
		if fit_now == fit_then:
			unfinished = False
	print(key)
	return porta(text, key, 0)


def portaMono(text, m):
	slices = slicer(text, m)
	monogram_load = get.get_monoF("MONO.txt", False)
	for i in range(m):
		best = (-1, 0)
		for j in range(65, 91, 2):
			tempText = porta(slices[i], chr(j), 0)
			fitnow = data.angle_fit(tempText, False, monogram_load)
			if fitnow > best[0]:
				best = (fitnow, j)
		print(chr(best[1]))
		slices[i] = porta(slices[i], chr(best[1]), 0)
	final = ""
	for i in range(len(text)):
		final += slices[i % m][i // m]
	return final


def bellaso(text, key):
	all_keys = []
	
	keys = []
	total_len = len(text)
	key_len = len(key)
	for letter in key:
		keys.append(ord(letter) - 65)
	text = slicer(text, key_len)
	for i in range(len(keys)):
		key = ""
		for j in range(13):
			key += chr(78 + ((j-keys[i]) % 13))
		for j in range(13):
			key += chr(65 + ((j+keys[i]) % 13))
		if keys[i] >= 13:
			key = mono.atbash(key)
		text[i] = mono.encrypt(text[i], key)
	final = ""
	for i in range(total_len):
		final += text[i % key_len][i // key_len]
	return final


def bellAutoDe(text):
	best = -100
	tetragram_load = get.get_tetraF("TetraNO.txt")
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(1, 21):
		combos = list(product(letters, repeat=i))
		for combo in combos:
			decryption = bellaso(text, combo)
			fit = data.tetra_fit(decryption, False, tetragram_load)
			if fit >= best:
				best = fit
				print(combo, fit)
				print(decryption)


def bellAutoDict(text):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_result = -100
	best_word = words[0]
	for word in words:
		tempText = bellaso(text, word)
		fit = data.tetra_fit(tempText, False, tetragram_load)
		if fit > best_result:
			best_result, best_word = fit, word
			print("New high fitness", fit, word)
	return bellaso(text, best_word)


def bellAutoHill(text, m):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	key = ['A' for i in range(m)]
	best_key = deepcopy(key)
	fit_now = data.tetra_fit(text, False, tetragram_load)
	unfinished = True
	while unfinished:
		fit_then = fit_now
		for i in range(m):
			fit_max = fit_now
			for j in range(65, 91):
				key[i] = chr(j)
				tempText = bellaso(text, key)
				fit_now = data.tetra_fit(tempText, False, tetragram_load)
				if fit_now > fit_max:
					fit_max = fit_now
					best_key[i] = chr(j)
			key = deepcopy(best_key)
			fit_now = fit_max
		if fit_now == fit_then:
			unfinished = False
	print(key)
	return bellaso(text, key)


def bellMono(text, m):
	slices = slicer(text, m)
	monogram_load = get.get_monoF("MONO.txt", False)
	for i in range(m):
		best = (-1, 0)
		for j in range(65, 91):
			tempText = bellaso(slices[i], chr(j))
			fitnow = data.angle_fit(tempText, False, monogram_load)
			if fitnow > best[0]:
				best = (fitnow, j)
		print(chr(best[1]))
		slices[i] = bellaso(slices[i], chr(best[1]))
	final = ""
	for i in range(len(text)):
		final += slices[i % m][i // m]
	return final


def periodAffineEn(text, key):
	total_len = len(text)
	word_len = len(word)
	text = slicer(text, word_len)
	for i in range(word_len):
		text[i] = mono.affineEn(text[i], key[i][0], key[i][1])
	final = ""
	for i in range(total_len):
		final += text[i % word_len][i // word_len]
	return final


def periodAffineDe(text, key):
	total_len = len(text)
	word_len = len(key)
	text = slicer(text, word_len)
	for i in range(word_len):
		text[i] = mono.affineDe(text[i], key[i][0], key[i][1])
	final = ""
	for i in range(total_len):
		final += text[i % word_len][i // word_len]
	return final


def affineAuto(text, m):
	slices = slicer(text, m)
	for i in range(m):
		slices[i] = mono.affineBruteMono(slices[i])
	final = ""
	for i in range(len(text)):
		final += slices[i % m][i // m]
	return final


def quagIEn(text, key, key2):
	top_k = mono.keywordGen(key, 0)
	total_len = len(text)
	word_len = len(word)
	text = slicer(text, word_len)
	for i in range(word_len):
		text[i] = mono.affineEn(text[i], key[i][0], key[i][1])
	final = ""
	for i in range(total_len):
		final += text[i % word_len][i // word_len]
	return final


def AutoPolyDe(text, m):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	big_count = 0
	fit_best = data.tetra_fit(text, False, tetragram_load)
	slices = slicer(text, m)
	parentK = [list(mono.best_mono_key(slices[i])) for i in range(m)]
	
	while big_count < (m * m) * 1000000:
		for i in range(m):
			shuffle(parentK[i])
			tempText = decrypt(text, parentK)
			parentF = data.tetra_fit(tempText, False, tetragram_load)
			little_count = 0
			while little_count < 1000:
				childK = deepcopy(parentK)
				a, b = randint(0, 25), randint(0, 25)
				childK[i][a], childK[i][b] = childK[i][b], childK[i][a]
				tempText = decrypt(text, childK)
				childF = data.tetra_fit(tempText, False, tetragram_load)
				
				if childF > parentF:
					parentK[i][a], parentK[i][b] = parentK[i][b], parentK[i][a]
					parentF = childF
					little_count = 0
				little_count += 1
				if childF > fit_best:
					fit_best = childF
					parentF = childF
					parentK = deepcopy(childK)
					big_count = 0
					print(parentK, tempText, childF)
				big_count += 1
