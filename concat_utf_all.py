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

dirname_H = '/media/sf_vm/transferts_vers_REDHAT/signaux/batch' + str(batch) + '_' + str(locut) + '_H'
dirname_B = '/media/sf_vm/transferts_vers_REDHAT/signaux/batch' + str(batch) + '_' + str(locut) + '_B'

LH = dirname_H + '/*.wav'
LB = dirname_B + '/*.wav'

infiles_B = sorted(glob.glob(LB))
print(infiles_B)
nb_B = len(infiles_B)
infiles_H = sorted(glob.glob(LH))
print(infiles_H)
nb_H = len(infiles_H)

nb_tot = nb_H + nb_B

if  nb_B - nb_H == 0:
	outfile_REG = "/media/sf_vm/transferts_vers_REDHAT/signaux/One_file_Batch" + str(batch) + '_' + str(locut) + 'regular.wav'
	outfile_GOO = "/media/sf_vm/transferts_vers_REDHAT/signaux/One_file_Batch" + str(batch) + '_' + str(locut) + 'goofy.wav'
	
	
	
	#input
	data= []
	
	
	for infile in infiles_H:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()
	

	for infile in infiles_B:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()

	#output initialisation
	output_REG = wave.open(outfile_REG, 'wb')
	output_REG.setparams(data[0][0])
	output_GOO = wave.open(outfile_GOO, 'wb')
	output_GOO.setparams(data[0][0])
	
	
	i=0
	while i < nb_H:
		output_REG.writeframes(data[i+nb_H][1])
		output_REG.writeframes(data[i][1])
		output_GOO.writeframes(data[i][1])
		output_GOO.writeframes(data[i+nb_H][1])
		i += 1
	output_REG.close()
	output_GOO.close()
	#outworkH.close()
	#outworkB.close()

else:
	print("erreur : le nombre de textgrids est different entre dir _B et _H")

