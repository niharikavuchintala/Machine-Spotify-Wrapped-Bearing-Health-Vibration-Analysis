# Machine Spotify Wrapped: Bearing Health & Vibration Analysis

## Link to see the direct working in Google Colab
https://colab.research.google.com/drive/1A2o2mPvvk2zwJzQZyTe-5dNoZadQoUcn?usp=sharing

## Aim of the Project
The primary aim of this project is to successfully detect mechanical faults in industrial machinery by analyzing raw vibration data. By calculating statistical "Red Flag" metrics (RMS, Kurtosis, Peak-to-Peak) and applying Fast Fourier Transform (FFT) analysis, this project aims to prove how clearly we can distinguish a perfectly healthy machine from one with a broken bearing. Finally, it presents these complex engineering results in a fun, accessible "Spotify Wrapped" format.

## Project Overview
Using the famous **CWRU (Case Western Reserve University) Bearing Dataset**, we compare the vibration signals of two machines:
1. A perfectly healthy bearing (97_Normal_0.mat)
2. A broken bearing with an outer race fault (OR007_6_1_136.mat)

To make the engineering analysis fun and easy to read, the final output is generated as a **"Spotify Wrapped"** summary card, translating complex mathematical health metrics into creative, music-themed verdicts.

## Tools & Libraries Used
This project uses standard Python data science libraries:
* **scipy.io:** Used to open and read the special .mat data files.
* **scipy.stats:** Used as our calculator to compute complex statistics like Kurtosis.
* **numpy:** Used to process the data and calculate the Fast Fourier Transform (FFT).
* **matplotlib.pyplot:** Used to draw and plot the raw waves and equalizer graphs.

## What This Code Computes
The code extracts exactly **4096** vibration readings from each machine and calculates four critical flags:
1. **Kurtosis (The Spikiness Score):** Detects sudden, sharp impacts caused by the bearing rolling over a crack. 
2. **RMS (Root Mean Square):** Measures the overall energy, or "loudness," of the machine's vibration.
3. **Peak-to-Peak:** Measures the maximum swing from the highest vibration to the lowest vibration.
4. **FFT (Fast Fourier Transform):** Acts like an audio equalizer. It converts the messy raw vibration wave into individual frequencies (pitches) so we can see the specific rhythmic "thud" caused by the broken part.

## Prerequisites 
To run this project on your local machine, you will need:
* **Python 3.x** installed on your computer.
* **Visual Studio Code (VS Code)** or another code editor.
* The two data files (97_Normal_0.mat and OR007_6_1_136.mat), which are included in this repository.

## How to Run This Code in VS Code

Follow these exact steps to run the analysis on your own computer:

**1. Create your Project Folder**
Create a new folder on your computer.

**2. Put Everything in the Same Folder**
Make sure your Python script code.py and the two .mat data files are placed directly inside this folder. 
**If they are in different folders, the code will crash and say "File Not Found"!**

**3. Open the Folder in VS Code**
Open VS Code, click on **File** in the top left corner, select **Open Folder**, and choose the folder you just created.

**4. Open the VS Code Terminal**
At the very top of the VS Code window, click on **Terminal** and click on **New Terminal**. A command prompt will open at the bottom of your screen.

**5. Install the Required Math Tools**
In that new terminal, type the following command and press Enter to install the tools Python needs:
python -m pip install scipy numpy matplotlib

**6. Run the Code**
 Type the following command and press Enter for the execution of the code:
 python code.py
