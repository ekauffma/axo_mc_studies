import argparse
import awkward as ak
import datetime
import json
import numpy as np
import ROOT
from sampleBuilder import samples

def load_cpp():
    """Load C++ helper functions."""
    cpp_source = "helpers.h"
    ROOT.gInterpreter.Declare(f'#include "{str(cpp_source)}"')

todaysDate = datetime.date.today().strftime('%Y%m%d')

# limits for histograms
min_score_v3 = 0
max_score_v3 = 4000
min_score_v4 = 0
max_score_v4 = 200
bins_score = 400

# axol1tl thresholds
threshold_vtight_v3 = 25000/16
threshold_tight_v3 = 20486/16
threshold_nominal_v3 = 18580/16
threshold_loose_v3 = 17596/16
threshold_vloose_v3 = 15717/16
threshold_vtight_v4 = 557/16
threshold_tight_v4 = 456/16
threshold_nominal_v4 = 415/16
threshold_loose_v4 = 389/16
threshold_vloose_v4 = 346/16



def main(dataset, out_dir):

    # get dataframe from samples
    print("Getting dataframes")
    df = samples[dataset].getNewDataframe()

    # create output ROOT file
    print("Creating output ROOT file")
    fileName = f'{out_dir}/hists_{dataset}_{todaysDate}.root'
    output_file = ROOT.TFile(
        fileName,
        'RECREATE'
    )

    print("Creating and writing histogram for AXO v3 score")
    histModel = ROOT.RDF.TH1DModel(
        "axol1tl_score_v3",
        "axol1tl_score_v3",
        bins_score,
        min_score_v3,
        max_score_v3,
    )
    hist_score_v3 = df.Histo1D(
        histModel,
        "axol1tl_score_v3"
    )
    hist_score_v3.Write()

    print("Creating and writing histogram for AXO v4 score")
    histModel = ROOT.RDF.TH1DModel(
        "axol1tl_score_v4",
        "axol1tl_score_v4",
        bins_score,
        min_score_v4,
        max_score_v4,
    )
    hist_score_v4 = df.Histo1D(
        histModel,
        "axol1tl_score_v4"
    )
    hist_score_v4.Write()

    print("Creating and writing histogram for AXO v3 efficiency")
    hist_eff_v3 = ROOT.TH1D(
        "axo_efficiency_v3",
        "axo_efficiency_v3",
        hist_score_v3.GetNbinsX(),
        hist_score_v3.GetXaxis().GetXmin(),
        hist_score_v3.GetXaxis().GetXmax()
    )
    score_integral = float(hist_score_v3.Integral())
    for j in range(1, hist_score_v3.GetNbinsX()+1):
        # calculate partial sum
        score_integral_current = float(hist_score_v3.Integral(j, hist_score_v3.GetNbinsX()))
        # calculate uncertainty as sqrt(N)
        uncertainty = np.sqrt(score_integral_current)
        # scale sum and uncertainty by total integral
        score_integral_current = score_integral_current/score_integral
        uncertainty = uncertainty/score_integral

        # set bin content and error of histogram
        hist_eff_v3.SetBinContent(j, score_integral_current)
        hist_eff_v3.SetBinError(j, uncertainty)
    hist_eff_v3.Write()

    print("Creating and writing histogram for AXO v4 efficiency")
    hist_eff_v4 = ROOT.TH1D(
        "axo_efficiency_v4",
        "axo_efficiency_v4",
        hist_score_v4.GetNbinsX(),
        hist_score_v4.GetXaxis().GetXmin(),
        hist_score_v4.GetXaxis().GetXmax()
    )
    score_integral = float(hist_score_v4.Integral())
    for j in range(1, hist_score_v4.GetNbinsX()+1):
        # calculate partial sum
        score_integral_current = float(hist_score_v4.Integral(j, hist_score_v4.GetNbinsX()))
        # calculate uncertainty as sqrt(N)
        uncertainty = np.sqrt(score_integral_current)
        # scale sum and uncertainty by total integral
        score_integral_current = score_integral_current/score_integral
        uncertainty = uncertainty/score_integral
                                                                                             
        # set bin content and error of histogram
        hist_eff_v4.SetBinContent(j, score_integral_current)
        hist_eff_v4.SetBinError(j, uncertainty)
    hist_eff_v4.Write()

    print(f"Efficiency Values for AXOL1TL v3 with {dataset} MC:")
    print(f"    VTight Threshold = {threshold_vtight_v3}: ", hist_eff_v3.GetBinContent(hist_eff_v3.FindBin(threshold_vtight_v3)))
    print(f"    Tight Threshold = {threshold_tight_v3}: ", hist_eff_v3.GetBinContent(hist_eff_v3.FindBin(threshold_tight_v3)))
    print(f"    Nominal Threshold = {threshold_nominal_v3}: ", hist_eff_v3.GetBinContent(hist_eff_v3.FindBin(threshold_nominal_v3)))
    print(f"    Loose Threshold = {threshold_loose_v3}: ", hist_eff_v3.GetBinContent(hist_eff_v3.FindBin(threshold_loose_v3)))
    print(f"    VLoose Threshold = {threshold_vloose_v3}: ", hist_eff_v3.GetBinContent(hist_eff_v3.FindBin(threshold_vloose_v3)))

    print(f"Efficiency Values for AXOL1TL v4 with {dataset} MC:")
    print(f"    VTight Threshold = {threshold_vtight_v4}: ", hist_eff_v4.GetBinContent(hist_eff_v4.FindBin(threshold_vtight_v4)))
    print(f"    Tight Threshold = {threshold_tight_v4}: ", hist_eff_v4.GetBinContent(hist_eff_v4.FindBin(threshold_tight_v4)))
    print(f"    Nominal Threshold = {threshold_nominal_v4}: ", hist_eff_v4.GetBinContent(hist_eff_v4.FindBin(threshold_nominal_v4)))
    print(f"    Loose Threshold = {threshold_loose_v4}: ", hist_eff_v4.GetBinContent(hist_eff_v4.FindBin(threshold_loose_v4)))
    print(f"    VLoose Threshold = {threshold_vloose_v4}: ", hist_eff_v4.GetBinContent(hist_eff_v4.FindBin(threshold_vloose_v4)))

    df = df.Filter("nScoutingMuon>=2")
    df = df.Define("leadMuonCharge","ScoutingMuon_charge.empty()? 0.f : ScoutingMuon_charge[0]")
    df = df.Define("subLeadMuonCharge","ScoutingMuon_charge.empty()? 0.f : ScoutingMuon_charge[1]")
    df = df.Define("oppositeMuonCharge", "leadMuonCharge!=subLeadMuonCharge")
    df = df.Filter("oppositeMuonCharge")
    df = df.Define("muonP4", "ConstructP4(ScoutingMuon_pt, ScoutingMuon_eta, ScoutingMuon_phi, ScoutingMuon_m)")
    df = df.Define("diMuonInvMass", "(muonP4[0] + muonP4[1]).M()")

    print("Creating and writing histogram for dimuon inv. mass + axo v3")
    histModel = ROOT.RDF.TH2DModel(
        "diMuonInvMass_axov3",
        "diMuonInvMass_axov3",
        200,
        0.0,
        15.0,
        hist_score_v3.GetNbinsX(),
        hist_score_v3.GetXaxis().GetXmin(),
        hist_score_v3.GetXaxis().GetXmax()
    )
    hist_dimuonmass_v3 = df.Histo2D(
        histModel,
        "diMuonInvMass",
        "axol1tl_score_v3"
    )
    hist_dimuonmass_v3.Write()

    print("Creating and writing histogram for dimuon inv. mass + axo v4")
    histModel = ROOT.RDF.TH2DModel(
        "diMuonInvMass_axov4",
        "diMuonInvMass_axov4",
        200,
        0.0,
        15.0,
        hist_score_v4.GetNbinsX(),
        hist_score_v4.GetXaxis().GetXmin(),
        hist_score_v4.GetXaxis().GetXmax()
    )
    hist_dimuonmass_v4 = df.Histo2D(
        histModel,
        "diMuonInvMass",
        "axol1tl_score_v4"
    )
    hist_dimuonmass_v4.Write()

    output_file.Close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This program creates a histogram of the AXO score and efficiency for a given sample"
    )
    parser.add_argument(
        "-d",
        "--dataset",
        help="which dataset to create the histogram for"
    )
    parser.add_argument(
        "-o",
        "--out_dir",
        default = ".",
        help="directory to save files to"
    )

    args = parser.parse_args()

    load_cpp()

    main(args.dataset, args.out_dir)
