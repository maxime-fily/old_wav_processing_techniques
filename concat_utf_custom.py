import codecs 
import random
import wave
import os
import numpy as np
import re
import glob
import io
import sys

from pprint import pprint

batch = sys.argv[1] #batch number is first arg (INT)
locut = sys.argv[2] #speaker initals is second arg (STR)
mot1 = sys.argv[3]
mot2 = sys.argv[4]
mot3 = sys.argv[5]

dirname_H = '/media/sf_vm/transferts_vers_REDHAT/signaux/batch' + str(batch) + '_' + str(locut) + '_H'
dirname_B = '/media/sf_vm/transferts_vers_REDHAT/signaux/batch' + str(batch) + '_' + str(locut) + '_B'

LH = dirname_H + '/*.wav'
LB = dirname_B + '/*.wav'

infiles_B = sorted(glob.glob(LB))
nb_B = len(infiles_B)
infiles_H = sorted(glob.glob(LH))
nb_H = len(infiles_H)

nb_tot = nb_H + nb_B

if  nb_B - nb_H == 0:
	outfile_REG = "/media/sf_vm/transferts_vers_REDHAT/signaux/One_file_Batch" + str(batch) + '_' + str(locut) + 'regular.wav'
	outfile_GOO = "/media/sf_vm/transferts_vers_REDHAT/signaux/One_file_Batch" + str(batch) + '_' + str(locut) + 'goofy.wav'
	outfile_B_only = "/media/sf_vm/transferts_vers_REDHAT/signaux/One_file_Batch" + str(batch) + '_' + str(locut) + 'B_only.wav'
	
	
	
	#input
	data= []
	
	#Traitement des signaux _b
	os.chdir(dirname_B)
	for k in range(1,4):
		infile = str(mot1) + str(k) + '.wav'
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		infile = str(mot2) + str(k) + '.wav'
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		infile = str(mot3) + str(k) + '.wav'
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		w.close()
	
	#Traitement des signaux _h
	os.chdir(dirname_H)
	for k in range(1,4):
		infile = str(mot1) + str(k) + '.wav'
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		infile = str(mot2) + str(k) + '.wav'
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		infile = str(mot3) + str(k) + '.wav'
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		w.close()
	
	#output initialisation
	output_REG = wave.open(outfile_REG, 'wb')
	output_REG.setparams(data[0][0])
	output_GOO = wave.open(outfile_GOO, 'wb')
	output_GOO.setparams(data[0][0])
	output_BON = wave.open(outfile_B_only, 'wb')
	output_BON.setparams(data[0][0])	
	
	i=0
	while i < nb_H:
		output_GOO.writeframes(data[i+nb_H][1])
		output_GOO.writeframes(data[i][1])
		output_REG.writeframes(data[i][1])
		output_REG.writeframes(data[i+nb_H][1])
		output_BON.writeframes(data[i][1])
		i += 1

	output_REG.close()
	output_GOO.close()
	output_BON.close()
	
else:
	print("erreur : le nombre de textgrids est different entre dir _B et _H")

