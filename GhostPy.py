# -*- coding: utf-8 -*-
__author__ = 'NerdyZonky'

import os

print('GhostPy Version 0.2\n')
print('Bitte wählen Sie aus:\n')
print('1 = Mehrere PDFs aus einem Verzeichnis komprimieren \n')
print('2 = Einzelne PDF komprimieren \n')
print('Andere Tasten = Beende Programm\n')

choose = input()

if choose == '1':
    loop = 'true'
    while loop == 'true':
        InputFiles = input('Geben Sie das zu komprimierende Verzeichnis an: \n')
        OutputFiles = input('Geben Sie den Ausgabepfad an: \n')
        FalseInput = 'true'
        print('Folgende Angaben wurden gemacht:\n')
        print('Inputverzeichnis: ' + InputFiles)
        print('Outputverzeichnis: ' + OutputFiles + "\n")
        print('Sind diese Angaben korrekt?')
        print('j/n/q')

        choose1 = input()

        if choose1 == 'j':
            loop = 'false'
        if choose1 == 'n':
            loop = 'true'
        if choose1 == 'q':
            print('beende programm')
            exit()

    if not os.path.exists(OutputFiles):
        os.makedirs(OutputFiles)

    files = os.listdir(InputFiles)

    for i in range(len(files)):
        files[i] = files[i].replace(' ', '\\ ')
        os.system('gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -r150 -sOutputFile=' + OutputFiles + '/' + files[i] + ' ' + InputFiles + '/' + files[i])

    print('Komprimierung abgeschlossen')
    exit()

if choose == '2':
    InputFile = input('Geben Sie die zu komprimierende Datei an: \n')
    OutputFile = input('Geben Sie den Ausgabepfad an: \n')
    SplitInput = InputFile.split('/')
    file = SplitInput[len(SplitInput)-1]
    file = file.replace(' ', '\\ ')
    SplitInput.pop()
    InputFile= '/'.join(SplitInput)
    print('Möchten Sie den Namen der Ausgabedatei ändern? \n')
    ChooseFile = input('j/n')

    if ChooseFile == 'j':
        NewFile = input ('Geben Sie den neuen Namen der Ausgabedatei ein: \n')
        NewFile = NewFile.replace(' ', '\\ ')
        os.system('gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -r150 -sOutputFile=' + OutputFile + '/' + NewFile + ' ' + InputFile + '/' + file)
        exit()
        print('Komprimierung abgeschlossen!')

    if ChooseFile == 'n':
        pass

    print('Starte komprimierung...')
    os.system('gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -r150 -sOutputFile=' + OutputFile + '/' + file + ' ' + InputFile + '/' + file)
    print('Komprimierung abgeschlossen!')
    exit()

else:
    print('Beende Programm...')
    exit()