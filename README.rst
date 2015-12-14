Hadronic Final State Forum 2015
===============================

macros
------

This contains a series of useful macros -- both python and C++ -- to help move you along to the fun stuff.

To do work:

```mkdir MyWorkDir && cd MyWorkDir

asetup 2.3.38,here

git clone https://github.com/UCATLAS/xAODAnaHelpers.git

git clone https://github.com/US-ATLAS-HFSF/HFSF2015.git

rc find_packages

rc compile

cd HFSF2015/example

rucio download --nrandom 1 mc15_13TeV.423104.Pythia8EvtGen_A14NNPDF23LO_gammajet_DP140_280.merge.DAOD_JETM4.e3791_s2608_s2183_r6765_r6282_p2452
xAH_run.py --nevents 10 --files /your/test/file.root --config gamma_b.py --force direct
```
