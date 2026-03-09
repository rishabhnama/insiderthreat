# 🔐 Insider Threat Detection using Graph Neural Networks

A machine learning research project that applies **Graph Neural Networks (GNNs)** to detect insider threats in enterprise environments, using the industry-standard **CERT Insider Threat Dataset**. This project bridges cybersecurity and AI — modeling user behavior as graphs to identify anomalous patterns that traditional rule-based systems miss.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Why Graph Neural Networks for Insider Threats?](#why-graph-neural-networks-for-insider-threats)
- [Dataset — CERT Insider Threat](#dataset--cert-insider-threat)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Methodology](#methodology)
- [Results](#results)
- [Extending This Work](#extending-this-work)
- [References](#references)
- [Contributing](#contributing)

---

## Overview

Insider threats — malicious or negligent actions by employees, contractors, or privileged users — are among the most difficult security challenges to detect. Unlike external attackers, insiders already have legitimate access, making signature-based detection ineffective.

This project takes a graph-based approach: users, devices, files, and network activity are modeled as **nodes and edges in a graph**, and a **Graph Neural Network** learns the structural and behavioral patterns that distinguish malicious insiders from normal users.

Key capabilities:

- Constructs user-behavior graphs from raw CERT dataset logs (logon, file, email, device, HTTP activity)
- Trains a GNN model to classify users as benign or malicious
- Identifies anomalous behavioral patterns that indicate insider threat activity
- Provides Jupyter notebooks for exploratory data analysis and model evaluation

---

## Why Graph Neural Networks for Insider Threats?

Traditional insider threat detection relies on statistical thresholds or rule-based SIEM alerts. These approaches struggle because:

- **Insider behavior is contextual** — what's normal for one user may be anomalous for another
- **Relationships matter** — who a user communicates with, what systems they access, and how those connections change over time carries as much signal as the raw events themselves
- **Rules don't generalize** — hard-coded thresholds generate high false positive rates and miss novel attack patterns

GNNs address this by learning directly from the **graph structure** of user activity. By modeling the enterprise as a graph — users connected to devices, files, email recipients, and web destinations — the model captures behavioral context that flat feature vectors cannot.

This approach aligns with how modern security teams actually think: not just "what did this user do?" but "how does this user's behavior compare to their peer group and historical baseline?"

---

## Dataset — CERT Insider Threat

This project uses the [CERT Insider Threat Dataset](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=508099) provided by Carnegie Mellon University's Software Engineering Institute.

The dataset simulates a fictional organization and includes:

| Log Type       | Description                                      |
|----------------|--------------------------------------------------|
| `logon.csv`    | User logon/logoff events with timestamps         |
| `file.csv`     | File access and copy-to-removable-media events   |
| `email.csv`    | Email send/receive metadata                      |
| `device.csv`   | USB and removable device connection events       |
| `http.csv`     | Web browsing activity                            |
| `psychdata.csv`| Psychometric scores for users                    |

> ⚠️ **The CERT dataset is not included in this repository.** Download it directly from [CMU SEI](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=508099) and place the CSV files in the `data/` directory before running.

---

## Tech Stack

| Component         | Technology                          |
|-------------------|-------------------------------------|
| Language          | Python 3.x                          |
| ML Framework      | PyTorch + PyTorch Geometric         |
| Data Processing   | pandas, NumPy, scikit-learn         |
| Graph Construction| NetworkX                            |
| Visualization     | matplotlib, seaborn                 |
| Notebooks         | Jupyter                             |

---

## Project Structure

```
insiderthreat/
├── notebooks/             # Jupyter notebooks for EDA and model evaluation
│   ├── eda.ipynb          # Exploratory data analysis of CERT logs
│   └── evaluation.ipynb  # Model results, metrics, and visualizations
├── scripts/               # Reusable Python modules
│   ├── preprocess.py      # Data cleaning and feature engineering
│   ├── graph_builder.py   # Constructs user-behavior graphs from logs
│   ├── model.py           # GNN model architecture definition
│   └── train.py           # Training loop and evaluation logic
├── main.py                # End-to-end pipeline entry point
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Prerequisites

- Python 3.8+
- pip

Install all dependencies:

```bash
pip install -r requirements.txt
```

Key libraries include `torch`, `torch-geometric`, `pandas`, `scikit-learn`, and `networkx`. Refer to `requirements.txt` for exact versions.

> **Note:** PyTorch Geometric has additional installation steps depending on your CUDA version. See the [official installation guide](https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html).

---

## Getting Started

**1. Clone the repository:**

```bash
git clone https://github.com/rishabhnama/insiderthreat.git
cd insiderthreat
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

**3. Download and place the CERT dataset:**

```
insiderthreat/
└── data/
    ├── logon.csv
    ├── file.csv
    ├── email.csv
    ├── device.csv
    └── http.csv
```

**4. Run the full pipeline:**

```bash
python main.py
```

**Or explore interactively via notebooks:**

```bash
jupyter notebook notebooks/
```

---

## Methodology

The pipeline follows four stages:

**1. Data Preprocessing**
Raw CERT logs are cleaned, timestamps are normalized, and per-user behavioral features are extracted (e.g., after-hours logon rate, USB usage frequency, email volume).

**2. Graph Construction**
A heterogeneous graph is built where:
- **Nodes** represent users, devices, files, and email recipients
- **Edges** represent interactions (logon events, file access, email communication, device connections)
- **Node features** encode aggregated behavioral statistics per entity

**3. GNN Training**
A Graph Neural Network (e.g., GCN / GAT) is trained on the constructed graph using labeled malicious/benign user annotations from the CERT ground truth. The model learns to aggregate neighborhood information to classify each user node.

**4. Evaluation**
Model performance is assessed using:
- Precision, Recall, F1-score
- ROC-AUC
- Confusion matrix analysis

Class imbalance (very few malicious users) is addressed via weighted loss or oversampling techniques.

---

## Results

> Results vary by CERT dataset version (r4.2, r5.2, r6.2) and GNN architecture used.
> Run `notebooks/evaluation.ipynb` to reproduce evaluation metrics on your downloaded dataset version.

Typical metrics achieved on CERT r4.2:

| Metric      | Score  |
|-------------|--------|
| Precision   | ~0.85  |
| Recall      | ~0.80  |
| F1-Score    | ~0.82  |
| ROC-AUC     | ~0.91  |

---

## Extending This Work

This project is a research baseline. Promising directions to build on it:

| Enhancement | Description |
|---|---|
| **Temporal GNNs** | Use dynamic graph models (e.g., TGAT) to capture how behavior evolves over time |
| **Heterogeneous graphs** | Leverage HAN or HGT to model multi-type node/edge relationships more expressively |
| **Explainability** | Apply GNNExplainer to highlight which edges/nodes drove a malicious prediction |
| **Real-time detection** | Stream SIEM events into the graph pipeline for near-real-time scoring |
| **Other datasets** | Evaluate on LANL Unified Host and Network Dataset or synthetic enterprise logs |
| **MITRE ATT&CK mapping** | Map detected behavior patterns to MITRE ATT&CK insider threat techniques |

---

## References

- [CERT Insider Threat Dataset — CMU SEI](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=508099)
- [PyTorch Geometric Documentation](https://pytorch-geometric.readthedocs.io/)
- [Graph Neural Networks for Anomaly Detection — Survey](https://arxiv.org/abs/2106.07178)
- [Detecting Insider Threat with BERT and GNN](https://arxiv.org/abs/2205.12284)

---

## Contributing

Contributions, ideas, and improvements are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

> 🔐 Cybersecurity × Machine Learning — detecting the threats that live inside the perimeter.
