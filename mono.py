from copy import deepcopy
from random import randint
import data, get

def thinkMono(text):
	coin = data.IndexCoin(text, False)
	if (1.70 <= coin <= 1.77) and data.angle_fit(text) < 0.8:
		return True
	return False


def invert(key):
	new_key = ""
	for i in range(65, 91):
		new_key += chr(key.index(chr(i)) + 65)
	
	return new_key


def encrypt(text, key):
	new_text = ""
	for letter in text:
		x = ord(letter)
		if 65 <= x <= 90:
			new_text += key[x - 65]
		else:
			new_text += letter
	return new_text


def decrypt(text, key):
	return encrypt(text, invert(key))


def atbash(text):
	return encrypt(text, "ZYXWVUTSRQPONMLKJIHGFEDCBA")


def getCaeserKey(keyNo):
	key = ""
	for i in range(26):
		key += chr((i + keyNo) % 26 + 65)
	return key


def caeser(text, key):
	return encrypt(text, getCaeserKey(key))


def caeserBruteTetra(text):
	fitness = []
	tetragram_load = get.get_tetraF("TetraNO.txt")
	for i in range(26):
		tempText = caeser(text, i)
		fitness.append(data.tetra_fit(tempText, False, tetragram_load))
	return caeser(text, fitness.index(max(fitness)))


def caeserCrib(text, crib):
	possible = []
	for i in range(26):
		new_inversion = caeser(crib, i)
		if new_inversion in text:
			possible.append(i)
	return possible


def caeserBruteMono(text):
	fitness = []
	monogram_load = get.get_monoF("MONO.txt", False)
	for i in range(26):
		tempText = caeser(text, i)
		fitness.append(data.angle_fit(tempText, False, monogram_load))
	return caeser(text, fitness.index(max(fitness)))


def HCF(m, n):
	while n != 0:
		m = m % n
		m, n = n, m
	return m


def LCM(m, n):
	return (m * n) // HCF(m, n)


def coprime(m, n):
	if HCF(m, n) == 1:
		return True
	return False


def inverse(x, m):
	t, tt, r, rr = 0, 1, m, x
	while rr != 0:
		q = r // rr
		t, tt = tt, t - q * tt
		r, rr = rr, r - q * rr
	if r != 1:
		return -1
	return t % m


def affineValid(a):
	return coprime(a, 26)


def getAffineKey(a, b):
	if not affineValid(a):
		return ""
	key = ""
	for i in range(26):
		key += chr(((i * a + b) % 26) + 65)
	return key


def affineEn(text, a, b):
	key = getAffineKey(a, b)
	if not key:
		raise KeyError ("Invalid a")
	return encrypt(text, key)


def affineDe(text, a, b):
	a = inverse(a, 26)
	return affineEn(text, a, -b * a)


def affineBruteTetra(text):
	high = -100
	hiA = 0
	hiB = 0
	tetragram_load = get.get_tetraF("TetraNO.txt")
	for a in range(26):
		if not affineValid(a):
			continue
		for b in range(26):
			tempText = affineEn(text, a, b)
			fitness = data.tetra_fit(tempText, False, tetragram_load)
			if fitness > high:
				high, hiA, hiB = fitness, a, b
	return affineEn(text, hiA, hiB)


def affineBruteMono(text):
	high = -1.0
	hiA = 0
	hiB = 0
	monogram_load = get.get_monoF("MONO.txt", False)
	this_mono = data.mono(text, False)
	mono_shuffle = [0 for i in range(26)]
	for a in range(26):
		if not affineValid(a):
			continue
		for b in range(26):
			for i in range(26):
				mono_shuffle[i] = this_mono[(a * i + b) % 26]
			fitness = data.angle(monogram_load, mono_shuffle)
			if fitness > high:
				high, hiA, hiB = fitness, a, b
	return affineDe(text, hiA, hiB)


def affineCrib(text, crib):
	possible = []
	for a in range(26):
		if not affineValid(a):
			continue
		for b in range(26):
			new_inversion = affineEn(crib, a, b)
			if new_inversion in text:
				possible.append([a, b])
	print(possible)
	return possible


def keywordGen(word, type=0):
	key = ""
	last = -1
	for letter in word:
		if ord(letter) > last:
			last = ord(letter)
		if not letter in key:
			key += letter
	
	if type == 0:
		for i in range(65, 91):
			if not chr(i) in key:
				key += chr(i)
	elif type == 1:
		for i in range(ord(key[-1]) - 65, ord(key[-1]) - 39):
			if not chr((i % 26) + 65) in key:
				key += chr((i % 26) + 65)
	elif type == 2:
		for i in range(last - 65, last - 39):
			if not chr((i % 26) + 65) in key:
				key += chr((i % 26) + 65)
	return key


def keywordEn(text, word, type):
	key = keywordGen(word, type)
	return encrypt(text, key)


def keyword2En(text, key1, key2):
	key = ["" for i in range(26)]
	print(key1, key2)
	for i in range(26):
		key[ord(key1[i]) - 65] = key2[i]
	key = "".join(key)
	print(key)
	return encrypt(text, key)


def keywordDe(text, word, type):
	key = keywordGen(word, type)
	return encrypt(text, invert(key))


def keywordAttack(text):
	words = get.get_words("ALPHA.txt", 'a')
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_result = -100
	best_word = words[0]
	best_i = 0
	for i in range(3):
		for word in words:
			tempText = keywordDe(text, word, i)
			fit = data.tetra_fit(tempText, False, tetragram_load)
			if fit > best_result:
				best_result, best_word, best_i = fit, word, i
				print("New high fitness", fit, word, i)
	return keywordDe(text, best_word, best_i)


def best_mono_key(text):
	mono_f = get.get_monoF("MONO.txt", False)
	freqs = [i for i in range(26)]
	freqs.sort(key = lambda i: -mono_f[i])
	this_mono = data.mono(text, False)
	key = ["" for i in range(26)]
	for i in range(26):
		x = this_mono.index(max(this_mono))
		this_mono[x] = -1
		key[x] = chr(freqs[i] + 65)
	return "".join(key)


def brute(text):
	print("Compiling parent key + plaintext")
	parent_k = best_mono_key(text)
	tetragram_load = get.get_tetraF("TetraNO.txt")
	parent_t = decrypt(text, parent_k)
	parent_f = data.tetra_fit(parent_t, False, tetragram_load)
	count = 0
	same_count = 0
	print("Starting main. Parent key:", parent_k)
	
	while count < 100000 and same_count < 100:
		child_k = list(parent_k)
		x, y = randint(0, 25), randint(0, 25)
		child_k[x], child_k[y] = child_k[y], child_k[x]
		child_k = "".join(child_k)
		child_t = decrypt(text, child_k)
		child_f = data.tetra_fit(child_t, False, tetragram_load)
		if child_f == parent_f:
			same_count += 1
			parent_k, parent_t, parent_f = child_k, child_t, child_f
			print(parent_k, parent_f)
			count = 0
		elif child_f > parent_f:
			parent_k, parent_t, parent_f = child_k, child_t, child_f
			print(parent_k, parent_f)
			count = 0
			same_count = 0
		
		count += 1
	return parent_t
