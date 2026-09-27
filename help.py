def Summary():
	print("Usage: cipher  [options...]")
	print("data - Some Corpus and Fittness functions")
	print("mono - Monalphabetic substitution cipher solver/encoders")
	print("poly - Polyalphabetic substitution cipher solver/encoders")
	print("transpose - Transposition cipher solver/encoders")
	print("grid - solver/encoder for ciphers based on grids")
	print("matrix - solver/encoder for ciphers based on matrices")
	print("stream - Stream ciphers solver/encoder")
	print("code")
	print("proto - Protomechanical ciphers solver/encoder")
	print("other - Miscelanious ciphers")
	print()
	print("This is not the full help, this menu is stripped into categories.")
	print("Use \"--help [catagory name]\" to get an overview of a category.")
	print("For all options, use the manual, or type \"--help all\".")

def Data():
	print("clean input.txt [output.txt] - strips a corpus of its punctuation")
	print("alphabetical input.txt [output.txt] - compiles a list sorted alphabetically of lists from a corpus")
	print("frequency input.txt [output.txt] - Compiles a list sorted by frequency of words from a corpus")
	print("mono input.txt [output.txt] - Compiles monogram frequencies.")
	print("tetra input.txt noSpaceOut.txt SpaceOut.txt - Compiles logs of tetragram frequencies.")
	print("setup input.txt - Takes an uncleaned corpus, and compiles frequencies and word lists.")
	print("anglefit input.txt [space (1/0)] - Angle between vectors fitness evaluation.")
	print("tetrafit input.txt [space (1/0)] - Tetragram fitness evaluation.")
	print("index input.txt [space (1/0)] - Index of Coincidence fitness evaluation.")
	print()
	print("If an output file is not specified, the contents of the input file will be rewritten.")


def Mono():
	print("used input.txt - tentitively predicts if a monoalphabetic cipher was used.")
	print("encrypt input.txt key - encrypts a text using an encipherment key.")
	print("decrypt input.txt key - decrypts a text using an encipherment key.")
	print("atbash input.txt - encrypts/decrypts a text that uses the atbash cipher.")
	print("caeseren input.txt key - encrypts a text that uses the caeser cipher with a given key.")
	print("caeserde input.txt key - decrypts a text that uses the caeser cipher with a given key.")
	print("caeserbrutetetra input.txt - performs a brute force attack on the caeser cipher using tetragram fitness.")
	print("caeserbrutemono input.txt - performs a brute force attack on the caeser cipher using monogram fitness.")
	print("caesercrib input.txt crib - performs a known word attack on the caeser cipher.")
	print("affineen input.txt keyA keyB - encrypts a text that uses the affine cipher with a given key.")
	print("affinede input.txt keyA keyB - decrypts a text that uses the affine cipher with a given key.")
	print("affinebrutetetra input.txt - performs a brute force attack on the affine cipher using tetragram fitness.")
	print("affinebrutemono input.txt - performs a brute force attack on the affine cipher using monogram fitness.")
	print("affinecrib input.txt crib - performs a known word attack on the affine cipher.")
	print("keyworden input.txt word1 type1 - encrypts a keyword substitution cipher.")
	print("keywordde input.txt word1 type1 - decrypts a keyword substitution cipher.")
	print("keywordbrute input.txt - Performs a dictionary attack on the keyword substitution cipher.")
	print("brute input.txt - Implements a stochastic hill-climbing attack on the cipher. You may need to run it a few times to get an accurate decryption")
	print()
	print("The 'type' arguement is 0/1/2 - 0 is fill from A, 1 is fill from last letter, 2 is fill from last letter in word.")
	


def Poly():
	print("encrypt input.txt keys.txt - encrypts a text using a series of keys.")
	print("decrypt input.txt keys.txt - decrypts a text using a series of keys.")
	print("keylen input.txt - guesses the key length of a text.")
	print("twistlen input.txt - guesses the key length of a text.")
	print("vigenereen input.txt key - encrypts a text that uses the vigenere cipher.")
	print("vigenerede input.txt key - decrypts a text that uses the vigenere cipher.")
	print("vigauto input.txt - performs a brute force attack on a text that uses the vigenere cipher.")
	print("vigdict input.txt - performs a dictionary attack on a text that uses the vigenere cipher.")
	print("vighill input.txt keylen - performs a hill-climbing attack on a text that uses the vigenere cipher. Requires key length.")
	print("vigmono input.txt keylen - Decrypts the vigenere as a periodic caeser cipher. Requires key length.")
	print("beaufort input.txt key - encrypts/decrypts a text that uses the beaufort cipher.")
	print("beauauto input.txt - performs a brute force attack on a text that uses the beaufort cipher.")
	print("beaudict input.txt - performs a dictionary attack on a text that uses the beaufort cipher.")
	print("beauhill input.txt keylen - performs a hill-climbing attack on a text that uses the beaufort cipher. Requires key length.")
	print("beaumono input.txt keylen - Decrypts the beaufort as a periodic atbash caeser cipher. Requires key length.")
	print("beauvaren input.txt key - encrypts a text that uses the varient beaufort cipher.")
	print("beauvarde input.txt key - decrypts a text that uses the varient beaufort cipher.")
	print("beauvarauto input.txt - performs a brute force attack on a text that uses the varient beaufort cipher.")
	print("beauvardict input.txt - performs a dictionary attack on a text that uses the varient beaufort cipher.")
	print("beauvarhill input.txt keylen - performs a hill-climbing attack on a text that uses the varient beaufort cipher. Requires key length.")
	print("beauvarmono input.txt keylen - Decrypts the varient beaufort as a periodic reverse vignere cipher. Requires key length.")
	print("porta input.txt key style[0/1] - encrypts/decrypts a text that uses the porta cipher.")
	print("portaeng key - Finds possibilities for an english keyword from a key.")
	print("portaauto input.txt - performs a brute force attack on a text that uses the porta cipher.")
	print("portadict input.txt - performs a dictionary attack on a text that uses the porta cipher.")
	print("portahill input.txt keylen - performs a hill-climbing attack on a text that uses the porta cipher. Requires key length.")
	print("portamono input.txt keylen - Decrypts the porta cipher using monogram fitness. Requires key length.")
	print("bellaso input.txt key - encrypts/decrypts a text that uses the bellaso varient porta cipher.")
	print("bellauto input.txt - performs a brute force attack on a text that uses the bellaso varient porta cipher.")
	print("belldict input.txt - performs a dictionary attack on a text that uses the bellaso varient porta cipher.")
	print("bellhill input.txt keylen - performs a hill-climbing attack on a text that uses the bellaso varient porta cipher. Requires key length.")
	print("bellmono input.txt keylen - Decrypts the bellaso varient porta as a periodic caeser cipher. Requires key length.")
	print("affineen input.txt codes.txt - Encrypts a periodic affine cipher using codes. Sets of codes are seperated by new lines. Codes are seperated by spaces.")
	print("affinede input.txt codes.txt - Decrypts a periodic affine cipher using codes. Sets of codes are seperated by new lines. Codes are seperated by spaces.")
	print("affineauto input.txt keylen - Decrypts the text as a periodic affine cipher. Requires key length.")
	print("polyauto input.txt keylen - Automatically decrypts a polyalphabetic substitution cipher, performing a stochastic hill-climbing attack. Requires key length.")


def Trans():
	print("permen input.txt key fillRep(0/1) - encrypts a text using a permutation cipher.")
	print("permde input.txt key fillRep(0/1) - decrypts a text using a permutation cipher.")
	print("getword key - prints a possible keywords of a text.")
	print("permbrute input.txt - performs a brute force attack on a text using a permutation cipher.")
	print("permhill input.txt keylen - performs a hill-climbing attack on a text using a permutation cipher.")
	print("scytaleen input.txt height width - encrypts a text using a matrix/scytale cipher.")
	print("scytalede input.txt height width - decrypts a text using a matrix/scytale cipher.")
	print("scytalebrute input.txt - performs a brute force attack on a text using a matrix/scytale cipher.")
	print("twisten input.txt width twist - encrypts a text using a twisted scytale cipher.")
	print("twistde input.txt width twist - decrypts a text using a twisted scytale cipher.")
	print("twistbrute input.txt - performs a brute force attack on a text using a twisted scytale cipher.")
	print("colen input.txt key - encrypts a text using a columnar transposition cipher.")
	print("colde input.txt key - decrypts a text using a columnar transposition cipher.")
	print("colbrute input.txt - performs a brute force attack on a text using a columnar transposition cipher.")
	print("colhill input.txt keylen - performs a hill-climbing attack on a text using a columnar transposition cipher.")
	print("doubleen input.txt key1 key2 - encrypts a text using a double columnar transposition cipher.")
	print("doublede input.txt key1 key2 - decrypts a text using a double columnar transposition cipher.")
	print("colbrute input.txt - performs a brute force attack on a text using a columnar transposition cipher.")
	print("railen input.txt rails skips - encrypts a text using a rail fence cipher.")
	print("railde input.txt rails skips - decrypts a text using a rail fence cipher.")
	print("railbrute input.txt - performs a brute force attack on a text using a rail fence cipher.")


def Grid():
	return;


def Matrix():
	return;


def Streams():
	return;


def Code():
	return;


def Other():
	return;


def Proto():
	return;
