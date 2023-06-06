import sys, getopt

def main(argv):
   input_dir = ''
   output_dir = ''
   opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is ', input_dir)
   print ('Output file is ', output_dir)


if __name__ == "__main__":
   main(sys.argv[1:])


