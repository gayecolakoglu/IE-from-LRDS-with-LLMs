# 🚀 Problem Solved? Information Extraction Design Space for Layout-Rich Documents using LLMs

This project explores core challenges in *information extraction* from layout-rich documents, including:
- ✅ *Input representation*
- ✅ *Chunking*
- ✅ *Prompting*
- ✅ *Selection of LLMs and multimodal models*

It benchmarks the outcomes of different design choices against *LayoutLMv3* and *GPT-4o Vision*.

📄 **[Read the Paper](https://github.com/user-attachments/assets/78d2c111-0716-4571-809c-ce9ad38524f5)**  
![Paper](https://github.com/user-attachments/assets/78d2c111-0716-4571-809c-ce9ad38524f5)

---

## ⚙️ Setup

### 1️⃣ Install the Project
Tested with *Python 3.11.6* and *Conda* on a *Linux server (Ubuntu 5.15.0-124-generic)*.

```bash
# Clone the repository
git clone git@github.com:gayecolakoglu/LayIE-LLM.git
cd LayIE-LLM

# Create and activate a Conda environment
conda create -n LayIE-LLM python=3.11
conda activate LayIE-LLM

# Install dependencies
pip install -r requirements.txt
pip install -e .
```


### 2️⃣ Dataset 📂
- The vrdu2 folder contains required files for testing *LLaMA, GPT-3.5, and GPT-4o*.
- This project specifically tests *registration-form* data (filtered as explained in Appendix A.2 of the paper).
- Full dataset available at: [VRDU Dataset](https://github.com/google-research-datasets/vrdu).

### 3️⃣ API Keys 🔑
Create a *keys.env* file in the same directory as *config.py* with the following format:

```
api_key_llama="YOUR_API_KEY"
api_key_gpt="YOUR_API_KEY"
```

---

## ▶️ How to Run

### 📌 Input Types
- *main.ipynb* → Runs all three models (LLaMA 3, GPT-3.5, GPT-4o) with *OCR input*.
- *main_md.ipynb* → Runs the same models with *Markdown input*.
- *main-gpt4-Image.ipynb* → Runs GPT-4o Vision with *Image input*.

### 📌 Selecting LLM
Modify the *Arrange working dirs* section in the main scripts to change the model as shown in the attached example
```
MODEL_gpt_3  # Other options: MODEL_llama, MODEL_gpt_4
```
![Model Selection](https://github.com/user-attachments/assets/97e13c9c-1418-4e0d-bad3-15c34abab1c7)

### 📌 Other Notebooks
| Notebook | Purpose |
|----------|---------|
| *main-gpt4-Markdown_batch.ipynb* | Converts documents to Markdown format |
| *llama-token-calc.ipynb* | Estimates token usage for LLaMA |
| *llama-postprocess.ipynb* | Tests updated post-processing methods without re-running models |
| *error_markdown_files.ipynb* | Updates files that caused errors during model interaction |
| *editing_scripts.ipynb* | Various scripts for analyzing model outputs |

### 📌 Output Folders
| Folder | Contents |
|--------|----------|
| *llama3_70b_outputs* | Output for LLaMA-3 (OCR input) |
| *gpt4_outputs* | Output for GPT-4 (OCR input) |
| *gpt3.5_outputs* | Output for GPT-3.5 (OCR input) |
| *gpt4_Markdown_Llama3_outputs* | Markdown input - LLaMA-3 |
| *gpt4_Markdown_gpt4_outputs* | Markdown input - GPT-4 |
| *gpt4_Markdown_gpt3_outputs* | Markdown input - GPT-3.5 |
| *gpt4_outputs_Image* | Image input - GPT-4o Vision |
| *gpt4_Markdown_outputs* | Markdown conversion of documents |

---

## 🏆 Conclusion
This project provides a comprehensive evaluation of *LLM-based information extraction* from *layout-rich documents, comparing different **input formats, models, and processing techniques*.

💡 *Feel free to contribute, suggest improvements, or report issues!* 🚀

## 📚 Reference
The following citation should be used for the paper associated with this project:

```
@misc{colakoglu2025problemsolvedinformationextraction,
      title={Problem Solved? Information Extraction Design Space for Layout-Rich Documents using LLMs}, 
      author={Gaye Colakoglu and Gürkan Solmaz and Jonathan Fürst},
      year={2025},
      eprint={2502.18179},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.18179}, 
}
```

