import sys
import os


print("Usage: python fuzzer.py path/to/iplist.txt output.txt path/to/fuzz.txt")
input1 = sys.argv[1]
output1 = open(sys.argv[2], 'w')
fuzz = sys.argv[3]
with open(input1, 'r') as filer:
    for line in filer:
        with open(fuzz, 'r') as filee:
            for fuzzline in filee:
                process = os.popen("curl -so /dev/null https://"+line.rstrip()+"/"+fuzzline.rstrip()+" -w %{http_code}").read()
                if process == '200' or process == '403':
                    print("https://"+line.rstrip()+"/"+fuzzline.rstrip()+"    "+process+"\r")
                    print("https://"+line.rstrip()+"/"+fuzzline.rstrip()+"    "+process+"\r", file=output1)
                process = os.popen("curl -so /dev/null http://"+line.rstrip()+"/"+fuzzline.rstrip()+" -w %{http_code}").read()
                if process == '200' or process == '403':
                    print("http://"+line.rstrip()+"/"+fuzzline.rstrip()+"     "+process+"\r")
                    print("http://"+line.rstrip()+"/"+fuzzline.rstrip()+"     "+process+"\r", file=output1)
                
                print("https://"+line.rstrip()+"/"+fuzzline.rstrip()+"     "+process+"\r", end="\r", flush=True)

                
