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

dirname_B = '/media/sf_vm/transferts_vers_REDHAT/signaux/batch' + str(batch) + '_' + str(locut) + '_B'

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

#output initialisation
output_BON = wave.open(outfile_B_only, 'wb')
output_BON.setparams(data[0][0])	

i=0
while i < 9:
	output_BON.writeframes(data[i][1])
	i += 1
output_BON.close()
