text = ["Compressor-1/4-R134a        99","Compressor-1/4-R600a        99","Filter-15g                  99","Filter-20g                  99","Filter-30g                  99", 
        "Capilre                     99","Relie-7ajra                 99","Klixon-k7al                 99","Thermostat-3adiya           99","Thermostat-9sira            99",
        "Thermostat-twila            99","Plaka-125L                  99","Plaka-230L                  99","Plaka-290L                  99","Plaka-500L                  99",
        "Plaka-800L                  99","Valve-Avee-Tige             99","Valve-sans-Tige             99","Valve-Rapid                 99","Coutube-P.T                 99",
        "Condensseur-1/4             99","Condensseur-1/5             99","R-134-1kg                   99","R-134-3kg                   99","R-134-1kg-A.V               99",
        "R-600-3kg                   99"]
with open("1test.txt", 'w') as f:
    for i in text:
        f.write(i+'\n')