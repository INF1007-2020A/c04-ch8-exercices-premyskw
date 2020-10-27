#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}
def exercice1(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        for index, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"Les fichiers sont différents! À la ligne {index+1}, on a:")
                print(line1)
                print("et on a:")
                print(line2)
                break
def exercice2(input_file,output_file):
    with open(input_file, encoding="utf-8") as in_file, open(output_file, "w", encoding="utf-8") as out_file:
        for line in in_file:
            out_file.write(line.replace(" ", "   "))

def exercice3(file_path,save_path):
    with open(file_path, encoding='utf-8') as notes:
        note_percent = notes.readlines()
    with open(save_path, 'w', encoding='utf-8') as f:
        print(f)
        for note in note_percent:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(note) < value[1]:
                    f.write(note.strip() + ' ' + key + '\n')
                    break

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice1('./exemple.txt','./exemple2.txt')
    exercice2('./exemple.txt','./exemple2.txt')
    pass
