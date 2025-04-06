# 🖼️ Azure OCR Tool

A Python-based application leveraging **Azure Cognitive Services' Document Intelligence (formerly Form Recognizer) API** to intelligently extract text, tables, and other valuable data from various image formats (JPEG, PNG, etc.). This tool provides a seamless and intuitive user experience through a **Streamlit**-powered graphical interface.

## ✨ Key Features

* **Intelligent Text Extraction:** Accurately extracts textual content from images using the robust OCR capabilities of Azure Document Intelligence.
* **Multiple Output Formats:** Supports exporting extracted text in flexible formats:
    * Plain **Text** (`.txt`) for simple text retrieval.
    * **Microsoft Word** (`.docx`) for formatted document output.
    * **PDF** (`.pdf`) for portable document archiving.
* **User-Friendly Interface:** An intuitive and responsive web interface built with Streamlit, making OCR tasks accessible to everyone.
* **Structured Data Extraction:** Capable of identifying and extracting tables and other structured data elements embedded within images.

## 💰 Azure Document Intelligence Free Tier

Microsoft Azure offers a **free tier** for its Document Intelligence service, allowing you to explore and test its capabilities without immediate cost. However, it's important to be aware of the following limitations associated with the free tier (these limits are subject to change, so please refer to the official [Azure Document Intelligence pricing page](https://azure.microsoft.com/en-us/pricing/details/ai-services/document-intelligence/) for the most up-to-date information):

* **Limited Free Credits:** You typically receive a certain amount of free credits that can be used for processing documents.
* **Usage Limits:** There are usually monthly limits on the number of pages you can analyze and the number of API calls you can make.
* **Service Limitations:** Some advanced features or higher processing speeds might not be available in the free tier.

**Recommendation:** For production environments or high-volume processing, consider upgrading to a paid tier to avoid service interruptions and access the full capabilities of Azure Document Intelligence.

## ⚙️ Prerequisites

* **Python:** Version **3.8 or higher** is required.
* **Anaconda:** Recommended for streamlined environment management (or any preferred virtual environment tool).
* **Azure Cognitive Services Subscription:** An active Azure subscription with access to the Document Intelligence service is necessary to utilize the API.

### 🛠️ Python Environment Setup

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/salaimanis/azure-ocr-tool.git](https://github.com/salaimanis/azure-ocr-tool.git)
    cd azure-ocr-tool
    ```

2.  **Create the Conda Environment (Recommended):**

    If you have Anaconda installed, create a dedicated environment using the provided `environment.yml` file:

    ```bash
    conda env create -f environment.yml
    conda activate azure-ocr-tool
    ```

3.  **Install Dependencies (If Not Using Conda):**

    If you prefer not to use Conda, install the necessary Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

### ☁️ Azure Setup

1.  **Create Azure Cognitive Services Resource:** Navigate to the [Azure Portal](https://portal.azure.com/) and create a new **Cognitive Services** resource. Choose the **Document Intelligence** service option.

2.  **Retrieve API Key and Endpoint:** Once the resource is provisioned, go to its overview page in the Azure Portal. Under the "Resource Management" section, find and note down your:
    * **API Key (Key 1 or Key 2)**
    * **Endpoint**

3.  **Configure Credentials:** Create a `.streamlit` directory in the root of your project if it doesn't already exist. Inside this directory, create a file named `secrets.toml` and add your Azure credentials as follows:

    ```toml
    [azure]
    endpoint = "your_azure_endpoint"
    key = "your_azure_key"
    ```

    **Important:** Ensure the `.streamlit` directory and `secrets.toml` file are in the same directory as your `ocr_gui_app.py` script.

### 🚀 Running the Application

1.  **Open your terminal or command prompt.**

2.  **Navigate to the project directory:**

    ```bash
    cd azure-ocr-tool
    ```

3.  **Run the Streamlit application:**

    ```bash
    streamlit run ocr_gui_app.py
    ```

4.  **Access the Application:** Streamlit will automatically open the application in your default web browser. If it doesn't, manually open the URL provided in the terminal (usually `http://localhost:8501`).

5.  **Start Processing:**
    * **Upload an image** using the file uploader.
    * **Select your desired output format** (Text, Word, or PDF) from the dropdown.
    * Click the **"Extract Text"** button to initiate the OCR process.
    * The extracted results will be displayed on the screen, and you'll have the option to download the output file in your chosen format.

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
