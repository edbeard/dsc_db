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
                   "Ruthenizer 535-bisTBA"],
        'name': "1-Butanaminium, N,N,N-tributyl-, hydrogen (OC-6-32)-[[2,2´:6´,2´´-terpyridine]-4,4´,4´´-tricarboxylato(3-)-κN1,κN1´,κN1´´]tris(thiocyanato-κN)ruthenate(4-) (2:2:1)",
        'smiles': ''
    },

    'DN-FR04': {
        'labels': ['DN-FR04', 'C101', "Ruthenate(2-), [[2,2´-bipyridine]-4,4´-dicarboxylato(2-)-κN1,κN1´][4,4´-bis(5-hexyl-2-thienyl)-2,2´-bipyridine-κN1,κN1´]bis(thiocyanato-κN)-, hydrogen (1:2), (OC-6-32)-"],
        'name': "Ruthenate(2-), [[2,2´-bipyridine]-4,4´-dicarboxylato(2-)-κN1,κN1´][4,4´-bis(5-hexyl-2-thienyl)-2,2´-bipyridine-κN1,κN1´]bis(thiocyanato-κN)-, hydrogen (1:2), (OC-6-32)-",
        'smiles': ''
    }
}

all_dyes = dyenamo_dyes