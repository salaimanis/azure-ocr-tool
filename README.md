# 🖼️ Azure OCR Tool

A Python app using **Azure Document Intelligence API** to extract text and tables from image files (JPEG, PNG, etc.). It features a simple **Streamlit** GUI for a smooth user experience.

---

## ✨ Features

- **Text & Table Extraction:** Uses Azure OCR for accurate text and table recognition.
- **Multiple Output Formats:**
  - **Text** (.txt)
  - **Word** (.docx)
  - **PDF** (.pdf)
  - **Excel** (.xlsx)
  - **Table and Multiple Language Support**
  - **High Accuracy:** Leverages sophisticated AI for reliable text and table extraction.
- **Streamlit UI:** Clean and interactive interface.
- **Structured Data Support:** Detects tables from documents.

---

## 💰 Azure Free Tier

Azure provides limited free usage of Document Intelligence. This includes:
- Free API calls/month.
- Limits on pages processed.
- Some advanced features may be locked.

[Check Azure pricing →](https://azure.microsoft.com/en-us/pricing/details/ai-services/document-intelligence/)

---

## ⚙️ Prerequisites

- Python 3.8+
- [Anaconda](https://www.anaconda.com/) (recommended)
- Azure Subscription with Document Intelligence enabled (Free Tier Available) 

---

## 🛠️ Setup

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/azure-ocr-tool.git
cd azure-ocr-tool
```

### 2. Create and Activate Conda Environment (Recommended)  
```bash
conda env create -f environment.yml
conda activate azure-ocr-tool
```

## ☁️ Azure Setup

### 1. Create Azure Cognitive Services Resource  
- Go to the Azure Portal: https://portal.azure.com/  
- Create a new **Cognitive Services** resource  
- Choose **Document Intelligence (Form Recognizer)** as the service  

### 2. Retrieve API Key and Endpoint  
- After creation, go to **Keys and Endpoint** section  
- Note down:  
  - **API Key** (Key 1 or 2)  
  - **Endpoint URL**

### 3. Configure Credentials  
- Create a `.streamlit` folder in the root of your project  
- Inside it, create a file named `secrets.toml` and add your credentials:

```toml
[azure]
AZURE_ENDPOINT = "your_azure_endpoint"
AZURE_KEY = "your_azure_key"
```

> ⚠️ Make sure `.streamlit/secrets.toml` is in the same directory as your `ocr_gui_app.py`

## 🚀 Running the Application

### 1. Launch the App  
```bash
streamlit run ocr_gui_app.py
```

### 2. Open the App  
- The browser should open automatically  
- If not, open: http://localhost:8501

## 🖼️ How to Use

1. Upload an image file (JPG, JPEG, or PNG)
2. Select the output format: Text, Word, PDF, or Excel
3. Choose OCR model: 
   - `prebuilt-document` → Structured (tables, forms)
   - `prebuilt-read` → Simple text or handwriting
4. Click **Extract Text**
5. View the results and download the output file

## ✅ To Do

* **Enhance Table Recognition:** Improve the accuracy and formatting of extracted tables to better represent the original structure. This could involve:
    * Identifying complex table layouts with merged cells or varying row/column spans.
    * Providing options for outputting tables in structured formats like CSV or Markdown.
    * Allowing users to define table regions manually for more precise extraction.
* **Refine Text Formatting:** Implement features to better preserve the original formatting of the extracted text, such as:
    * Recognizing and maintaining paragraph breaks.
    * Identifying and applying basic text styles (bold, italics, underlines).
    * Handling text orientation and multi-column layouts more effectively.

## ⚠️ Limitations

* **Azure Free Tier Constraints:** As mentioned earlier, the Azure free tier for Document Intelligence has usage limits.
* **Complexity of Images:** The accuracy of text and table extraction can be affected by the quality, resolution, and complexity of the input images. Images with significant noise, skew, or poor lighting may yield less accurate results.

## 🤝 Contributing

We welcome contributions! If you have ideas for improvements, especially regarding table and text formatting enhancements, or find any issues, please feel free to:

1.  **Fork** the repository on GitHub.
2.  **Create a new branch** with your changes.
3.  **Submit a pull request** with a clear description of your modifications.

## 📄 License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for complete details.
