"""
data.py

Dictionaries of dye information (manually extracted from relevant websites)
.. codeauthor: Ed Beard <ed.beard94@gmail.com>
"""


dyenamo_dyes = {

    'DN-F13' : {
        'labels' :['dyenamo cloudberry orange', 'DN-F13', "(E)-3-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)-2-cyanoacrylic acid"],
        'name' : "(E)-3-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)-2-cyanoacrylic acid",
        'smiles' : "CCCCOc1ccc(c(OCCCC)c1)c2ccc(cc2)N(c3ccc(cc3)\C=C(C#N)\C(O)=O)c4ccc(cc4)c5ccc(OCCCC)cc5OCCCC"
    },

    'DN-F12' : {
        'lables' : ['DN-F12', 'YD2', 'YD-2', "Zinc(II) 5,15-Bis(3,5-di-tert-butylphenyl)-10-(bis(4-hexylphenyl)amino)-20-(4-carboxyphenylethynyl)porphyrin"],
        'name' : "Zinc(II) 5,15-Bis(3,5-di-tert-butylphenyl)-10-(bis(4-hexylphenyl)amino)-20-(4-carboxyphenylethynyl)porphyrin",
        'smiles' : "[Zn++].CCCCCCc1ccc(cc1)N(c2ccc(CCCCCC)cc2)c3c4[nH]c(cc4)c(c5cc(cc(c5)C(C)(C)C)C(C)(C)C)c6ccc(n6)c(C#Cc7ccc(cc7)C(O)=O)c8[nH]c(cc8)c(c9cc(cc(c9)C(C)(C)C)C(C)(C)C)c%10ccc3n%10"
    },

    'DN-F11': {
        'labels': ['DPP13', 'DN-F11', "(E)-3-(5-(4-(4-(5-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)thiophen-2-yl)-2,5-bis(2-ethylhexyl)-3,6-dioxo-2,3,5,6-tetrahydropyrrolo[3,4-c]pyrrol-1-yl)phenyl)furan-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(5-(4-(4-(5-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)thiophen-2-yl)-2,5-bis(2-ethylhexyl)-3,6-dioxo-2,3,5,6-tetrahydropyrrolo[3,4-c]pyrrol-1-yl)phenyl)furan-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCCCOc1ccc(cc1)N(c2ccc(OCCCCCC)cc2)c3ccc(cc3)c4sc(cc4)C5=C6C(=O)N(CC(CC)CCCC)C(=C6C(=O)N5CC(CC)CCCC)c7ccc(cc7)c8oc(cc8)\C=C(C#N)\C(O)=O'
    },

    'DN-F10': {
        'labels': ['dyenamo blue', 'DN-F10', "(E)-3-(5-(4-(4-(5-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2,5-bis(2-ethylhexyl)-3,6-dioxo-2,3,5,6-tetrahydropyrrolo[3,4-c]pyrrol-1-yl)phenyl)furan-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(5-(4-(4-(5-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2,5-bis(2-ethylhexyl)-3,6-dioxo-2,3,5,6-tetrahydropyrrolo[3,4-c]pyrrol-1-yl)phenyl)furan-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCOc1ccc(c(OCCCC)c1)c2ccc(cc2)N(c3ccc(cc3)c4sc(cc4)C5=C6C(=O)N(CC(CC)CCCC)C(=C6C(=O)N5CC(CC)CCCC)c7ccc(cc7)c8oc(cc8)\C=C(C#N)\C(O)=O)c9ccc(cc9)c%10ccc(OCCCC)cc%10OCCCC',
    },

    'DN-F10M': {
        'labels': ['DN-F10M', 'Dyenamo Blue 2016', "(E)-3-(5-(4-(4-(5-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2,5-dioctyl-3,6-dioxo-2,3,5,6-tetrahydropyrrolo[3,4-c]pyrrol-1-yl)phenyl)furan-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(5-(4-(4-(5-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2,5-dioctyl-3,6-dioxo-2,3,5,6-tetrahydropyrrolo[3,4-c]pyrrol-1-yl)phenyl)furan-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCCCCCN1C(=O)C2=C(N(CCCCCCCC)C(=O)C2=C1c3sc(cc3)c4ccc(cc4)N(c5ccc(cc5)c6ccc(OCCCC)cc6OCCCC)c7ccc(cc7)c8ccc(OCCCC)cc8OCCCC)c9ccc(cc9)c%10oc(cc%10)\C=C(C#N)\C(O)=O'
    },

    'DN-F05': {
        'labels': ['DN-F05', 'dyenamo red', 'D35CPDT', 'LEG4', "3-{6-{4-[bis(2',4'-dibutyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiophene-2-yl}-2-cyanoacrylic acid"],
        'name': "3-{6-{4-[bis(2',4'-dibutyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiophene-2-yl}-2-cyanoacrylic acid",
        'smiles': 'CCCCOc1ccc(c(OCCCC)c1)c2ccc(cc2)N(c3ccc(cc3)c4sc(cc4)c5sc(cc5)\C=C(C#N)\C(O)=O)c6ccc(cc6)c7ccc(OCCCC)cc7OCCCC'
    },

    'DN-F04': {
        'labels': ['DN-F04', 'dyenamo orange', 'D35', "(E)-3-(5-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(5-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCOc1ccc(c(OCCCC)c1)c2ccc(cc2)N(c3ccc(cc3)c4sc(cc4)\C=C(C#N)\C(O)=O)c5ccc(cc5)c6ccc(OCCCC)cc6OCCCC'
    },

    'DN-F01': {
        'labels': ['DN-F01', 'dyenamo yellow', 'L0', '4-(diphenylamino)phenylcyanoacrylic acid'],
        'name': '4-(diphenylamino)phenylcyanoacrylic acid',
        'smiles': 'OC(=O)C(=Cc1ccc(cc1)N(c2ccccc2)c3ccccc3)C#N'
    },

    'DN-F14': {
        'labels': ['dyenamo mareel blue', 'DN-F14', 'VG1-C8', '(E)-4-((5-carboxy-3,3-dimethyl-1-octyl-3H-indol-1-ium-2-yl)methylene)-2-(((E)-5-carboxy-3,3-dimethyl-1-octylindolin-2-ylidene)methyl)-3-oxocyclobut-1-en-1-olate'],
        'name': '(E)-4-((5-carboxy-3,3-dimethyl-1-octyl-3H-indol-1-ium-2-yl)methylene)-2-(((E)-5-carboxy-3,3-dimethyl-1-octylindolin-2-ylidene)methyl)-3-oxocyclobut-1-en-1-olate',
        'smiles': 'CCCCCCCCN/1c2ccc(cc2C(C)(C)C1=C/[C]3=C([O-])[C](=[CH]C4=[N+](CCCCCCCC)c5ccc(cc5C4(C)C)C(O)=O)C3=O)C(O)=O'
    },

    'DN-F15': {
        'labels': ['DN-F15', 'dyenamo transparent green', 'HSQ4', "(3Z,4Z)-4-((5-carboxy-3,3-dimethyl-1-octyl-3H-indol-1-ium-2-yl)methylene)-2-(((E)-5-carboxy-3,3-dimethyl-1-octylindolin-2-ylidene)methyl)-3-(1-cyano-2-ethoxy-2-oxoethylidene)cyclobut-1-en-1-olate"],
        'name': "(3Z,4Z)-4-((5-carboxy-3,3-dimethyl-1-octyl-3H-indol-1-ium-2-yl)methylene)-2-(((E)-5-carboxy-3,3-dimethyl-1-octylindolin-2-ylidene)methyl)-3-(1-cyano-2-ethoxy-2-oxoethylidene)cyclobut-1-en-1-olate",
        'smiles': 'CCCCCCCCN/1c2ccc(cc2C(C)(C)C1=C/C3=[C]([O-])C(=C/C4=[N+](CCCCCCCC)c5ccc(cc5C4(C)C)C(O)=O)\[C]3=[C](C#N)C(=O)OCC)C(O)=O'
    },

    # DN-F series
    'DN-F21': {
        'labels': ['DN-F21', 'SC-4', "4-(7-(5'-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)-3,3'-dihexyl-[2,2'-bithiophen]-5-yl)benzo[c][1,2,5]thiadiazol-4-yl)benzoic acid"],
        'name': "4-(7-(5'-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)-3,3'-dihexyl-[2,2'-bithiophen]-5-yl)benzo[c][1,2,5]thiadiazol-4-yl)benzoic acid",
        'smiles': 'CCCCCCOc1ccc(cc1)N(c2ccc(OCCCCCC)cc2)c3ccc(cc3)c4sc(c(CCCCCC)c4)c5sc(cc5CCCCCC)c6ccc(c7ccc(cc7)C(O)=O)c8nsnc68'
    },

    'DN-F20': {
        'labels': ['DN-F20', 'C268', "4-((7-(6-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)benzo[c][1,2,5]thiadiazol-4-yl)ethynyl)benzoic acid"],
        'name': "4-((7-(6-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)benzo[c][1,2,5]thiadiazol-4-yl)ethynyl)benzoic acid",
        'smiles': 'CCCCCCOc1ccc(cc1)N(c2ccc(OCCCCCC)cc2)c3ccc(cc3)c4sc5c6sc(cc6C(CCCCCC)(CCCCCC)c5c4)c7ccc(C#Cc8ccc(cc8)C(O)=O)c9nsnc79'
    },

    'DN-F19': {
        'labels': ['DN-F19', 'C218', "(E)-3-(6-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(6-(4-(bis(4-(hexyloxy)phenyl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCCCOc1ccc(cc1)N(c2ccc(OCCCCCC)cc2)c3ccc(cc3)c4sc5c6sc(\C=C(C#N)\C(O)=O)cc6C(CCCCCC)(CCCCCC)c5c4'
    },

    'DN-F18': {
        'labels': ['DN-F18', 'WS-72', "(E)-3-(6-(8-(4-(bis(2',4'-bis(hexyloxy)-[1,1'-biphenyl]-4-yl)amino)phenyl)-2,3-bis(4-(hexyloxy)phenyl)quinoxalin-5-yl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(6-(8-(4-(bis(2',4'-bis(hexyloxy)-[1,1'-biphenyl]-4-yl)amino)phenyl)-2,3-bis(4-(hexyloxy)phenyl)quinoxalin-5-yl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCCCOc1ccc(cc1)c2nc3c(ccc(c4ccc(cc4)N(c5ccc(cc5)c6ccc(OCCCCCC)cc6OCCCCCC)c7ccc(cc7)c8ccc(OCCCCCC)cc8OCCCCCC)c3nc2c9ccc(OCCCCCC)cc9)c%10sc%11c%12sc(\C=C(C#N)\C(O)=O)cc%12C(CCCCCC)(CCCCCC)c%11c%10'
    },

    'DN-F17' : {
        'labels' : ['DN-F17', 'R6', "4-(7-((15-(Bis(4-(hexyloxy)phenyl)amino)-9,9,19,19-tetrakis(4-hexylphenyl)-9,19-dihydrobenzo[1',10']phenanthro[3',4':4,5]thieno[3,2-b]benzo[1,10]phenanthro[3,4-d]thiophen-5-yl)ethynyl)benzo[c][1,2,5]thiadiazol-4-yl)benzoic acid" ],
        'name' : "4-(7-((15-(Bis(4-(hexyloxy)phenyl)amino)-9,9,19,19-tetrakis(4-hexylphenyl)-9,19-dihydrobenzo[1',10']phenanthro[3',4':4,5]thieno[3,2-b]benzo[1,10]phenanthro[3,4-d]thiophen-5-yl)ethynyl)benzo[c][1,2,5]thiadiazol-4-yl)benzoic acid",
        'smiles': 'CCCCCCOc1ccc(cc1)N(c2ccc(OCCCCCC)cc2)c3c4ccccc4c5c6sc7c(sc8c9c%10ccccc%10c(C#Cc%11ccc(c%12ccc(cc%12)C(O)=O)c%13nsnc%11%13)c%14cccc(c9%14)C(c%15ccc(CCCCCC)cc%15)(c%16ccc(CCCCCC)cc%16)c78)c6C(c%17ccc(CCCCCC)cc%17)(c%18ccc(CCCCCC)cc%18)c%19cccc3c5%19'
    },

    'DN-F16': {
        'labels' : ['DN-F16', 'XY1', "(E)-3-(4-(6-(7-(4-(bis(2',4'-bis((2-ethylhexyl)oxy)-[1,1'-biphenyl]-4-yl)amino)phenyl)benzo[c][1,2,5]thiadiazol-4-yl)-4,4-bis(2-ethylhexyl)-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)phenyl)-2-cyanoacrylic acid" ],
        'name' : "(E)-3-(4-(6-(7-(4-(bis(2',4'-bis((2-ethylhexyl)oxy)-[1,1'-biphenyl]-4-yl)amino)phenyl)benzo[c][1,2,5]thiadiazol-4-yl)-4,4-bis(2-ethylhexyl)-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)phenyl)-2-cyanoacrylic acid",
        'smiles': 'CCCCC(CC)COc1ccc(c(OCC(CC)CCCC)c1)c2ccc(cc2)N(c3ccc(cc3)c4ccc(OCC(CC)CCCC)cc4OCC(CC)CCCC)c5ccc(cc5)c6ccc(c7sc8c9sc(cc9C(CC(CC)CCCC)(CC(CC)CCCC)c8c7)c%10ccc(cc%10)\C=C(C#N)\C(O)=O)c%11nsnc6%11'
    },

    'DN-F16B': {
        'labels': ['DN-F16B', 'XY1b', "(E)-3-(4-(6-(7-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)benzo[c][1,2,5]thiadiazol-4-yl)-4,4-bis(2-ethylhexyl)-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)phenyl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(4-(6-(7-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)benzo[c][1,2,5]thiadiazol-4-yl)-4,4-bis(2-ethylhexyl)-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)phenyl)-2-cyanoacrylic acid",
        'smiles': 'CCCCOc1ccc(c(OCCCC)c1)c2ccc(cc2)N(c3ccc(cc3)c4ccc(OCCCC)cc4OCCCC)c5ccc(cc5)c6ccc(c7sc8c9sc(cc9C(CC(CC)CCCC)(CC(CC)CCCC)c8c7)c%10ccc(cc%10)\C=C(C#N)\C(O)=O)c%11nsnc6%11'
    },

    'DN-F04M': {
        'labels': ['DN-F04M', 'D45', "(E)-3-(5-(4-(bis(2',4'-dimethoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(5-(4-(bis(2',4'-dimethoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)thiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': 'COc1ccc(c(OC)c1)c2ccc(cc2)N(c3ccc(cc3)c4sc(cc4)\C=C(C#N)\C(O)=O)c5ccc(cc5)c6ccc(OC)cc6OC'
    },

    'DN-F05M': {
        'labels': ['DN-F05M', 'D51', "(E)-3-(6-(4-(bis(2',4'-dimethoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(6-(4-(bis(2',4'-dimethoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': "CCCCCCC1(CCCCCC)c2cc(sc2c3sc(cc13)c4ccc(cc4)N(c5ccc(cc5)c6ccc(OC)cc6OC)c7ccc(cc7)c8ccc(OC)cc8OC)\C=C(C#N)\C(O)=O"
    },

    'DN-F05Y': {
        'labels': ['DN-F05Y', 'Y123', "3-{6-{4-[bis(2',4'-dihexyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiphene-2-yl}-2-cyanoacrylic acid"],
        'name': "3-{6-{4-[bis(2',4'-dihexyloxybiphenyl-4-yl)amino-]phenyl}-4,4-dihexyl-cyclopenta-[2,1-b:3,4-b']dithiphene-2-yl}-2-cyanoacrylic acid",
        'smiles': 'CCCCCCOc1ccc(c(OCCCCCC)c1)c2ccc(cc2)N(c3ccc(cc3)c4sc5c6sc(C=C(C#N)C(O)=O)cc6C(CCCCCC)(CCCCCC)c5c4)c7ccc(cc7)c8ccc(OCCCCCC)cc8OCCCCCC'
    },

    'DN-F08': {
        'labels': ['DN-F08', 'JF419', "(E)-3-(6-(4-(bis(5,7-bis(hexyloxy)-9,9-dimethyl-9H-fluoren-2-yl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(6-(4-(bis(5,7-bis(hexyloxy)-9,9-dimethyl-9H-fluoren-2-yl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCCCOc1cc(OCCCCCC)c2c3ccc(cc3C(C)(C)c2c1)N(c4ccc(cc4)c5sc6c7sc(\C=C(C#N)\C(O)=O)cc7C(CCCCCC)(CCCCCC)c6c5)c8ccc9c(c8)C(C)(C)c%10cc(OCCCCCC)cc(OCCCCCC)c9%10'
    },

    'DN-F09': {
        'labels': ['DN-F09', 'MKA253', "(E)-3-(6-(4-(bis(5,7-dibutoxy-9,9-dimethyl-9H-fluoren-2-yl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(6-(4-(bis(5,7-dibutoxy-9,9-dimethyl-9H-fluoren-2-yl)amino)phenyl)-4,4-dihexyl-4H-cyclopenta[2,1-b:3,4-b']dithiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': 'CCCCCCC1(CCCCCC)c2cc(sc2c3sc(cc13)c4ccc(cc4)N(c5ccc6c(c5)C(C)(C)c7cc(OCCCC)cc(OCCCC)c67)c8ccc9c(c8)C(C)(C)c%10cc(OCCCC)cc(OCCCC)c9%10)\C=C(C#N)\C(O)=O'
    },

    'DN-F02': {
        'labels': ['DN-F02', 'L1', "5-[4-(diphenylamino)phenyl]thiophene-2-cyanoacrylic acid"],
        'name': "5-[4-(diphenylamino)phenyl]thiophene-2-cyanoacrylic acid",
        'smiles': 'OC(=O)C(=C)C#N.s1cccc1c2ccc(cc2)N(c3ccccc3)c4ccccc4'
    },

    'DN-F03': {
        'labels': ['DN-F03', 'D5', 'L2', "3-(5-(4-(diphenylamino)styryl)thiophen-2-yl)-2-cyanoacrylic acid"],
        'name': "3-(5-(4-(diphenylamino)styryl)thiophen-2-yl)-2-cyanoacrylic acid",
        'smiles': 'OC(=O)C(=Cc1sc(cc1)C=Cc2ccc(cc2)N(c3ccccc3)c4ccccc4)C#N'
    },

    'DN-F13': {
        'labels': ['DN-F13', 'dyenamo cloudberry orange', "(E)-3-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)-2-cyanoacrylic acid"],
        'name': "(E)-3-(4-(bis(2',4'-dibutoxy-[1,1'-biphenyl]-4-yl)amino)phenyl)-2-cyanoacrylic acid",
        'smiles': 'CCCCOc1ccc(c(OCCCC)c1)c2ccc(cc2)N(c3ccc(cc3)\C=C(C#N)\C(O)=O)c4ccc(cc4)c5ccc(OCCCC)cc5OCCCC'
    },

    'DN-F12': {
        'labels': ['YD2', 'DN-F12', 'YD-2', "Zinc(II) 5,15-Bis(3,5-di-tert-butylphenyl)-10-(bis(4-hexylphenyl)amino)-20-(4-carboxyphenylethynyl)porphyrin"],
        'name': "Zinc(II) 5,15-Bis(3,5-di-tert-butylphenyl)-10-(bis(4-hexylphenyl)amino)-20-(4-carboxyphenylethynyl)porphyrin",
        'smiles': '[Zn++].CCCCCCc1ccc(cc1)N(c2ccc(CCCCCC)cc2)c3c4[nH]c(cc4)c(c5cc(cc(c5)C(C)(C)C)C(C)(C)C)c6ccc(n6)c(C#Cc7ccc(cc7)C(O)=O)c8[nH]c(cc8)c(c9cc(cc(c9)C(C)(C)C)C(C)(C)C)c%10ccc3n%10'
    },

    # DN-FI-Series

    'DN-FI07': {
        'labels': ['DN-FI07', 'MK245', "3-(2-((E)-2-((E)-3-((Z)-2-(3-(2-carboxyethyl)-1,1-dimethyl-1,3-dihydro-2H-benzo[e]indol-2-ylidene)ethylidene)-2-chlorocyclohex-1-en-1-yl)vinyl)-1,1-dimethyl-1H-benzo[e]indol-3-ium-3-yl)propanoate"],
        'name': "3-(2-((E)-2-((E)-3-((Z)-2-(3-(2-carboxyethyl)-1,1-dimethyl-1,3-dihydro-2H-benzo[e]indol-2-ylidene)ethylidene)-2-chlorocyclohex-1-en-1-yl)vinyl)-1,1-dimethyl-1H-benzo[e]indol-3-ium-3-yl)propanoate",
        'smiles': ''
    },

    #DN-FP-Series

    'DN-FP01': {
        'labels': ['DN-FP01', 'P1', "4-(Bis-{4-[5-(2,2-dicyano-vinyl)-thiophene-2-yl]-phenyl}-amino)-benzoic acid"],
        'name': "4-(Bis-{4-[5-(2,2-dicyano-vinyl)-thiophene-2-yl]-phenyl}-amino)-benzoic acid",
        'smiles': 'OC(=O)c1ccc(cc1)N(c2ccc(cc2)c3sc(cc3)C=C(C#N)C#N)c4ccc(cc4)c5sc(cc5)C=C(C#N)C#N'
    },

    'DN-FP02': {
        'labels': ['DN-FP02', 'PB6', "4,4'-((4-(5-(2-(2,6-diisopropylphenyl)-1,3-dioxo-2,3-dihydro-1H-benzo[10,5]anthra[2,1,9-def]isoquinolin-8-yl)thiophen-2-yl)phenyl)azanediyl)dibenzoic acid"],
        'name': "4,4'-((4-(5-(2-(2,6-diisopropylphenyl)-1,3-dioxo-2,3-dihydro-1H-benzo[10,5]anthra[2,1,9-def]isoquinolin-8-yl)thiophen-2-yl)phenyl)azanediyl)dibenzoic acid",
        'smiles': 'CC(C)c1cccc(C(C)C)c1N2C(=O)c3ccc4c5cccc6c(ccc(c7ccc(C2=O)c3c47)c56)c8sc(cc8)c9ccc(cc9)N(c%10ccc(cc%10)C(O)=O)c%11ccc(cc%11)C(O)=O'
    },

    # Metal-organic sensitizing dyes

    'DN-FR01': {
        'labels': ['DN-FR01', 'K77', 'Ru(2,2´–bipyridine-4,4´-dicarboxylic acid)(4,4´-bis(2-(4-tert-butyloxyphenyl)ethenyl)-2,2´–bipyridine) (NCS)2'],
        'name': "Ru(2,2´–bipyridine-4,4´-dicarboxylic acid)(4,4´-bis(2-(4-tert-butyloxyphenyl)ethenyl)-2,2´–bipyridine) (NCS)2",
        'smiles': ''
    },

    'DN-FR02': {
        'labels': ['DN-FR02', 'B11', 'CYC-B11', "Ruthenate(2-), [[2,2´-bipyridine]-4,4´-dicarboxylato(2-)-κN1,κN1´][4,4´-bis[5´-(hexylthio)[2,2´-bithiophen]-5-yl]-2,2´-bipyridine-κN1,κN1´]bis(thiocyanato-κN)-, hydrogen (1:2), (OC-6-32)-"],
        'name': "Ruthenate(2-), [[2,2´-bipyridine]-4,4´-dicarboxylato(2-)-κN1,κN1´][4,4´-bis[5´-(hexylthio)[2,2´-bithiophen]-5-yl]-2,2´-bipyridine-κN1,κN1´]bis(thiocyanato-κN)-, hydrogen (1:2), (OC-6-32)-",
        'smiles': ''
    },

    'DN-FR03': {
        'labels': ['DN-FR03', 'N719', 'N-719', 'black dye', 'N719 black dye', "1-Butanaminium, N,N,N-tributyl-, hydrogen (OC-6-32)-[[2,2´:6´,2´´-terpyridine]-4,4´,4´´-tricarboxylato(3-)-κN1,κN1´,κN1´´]tris(thiocyanato-κN)ruthenate(4-) (2:2:1)",
                   "Di-tetrabutylammonium cis-bis(isothiocyanato)bis(2,2′-bipyridyl-4,4′-dicarboxylato)ruthenium(II)",
                   "Ruthenium(2+) N,N,N-tributyl-1-butanaminium 4'-carboxy-2,2'-bipyridine-4-carboxylate (thioxomethylene)azanide (1:2:2:2)",
                   "Ruthenium(2+)-N,N,N-tributyl-1-butanaminium-4'-carboxy-2,2'-bipyridin-4-carboxylat-(thioxomethylen)azanid (1:2:2:2)",
                   "Ruthenizer 535-bisTBA",
                   "cis-diisothiocyanato-bis(2,2’-bipyridyl-4,4’-dicarboxylato) ruthenium(II) bis(tetrabutylammonium)"],
        'name': "1-Butanaminium, N,N,N-tributyl-, hydrogen (OC-6-32)-[[2,2´:6´,2´´-terpyridine]-4,4´,4´´-tricarboxylato(3-)-κN1,κN1´,κN1´´]tris(thiocyanato-κN)ruthenate(4-) (2:2:1)",
        'smiles': '[Ru++].CCCC[N+](CCCC)(CCCC)CCCC.CCCC[N+](CCCC)(CCCC)CCCC.OC(=O)c1ccnc(c1)c2cc(ccn2)C([O-])=O.OC(=O)c3ccnc(c3)c4cc(ccn4)C([O-])=O.[N-]=C=S.[N-]=C=S'
    },

    'DN-FR04': {
        'labels': ['DN-FR04', 'C101', 'C-101' "Ruthenate(2-), [[2,2´-bipyridine]-4,4´-dicarboxylato(2-)-κN1,κN1´][4,4´-bis(5-hexyl-2-thienyl)-2,2´-bipyridine-κN1,κN1´]bis(thiocyanato-κN)-, hydrogen (1:2), (OC-6-32)-"],
        'name': "Ruthenate(2-), [[2,2´-bipyridine]-4,4´-dicarboxylato(2-)-κN1,κN1´][4,4´-bis(5-hexyl-2-thienyl)-2,2´-bipyridine-κN1,κN1´]bis(thiocyanato-κN)-, hydrogen (1:2), (OC-6-32)-",
        'smiles': ''
    }
}

solaronix_dyes = {

    'Ruthenizer 535': {
        'labels' : ['Ruthenizer 535', 'N3', 'N-3' "cis-diisothiocyanato-bis(2,2’-bipyridyl-4,4’-dicarboxylic acid) ruthenium(II)"],
        'name': "cis-diisothiocyanato-bis(2,2’-bipyridyl-4,4’-dicarboxylic acid) ruthenium(II)",
        'smiles': ""
    },

    'Ruthenizer 620-1H3TBA': {
        'labels': ['Ruthenizer 620-1H3TBA', '620-1H3TBA', 'N749', "triisothiocyanato-(2,2’:6’,6”-terpyridyl-4,4’,4”-tricarboxylato) ruthenium(II) tris(tetra-butylammonium)"
                   'Ruthenium 620', 'Greatcell Solar'],
        'name': "triisothiocyanato-(2,2’:6’,6”-terpyridyl-4,4’,4”-tricarboxylato) ruthenium(II) tris(tetra-butylammonium)",
        'smiles': ""
    },

    'Ruthenizer 520-DN': {
        'labels': ['Ruthenizer 520-DN', 'Z907', 'Z-907', '520-DN', "cis-diisothiocyanato-(2,2’-bipyridyl-4,4’-dicarboxylic acid)-(2,2’-bipyridyl-4,4’-dinonyl) ruthenium(II)"],
        'name': "cis-diisothiocyanato-(2,2’-bipyridyl-4,4’-dicarboxylic acid)-(2,2’-bipyridyl-4,4’-dinonyl) ruthenium(II)",
        'smiles': "CCCCCCCCCC1=CC(=NC=C1)C2=NC=CC(=C2)CCCCCCCCC.C1=CN=C(C=C1C(=O)O)C2=NC=CC(=C2)C(=O)O.C(=[N-])=S.C(=[N-])=S.[Ru+2]"
    },

    'Ruthenizer 535-4TBA': {
        'labels': ['Ruthenizer 535-4TBA', 'N712', '535-4TBA', "cis-diisothiocyanato-bis(2,2’-bipyridyl-4,4’-dicarboxylato) ruthenium(II) tetrakis(tetrabutylammonium)"],
        'name': "cis-diisothiocyanato-bis(2,2’-bipyridyl-4,4’-dicarboxylato) ruthenium(II) tetrakis(tetrabutylammonium)",
        'smiles': ""
    },

    'Ruthenizer 505': {
        'labels': ['Ruthenizer 505', 'cis-dicyano-bis(2,2’-bipyridyl-4,4’-dicarboxylic acid) ruthenium(II)'],
        'name': "cis-dicyano-bis(2,2’-bipyridyl-4,4’-dicarboxylic acid) ruthenium(II)",
        'smiles': ""
    },

    'Sensidizer SQ2': {
        'labels': ['Sensidizer SQ2', 'SQ2', "5-carboxy-2-[[3-[(2,3-dihydro-1,1-dimethyl-3-ethyl-1H-benzo[e]indol-2-ylidene)methyl]-2-hydroxy-4-oxo-2-cyclobuten-1-ylidene]methyl]-3,3-dimethyl-1-octyl-3H-indolium"],
        'name': "5-carboxy-2-[[3-[(2,3-dihydro-1,1-dimethyl-3-ethyl-1H-benzo[e]indol-2-ylidene)methyl]-2-hydroxy-4-oxo-2-cyclobuten-1-ylidene]methyl]-3,3-dimethyl-1-octyl-3H-indolium",
        'smiles': "CCCCCCCC[N+]1=C(C=C2C(=C(C=C3N(CC)c4ccc5ccccc5c4C3(C)C)C2=O)O)C(C)(C)c6cc(ccc16)C(O)=O"
    },

    'Sensidizer RK1': {
        'labels': ['Sensidizer RK1', 'RK1', '2-cyano-3-(4-(7-(5-(4- (diphenylamino)phenyl)-4- octylthiophen-2-yl)benzo[c][1,2,5] thiadiazol-4-yl)phenyl) acrylic acid'],
        'name': "2-cyano-3-(4-(7-(5-(4- (diphenylamino)phenyl)-4- octylthiophen-2-yl)benzo[c][1,2,5] thiadiazol-4-yl)phenyl) acrylic acid",
        'smiles': "CCCCCCCCc1cc(sc1c2ccc(cc2)N(c3ccccc3)c4ccccc4)c5ccc(c6ccc(cc6)C=C(C#N)C(O)=O)c7nsnc57"
    },

    'Sensidizer BA741': {
        'labels': ['Sensidizer BA741', 'BA741', "2-(6-(5'-(4-(bis(9,9-dimethyl-9H-fluoren-2-yl)amino) phenyl)-[2,2'-bithiophen]-5-yl)-1,3-dioxo-1H-benzo[d e]isoquinolin-2(3H)-yl)acetic acid "],
        'name': "2-(6-(5'-(4-(bis(9,9-dimethyl-9H-fluoren-2-yl)amino) phenyl)-[2,2'-bithiophen]-5-yl)-1,3-dioxo-1H-benzo[d e]isoquinolin-2(3H)-yl)acetic acid ",
        'smiles': "CC1(C)c2ccccc2c3ccc(cc13)N(c4ccc(cc4)c5sc(cc5)c6sc(cc6)c7ccc8C(=O)N(CC(O)=O)C(=O)c9cccc7c89)c%10ccc%11c%12ccccc%12C(C)(C)c%11c%10"
    },

    'Sensidizer BA504': {
        'labels': ['Sensidizer BA504', 'BA504', "2-(9-(4-(bis(9,9-dimethyl-9H-fluoren-2-yl)amino)phe nyl)-1,3-dioxo-1H-benzo[5,10]anthra[2,1,9-def]isoqui nolin-2(3H,9H,13aH)-yl)acetic acid"],
        'name': "2-(9-(4-(bis(9,9-dimethyl-9H-fluoren-2-yl)amino)phe nyl)-1,3-dioxo-1H-benzo[5,10]anthra[2,1,9-def]isoqui nolin-2(3H,9H,13aH)-yl)acetic acid",
        'smiles': "CC1(C)c2ccccc2c3ccc(cc13)N(c4ccc(cc4)C5C=Cc6c7C=CC8C(=O)N(CC(O)=O)C(=O)c9ccc(c%10cccc5c6%10)c7c89)c%11ccc%12c%13ccccc%13C(C)(C)c%12c%11"
    }
}

sigma_aldrich = {

    'Squarylium dye III': {
            'labels' : ['Squarylium dye III', "1,3-Bis[4-(dimethylamino)phenyl]-2,4-dihydroxycyclobutenediylium dihydroxide, bis(inner salt)", '149063'],
            'name': "1,3-Bis[4-(dimethylamino)phenyl]-2,4-dihydroxycyclobutenediylium dihydroxide, bis(inner salt)",
            'smiles': "CN(C)c1ccc(cc1)[C]2[C]([O-])[C]([C]2[O-])c3ccc(cc3)N(C)C"
        },

    'Coumarin 6': {
        'labels': ['coumarin 6', 'coumarin-6', '3-(2-Benzothiazolyl)-N,N-diethylumbelliferylamine', '3-(2-Benzothiazolyl)-7-(diethylamino)coumarin'],
        'name': "3-(2-Benzothiazolyl)-N,N-diethylumbelliferylamine",
        'smiles': "CCN(CC)c1ccc2C=C(C(=O)Oc2c1)c3sc4ccccc4n3"
    },

    'Coumarin 30': {
        'labels': ['coumarin 30', 'coumarin-30', 'coumarin 515', "3-(2-N-Methylbenzimidazolyl)-7-N,N-diethylaminocoumarin"],
        'name': "3-(2-N-Methylbenzimidazolyl)-7-N,N-diethylaminocoumarin",
        'smiles': "CCN(CC)c1ccc2C=C(C(=O)Oc2c1)c3nc4ccccc4n3C"
    },

    'Coumarin 102': {
        'labels': ['coumarin 102', 'coumarin-102', 'coumarin 480', "2,3,6,7-Tetrahydro-9-methyl-1H,5H-quinolizino(9,1-gh)coumarin", "8-Methyl-2,3,5,6-tetrahydro-1H,4H-11-oxa-3a-aza-benzo(de)anthracen-10-one"],
        'name': "2,3,6,7-Tetrahydro-9-methyl-1H,5H-quinolizino(9,1-gh)coumarin",
        'smiles': "CC1=CC(=O)Oc2c3CCCN4CCCc(cc12)c34"
    },

    'Coumarin 153': {
        'labels': ['coumarin 153', 'coumarin-153', '2,3,6,7-Tetrahydro-9-(trifluoromethyl)-1H,5H,11H-[1]benzopyrano(6,7,8-ij)quinolizin-11-one',
                   '2,3,6,7-Tetrahydro-9-trifluoromethyl-1H,5H-quinolizino(9,1-gh)coumarin', '8-Trifluoromethyl-2,3,5,6-4H-1,H-11-oxa-3a-aza-benzo[de]anthracen-10-one',
                   'coumarin 540A'],
        'name': "2,3,6,7-Tetrahydro-9-(trifluoromethyl)-1H,5H,11H-[1]benzopyrano(6,7,8-ij)quinolizin-11-one",
        'smiles': "FC(F)(F)C1=CC(=O)Oc2c3CCCN4CCCc(cc12)c34"
    },

    'D102': {
        'labels': ['D102', "(5-{4-[4-(2,2-diphenyl-vinyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopenta[b]indol-7-ylmethylene}-4-oxo-2-thioxo-thiazolidin-3-yl)acetic acid"],
        'name': "(5-{4-[4-(2,2-diphenyl-vinyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopenta[b]indol-7-ylmethylene}-4-oxo-2-thioxo-thiazolidin-3-yl)acetic acid",
        'smiles': "OC(=O)CN1C(=S)SC(=C/c2ccc3N(C4CCCC4c3c2)c5ccc(cc5)C=C(c6ccccc6)c7ccccc7)\C1=O"
    },

    'D131': {
        'labels': ['D131', "2-Cyano-3-[4-[4-(2,2-diphenylethenyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopent[b]indol-7-yl]-2-propenoic acid"],
        'name': "2-Cyano-3-[4-[4-(2,2-diphenylethenyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopent[b]indol-7-yl]-2-propenoic acid",
        'smiles': "OC(=O)C(=Cc1ccc2N(C3CCCC3c2c1)c4ccc(cc4)C=C(c5ccccc5)c6ccccc6)C#N"
    },

    'D149': {
        'labels': ['D149', "5-[[4-[4-(2,2-Diphenylethenyl)phenyl]-1,2,3-3a,4,8b-hexahydrocyclopent[b]indol-7-yl]methylene]-2-(3-ethyl-4-oxo-2-thioxo-5-thiazolidinylidene)-4-oxo-3-thiazolidineacetic acid"
                   'indoline dye D149', 'purple dye'],
        'name': "5-[[4-[4-(2,2-Diphenylethenyl)phenyl]-1,2,3-3a,4,8b-hexahydrocyclopent[b]indol-7-yl]methylene]-2-(3-ethyl-4-oxo-2-thioxo-5-thiazolidinylidene)-4-oxo-3-thiazolidineacetic acid",
        'smiles': "CCN1C(=S)SC(/C1=O)=C/2SC(=C/c3ccc4N([C@@H]5CCC[C@@H]5c4c3)c6ccc(cc6)C=C(c7ccccc7)c8ccccc8)/C(=O)N2CC(O)=O"
    },

    'D205': {
        'labels': ['D205', "5-[[4-[4-(2,2-Diphenylethenyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopent[b]indol-7-yl]methylene]-2-(3-octyl-4-oxo-2-thioxo-5-thiazolidinylidene)-4-oxo-3-thiazolidineacetic acid",
                   'indoline dye D205', 'purple dye'],
        'name': "5-[[4-[4-(2,2-Diphenylethenyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopent[b]indol-7-yl]methylene]-2-(3-octyl-4-oxo-2-thioxo-5-thiazolidinylidene)-4-oxo-3-thiazolidineacetic acid",
        'smiles': "CCCCCCCCN1C(=S)SC(C1=O)=C2SC(=Cc3ccc4N(C5CCCC5c4c3)c6ccc(cc6)C=C(c7ccccc7)c8ccccc8)C(=O)N2CC(O)=O"
    },

    'D358': {
        'labels': ['D358', "5-[3-(Carboxymethyl)-5-[[4-[4-(2,2-diphenylethenyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopent[b]indol-7-yl]methylene]-4-oxo-2-thiazoli dinylidene]-4-oxo-2-thioxo-3-thiazolidinedodecanoic acid"],
        'name': "5-[3-(Carboxymethyl)-5-[[4-[4-(2,2-diphenylethenyl)phenyl]-1,2,3,3a,4,8b-hexahydrocyclopent[b]indol-7-yl]methylene]-4-oxo-2-thiazoli dinylidene]-4-oxo-2-thioxo-3-thiazolidinedodecanoic acid",
        'smiles': "OC(=O)CCCCCCCCCCCN1C(=S)SC(C1=O)=C2SC(=Cc3ccc4N(C5CCCC5c4c3)c6ccc(cc6)C=C(c7ccccc7)c8ccccc8)C(=O)N2CC(O)=O"
    },

    'K19': {
        'labels': ['K19', 'Ru(4,4-dicarboxylic acid-2,2′-bipyridine)(4,4′-bis(p-hexyloxystyryl)-2,2-bipyridine)(NCS)2'],
        'name': "Ru(4,4-dicarboxylic acid-2,2′-bipyridine)(4,4′-bis(p-hexyloxystyryl)-2,2-bipyridine)(NCS)2",
        'smiles': "CCCCCCOC1=CC=C(C=C1)C=CC2=CC(=NC=C2)C3=NC=CC(=C3)C=CC4=CC=C(C=C4)OCCCCCC.C1=CN=C(C=C1C(=O)O)C2=NC=CC(=C2)C(=O)O.C(=[N-])=S.C(=[N-])=S.[Ru+2]"
    },

    'Merocyanine 540': {
        'labels': ['Merocyanine 540', '3(2H)-Benzoxazolepropanesulfonic acid, 2-[4-(1,3-dibutyltetrahydro-4,6-dioxo-2-thioxo-5(2H)-pyrimidinylidene)-2-butenylidene]-, sodium salt'],
        'name': "3(2H)-Benzoxazolepropanesulfonic acid, 2-[4-(1,3-dibutyltetrahydro-4,6-dioxo-2-thioxo-5(2H)-pyrimidinylidene)-2-butenylidene]-, sodium salt",
        'smiles': "[Na+].CCCCN1C(=O)C(=C/C=C\C=C2/Oc3ccccc3N2CCC[S]([O-])(=O)=O)C(=O)N(CCCC)C1=S"
    }

}

greatcell_solar = {

    'C106': {
        'labels': ['C106', '2-(4-Carboxypyridin-2-yl)pyridine-4-carboxylic acid;4-(5-hexylsulfanylthiophen-2-yl)-2-[4-(5-hexylsulfanylthiophen-2-yl)pyridin-2-yl]pyridine;ruthenium(2+);diisothiocyanate'],
        'name': "2-(4-Carboxypyridin-2-yl)pyridine-4-carboxylic acid;4-(5-hexylsulfanylthiophen-2-yl)-2-[4-(5-hexylsulfanylthiophen-2-yl)pyridin-2-yl]pyridine;ruthenium(2+);diisothiocyanate",
        'smiles': "CCCCCCSC1=CC=C(S1)C2=CC(=NC=C2)C3=NC=CC(=C3)C4=CC=C(S4)SCCCCCC.C1=CN=C(C=C1C(=O)O)C2=NC=CC(=C2)C(=O)O.C(=[N-])=S.C(=[N-])=S.[Ru+2]"
    }

}

# Combine dictionaries
all_dyes = {**dyenamo_dyes, **solaronix_dyes, **sigma_aldrich, **greatcell_solar}

# Merging redox couple data.
redox_couples = {
        'triiodide/iodide' : {'match' : ['I/I3', 'I3/I', 'triiodide/iodide', 'iodide/triiodide'],
                              'names':['I-/I3-', 'I3-/I-', 'triiodide/iodide', 'iodide/triiodide']
                              },
        'disulfide/thiolate' : { 'match' : ['T2/T', 'T/T2', 'disulfide/thiolate', 'thiolate/disulfide'],
                                 'names': ['T2/T-', 'T-/T2', 'disulfide/thiolate', 'thiolate/disulfide']
                                }
    }

#### Common Perovskite Materials ####

## Hole Transport Materials

solaronix_htls = {

    'Spiro-OMeTAD': {
        'labels': ['Spiro-OMeTAD',
                   "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
                   'C81H68N4O8',
                   'Spiro-MeOTAD',
                   'N7′-octakis(4-methoxyphenyl)-9,9′-spirobi[9H-fluorene]-2,2′,7,7′-tetramine',
                   'pp-Spiro-OMeTAD'
                   ],
        'name': "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
        'smiles': "COC1=CC=C(C=C1)N(C2=CC=C(C=C2)OC)C3=CC4=C(C=C3)C5=C(C46C7=C(C=CC(=C7)N(C8=CC=C(C=C8)OC)C9=CC=C(C=C9)OC)C1=C6C=C(C=C1)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC)C=C(C=C5)N(C1=CC=C(C=C1)OC)C1=CC=C(C=C1)OC"
    }
}

sigma_aldrich_htls = {
    'Cuprous thiocyanate': {
        'labels': ['Cuprous thiocyanate',
                   'Copper(I) thiocyanate',
                   "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
                   'CCuNS'
                   ],
        'name': "2,2',7,7'-Tetrakis-(N,N-di-4-methoxyphenylamino)-9,9'-spirobifluorene",
        'smiles': "C(#N)[S-].[Cu+]"
    },

    'EH44': {
        'labels': ['EH44',
                   "9-(2-Ethylhexyl)-N,N,N,N-tetrakis(4-methoxyphenyl)- 9H-carbazole-2,7-diamine)",
                   'C48H51N3O4'
                   ],
        'name': "9-(2-Ethylhexyl)-N,N,N,N-tetrakis(4-methoxyphenyl)- 9H-carbazole-2,7-diamine)",
        'smiles': ""
    },

    'Poly-TPD': {
        'labels': ['Poly-TPD',
                   "4-butyl-N,N-diphenylaniline",
                   'C22H23N'
                   ],
        'name': "4-butyl-N,N-diphenylaniline",
        'smiles': "CCCCC1=CC=C(C=C1)N(C2=CC=CC=C2)C3=CC=CC=C3"
    },

    'X59': {
        'labels': ['X59',
                   'Spiro[9H-fluorene-9,9′-[9H]xanthene]-2,7-diamine',
                   "N,N,N′,N′-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9′-xanthene]-2,7-diamine",
                   "2-N,2-N,7-N,7-N-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9'-xanthene]-2,7-diamine",
                   "N′,N′,N′′,N′′-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9′-xanthene]−2,7-diamine"
                   'C53H42N2O5'
                   ],
        'name': "2-N,2-N,7-N,7-N-tetrakis(4-methoxyphenyl)spiro[fluorene-9,9'-xanthene]-2,7-diamine",
        'smiles': "COC1=CC=C(C=C1)N(C2=CC=C(C=C2)OC)C3=CC4=C(C=C3)C5=C(C46C7=CC=CC=C7OC8=CC=CC=C68)C=C(C=C5)N(C9=CC=C(C=C9)OC)C1=CC=C(C=C1)OC"
    },

    'TFB': {
        'labels': ['TFB',
                   "N-(4-Butan-2-ylphenyl)-4-methyl-N-[4-(7-methyl-9,9-dioctylfluoren-2-yl)phenyl]aniline",
                   'C53H67N'
                   ],
        'name': "N-(4-Butan-2-ylphenyl)-4-methyl-N-[4-(7-methyl-9,9-dioctylfluoren-2-yl)phenyl]aniline",
        'smiles': "CCCCCCCCC1(C2=C(C=CC(=C2)C)C3=C1C=C(C=C3)C4=CC=C(C=C4)N(C5=CC=C(C=C5)C)C6=CC=C(C=C6)C(C)CC)CCCCCCCC"
    },
}

review_paper_htls = {

    'PTAA': {
        'labels': [
            "PTAA",
            "poly[bis(4-phenyl)(2,4,6-trimethylphenyl)amine]",
            "polytriarylamine"
            ],
        "name":'poly[bis(4-phenyl)(2,4,6-trimethylphenyl)amine]',
        "smiles": ""
    },

    '4-Ethyl-N-(4-ethylphenyl)aniline': {
        'labels': [
            "4-Ethyl-N-(4-ethylphenyl)aniline"
        ],
        "name": '4-Ethyl-N-(4-ethylphenyl)aniline',
        "smiles": "CCc1ccc(Nc2ccc(CC)cc2)cc1"
    },

    'N1-(4-(dimethylamino)phenyl)-N4,N4-dimethylbenzene-1,4-diamine': {
        'labels': [
            "N1-(4-(dimethylamino)phenyl)-N4,N4-dimethylbenzene-1,4-diamine"
        ],
        "name": 'N1-(4-(dimethylamino)phenyl)-N4,N4-dimethylbenzene-1,4-diamine',
        "smiles": "CN(C)c1ccc(Nc2ccc(cc2)N(C)C)cc1"
    },

    'bis(4-methylthiophenyl)amine': {
        'labels': [
            "bis(4-methylthiophenyl)amine"
        ],
        "name": 'bis(4-methylthiophenyl)amine',
        "smiles": "Cc1csc(Nc2scc(C)c2)c1"
    },

    'mp-SFX-3PA': {
        'labels': [
            "mp-SFX-3PA"
        ],
        "name": 'mp-SFX-3PA',
        "smiles": ""
    },
    'mm-SFX-3PA': {
        'labels': [
            "mm-SFX-3PA"
        ],
        "name": 'mm-SFX-3PA',
        "smiles": ""
    },
    'mp-SFX-2PA': {
        'labels': [
            "mp-SFX-2PA"
        ],
        "name": 'mp-SFX-2PA',
        "smiles": ""
    },
    'mm-SFX-2PA': {
        'labels': [
            "mm-SFX-2PA"
        ],
        "name": 'mm-SFX-2PA',
        "smiles": ""
    },
    'FDT': {
        'labels': [
            "FDT",
            "2′,7′-bis(bis(4-methoxyphenyl)amino)spiro[cyclopenta[2,1-b:3,4-b′]dithiophene-4,9′-fluorene]"
        ],
        "name": '2′,7′-bis(bis(4-methoxyphenyl)amino)spiro[cyclopenta[2,1-b:3,4-b′]dithiophene-4,9′-fluorene]',
        "smiles": "COc1ccc(cc1)N(c2ccc(OC)cc2)c3ccc4c5ccc(cc5C6(c7ccsc7c8sccc68)c4c3)N(c9ccc(OC)cc9)c%10ccc(OC)cc%10"
    },
    'X60': {
        'labels': [
            "X60",
            "N2,N2,N2',N2',N7,N7,N7',N7'-octakis(4-methoxyphenyl)spiro[fluorene-9,9'- xanthene]-2,2',7,7'-tetraamine"
        ],
        "name": "N2,N2,N2',N2',N7,N7,N7',N7'-octakis(4-methoxyphenyl)spiro[fluorene-9,9'- xanthene]-2,2',7,7'-tetraamine",
        "smiles": "COc1ccc(cc1)N(c2ccc(OC)cc2)c3ccc4c5ccc(cc5C6(c7ccsc7c8sccc68)c4c3)N(c9ccc(OC)cc9)c%10ccc(OC)cc%10"
    },
    'Spiro-S': {
        'labels': [
            "Spiro-S",
            "2,2′,7,7′-tetrakis[N,N-bis(p-methylsulfanylphenyl)amino]-9,9′-spirobifluorene"
        ],
        "name": "2,2′,7,7′-tetrakis[N,N-bis(p-methylsulfanylphenyl)amino]-9,9′-spirobifluorene",
        "smiles": "CSc1ccc(cc1)N(c2ccc(SC)cc2)c3ccc4c5ccc(cc5C6(c4c3)c7cc(ccc7c8ccc(cc68)N(c9ccc(SC)cc9)c%10ccc(SC)cc%10)N(c%11ccc(SC)cc%11)c%12ccc(SC)cc%12)N(c%13ccc(SC)cc%13)c%14ccc(SC)cc%14"
    },
    'Spiro-N': {
        'labels': [
            "Spiro-N",
            "2,2′,7,7′-tetrakis[N,N-bis(p-N,N-dimethylaminophenyl)amino]-9,9′-spirobifluorene"
        ],
        "name": "2,2′,7,7′-tetrakis[N,N-bis(p-N,N-dimethylaminophenyl)amino]-9,9′-spirobifluorene",
        "smiles": "CN(C)c1ccc(cc1)N(c2ccc(cc2)N(C)C)c3ccc4c5ccc(cc5C6(c4c3)c7cc(ccc7c8ccc(cc68)N(c9ccc(cc9)N(C)C)c%10ccc(cc%10)N(C)C)N(c%11ccc(cc%11)N(C)C)c%12ccc(cc%12)N(C)C)N(c%13ccc(cc%13)N(C)C)c%14ccc(cc%14)N(C)C"
    },
    'Spiro-E': {
        'labels': [
            "Spiro-E",
            "2,2′,7,7′-tetrakis[N,N-bis(p-ethylphenyl)amino]-9,9′-spirobifluorene"
        ],
        "name": "2,2′,7,7′-tetrakis[N,N-bis(p-ethylphenyl)amino]-9,9′-spirobifluorene",
        "smiles": "CCc1ccc(cc1)N(c2ccc(CC)cc2)c3ccc4c5ccc(cc5C6(c4c3)c7cc(ccc7c8ccc(cc68)N(c9ccc(CC)cc9)c%10ccc(CC)cc%10)N(c%11ccc(CC)cc%11)c%12ccc(CC)cc%12)N(c%13ccc(CC)cc%13)c%14ccc(CC)cc%14"
    },
    'P3HT': {
        'labels': [
            "P3HT",
            "Poly(3-hexylthiophene-2,5-diyl)"
        ],
        "name": "Poly(3-hexylthiophene-2,5-diyl)",
        "smiles": ""
    },
    'PCBTDPP': {
        'labels': [
            "PCBTDPP",
            "Poly[N-90-heptadecanyl-2,7carbazole-alt-3,6-bis(thiophen-5-yl)-2,5-dioctyl-2,5-dihydropyrrolo[3,4]pyrrole-1,4-dione]"
        ],
        "name": "Poly[N-90-heptadecanyl-2,7carbazole-alt-3,6-bis(thiophen-5-yl)-2,5-dioctyl-2,5-dihydropyrrolo[3,4]pyrrole-1,4-dione]",
        "smiles": ""
    },
    'PCPDTBT': {
        'labels': [
            "PCPDTBT",
            "Poly[2,6-(4,4-bis-(2-ethylhexyl)-4H-cyclopenta [2,1-b;3,4-b′]dithiophene)-alt-4,7(2,1,3-benzothiadiazole)]"
        ],
        "name": "Poly[2,6-(4,4-bis-(2-ethylhexyl)-4H-cyclopenta [2,1-b;3,4-b′]dithiophene)-alt-4,7(2,1,3-benzothiadiazole)]",
        "smiles": ""
    },
    'PDI': {
        'labels': [
            "PDI",
            "N,N′-dialkylperylenediimide"
        ],
        "name": "N,N′-dialkylperylenediimide",
        "smiles": ""
    },
    'TPD': {
        'labels': [
            "TPD",
            "N,N′-bis(3-methylphenyl)-N,N′-diphenylbenzidine"
        ],
        "name": "N,N′-bis(3-methylphenyl)-N,N′-diphenylbenzidine",
        "smiles": "Cc1cccc(c1)N(c2ccccc2)c3ccc(cc3)c4ccc(cc4)N(c5ccccc5)c6cccc(C)c6"
    },
    'pm-spiro-OMeTAD': {
        'labels': [
            "pm-spiro-OMeTAD",
            "N2 ,N2’,N7 ,N7’-tetrakis(3-methoxyphenyl)-N2 ,N2’,N7 ,N7’-tetrakis(4- methoxyphenyl)-9,9’-spirobi[fluorene]-2,2’,7,7’-tetraamine",
        ],
        "name": "N2 ,N2’,N7 ,N7’-tetrakis(3-methoxyphenyl)-N2 ,N2’,N7 ,N7’-tetrakis(4- methoxyphenyl)-9,9’-spirobi[fluorene]-2,2’,7,7’-tetraamine",
        "smiles": "COc1ccc(cc1)N(c2cccc(OC)c2)c3ccc4c5ccc(cc5C6(c4c3)c7cc(ccc7c8ccc(cc68)N(c9ccc(OC)cc9)c%10cccc(OC)c%10)N(c%11ccc(OC)cc%11)c%12cccc(OC)c%12)N(c%13ccc(OC)cc%13)c%14cccc(OC)c%14"
    },
    'po-spiro-OMeTAD': {
        'labels': [
            "po-spiro-OMeTAD",
            "N2,N2’,N7 ,N7’-tetrakis(2-methoxyphenyl)-N2,N2’,N7,N7’-tetrakis(4- methoxyphenyl)-9,9’-spirobi[fluorene]-2,2’,7,7’-tetraamine"

        ],
        "name": "N2,N2’,N7 ,N7’-tetrakis(2-methoxyphenyl)-N2,N2’,N7,N7’-tetrakis(4- methoxyphenyl)-9,9’-spirobi[fluorene]-2,2’,7,7’-tetraamine",
        "smiles": "COc1ccc(cc1)N(c2ccc3c4ccc(cc4C5(c3c2)c6cc(ccc6c7ccc(cc57)N(c8ccc(OC)cc8)c9ccccc9OC)N(c%10ccc(OC)cc%10)c%11ccccc%11OC)N(c%12ccc(OC)cc%12)c%13ccccc%13OC)c%14ccccc%14OC"
    },
    'PPyra‐XA': {
        'labels': [
            "PPyra‐XA",
        ],
        "name": "PPyra‐XA",
        "smiles": ""
    },
    'PPyra‐TXA': {
        'labels': [
            "PPyra‐TXA",
        ],
        "name": "PPyra‐TXA",
        "smiles": ""
    },
    'PPyra‐ACD': {
        'labels': [
            "PPyra‐ACD",
        ],
        "name": "PPyra‐ACD",
        "smiles": ""
    },
    'WY-1': {
        'labels': [
            "WY-1",
        ],
        "name": "WY-1",
        "smiles": ""
    },
    'WY-2': {
        'labels': [
            "WY-2",
        ],
        "name": "WY-2",
        "smiles": ""
    },
    'WY-3': {
        'labels': [
            "WY-3",
        ],
        "name": "WY-3",
        "smiles": ""
    },
    'CBP': {
        'labels': [
            "CBP",
            "4,4-N,N′-dicarbazole-1,1′-biphenyl"
        ],
        "name": "4,4-N,N′-dicarbazole-1,1′-biphenyl",
        "smiles": "C1=CC=C2C(=C1)C3=CC=CC=C3N2C4=CC=C(C=C4)C5=CC=C(C=C5)N6C7=CC=CC=C7C8=CC=CC=C86"
    },
    'pyrene': {
        'labels': [
            "pyrene",
        ],
        "name": "pyrene",
        "smiles": "c1cc2ccc3cccc4ccc(c1)c2c34"
    },
    'TPE': {
        'labels': [
            "TPE",
            "1,1,2,2-tetraphenylethene"
        ],
        "name": "1,1,2,2-tetraphenylethene",
        "smiles": "c1ccc(cc1)C(c2ccccc2)=C(c3ccccc3)c4ccccc4"
    },
    'bifluorenylidene': {
        'labels': [
            "bifluorenylidene",
        ],
        "name": "bifluorenylidene",
        "smiles": "c1ccc2c(c1)C=C3C2=CC=CC3=C4C=CC=C5c6ccccc6C=C45"
    },
    'CuSCN': {
        'labels': [
            "CuSCN",
            "Copper(I) thiocyanate"
        ],
        "name": "Copper(I) thiocyanate",
        "smiles": "[Cu]SC#N"
    },
    'TIPS-P': {
        'labels': [
            "TIPS-pentacene",
            "TIPS-P",
            "6,13-bis(triisopropylsilylethynyl) pentacene"
        ],
        "name": "6,13-bis(triisopropylsilylethynyl) pentacene",
        "smiles": "CC(C)[Si](C#Cc1c2cc3ccccc3cc2c(C#C[Si](C(C)C)(C(C)C)C(C)C)c4cc5ccccc5cc14)(C(C)C)C(C)C"
    },
    'KR216': {
        'labels': [
            "KR216",
            "4,4′‐dimethoxydiphenylamine‐substituted 9,9′‐bifluorenylidene"
        ],
        "name": "4,4′‐dimethoxydiphenylamine‐substituted 9,9′‐bifluorenylidene",
        "smiles": ""
    },
    'H11': {
        'labels': [
            "H11",
            "N2,N2,N2',N2',N7,N7,N7',N7'-octakis(4-methoxyphenyl)-9H,9'H-[9,9'-bifluorene]-2,2',7,7'- tetraamine"
        ],
        "name": "N2,N2,N2',N2',N7,N7,N7',N7'-octakis(4-methoxyphenyl)-9H,9'H-[9,9'-bifluorene]-2,2',7,7'- tetraamine",
        "smiles": "COc1ccc(cc1)N(c2ccc(OC)cc2)c3ccc4c(c3)C(C5c6cc(ccc6c7ccc(cc57)N(c8ccc(OC)cc8)c9ccc(OC)cc9)N(c%10ccc(OC)cc%10)c%11ccc(OC)cc%11)c%12cc(ccc4%12)N(c%13ccc(OC)cc%13)c%14ccc(OC)cc%14"
    },
    'H12': {
        'labels': [
            "H12",
            "N2,N2,N2',N2',N7,N7,N7',N7'-octakis(4-methoxyphenyl)-[9,9'-bifluorenylidene]-2,2',7,7'- tetraamine"
        ],
        "name": "N2,N2,N2',N2',N7,N7,N7',N7'-octakis(4-methoxyphenyl)-[9,9'-bifluorenylidene]-2,2',7,7'- tetraamine",
        "smiles": "COc1ccc(cc1)N(c2ccc(OC)cc2)c3ccc4c5ccc(cc5C(c4c3)=C6c7cc(ccc7c8ccc(cc68)N(c9ccc(OC)cc9)c%10ccc(OC)cc%10)N(c%11ccc(OC)cc%11)c%12ccc(OC)cc%12)N(c%13ccc(OC)cc%13)c%14ccc(OC)cc%14"
    },
    '1,3-Bis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)azulene': {
        'labels': [
            "1,3-Bis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)azulene"
        ],
        "name": "1,3-Bis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)azulene",
        "smiles": "CCCCCCCCOc1cc2N3c4ccccc4Oc5cccc(Oc2cc1c6cc(c7cc8Oc9cccc%10Oc%11ccccc%11N(c8cc7OCCCCCCCC)c9%10)c%12cccccc6%12)c35"
    },
    '5,7-Bis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)azulene': {
        'labels': [
            "5,7-Bis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)azulene"
        ],
        "name": "5,7-Bis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)azulene",
        "smiles": "CCCCCCCCOc1cc2N3c4ccccc4Oc5cccc(Oc2cc1c6cc7cccc7cc(c6)c8cc9Oc%10cccc%11Oc%12ccccc%12N(c9cc8OCCCCCCCC)c%10%11)c35"
    },
    '3,3´,5,5´-Tetrakis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)-1,1´-biphenyl': {
        'labels': [
            "3,3´,5,5´-Tetrakis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)-1,1´-biphenyl"
        ],
        "name": "3,3´,5,5´-Tetrakis(2-(octyloxy)benzo[5,6][1,4]oxazino[2,3,4-kl]phenoxazin-3-yl)-1,1´-biphenyl",
        "smiles": "CCCCCCCCOc1cc2N3c4ccccc4Oc5cccc(Oc2cc1c6cc(cc(c6)c7cc8Oc9cccc%10Oc%11ccccc%11N(c8cc7OCCCCCCCC)c9%10)c%12cc(cc(c%12)c%13cc%14Oc%15cccc%16Oc%17ccccc%17N(c%14cc%13OCCCCCCCC)c%15%16)c%18cc%19Oc%20cccc%21Oc%22ccccc%22N(c%19cc%18OCCCCCCCC)c%20%21)c35"
    },
    'di-TPA': {
        'labels': [
            "di-TPA",
            "N,N,N'',N''-tetrakis(4-methoxyphenyl)-[1,1':4',1''-terphenyl]-4,4''-diamine"
        ],
        "name": "N,N,N'',N''-tetrakis(4-methoxyphenyl)-[1,1':4',1''-terphenyl]-4,4''-diamine",
        "smiles": ""
    },
    'tri-TPA': {
        'labels': [
            "tri-TPA",
            "4,7,12-tris-[4-amino-[N,N-di-(4-methoxyphenyl)]-phenyl]-[2,2]paracyclophane"
        ],
        "name": "4,7,12-tris-[4-amino-[N,N-di-(4-methoxyphenyl)]-phenyl]-[2,2]paracyclophane",
        "smiles": ""
    },
    'tetra-TPA': {
        'labels': [
            "tetra-TPA",
            "4,7,12,15-tetrakis-[4-amino-[N,N-di-(4-methoxyphenyl)]-phenyl]-[2,2]paracyclophane",
            "PCP-TPA"
        ],
        "name": "4,7,12,15-tetrakis-[4-amino-[N,N-di-(4-methoxyphenyl)]-phenyl]-[2,2]paracyclophane",
        "smiles": ""
    },
    'TAE-1': {
        'labels': [
            "TAE-1",
            "tetra{4-[N,N-(4,4′-dimethoxydiphenylamino)]phenyl}ethene"
        ],
        "name": "tetra{4-[N,N-(4,4′-dimethoxydiphenylamino)]phenyl}ethene",
        "smiles": ""
    },
    'V852': {
        'labels': [
            "V852",
            "9,9',9''-(benzene-1,3,5-triyltrimethylylidene)tris[N,N,N',N'-tetrakis(4-methoxyphenyl)-9Hfluorene-2,7-diamine]"
        ],
        "name": "9,9',9''-(benzene-1,3,5-triyltrimethylylidene)tris[N,N,N',N'-tetrakis(4-methoxyphenyl)-9Hfluorene-2,7-diamine]",
        "smiles": ""
    },
    'V859': {
        'labels': [
            "V859",
            "9,9'-(benzene-1,2-diyldimethylylidene)bis[N,N,N',N'-tetrakis(4-methoxyphenyl)-9H-fluorene-2,7-diamine]"
        ],
        "name": "9,9'-(benzene-1,2-diyldimethylylidene)bis[N,N,N',N'-tetrakis(4-methoxyphenyl)-9H-fluorene-2,7-diamine]",
        "smiles": ""
    },
    'V862': {
        'labels': [
            "V862",
            "9,9'-(thiene-2,5-diyldimethylylidene)bis[N,N,N',N'-tetrakis(4-methoxyphenyl)-9H-fluorene-2,7-diamine]"
        ],
        "name": "9,9'-(thiene-2,5-diyldimethylylidene)bis[N,N,N',N'-tetrakis(4-methoxyphenyl)-9H-fluorene-2,7-diamine]",
        "smiles": ""
    },
    'PETMP': {
        'labels': [
            "PETMP",
            "pentaerythritol tetrakis(3-mercaptopropionate)"
        ],
        "name": "pentaerythritol tetrakis(3-mercaptopropionate)",
        "smiles": "OCC(CO)(CO)CO.OC(=O)CCS.OC(=O)CCS.OC(=O)CCS.OC(=O)CCS"
    },
    'PEDOT:PSS': {
        'labels': [
            "PEDOT:PSS",
            "poly(3,4-ethylenedioxythiophene) polystyrene sulfonate"
        ],
        "name": "poly(3,4-ethylenedioxythiophene) polystyrene sulfonate",
        "smiles": ""
    },
    'NiO': {
        'labels': [
            "NiO",
            "nickel oxide"
        ],
        "name": "nickel oxide",
        "smiles": ""
    },
    'Poly TPD': {
        'labels': [
            "poly TPD",
            "poly(4-butyl-N,N-diphenylaniline)"
        ],
        "name": "poly(4-butyl-N,N-diphenylaniline)",
        "smiles": "CCCCC1=CC=C(C=C1)N(C2=CC=CC=C2)C3=CC=CC=C3"
    },
}

all_htls = {**solaronix_htls, **sigma_aldrich_htls, **review_paper_htls}

all_etls = {
    'TiO2': { 'labels': [ 'titanium dioxide', 'TiO2'], 'name': 'titanium dioxide' },
'ZnO':{ 'labels':	['zinc oxide', 'ZnO'], 'name':'zinc oxide' },
'SnO2':{'labels': 	['tin dioxide', 'stannic oxide', 'SnO2'], 'name': 'tin dioxide' },
'SiO2': { 'labels':	['silicon dioxide', 'SiO2'], 'name': 'silicon dioxide'},
'NiO': { 'labels':	['nickel oxide', 'NiO'], 'name':'nickel oxide'},
'ZrO2': {	'labels':['zirconium dioxide', 'ZrO2'], 'name': 'zirconium dioxide'},
'PCBM' :{'labels': ['phenyl-C61-butyric acid methyl ester', 'PCBM'], 'name':'phenyl-C61-butyric acid methyl ester'},
'm-TiO2':{ 'labels':	['m-TiO2', 'meso-TiO2', 'mesoporous titanium dioxide'], 'structure': 'mesoporous', 'name':'titanium dioxide'},
'c-TiO2' :{'labels':	['c-TiO2', 'compact titanium dioxide' ], 'structure': 'compact', 'name': 'titanium dioxide'},
'c-SnO2' :{'labels':	['c-SnO2', 'compact tin dioxide' ], 'structure': 'compact', 'name': 'tin dioxide'},
'MgO/TiO2':{ 'labels':['MgO/TiO2'], 'structure': 'core-shell', 'name': 'magnesium oxide / titanium dioxide'},
'Al2O3/TiO2':{'labels':	[ 'Al2O3/TiO2'],	'structure': 'core-shell', 'name': 'aluminium oxide / titanium dioxide'},
'ZnO/TiO2': { 'labels':	['ZnO/TiO2'],	'structure': 'core-shell', 'name': 'zinc oxide / titanium dioxide'},
'TiO2/MgO':	{ 'labels':	[ 'TiO2/MgO'], 'structure': 'core-shell', 'name': 'titanium dioxide / magnesium oxide'},
'WO3/TiO2' : { 'labels': ['WO3/TiO2'], 'structure': 'core-shell', 'name': 'tungsten trioxide / titanium dioxide'},
'np-TiO2' 	: { 'structure': 'nanoparticle', 'labels': ['np-TiO2', 'titanium dioxide nanoparticles', 'TiO2 nanoparticles'], 'name': 'titanium dioxide nanoparticles'},
'Al2O3/ZnO' : { 'labels':	['Al2O3/ZnO'],	'structure': 'core-shell', 'name': 'aluminium oxide / zinc oxide'},
'ITO/ZnO' 	:{ 'labels':['ITO/ZnO'],	'structure': 'core-shell', 'name': 'indium tin oxide / zinc oxide'},
'ITO/Al2O3' :{ 'labels':['ITO/Al2O3'],	 'structure': 'core-shell', 'name': 'indium tin oxide / aluminium oxide'},
'ITO/V2O5' 	:{ 'labels':['ITO/V2O5'],	'structure': 'core-shell', 'name': 'indium tin oxide / vanadium(V) oxide'},
'ITO/TiO2' 	:{ 'labels':['ITO/TiO2'], 'structure': 'core-shell', 'name': 'indium tin oxide / titanium dioxide'},
'AZO':{ 'labels':	['aluminum doped zinc oxide', 'AZO', 'ZnO:Al'], 'name': 'aluminium doped zinc oxide'},
'HfO2':{ 	'labels':	['hafnium(IV) oxide', 'HfO2'], 'name':' hafnium(IV) oxide'},
'PEI/TiO2':{ 	'labels':	['polyethyleneimine / titanium dioxide', 'PEI/TiO2'], 'structure' : 'polyethyleneimine (PEI) thin layer on titanium dioxide',
                'name': 'polyethyleneimine / titanium dioxide '},
'PEI/ZnO' :	{'labels':	['polyethyleneimine / zinc oxide', 'PEI/ZnO' ] ,'structure': 'polyethyleneimine (PEI) thin layer on zinc oxide',
                'name': 'polyethyleneimine / zinc oxide'},
'Al2O3': {'labels':	['aluminium oxide ', 'Al2O3' ] ,
                'name': 'aluminium oxide'},
'ZSO': {'labels':	['Zn2SnO4 ', 'zinc stannate' ] ,
                'name': 'zinc stannate'},
'BCP': {'labels': ['BCP', 'bathocuproine', 'C26H20N2', 'CC3=NC2=C1N=C(C=C(C1=CC=C2C(=C3)C4=CC=CC=C4)C5=CC=CC=C5)C'], 'name': 'bathocuproine'},
'C60': {'labels': ['C60', 'buckminsterfullerene'], 'name': 'buckminsterfullerene'}
}

# Common perovskite abbreviations

perovskite_abbreviations = {
    'MA' : 'CH3NH3',
    'BA': 'C4H11N',
    'FA':'CH5N2',
    'PEA': 'C8H11N',
    'EDA': 'C2H8N2'
}

# List of disallowed tags for section headings
blacklist_headings = [
    'intro', 'introduction', 'background', 'theory', 'result', 'results', 'discussion', 'discussions', 'conclusion', 'conclusions', 'analysis'
]


common_quantum_dot_materials = [
    'CdS',
]

# Lists of key terms for classification of different PV types...
psc_indicators = [
    'perovskite', 'perovskites', 'psc', 'pscs', 'spiro ometad', 'pedot'
]

qdsc_indicators = [
    'quantum dot', 'qdsc', 'qdscs', 'qdssc', 'qdsscs', 'quantum dots', 'cds', 'cdse'
]

dsc_indicators = [
    'dye sensitized', 'dye sensitised', 'dsc', 'dscs', 'dssc', 'dsscs', 'n719', 'co sensitization', 'cosensitization',
    'co sensitisation', 'cosensitisation'
]

# specific tokens that should be merged together in classification analysis
token_tuples_to_merge = {
    ('quantum', 'dot'), ('quantum', 'dots'), ('spiro', 'ometad'), ('dye', 'sensitized'), ('dye', 'sensitised'), ('co', 'sensitization'),
    ('co', 'sensitisation')
}
