import function.locView as locView
import function.locInsert as locInsert
import function.locDelete as locDelete
import function.calSort as calSort
import function.locSavecsv as locCSV
import function.locHelp as locHelp
import os, time

def Portal(code:str, dbKey):
    if code == '':
        locView.now(dbKey)
    if code.lower() == 'v':
        locView.now(dbKey)
    if code.lower() == 'd':
        locDelete.now(dbKey)
        locView.now(dbKey)
    if code.lower() == 'a':
        locInsert.now(dbKey)
        locView.now(dbKey)
    if code.lower() == 'x':
        os.system('cls')
        exit("""
    ██████████████████████████████████████████████████████████████
    █░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░████
    █░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░████
    █░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░████
    █░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████░░▄▀░░████
    █░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░████
    █░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░████
    █░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█░░░░░░████
    █░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀░░███████████████████
    █░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█░░░░░░████
    █░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░████
    █░░░░░░░░░░░░░░░░███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░████
    ██████████████████████████████████████████████████████████████""")
    
    #MORE OPTIONS

    if code.lower() == 's':
        calSort.Get_Sort_Type(edit_mode=True)
        locView.now(dbKey)

    if code.lower() == 'c':
        locCSV.Write_To_CSV(dbKey)
        locView.now(dbKey)
    
    #HELP AND SETTINGS

    if code.lower() == 'h':
        locHelp.Wiki()
        locView.now(dbKey)