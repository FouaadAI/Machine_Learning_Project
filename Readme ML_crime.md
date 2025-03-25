Crime Analysis and Risk Detection

🚀 A Python-based crime analysis tool using KDE (Kernel Density Estimation) to identify high-risk areas.

📖 Overview

This project analyzes crime data using pandas, numpy, and sklearn to generate a crime density map. It allows users to:

✅ Detect high-risk areas based on density estimation.

✅ Input new observations manually or via file to check risk levels.

✅ Generate a heatmap of crime hotspots using matplotlib.


---

⚙ Installation

🔹 1. Install Required Libraries

Before running the program, install all required dependencies:

pip install pandas numpy matplotlib scikit-learn

🔹 2. Running the Script Directly (Python Users)

If you want to run the script without creating an executable, use:

python crime_analysis.py

🔹 3. Creating an Executable (.exe)

To convert the script into a standalone Windows executable:

pyinstaller --onefile crime_analysis.py

The .exe file will be found in the dist folder.

Move crim_analyzed.csv into the dist folder before running.

Run the executable:

cd dist
crime_analysis.exe



---

📂 File Structure

Crime_Analysis_Project/
│── crime_analysis.py       # Main Python script  
│── crim_analyzed.csv       # Crime data file (Must be in the same directory)  
│── README.md               # Documentation  
│── dist/                   # Contains crime_analysis.exe after PyInstaller  
│── build/                  # Temporary PyInstaller files  
└── _pycache_/            # Compiled Python cache


---

📊 Features

✔ Optimizes bandwidth for KDE crime analysis
✔ Predicts risk levels for new locations
✔ User-friendly input methods (manual or file-based)
✔ Generates a crime heatmap using matplotlib


---

🛠 Troubleshooting

❌ FileNotFoundError: ‘crim_analyzed.csv’

✔ Solution: Move crim_analyzed.csv into the dist folder.

❌ ModuleNotFoundError (Missing Libraries)

✔ Solution: Install missing libraries using:

pip install pandas numpy matplotlib scikit-learn


---

📢 Contributing

Feel free to improve this project! Fork the repository and submit a pull request.

📧 Contact: alkamsha.berlin@gmail.com
"""
