import ROOT
import argparse
import datetime
import json
import numpy as np

todaysDate = datetime.date.today().strftime('%Y%m%d')

# axol1tl thresholds
thresholds_values_v3 = [25000/16, 20486/16, 18580/16, 17596/16, 15717/16]
thresholds_values_v4 = [557/16, 456/16, 415/16, 389/16, 346/16]
thresholds_names = ["VTight", "Tight", "Nominal", "Loose", "VLoose"]
thresholds_colors = ["#5790fc", "#f89c20", "#e42536", "#964a8b", "#9c9ca1"]

# for computing signal yield
n_sigma = 3
jpsi_low_edge = 3.0969 - n_sigma * 0.03615
jpsi_high_edge = 3.0969 + n_sigma * 0.03615

def main(input_file, output_dir, dataset):

    ROOT.gStyle.SetTitleSize(0.05, "X")
    ROOT.gStyle.SetTitleSize(0.05, "Y")

    f = ROOT.TFile(input_file)

    # load histograms from input file
    score_hist_v3 = f.Get("axol1tl_score_v3")
    score_hist_v4 = f.Get("axol1tl_score_v4")
    eff_hist_v3 = f.Get("axo_efficiency_v3")
    eff_hist_v4 = f.Get("axo_efficiency_v4")

    # draw score plot for v3
    c_score_v3 = ROOT.TCanvas("c_score_v3", "Anomaly Score", 1000, 600)

    score_hist_v3.SetMarkerColor(1)
    score_hist_v3.SetMarkerStyle(20)
    score_hist_v3.GetXaxis().SetTitle("AXOL1TL v3 Score")
    score_hist_v3.GetYaxis().SetTitle("Counts")
    score_hist_v3.SetStats(0)
    score_hist_v3.SetTitle(" ")
    max_val = 10*score_hist_v3.GetBinContent(score_hist_v3.GetMaximumBin())
    score_hist_v3.GetYaxis().SetRangeUser(1e-1, max_val)
    score_hist_v3.GetXaxis().SetRangeUser(0, 3000)
    score_hist_v3.Draw("HIST")
    
    lines = []
    for i in range(len(thresholds_names)):
        lines.append(ROOT.TLine(thresholds_values_v3[i], 0, thresholds_values_v3[i], max_val))
        lines[-1].SetLineColor(ROOT.TColor.GetColor(thresholds_colors[i]))
        lines[-1].SetLineStyle(2)
        lines[-1].SetLineWidth(2)
        lines[-1].Draw("same")

    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(score_hist_v3, f"{dataset} Score", "l")
    for i in range(len(lines)):
        legend.AddEntry(lines[i], f"AXO {thresholds_names[i]} Threshold", "l")
    legend.SetTextSize(0.04)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()

    c_score_v3.SetLogy()
    c_score_v3.Draw()
    c_score_v3.SaveAs(f"{output_dir}/axo_score_v3_{dataset}_{todaysDate}.png")
    c_score_v3.Close()


    # draw score plot for v4
    c_score_v4 = ROOT.TCanvas("c_score_v4", "Anomaly Score", 1000, 600)
                                                                               
    score_hist_v4.SetMarkerColor(1)
    score_hist_v4.SetMarkerStyle(20)
    score_hist_v4.GetXaxis().SetTitle("AXOL1TL v4 Score")
    score_hist_v4.GetYaxis().SetTitle("Counts")
    score_hist_v4.SetStats(0)
    score_hist_v4.SetTitle(" ")
    max_val = 10*score_hist_v4.GetBinContent(score_hist_v4.GetMaximumBin())
    score_hist_v4.GetYaxis().SetRangeUser(1e-1, max_val)
    score_hist_v4.GetXaxis().SetRangeUser(0, 150)
    score_hist_v4.Draw("HIST")
    
    lines = []                                                                                 
    for i in range(len(thresholds_names)):                                                                                                                              
        lines.append(ROOT.TLine(thresholds_values_v4[i], 0, thresholds_values_v4[i], max_val))
        lines[-1].SetLineColor(ROOT.TColor.GetColor(thresholds_colors[i]))
        lines[-1].SetLineStyle(2)
        lines[-1].SetLineWidth(2)
        lines[-1].Draw("same")

    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(score_hist_v4, f"{dataset} Score", "l")
    for i in range(len(lines)):
        legend.AddEntry(lines[i], f"AXO {thresholds_names[i]} Threshold", "l")
    legend.SetTextSize(0.04)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
                                                                               
    c_score_v4.SetLogy()
    c_score_v4.Draw()
    c_score_v4.SaveAs(f"{output_dir}/axo_score_v4_{dataset}_{todaysDate}.png")
    c_score_v4.Close()

    # draw efficiency histogram for v3
    c_eff_v3 = ROOT.TCanvas("c_eff_v3", "Anomaly Score", 1000, 600)

    eff_hist_v3.SetMarkerColor(1)
    eff_hist_v3.GetXaxis().SetTitle("AXOL1TL v3 Score");
    eff_hist_v3.GetYaxis().SetTitle("Fraction of Events Passing Threshold");
    eff_hist_v3.SetStats(0)
    eff_hist_v3.SetTitle(" ")
    eff_hist_v3.GetYaxis().SetRangeUser(1e-8, 1.5)
    eff_hist_v3.GetXaxis().SetRangeUser(0, 3000)
    eff_hist_v3.Draw("HIST")

    lines = []
    for i in range(len(thresholds_names)):
        lines.append(ROOT.TLine(thresholds_values_v3[i], 0, thresholds_values_v3[i], 1.5))
        lines[-1].SetLineColor(ROOT.TColor.GetColor(thresholds_colors[i]))
        lines[-1].SetLineStyle(2)
        lines[-1].SetLineWidth(2)
        lines[-1].Draw("same")

    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(eff_hist_v3, f"{dataset} Efficiency", "l")
    for i in range(len(lines)):
        legend.AddEntry(lines[i], f"AXO {thresholds_names[i]} Threshold", "l")
    legend.SetTextSize(0.04)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()

    c_eff_v3.SetLogy()
    c_eff_v3.Draw()
    c_eff_v3.SaveAs(f"{output_dir}/axo_eff_v3_{dataset}_{todaysDate}.png")
    c_eff_v3.Close()


    # draw efficiency histogram for v4
    c_eff_v4 = ROOT.TCanvas("c_eff_v4", "Anomaly Score", 1000, 600)
                                                                             
    eff_hist_v4.SetMarkerColor(1)
    eff_hist_v4.GetXaxis().SetTitle("AXOL1TL v4 Score");
    eff_hist_v4.GetYaxis().SetTitle("Fraction of Events Passing Threshold");
    eff_hist_v4.SetStats(0)
    eff_hist_v4.SetTitle(" ")
    eff_hist_v4.GetYaxis().SetRangeUser(1e-8, 1.5)
    eff_hist_v4.GetXaxis().SetRangeUser(0, 150)
    eff_hist_v4.Draw("HIST")

    lines = []                                                                             
    for i in range(len(thresholds_names)):                                                                                                                         
        lines.append(ROOT.TLine(thresholds_values_v4[i], 0, thresholds_values_v4[i], 1.5))                                                                        
        lines[-1].SetLineColor(ROOT.TColor.GetColor(thresholds_colors[i]))
        lines[-1].SetLineStyle(2)
        lines[-1].SetLineWidth(2)
        lines[-1].Draw("same")

    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(eff_hist_v4, f"{dataset} Efficiency", "l")
    for i in range(len(lines)):                                                
        legend.AddEntry(lines[i], f"AXO {thresholds_names[i]} Threshold", "l")
    legend.SetTextSize(0.04)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
                                                                             
    c_eff_v4.SetLogy()
    c_eff_v4.Draw()
    c_eff_v4.SaveAs(f"{output_dir}/axo_eff_v4_{dataset}_{todaysDate}.png")
    c_eff_v4.Close()

    # dimuon invariant mass plots
    mass_hist_v3 = f.Get("diMuonInvMass_axov3")
    mass_hist_v4 = f.Get("diMuonInvMass_axov4")
    for i in range(len(thresholds_names)):
        mass_hist_v3_projection = mass_hist_v3.ProjectionX(
                "mass_hist_v3_projection", 
                mass_hist_v3.GetYaxis().FindBin(thresholds_values_v3[i]), 
                mass_hist_v3.GetYaxis().GetNbins()
        )
        mass_hist_v4_projection = mass_hist_v4.ProjectionX(
                "mass_hist_v4_projection", 
                mass_hist_v4.GetYaxis().FindBin(thresholds_values_v4[i]), 
                mass_hist_v4.GetYaxis().GetNbins()
        )

        signal_integral_v3 = mass_hist_v3_projection.Integral(
                mass_hist_v3_projection.GetXaxis().FindBin(jpsi_low_edge),
                mass_hist_v3_projection.GetXaxis().FindBin(jpsi_high_edge)
        )
        signal_integral_v4 = mass_hist_v4_projection.Integral(
                mass_hist_v4_projection.GetXaxis().FindBin(jpsi_low_edge),
                mass_hist_v4_projection.GetXaxis().FindBin(jpsi_high_edge)
        )
        print(f"AXO v3: Threshold = AXO {thresholds_names[i]} (Value = {thresholds_values_v3[i]}): Signal Yield = {signal_integral_v3}")
        print(f"AXO v4: Threshold = AXO {thresholds_names[i]} (Value = {thresholds_values_v4[i]}): Signal Yield = {signal_integral_v4}")
        mass_hist_v3_projection.Rebin(4)
        mass_hist_v4_projection.Rebin(4)

        c_mass_v3 = ROOT.TCanvas("c_mass_v3", "Dimuon Invariant Mass", 1000, 600)

        mass_hist_v3_projection.SetMarkerColor(1)
        mass_hist_v3_projection.GetXaxis().SetTitle("Dimuon invariant mass [GeV]");
        mass_hist_v3_projection.GetYaxis().SetTitle("Events");
        mass_hist_v3_projection.SetStats(0)
        mass_hist_v3_projection.SetTitle(f"AXO v3 {thresholds_names[i]} Threshold = {thresholds_values_v3[i]}")
        max_val = 10*mass_hist_v3_projection.GetBinContent(mass_hist_v3_projection.GetMaximumBin())
        mass_hist_v3_projection.GetYaxis().SetRangeUser(1e-1, max_val)
        mass_hist_v3_projection.GetXaxis().SetRangeUser(0, 15)
        mass_hist_v3_projection.Draw("HIST")
        mass_hist_v3_projection.Draw("E SAME")

        c_mass_v3.SetLogy()
        c_mass_v3.Draw()
        c_mass_v3.SaveAs(f"{output_dir}/dimuon_mass_axov3_{thresholds_names[i]}_{dataset}_{todaysDate}.png")
        c_mass_v3.Close()

        c_mass_v4 = ROOT.TCanvas("c_mass_v4", "Dimuon Invariant Mass", 1000, 600)
                                                                                                                
        mass_hist_v4_projection.SetMarkerColor(1)
        mass_hist_v4_projection.GetXaxis().SetTitle("Dimuon invariant mass [GeV]");
        mass_hist_v4_projection.GetYaxis().SetTitle("Events");
        mass_hist_v4_projection.SetStats(0)
        mass_hist_v4_projection.SetTitle(f"AXO v4 {thresholds_names[i]} Threshold = {thresholds_values_v4[i]}")
        max_val = 10*mass_hist_v4_projection.GetBinContent(mass_hist_v4_projection.GetMaximumBin())
        mass_hist_v4_projection.GetYaxis().SetRangeUser(1e-1, max_val)
        mass_hist_v4_projection.GetXaxis().SetRangeUser(0, 15)
        mass_hist_v4_projection.Draw("HIST")
        mass_hist_v4_projection.Draw("E SAME")
                                                                                                                
        c_mass_v4.SetLogy()
        c_mass_v4.Draw()
        c_mass_v4.SaveAs(f"{output_dir}/dimuon_mass_axov4_{thresholds_names[i]}_{dataset}_{todaysDate}.png")
        c_mass_v4.Close()


    f.Close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This program draws AXO score and efficiency histograms for the given sample")
    parser.add_argument("-i", "--input_file", help="path to input ROOT file containing hists")
    parser.add_argument("-o", "--output_dir", default='./', help="directory to save output plots")
    parser.add_argument("-d", "--dataset", help="name of sample")

    args = parser.parse_args()

    main(args.input_file, args.output_dir, args.dataset)
