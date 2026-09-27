import get, data
from copy import deepcopy
from random import randint, shuffle
from math import factorial

def inverse(perm):
	inv = []
	for i in range(len(perm)):
		inv.append(perm.index(i))
	return inv


def get_perm(word, repeat):
	if repeat:
		nums = [ord(let) - 65 for let in word]
		perm = [-1 for i in word]
		count = 0
		for i in range(26):
			for j in range(len(nums)):
				if nums[j] == i:
					perm[j] = count
					count += 1
		return perm
	nums = [ord(let) - 65 for let in word]
	no_rep = []
	for num in nums:
		if not num in no_rep:
			no_rep.append(num)
	for i in range(len(no_rep)):
		while not i in no_rep:
			for j in range(len(no_rep)):
				if no_rep[j] > i:
					no_rep[j] -= 1
	return no_rep


def find_eng(perm):
	words = get.get_words("ALPHA.txt", 'a')
	for i in range(2):
		for word in words:
			if get_perm(word, i) == perm:
				print(word, i)


def get_blocks(text, size):
	blocks = [text[i:i+size] for i in range(0, len(text), size)]
	while len(blocks[-1]) != size:
		blocks[-1] += "X"
	return blocks


def permEn(text, perm):
	blocks = get_blocks(text, len(perm))
	encode = [["X" for itemz in perm] for block in blocks]
	for i in range(len(blocks)):
		for j in range(len(perm)):
			encode[i][j] = blocks[i][perm.index(j)]
		encode[i] = "".join(encode[i])
	return "".join(encode)


def permDe(text, perm):
	return permEn(text, inverse(perm))


def getAllPerms(n):
	allz = [[i for i in range(n)]]
	ci = [0 for i in range(n)]
	i = 0
	while i < n:
		if ci[i] < i:
			new = deepcopy(allz[-1])
			if i % 2 == 0:
				new[0], new[i] = new[i], new[0]
			else:
				new[ci[i]], new[i] = new[i], new[ci[i]]
			allz.append(new)
			ci[i] += 1
			i = 0
		elif ci[i] == i:
			ci[i] = 0
			i += 1
	return allz


def intToFact(n):
	done = False
	backwards = []
	count = 1
	while n != 0:
		subtracter = n % count
		backwards.append(subtracter)
		n -= subtracter
		n = n // count
		count += 1
	return [backwards[-(i+1)] for i in range(len(backwards))]


def factToInt(n):
	total = 0
	for i in range(len(n)):
		total += n[-(i + 1)] * factorial(i)
	return total


def factToPerm(n, m):
	for i in range(m - len(n)):
		n.insert(0, 0)
	perm = [-1 for i in range(m)]
	available = [i for i in range(m)]
	for i in range(m):
		perm[available[n[i]]] = m - i
		available.pop(n[i])
	return perm


def permToFact(n):
	first_len = len(n)
	fact = [0 for i in range(0, first_len)]
	for i in range(first_len, 0, -1):
		print(fact)
		fact[first_len - i] = n.index(i)
		n.pop(n.index(i))
	return fact


def getPerm(n, m):
	return factToPerm(intToFact(n), m)


def findPerm(perm):
	return factToInt(permToFact(perm))


def permBrute(text):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_fit = data.tetra_fit(text, False, tetragram_load)
	for i in range(1, len(text)):
		perms = getAllPerms(i)
		for perm in perms:
			tempText = permDe(text, perm)
			fit = data.tetra_fit(tempText, False, tetragram_load)
			if fit > best_fit:
				print(tempText)
				print(perm, fit)
				best_fit = fit


def permHill(text, keyL):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_fit = data.tetra_fit(text, False, tetragram_load)
	parent = [i for i in range(keyL)]
	shuffle(parent)
	count = 0
	while count < 100 * keyL:
		child = deepcopy(parent)
		if randint(0, 1) == 0:
			a, b = randint(0, keyL - 1), randint(0, keyL - 1)
			child[a], child[b] = child[b], child[a]
		else:
			a = randint(0, keyL - 1)
			child = child[a:]
			for i in range(keyL - len(child)):
				child.append(parent[i])
		tempText = permDe(text, child)
		newFit = data.tetra_fit(tempText, False, tetragram_load)
		if (newFit > best_fit) or ((newFit + 0.13 > best_fit) and (randint(1, 20) == 1)):
			parent = deepcopy(child)
			best_fit = newFit
			count = 0
			print("NEW HIGH(?) FITNESS:", best_fit, parent)
		count += 1
	return permDe(text, parent)


def scytaleEn(text, h, w):
	while len(text) < w * h:
		text += " "
	matrix = [[	text[i * w + j] for j in range(w)] for i in range(h)]
	final = ""
	for i in range(w):
		for j in range(h):
			final += matrix[j][i] if matrix[j][i] != ' ' else ""
	return final


def scytaleDe(text, w, h):
	return scytaleEn(text, h, w)


def scytaleBrute(text):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_fit = data.tetra_fit(text, False, tetragram_load)
	best = (0, 0)
	for i in range(len(text)):
		for j in range(len(text)):
			tempText = scytaleDe(text, i, j)
			if len(tempText) == len(text):
				fit = data.tetra_fit(tempText, False, tetragram_load)
				if fit > best_fit:
					best_fit = fit
					best = (i, j)
					print("NEW HIGH FIT", fit, best)
					print(tempText)
	return scytaleDe(text, best[0], best[1])


def twistEn(text, key, twist):
	h, w = len(text) // key, key
	matrix = [[	text[i * w + j] for j in range(w)] for i in range(h)]
	for i in range(h):
		new = [matrix[i][(j + (twist * i)) % w] for j in range(w)]
		for j in range(w):
			matrix[i][j] = new[j]
	final = ""
	for i in range(w):
		for j in range(h):
			final += matrix[j][i]
	return final


def twistDe(text, key, twist):
	w, h = len(text) // key, key
	matrix = [[	text[j * w + i] for j in range(h)] for i in range(w)]
	final = ""
	for i in range(w):
		new = [matrix[i][(j + (-twist * i)) % h] for j in range(h)]
		final += "".join(new)
	return final


def twistBrute(text):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_fit = data.tetra_fit(text, False, tetragram_load)
	best = (0, 0)
	for i in range(1, 20):
		for j in range(1, len(text)):
			if len(text) % j != 0:
				continue
			tempText = twistDe(text, j, i)
			fit = data.tetra_fit(tempText, False, tetragram_load)
			if fit > best_fit:
				best_fit = fit
				best = (j, i)
				print("NEW HIGH FIT", fit, best)
				print(tempText)
	return twistDe(text, best[0], best[1])


def columnEn(text, perm):
	key_len = len(perm)
	while len(text) % key_len != 0:
		text += ' '
	columns = [text[i*key_len:(i+1)*key_len] for i in range(len(text)//key_len)]
	final = ''
	
	for i in range(key_len):
		curr_col = perm.index(i)
		for j in range(len(columns)):
			if columns[j][curr_col] != ' ':
				final += columns[j][curr_col]
	return final


def columnDe(text, perm):
	perm = inverse(perm)
	key_len = len(perm)
	row_no = len(text) // key_len
	if len(text) % key_len != 0:
		row_no += 1
	columns = [['' for j in range(key_len)] for i in range(row_no)]
	counter = 0
	full_cols = len(text) % key_len
	for i in range(key_len):
		for j in range(row_no):
			if j + 1 == row_no and perm[i] - full_cols >= 0:
				continue

			columns[j][i] = text[counter]
			counter += 1

	final = ''
	for i in range(row_no):
		for j in range(key_len):
			final += columns[i][perm.index(j)]
	return final


def colBrute(text):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_fit = data.tetra_fit(text, False, tetragram_load)
	for i in range(1, len(text)):
		perms = getAllPerms(i)
		for perm in perms:
			tempText = columnDe(text, perm)
			fit = data.tetra_fit(tempText, False, tetragram_load)
			if fit > best_fit:
				print(tempText)
				print(perm, fit)
				best_fit = fit


def colHill(text, keyL):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_fit = data.tetra_fit(text, False, tetragram_load)
	parent = [i for i in range(keyL)]
	shuffle(parent)
	count = 0
	while count < 100 * keyL:
		child = deepcopy(parent)
		if randint(0, 1) == 0:
			a, b = randint(0, keyL - 1), randint(0, keyL - 1)
			child[a], child[b] = child[b], child[a]
		else:
			a = randint(0, keyL - 1)
			child = child[a:]
			for i in range(keyL - len(child)):
				child.append(parent[i])
		tempText = columnDe(text, child)
		newFit = data.tetra_fit(tempText, False, tetragram_load)
		if (newFit > best_fit) or ((newFit + 0.13 > best_fit) and (randint(1, 20) == 1)):
			parent = deepcopy(child)
			best_fit = newFit
			count = 0
			print("NEW HIGH(?) FITNESS:", best_fit, parent)
		count += 1
	return columnDe(text, parent)


def doubleColEn(text, k1, k2):
	return columnEn(columnEn(text, k1), k2)


def doubleColDe(text, k1, k2):
	return columnDe(columnDe(text, k2), k1)


def railEn(text, rails, skips):
	text = (' ' * skips) + text
	rows = ['' for i in range(rails)]
	consts = ((rails - 1) * 2)
	
	for i in range(len(text)):
		if text[i] == ' ':
			continue
		if i % consts == 0:
			rows[0] += text[i]
		elif i % consts == rails - 1:
			rows[-1] += text[i]
		elif i % consts < rails - 1:
			rows[i % consts] += text[i]
		else:
			rows[(consts - i) % consts] += text[i]
	final = ''
	for row in rows:
		final += row
	return final



def railDe(text, rails, skips):
	rows = ['' for i in range(rails)]
	text_len = skips + len(text)
	consts = ((rails - 1) * 2)
	ends_away = text_len + (consts - (text_len % consts))
	row_lens = [2 * (ends_away // consts) for _ in range(rails - 2)]
	row_lens.insert(0, ends_away // consts)
	row_lens.append(ends_away // consts)
	for i in range(ends_away - text_len):
		if i < rails - 1:
			row_lens[i+1] -= 1
		else:
			row_lens[2 * rails - i - 3] -= 1
	for i in range(skips):
		if i % consts == 0:
			rows[0] += ' '
			row_lens[0] -= 1
		elif i % consts == rails - 1:
			rows[-1] += ' '
			row_lens[-1] -= 1
		elif i % consts < rails - 1:
			rows[i % consts] += ' '
			row_lens[i % consts] -= 1
		else:
			rows[(consts - i) % consts] += ' '
			row_lens[(consts - i) % consts] -= 1
	running_sum = 0
	for i in range(rails):
		rows[i] += text[running_sum:running_sum + row_lens[i]]
		running_sum += row_lens[i]
	final = ''
	for i in range(len(text) + skips):
		if (i % consts) == 0:
			final += rows[0][i//consts]
		elif (i % consts) == rails - 1:
			final += rows[-1][i//consts]
		elif (i % consts) < rails - 1:
			final += rows[i%consts][2 * (i//consts)]
		else:
			final += rows[consts - i%consts][2 * (i//consts) + 1]
			
		if final[-1] == ' ':
			final = final[:-1]
	return final


def railBrute(text):
	tetragram_load = get.get_tetraF("TetraNO.txt")
	best_fit = data.tetra_fit(text, False, tetragram_load)
	best_key = [1, 0]
	for i in range(2, len(text)):
		for j in range(2 * (i - 1)):
			tempText = railDe(text, i, j)
			temp_fit = data.tetra_fit(tempText, False, tetragram_load)
			if temp_fit >= best_fit:
				best_key = [i, j]
				best_fit = temp_fit
				print("NEW HIGH FITNESS", i, j, temp_fit)
				print(tempText)

	return railDe(text, best_key[0], best_key[1])


def amscoEn(text, perm, start):
	matrix = [[] for _ in range(len(perm))]
	two = bool(start - 1)
	count = 0
	lets_per_row = 0
	while count < len(text):
		
