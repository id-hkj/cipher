import sys
import help, data, mono, poly, trans, grid, matrix, stream, code, other, proto

def Help_Decide(args):
	if len(args) == 0:
		help.Summary()

	if args[0] == "-d" or args[0] == "--data" or args[0] == "data":
		help.Data()
	elif args[0] == "-m" or args[0] == "--mono" or args[0] == "mono":
		help.Mono()
	elif args[0] == "-p" or args[0] == "--poly" or args[0] == "poly":
		help.Poly()
	elif args[0] == "-t" or args[0] == "--trans" or args[0] == "trans":
		help.Trans()
	elif args[0] == "-g" or args[0] == "--grid" or args[0] == "grid":
		help.Grid()
	elif args[0] == "-M" or args[0] == "--matrix" or args[0] == "matrix":
		help.Matrix()
	elif args[0] == "-s" or args[0] == "--stream" or args[0] == "stream":
		help.Stream()
	elif args[0] == "-c" or args[0] == "--code" or args[0] == "code":
		help.Code()
	elif args[0] == "-o" or args[0] == "--other" or args[0] == "other":
		help.Other()
	elif args[0] == "-p" or args[0] == "--proto" or args[0] == "proto":
		help.Proto()
	else:
		print("Invalid Parameters")


def Data_Decide(args):
	if args[0] == "clean" and len(args) >= 2:
		text = open(args[1], 'r', encoding='utf-8').read()
		new_corp = data.clean(text)
		if len(args) == 2:
			open(args[1], 'w', encoding='utf-8').write(new_corp)
		else:
			open(args[2], 'w', encoding='utf-8').write(new_corp)
	elif args[0] == "alphabetical" and len(args) >= 2:
		text = open(args[1], 'r', encoding='utf-8').read()
		words = data.alphabetical(text)
		words = '\n'.join(words)
		if len(args) == 2:
			open(args[1], 'w', encoding='utf-8').write(words)
		else:
			open(args[2], 'w', encoding='utf-8').write(words)
	elif args[0] == "frequency" and len(args) >= 2:
		text = open(args[1], 'r', encoding='utf-8').read()
		words = data.frequency(text)
		words = list(words.items())
		for i in range(len(words)):
			words[i] = words[i][0] + ' ' + str(words[i][1])
		words = '\n'.join(words)
		if len(args) == 2:
			open(args[1], 'w', encoding='utf-8').write(words)
		else:
			open(args[2], 'w', encoding='utf-8').write(words)
	elif args[0] == "mono" and len(args) >= 2:
		text = open(args[1], 'r', encoding='utf-8').read()
		mono_none = data.mono(text, False)
		mono_space = data.mono(text, True)
		final = [str(mono_none[i]) + ' ' + str(mono_space[i]) for i in range(26)]
		final.append(' ' + str(mono_space[26]))
		final = '\n'.join(final)
		if len(args) == 2:
			open(args[1], 'w', encoding='utf-8').write(final)
		else:
			open(args[2], 'w', encoding='utf-8').write(final)
	elif args[0] == "tetra" and len(args) >= 4:
		text = open(args[1], 'r', encoding='utf-8').read()
		tetra_no = data.tetra(text, False)
		words = list(tetra_no.items())
		for i in range(len(words)):
			words[i] = words[i][0] + ' ' + str(words[i][1])
		words = '\n'.join(words)
		open(args[2], 'w', encoding='utf-8').write(words)
		
		tetra_yes = data.tetra(text, True)
		words = list(tetra_yes.items())
		for i in range(len(words)):
			words[i] = words[i][0] + ' ' + str(words[i][1])
		words = '\n'.join(words)
		open(args[3], 'w', encoding='utf-8').write(words)
	elif args[0] == "anglefit" and len(args) >= 2:
		text = open(args[1], 'r', encoding='utf-8').read()
		if len(args) > 2:
			if int(args[3]):
				print("Fitness with space:", data.angle_fit(text, True))
			else:
				print("Fitness without spaces:", data.angle_fit(text, False))
		else:
			print("Fitness with space:", data.angle_fit(text, True))
			print("Fitness without spaces:", data.angle_fit(text, False))
	elif args[0] == "tetrafit" and len(args) >= 2:
		text = open(args[1], 'r', encoding='utf-8').read()
		if len(args) > 2:
			if int(args[3]):
				print("Fitness with space:", data.tetra_fit(text, True))
			else:
				print("Fitness without spaces:", data.tetra_fit(text, False))
		else:
			print("Fitness with space:", data.tetra_fit(text, True))
			print("Fitness without spaces:", data.tetra_fit(text, False))
	elif args[0] == "index" and len(args) >= 2:
		text = open(args[1], 'r', encoding='utf-8').read()
		if len(args) > 2:
			if int(args[3]):
				print("Coincidence with space:", data.IndexCoin(text, True))
			else:
				print("Coincidence without spaces:", data.IndexCoin(text, False))
		else:
			print("Coincidence with space:", data.IndexCoin(text, True))
			print("Coincidence without spaces:", data.IndexCoin(text, False))
	elif args[0] == "setup" and len(args) >= 2:
		main("-d", "clean", args[1])
		main("-d", "alphabetical", args[1], "ALPHA.txt")
		main("-d", "frequency", args[1], "FREQ.txt")
		main("-d", "mono", args[1], "MONO.txt")
		main("-d", "tetra", args[1], "TetraNO.txt", "TetraSPACE.txt")
	else:
		print("Invalid Parameters")


def Mono_Decide(args):
	if args[0] == "used" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		if mono.thinkMono(text):
			print("We think a monoalphabetic cipher was used to encrypt this text.")
		else:
			print("We DO NOT think a monoalphabetic cipher was used to encrypt this text.")
	elif args[0] == "encrypt" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.encrypt(text, args[2]))
	elif args[0] == "decrypt" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.decrypt(text, args[2]))
	elif args[0] == "atbash" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.atbash(text))
	elif args[0] == "caeseren" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.caeser(text, int(args[2]) % 26))
	elif args[0] == "caeserde" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.caeser(text, -int(args[2]) % 26))
	elif args[0] == "caeserbrutetetra" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.caeserBruteTetra(text))
	elif args[0] == "caeserbrutemono" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.caeserBruteMono(text))
	elif args[0] == "caesercrib" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		possible = mono.caeserCrib(text, args[2])
		if len(possible) == 0:
			print("No solutions found.")
		elif len(possible) == 1:
			print(mono.caeser(text, -possible[0] % 26))
		else:
			print("Multiple solutions found with encryption keys:")
			print(", ".join(possible))
	elif args[0] == "affineen" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.affineEn(text, int(args[2]), int(args[3])))
	elif args[0] == "affinede" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.affineDe(text, int(args[2]), int(args[3])))
	elif args[0] == "affinebrutetetra" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.affineBruteTetra(text))
	elif args[0] == "affinebrutemono" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.affineBruteMono(text))
	elif args[0] == "affinecrib" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		possible = mono.affineCrib(text, args[2])
		if len(possible) == 0:
			print("No solutions found.")
		elif len(possible) == 1:
			print(mono.affineDe(text, possible[0][0], possible[0][1]))
		else:
			print("Multiple solutions found with encryption keys:")
			print(", ".join(possible))
	elif args[0] == "keyworden" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.keywordEn(text, args[2], int(args[3])))
	elif args[0] == "keywordde" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.keywordDe(text, args[2], int(args[3])))
	elif args[0] == "keywordbrute" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.keywordAttack(text))
	elif args[0] == "brute" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(mono.brute(text))
	else:
		print("Invalid Parameters")


def Poly_Decide(args):
	if args[0] == "encrypt" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		keys = open(args[2], 'r', encoding="utf-8").read().split('\n')
		print(poly.encrypt(text, keys))
	elif args[0] == "decrypt" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		keys = open(args[2], 'r', encoding="utf-8").read().split('\n')
		print(poly.decrypt(text, keys))
	elif args[0] == "keylen" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(", ".join(poly.get_key_len(text)))
	elif args[0] == "twistlen" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.getlentwist(text))
	elif args[0] == "vigenereen" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigEn(text, args[2]))
	elif args[0] == "vigenerede" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigDe(text, args[2]))
	elif args[0] == "vigauto" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		poly.vigAutoDe(text)
	elif args[0] == "vigdict" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigAutoDict(text))
	elif args[0] == "vighill" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigAutoHill(text, int(args[2])))
	elif args[0] == "vigmono" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigMono(text, int(args[2])))
	elif args[0] == "beaufort" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.beaufort(text, args[2]))
	elif args[0] == "beauauto" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		poly.beauAutoDe(text)
	elif args[0] == "beaudict" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.beauAutoDict(text))
	elif args[0] == "beauhill" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.beauAutoHill(text, int(args[2])))
	elif args[0] == "beaumono" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.beauMono(text, int(args[2])))
	elif args[0] == "beauvaren" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigDe(text, args[2]))
	elif args[0] == "beauvarde" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigEn(text, args[2]))
	elif args[0] == "beauvarauto" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		poly.beauvarAutoDe(text)
	elif args[0] == "beauvardict" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.beauvarAutoDict(text))
	elif args[0] == "beauvarhill" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.beauvarAutoHill(text, int(args[2])))
	elif args[0] == "beauvarmono" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.vigMono(text, int(args[2])))
	elif args[0] == "porta" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.porta(text, args[2], int(args[3])))
	elif args[0] == "portaeng" and len(args) >= 2:
		poly.find_eng(args[1])
	elif args[0] == "portaauto" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		poly.portaAutoDe(text)
	elif args[0] == "portadict" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.portaAutoDict(text))
	elif args[0] == "portahill" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.portaAutoHill(text, int(args[2])))
	elif args[0] == "portamono" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.portaMono(text, int(args[2])))
	elif args[0] == "bellaso" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.bellaso(text, args[2]))
	elif args[0] == "bellauto" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		poly.bellAutoDe(text)
	elif args[0] == "belldict" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.bellAutoDict(text))
	elif args[0] == "bellhill" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.bellAutoHill(text, int(args[2])))
	elif args[0] == "bellmono" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.bellMono(text, int(args[2])))
	elif args[0] == "affineen" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		codes = open(args[2], 'r', encoding="utf-8").read().split('\n')
		for i in range(len(codes)):
			codes[i] = codes[i].split(' ')
			codes[i][0], codes[i][1] = int(codes[i][0]), int(codes[i][1])
		print(poly.periodAffineEn(text, codes))
	elif args[0] == "affinede" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		codes = open(args[2], 'r', encoding="utf-8").read().split('\n')
		for i in range(len(codes)):
			codes[i] = codes[i].split(' ')
			codes[i][0], codes[i][1] = int(codes[i][0]), int(codes[i][1])
		print(poly.periodAffineDe(text, codes))
	elif args[0] == "affineauto" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.affineAuto(text, int(args[2])))
	elif args[0] == "polyauto" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(poly.AutoPolyDe(text, int(args[2])))
	else:
		print("Invalid Parameters")


def Trans_Decide(args):
	if args[0] == "permen" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		key = trans.get_perm(args[2], int(args[3]))
		print(trans.permEn(text, key))
	elif args[0] == "permde" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		key = trans.get_perm(args[2], int(args[3]))
		print(trans.permDe(text, key))
	elif args[0] == "getword" and len(args) >= 2:
		trans.find_eng(trans.get_perm(args[1], 0))
	elif args[0] == "permbrute" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.permBrute(text))
	elif args[0] == "permhill" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.permHill(text, int(args[2])))
	elif args[0] == "scytaleen" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.scytaleEn(text, int(args[2]), int(args[3])))
	elif args[0] == "scytalede" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.scytaleDe(text, int(args[2]), int(args[3])))
	elif args[0] == "scytalebrute" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.scytaleBrute(text))
	elif args[0] == "twisten" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.twistEn(text, int(args[2]), int(args[3])))
	elif args[0] == "twistde" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.twistDe(text, int(args[2]), int(args[3])))
	elif args[0] == "twistbrute" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.twistBrute(text))
	elif args[0] == "colen" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		key = trans.get_perm(args[2], 1)
		print(trans.columnEn(text, key))
	elif args[0] == "colde" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		key = trans.get_perm(args[2], 1)
		print(trans.columnDe(text, key))
	elif args[0] == "colbrute" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.colBrute(text))
	elif args[0] == "colhill" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.colHill(text, int(args[2])))
	elif args[0] == "doubleen" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		key1, key2 = trans.get_perm(args[2], 1), trans.get_perm(args[3], 1)
		print(trans.doubleColEn(text, key1, key2))
	elif args[0] == "doublede" and len(args) >= 3:
		text = open(args[1], 'r', encoding="utf-8").read()
		key1, key2 = trans.get_perm(args[2], 1), trans.get_perm(args[3], 1)
		print(trans.doubleColDe(text, key1, key2))
	elif args[0] == "railen" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.railEn(text, int(args[2]), int(args[3])))
	elif args[0] == "railde" and len(args) >= 4:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.railDe(text, int(args[2]), int(args[3])))
	elif args[0] == "railbrute" and len(args) >= 2:
		text = open(args[1], 'r', encoding="utf-8").read()
		print(trans.railBrute(text))
	else:
		print("Invalid Parameters")


def Grid_Decide(args):
	if False:
		pass
	else:
		print("Invalid Parameters")


def Matrix_Decide(args):
	if False:
		pass
	else:
		print("Invalid Parameters")


def Stream_Decide(args):
	if False:
		pass
	else:
		print("Invalid Parameters")


def Code_Decide(args):
	if False:
		pass
	else:
		print("Invalid Parameters")


def Other_Decide(args):
	if False:
		pass
	else:
		print("Invalid Parameters")


def Proto_Decide(args):
	if False:
		pass
	else:
		print("Invalid Parameters")


def main(args):	
	if len(args) == 0:
		print("Invalid Parameters")
		return;
	
	if args[0] == "-h" or args[0] == "--help":
		Help_Decide(args[1:])
	elif args[0] == "-d" or args[0] == "--data":
		Data_Decide(args[1:])
	elif args[0] == "-m" or args[0] == "--mono":
		Mono_Decide(args[1:])
	elif args[0] == "-p" or args[0] == "--poly":
		Poly_Decide(args[1:])
	elif args[0] == "-t" or args[0] == "--transpose":
		Trans_Decide(args[1:])
	elif args[0] == "-g" or args[0] == "--grid":
		Grid_Decide(args[1:])
	elif args[0] == "-M" or args[0] == "--matrix":
		Matrix_Decide(args[1:])
	elif args[0] == "-s" or args[0] == "--stream":
		Stream_Decide(args[1:])
	elif args[0] == "-c" or args[0] == "--code":
		Code_Decide(args[1:])
	elif args[0] == "-o" or args[0] == "--other":
		Other_Decide(args[1:])
	elif args[0] == "-p" or args[0] == "--proto":
		Proto_Decide(args[1:])
	else:
		print("Invalid Parameters")
	
	return;


if __name__ == "__main__":
	main(sys.argv[1:])