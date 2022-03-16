# Fluorescence_maize

Assessing nitrogen variability at early stages of maize using mobile fluorescence sensing

##-----------------------------------------------------------------------------------------------------------------------------------------------------------

Copyright (C) 2022 by PrecisionAg Lab, Agronomy, KSU

##-----------------------------------------------------------------------------------------------------------------------------------------------------------

(1) Signal denoising and outlier removal
Folder: Signal_denoising_outlier
Data description: 
ardec0710_excel.xlsx contains sample fluorescenec data (Multiplex3) over several plots.
These are raw signal.

Fluo_waveletTransform_signalDenoise.py performs wavelet transform based signal denoising for each plot individually. 

Data_cleaning_IQR.py performs data ommision (based on FRF_R threshold) and outlier removal using IQR method.


(2) Combile_all_plots>>Combile_data_plots.py  Combining fluorescence based vegetation indices over all plots together into a single file.

(3) SVR regression model training and test
SVR_Regression>>SVR_Biomass_V9.py
Sample data:  Ardec2012_Regression_Data (Sheet1#trainV9 and Sheet2#testV9)
