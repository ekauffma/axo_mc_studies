import ROOT
import argparse
import datetime
import json
import numpy as np

todaysDate = datetime.date.today().strftime('%Y%m%d')

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
    
    line1 = ROOT.TLine(threshold_vtight_v3, 0, threshold_vtight_v3, max_val)
    line1.SetLineColor(ROOT.TColor.GetColor("#5790fc"))
    line1.SetLineStyle(2)
    line1.SetLineWidth(2)
    line1.Draw("same")
    line2 = ROOT.TLine(threshold_tight_v3, 0, threshold_tight_v3, max_val)
    line2.SetLineColor(ROOT.TColor.GetColor("#f89c20"))
    line2.SetLineStyle(2)
    line2.SetLineWidth(2)
    line2.Draw("same")
    line3 = ROOT.TLine(threshold_nominal_v3, 0, threshold_nominal_v3, max_val)
    line3.SetLineColor(ROOT.TColor.GetColor("#e42536"))
    line3.SetLineStyle(2)
    line3.SetLineWidth(2)
    line3.Draw("same")
    line4 = ROOT.TLine(threshold_loose_v3, 0, threshold_loose_v3, max_val)
    line4.SetLineColor(ROOT.TColor.GetColor("#964a8b"))
    line4.SetLineStyle(2)
    line4.SetLineWidth(2)
    line4.Draw("same")
    line5 = ROOT.TLine(threshold_vloose_v3, 0, threshold_vloose_v3, max_val)
    line5.SetLineColor(ROOT.TColor.GetColor("#9c9ca1"))
    line5.SetLineStyle(2)
    line5.SetLineWidth(2)
    line5.Draw("same")

    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(score_hist_v3, f"{dataset} Score", "l")
    legend.AddEntry(line1, "AXO VTight Threshold", "l")
    legend.AddEntry(line2, "AXO Tight Threshold", "l")
    legend.AddEntry(line3, "AXO Nominal Threshold", "l")
    legend.AddEntry(line4, "AXO Loose Threshold", "l")
    legend.AddEntry(line5, "AXO VLoose Threshold", "l")
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
    
    line1 = ROOT.TLine(threshold_vtight_v4, 0, threshold_vtight_v4, max_val)
    line1.SetLineColor(ROOT.TColor.GetColor("#5790fc"))
    line1.SetLineStyle(2)
    line1.SetLineWidth(2)
    line1.Draw("same")
    line2 = ROOT.TLine(threshold_tight_v4, 0, threshold_tight_v4, max_val)
    line2.SetLineColor(ROOT.TColor.GetColor("#f89c20"))
    line2.SetLineStyle(2)
    line2.SetLineWidth(2)
    line2.Draw("same")
    line3 = ROOT.TLine(threshold_nominal_v4, 0, threshold_nominal_v4, max_val)
    line3.SetLineColor(ROOT.TColor.GetColor("#e42536"))
    line3.SetLineStyle(2)
    line3.SetLineWidth(2)
    line3.Draw("same")
    line4 = ROOT.TLine(threshold_loose_v4, 0, threshold_loose_v4, max_val)
    line4.SetLineColor(ROOT.TColor.GetColor("#964a8b"))
    line4.SetLineStyle(2)
    line4.SetLineWidth(2)
    line4.Draw("same")
    line5 = ROOT.TLine(threshold_vloose_v4, 0, threshold_vloose_v4, max_val)
    line5.SetLineColor(ROOT.TColor.GetColor("#9c9ca1"))
    line5.SetLineStyle(2)
    line5.SetLineWidth(2)
    line5.Draw("same")
                                                                               
    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(score_hist_v4, f"{dataset} Score", "l")
    legend.AddEntry(line1, "AXO VTight Threshold", "l")
    legend.AddEntry(line2, "AXO Tight Threshold", "l")
    legend.AddEntry(line3, "AXO Nominal Threshold", "l")
    legend.AddEntry(line4, "AXO Loose Threshold", "l")
    legend.AddEntry(line5, "AXO VLoose Threshold", "l")
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

    line1 = ROOT.TLine(threshold_vtight_v3, 0, threshold_vtight_v3, 1.5)
    line1.SetLineColor(ROOT.TColor.GetColor("#5790fc"))
    line1.SetLineStyle(2)
    line1.SetLineWidth(2)
    line1.Draw("same")
    line2 = ROOT.TLine(threshold_tight_v3, 0, threshold_tight_v3, 1.5)
    line2.SetLineColor(ROOT.TColor.GetColor("#f89c20"))
    line2.SetLineStyle(2)
    line2.SetLineWidth(2)
    line2.Draw("same")
    line3 = ROOT.TLine(threshold_nominal_v3, 0, threshold_nominal_v3, 1.5)
    line3.SetLineColor(ROOT.TColor.GetColor("#e42536"))
    line3.SetLineStyle(2)
    line3.SetLineWidth(2)
    line3.Draw("same")
    line4 = ROOT.TLine(threshold_loose_v3, 0, threshold_loose_v3, 1.5)
    line4.SetLineColor(ROOT.TColor.GetColor("#964a8b"))
    line4.SetLineStyle(2)
    line4.SetLineWidth(2)
    line4.Draw("same")
    line5 = ROOT.TLine(threshold_vloose_v3, 0, threshold_vloose_v3, 1.5)
    line5.SetLineColor(ROOT.TColor.GetColor("#9c9ca1"))
    line5.SetLineStyle(2)
    line5.SetLineWidth(2)
    line5.Draw("same")

    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(eff_hist_v3, f"{dataset} Efficiency", "l")
    legend.AddEntry(line1, "AXO VTight Threshold", "l")
    legend.AddEntry(line2, "AXO Tight Threshold", "l")
    legend.AddEntry(line3, "AXO Nominal Threshold", "l")
    legend.AddEntry(line4, "AXO Loose Threshold", "l")
    legend.AddEntry(line5, "AXO VLoose Threshold", "l")
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
                                                                             
    line1 = ROOT.TLine(threshold_vtight_v4, 0, threshold_vtight_v4, 1.5)
    line1.SetLineColor(ROOT.TColor.GetColor("#5790fc"))
    line1.SetLineStyle(2)
    line1.SetLineWidth(2)
    line1.Draw("same")
    line2 = ROOT.TLine(threshold_tight_v4, 0, threshold_tight_v4, 1.5)
    line2.SetLineColor(ROOT.TColor.GetColor("#f89c20"))
    line2.SetLineStyle(2)
    line2.SetLineWidth(2)
    line2.Draw("same")
    line3 = ROOT.TLine(threshold_nominal_v4, 0, threshold_nominal_v4, 1.5)
    line3.SetLineColor(ROOT.TColor.GetColor("#e42536"))
    line3.SetLineStyle(2)
    line3.SetLineWidth(2)
    line3.Draw("same")
    line4 = ROOT.TLine(threshold_loose_v4, 0, threshold_loose_v4, 1.5)
    line4.SetLineColor(ROOT.TColor.GetColor("#964a8b"))
    line4.SetLineStyle(2)
    line4.SetLineWidth(2)
    line4.Draw("same")
    line5 = ROOT.TLine(threshold_vloose_v4, 0, threshold_vloose_v4, 1.5)
    line5.SetLineColor(ROOT.TColor.GetColor("#9c9ca1"))
    line5.SetLineStyle(2)
    line5.SetLineWidth(2)
    line5.Draw("same")
                                                                             
    # create and draw legend
    legend = ROOT.TLegend(0.55, 0.6, 0.9, 0.9)
    legend.AddEntry(eff_hist_v4, f"{dataset} Efficiency", "l")
    legend.AddEntry(line1, "AXO VTight Threshold", "l")
    legend.AddEntry(line2, "AXO Tight Threshold", "l")
    legend.AddEntry(line3, "AXO Nominal Threshold", "l")
    legend.AddEntry(line4, "AXO Loose Threshold", "l")
    legend.AddEntry(line5, "AXO VLoose Threshold", "l")
    legend.SetTextSize(0.04)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
                                                                             
    c_eff_v4.SetLogy()
    c_eff_v4.Draw()
    c_eff_v4.SaveAs(f"{output_dir}/axo_eff_v4_{dataset}_{todaysDate}.png")
    c_eff_v4.Close()

    f.Close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This program draws AXO score and efficiency histograms for the given sample")
    parser.add_argument("-i", "--input_file", help="path to input ROOT file containing hists")
    parser.add_argument("-o", "--output_dir", default='./', help="directory to save output plots")
    parser.add_argument("-d", "--dataset", help="name of sample")

    args = parser.parse_args()

    main(args.input_file, args.output_dir, args.dataset)
