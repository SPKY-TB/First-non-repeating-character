def first_non_repeating_letter(string):
    uniqueChar='';
    noSpaceString=string.strip()
    for  char in noSpaceString:
        if noSpaceString.lower().count(char.lower())==1:
                uniqueChar=char;
                break;
    return uniqueChar;
