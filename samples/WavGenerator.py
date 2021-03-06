#############
# ECE 612 Spring 2017
# Joe Parrish
#
# Use the same logic from SpectrumTester.py to generate multiple sine waves
#  but write that output to a .wav file for file based testing of the project code
#############

import wave
import argparse
import numpy as np

def generate_sample_file(test_freqs, test_amps, chunk=4096, samplerate=44100):
   
   filename = 'Sample'

   x = np.arange(chunk)
   y = np.zeros(chunk)
   for test_freq,test_amp in zip(test_freqs,test_amps):
      filename += '_' + str(test_freq) + 'Hz@' + str(test_amp)
      y = np.add(y, np.sin(2 * np.pi * test_freq * x / samplerate) * test_amp)

   filename += '.wav'
   y = y.astype('i2')

   wave_writer = wave.open(filename, mode='wb')

   wave_writer.setnchannels(1)
   wave_writer.setsampwidth(2)
   wave_writer.setframerate(samplerate)

   for x in range(0,8):
      wave_writer.writeframes(y)
                       
if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Write a wave file containing Numpy generated sine waves')
   parser.add_argument('--freqs', nargs='+', type=int)
   parser.add_argument('--amps', nargs='+', type=int)
   args = parser.parse_args()
   
   generate_sample_file(args.freqs, args.amps)
   
