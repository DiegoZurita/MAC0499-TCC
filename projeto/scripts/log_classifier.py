import os
import linecache
import sys


def main():
    print(sys.argv)
    logFilePath = sys.argv[1]
    destPathFile = sys.argv[2]
    totalLines = int(sys.argv[3])
    startFromLine = int(sys.argv[4]) + 1

    if not os.path.isfile(destPathFile):
        print("file not exists, creating..")
        f = open(destPathFile, "w")
        f.close()
        

    destfile = open(destPathFile, "r+")

    print("Classifique as linhas abaixo (m = maliciosa, n = não maliciosa), q para sair")

    for i in range(startFromLine, totalLines):
        logLine = linecache.getline(logFilePath, i)
        
        classe = input("%s" % (logLine))

        if classe == "q":
            break

        destfile.write("%d, %s, %s\n" % (i, logLine.replace("\n", ""), classe) )

    destfile.close()
    

if __name__ == "__main__":
    main()