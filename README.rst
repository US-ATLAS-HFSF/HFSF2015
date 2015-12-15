Hadronic Final State Forum 2015
===============================

macros
------

This contains a series of useful macros -- both python and C++ -- to help move you along to the fun stuff.

To do work::

    mkdir MyWorkDir && cd MyWorkDir
    rcSetup Base,2.3.38
    git clone https://github.com/UCATLAS/xAODAnaHelpers.git
    git clone https://github.com/US-ATLAS-HFSF/HFSF2015.git
    rc find_packages
    rc compile
    cd HFSF2015/example
    rucio download --nrandom 1 mc15_13TeV.423104.Pythia8EvtGen_A14NNPDF23LO_gammajet_DP140_280.merge.DAOD_JETM4.e3791_s2608_s2183_r6765_r6282_p2452
    wget https://atlasdqm.web.cern.ch/atlasdqm/grlgen/All_Good/data15_13TeV.periodAllYear_DetStatus-v73-pro19-08_DQDefects-00-01-02_PHYS_StandardGRL_All_Good_25ns.xml $ROOTCOREBIN/data/xAODAnaHelpers/
    xAH_run.py --nevents 10 --files /your/test/file.root --config gamma_b.py --force direct

Documentation for xAH available here: https://xaodanahelpers.readthedocs.org/en/master/Intro.html

Can choose to directly make histograms (see https://xaodanahelpers.readthedocs.org/en/master/Histograms.html) or make nTuples (https://xaodanahelpers.readthedocs.org/en/master/Algorithms.html#ntuple-creation). 

Can run on grid, condor, LSF, or local. FAX supported: can use remote datasets locally! Use --inputDQ2 my_dataset_name/ (need grid proxy setup).

Need any easy way to fetch sample weights? https://github.com/kratsg/SampleWeights (documentation directly provided in README). The apply_weights.py script can add these weights to an ntuple; should be straightforward to use.

Need to calibrate and use fat jets? See example from X->hh->bbbb: https://svnweb.cern.ch/trac/atlasphys-exo/browser/Physics/Exotic/JDM/hh4b/Run2/Code/XhhCommon/trunk/scripts/XhhBoosted_config.py
