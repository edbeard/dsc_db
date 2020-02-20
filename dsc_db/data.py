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
    },

}


template = {
    'Ruthenizer 535': {
        'labels' : [],
        'name': "",
        'smiles': ""
    }
}

# Combine dictionaries
all_dyes = {**dyenamo_dyes, **solaronix_dyes, **sigma_aldrich, **greatcell_solar}