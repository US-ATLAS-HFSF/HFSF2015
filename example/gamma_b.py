'''
    Example python script to be run like

        xAH_run.py --files ... --config gamma_b.py ... <driver>

    Note that unlike the JSON configuration example, you also have access to
the command line arguments passed in and parsed by xAH_run.py under the global
variable `args`. For example, there is an `isMC` flag which can be used to
configure your job options dynamically

        if not args.is_MC:
            systName = "Nominal"
            systVal = 0
        else:
            systName = "All"
            systVal = 1

    If you want to know what arguments are passed in, you can simply write

        print(args)

    to see the namespace associated with it, or look at the source xAH_run.py
here: https://github.com/UCATLAS/xAODAnaHelpers/blob/master/scripts/xAH_run.py
'''

from xAH_config import xAH_config
c = xAH_config()

c.setalg("BasicEventSelection", {"m_debug": False,
                                 "m_truthLevelOnly": False,
                                 "m_applyGRLCut": True,
                                 "m_GRLxml": "$ROOTCOREBIN/data/xAODAnaHelpers/data15_13TeV.periodAllYear_DetStatus-v73-pro19-08_DQDefects-00-01-02_PHYS_StandardGRL_All_Good_25ns.xml",
                                 "m_doPUreweighting": False,
                                 "m_vertexContainerName": "PrimaryVertices",
                                 "m_PVNTrack": 2,
                                 "m_useMetaData": True,
                                 "m_derivationName": "JETM4",
                                 "m_triggerSelection": "HLT_g140_loose||HLT_g120_loose||HLT_g100_loose|HLT_g80_loose||HLT_g70_loose||HLT_g60_loose",
                                 "m_storeTrigDecisions": True,
                                 "m_applyTriggerCut": False,
                                 "m_storeTrigKeys": True,
                                 "m_storePassHLT": True
                                })

c.setalg("JetCalibrator", {"m_name": "JetCalibration",
                           "m_debug": False,
                           "m_inContainerName": "AntiKt4EMTopoJets",
                           "m_outContainerName": "AntiKt4EMTopoJetsCalib",
                           "m_jetAlgo": "AntiKt4EMTopo"
                          })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BJetTool70",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName": "$ROOTCOREBIN/data/xAODAnaHelpers/2015-PreRecomm-13TeV-MC12-CDI-October23_v1.root",
                                     "m_operatingPt": "FixedCutBEff_70",
                                     "m_decor": "BTag",
                                     "m_decorSF": ""
                                    })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BJetTool85",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName": "$ROOTCOREBIN/data/xAODAnaHelpers/2015-PreRecomm-13TeV-MC12-CDI-October23_v1.root",
                                     "m_operatingPt": "FixedCutBEff_85",
                                     "m_decor": "BTag",
                                     "m_decorSF": ""
                                    })

c.setalg("JetHistsAlgo", {"m_debug": False,
                          "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                          "m_detailStr": "kinematic",
                          "m_name": "NoPreSel"
                        })

c.setalg("PhotonCalibrator", {"m_debug": False,
                              "m_inContainerName": "Photons",
                              "m_outContainerName": "PhotonsCalib",
                              "m_esModel": "es2015PRE",
                              "m_decorrelationModel": "1NP_v1"
                             })

c.setalg("PhotonSelector", {"m_debug": False,
                            "m_inContainerName": "PhotonsCalib",
                            "m_outContainerName": "PhotonsBase",
                            "m_photonIdCut": "Tight",
                            "m_pT_min": 20,
                            "m_eta_max": 1.37,
                            "m_vetoCrack": False
                           })

c.setalg("OverlapRemover", {"m_debug": False,
                            "m_inContainerName_Photons": "PhotonsBase",
                            "m_inContainerName_Jets": "AntiKt4EMTopoJetsCalib",
                            "m_outContainerName_Photons": "PhotonsBaseOR",
                            "m_outContainerName_Jets": "AntiKt4EMTopoJetsCalibOR",
                            "m_decorateSelectedObjects": True,
                            "m_createSelectedContainers": True
                           })


c.setalg("TreeAlgo", {"m_debug": False,
                      "m_name": "GammaB",
                      "m_jetContainerName": "AntiKt4EMTopoJetsCalibOR",
                      "m_jetDetailStr": "kinematic energy scales substructure flavorTag truth trackPV sfFTagFix7085",
                      "m_photonContainerName": "PhotonsBaseOR",
                      "m_photonDetailStr": "kinematic isolation PID",
                      "m_trigDetailStr": "basic menuKeys passTriggers"
                    })
