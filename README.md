# Network Intrusion Detection System (IDS) using Machine Learning

This project implements a Machine Learning based Intrusion Detection System (IDS) using a Random Forest classifier to detect malicious network traffic from the CICIDS2017 dataset.

---

## Overview

The system processes network traffic data, performs feature selection, trains a machine learning model, and predicts whether traffic is **Normal** or an **Attack**.

Main steps:

* Data preprocessing and cleaning
* Feature selection using correlation analysis
* Random Forest model training
* Model evaluation and prediction

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook

---

## Dataset

Dataset used: **CICIDS2017**

Processed dataset used for training:

```
work_reduced.csv
```

Target variable:

```
Binary_Label
```

* **0 → Normal Traffic**
* **1 → Attack Traffic**

---

## Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/FariyaRafat/network-intrusion-detection-ml.git
cd network-intrusion-detection-ml
```

### Install Dependencies

```bash
pip install -r requirements.txt
```
## Train the Model

To train the model and generate the trained Random Forest model file:

1. Open the Jupyter notebook:

```bash
jupyter notebook
```

2. Open the notebook file:

```
network_intrusion_detection.ipynb
```

3. Run all the cells in the notebook.

After training, the notebook will generate the trained model file:

```
rf_model.pkl
```

This file will then be used by the prediction script

### Run Prediction

```bash
python predict.py
```

Example input:

```
4 2 12 6 6 6 0 0 3000000 500000 2 0 2 2 0 0 0 0 0 0 40 0 0 6 0 0 0 1 0 0 255 0 1 20 0 0 0 0
```

Output:

```
Normal Traffic
```

or

```
Attack Detected
```

---

## Model

**Random Forest Classifier**

Configuration:

* `n_estimators = 100`
* `random_state = 42`

---

## Model Performance

| Metric | Score |
|--------|--------|
| Accuracy | **99.90%** |

Evaluation metrics used:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Confusion Matrix:

![Confusion Matrix](confusion_matrix.png)

---

## Project Structure

```
network-intrusion-detection-ml
│
├── network_intrusion_detection.ipynb
├── predict.py
├── confusion_matrix.png
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```
---

## License

This project is licensed under the **Apache License 2.0**.

See the [LICENSE](LICENSE) file for more details.

---

## Author

**Fariya Rafat**
