from xAH_config import xAH_config
c = xAH_config()

c.setalg("BasicEventSelection", {"m_debug": false,
                                 "m_truthLevelOnly": false,
                                 "m_applyGRLCut": true,
                                 "m_GRLxml": "$ROOTCOREBIN/data/xAODAnaHelpers/data15_13TeV.periodAllYear_DetStatus-v73-pro19-08_DQDefects-00-01-02_PHYS_StandardGRL_All_Good_25ns.xml",
                                 "m_doPUreweighting": false,
                                 "m_vertexContainerName": "PrimaryVertices",
                                 "m_PVNTrack": 2,
                                 "m_useMetaData": false
                                })

c.setalg("JetCalibrator", {"m_name": "JetCalibration",
                           "m_debug": false,
                           "m_inContainerName": "AntiKt4EMTopoJets",
                           "m_outContainerName": "AntiKt4EMTopoJetsCalib",
                           "m_jetAlgo": "AntiKt4EMTopo"
                          })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BJetTool70",
                                     "m_debug": false,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName": "$ROOTCOREBIN/data/xAODAnaHelpers/2015-PreRecomm-13TeV-MC12-CDI-October23_v1.root",
                                     "m_operatingPt": "FixedCutBEff_70",
                                     "m_decor": "BTag",
                                     "m_decorSF": ""
                                    })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BJetTool85",
                                     "m_debug": false,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName": "$ROOTCOREBIN/data/xAODAnaHelpers/2015-PreRecomm-13TeV-MC12-CDI-October23_v1.root",
                                     "m_operatingPt": "FixedCutBEff_85",
                                     "m_decor": "BTag",
                                     "m_decorSF": ""
                                    })

c.setalg("JetHistsAlgo", {"m_debug": false,
                          "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                          "m_detailStr": "kinematic",
                          "m_name": "NoPreSel"
                        })

c.setalg("PhotonCalibrator", {"m_debug": false,
                              "m_inContainerName": "Photons",
                              "m_outContainerName": "PhotonsCalib",
                              "m_esModel": "es2015PRE",
                              "m_decorrelationModel": "1NP_v1"
                             })

c.setalg("PhotonSelector", {"m_debug": false,
                            "m_inContainerName": "PhotonsCalib",
                            "m_outContainerName": "PhotonsBase",
                            "m_pT_min": 150,
                            "m_eta_max": 1.37,
                            "m_vetoCrack": false
                           })

c.setalg("TreeAlgo", {"m_debug": false,
                      "m_name": "GammaB",
                      "m_jetContainerName": "AntiKt4EMTopoJetsCalib",
                      "m_jetDetailStr": "kinematic energy scales flavorTag sfFTagFix7085",
                      "m_photonContainerName": "PhotonsBase",
                      "m_photonDetailStr": "kinematic isolation PID"
                    })
