if uploaded_file and st.button("Extract Text"):
    image = Image.open(uploaded_file)
    image = image.convert('RGB')  # Ensures image is in a consistent format
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert the image to bytes (JPEG format)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="JPEG")  # Use "JPEG" or "PNG"
    image_bytes.seek(0)  # Reset the pointer to the beginning of the byte stream

    with st.spinner("Extracting text using Azure Document Intelligence..."):
        try:
            # Use the Document Analysis client to process the image
            poller = client.begin_analyze_document("prebuilt-read", document=image_bytes)
            result = poller.result()

            extracted_text = ""
            tables = []

            for page in result.pages:
                # Extract text
                for line in page.lines:
                    extracted_text += line.content + "\n"

                # Extract tables
                if len(result.tables) > 0:
                    st.write(f"Tables detected in page {page.page_number}")
                    for table in result.tables:
                        table_content = []
                        for row in table.rows:
                            row_content = [cell.content for cell in row.cells]
                            table_content.append(row_content)
                        tables.append(table_content)

            # Display extracted tables for debugging
            if tables:
                st.subheader("Extracted Tables")
                for idx, table in enumerate(tables):
                    st.write(f"Table {idx + 1}:")
                    for row in table:
                        st.write(row)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            extracted_text = ""
            tables = []

    if extracted_text:
        st.subheader("Extracted Text")
        st.text_area("Extracted Text", extracted_text, height=300, label_visibility="collapsed")


        # Saving the output in different formats based on user selection
        if output_format == "Text":
            with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
                f.write(extracted_text)
            with open(f"{file_name}.txt", "rb") as f:
                st.download_button("Download Text", f, file_name=f"{file_name}.txt")

        elif output_format == "Word":
            doc = Document()
            doc.add_paragraph(extracted_text)
            
            # Add tables to Word document
            if tables:
                for table in tables:
                    word_table = doc.add_table(rows=len(table), cols=len(table[0]))
                    for row_idx, row in enumerate(table):
                        for col_idx, cell in enumerate(row):
                            word_table.cell(row_idx, col_idx).text = cell
            doc.save(f"{file_name}.docx")
            with open(f"{file_name}.docx", "rb") as f:
                st.download_button("Download Word", f, file_name=f"{file_name}.docx")

        elif output_format == "PDF":
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in extracted_text.split("\n"):
                pdf.multi_cell(0, 10, txt=line)

            # Add tables to PDF
            if tables:
                pdf.ln(10)  # Add some space between text and tables
                for table in tables:
                    for row in table:
                        pdf.cell(40, 10, txt="\t".join(row), ln=True)
                    pdf.ln(5)  # Add space between rows

            pdf.output(f"{file_name}.pdf")
            with open(f"{file_name}.pdf", "rb") as f:
                st.download_button("Download PDF", f, file_name=f"{file_name}.pdf")

        st.success("✅ Done!")
    else:
        st.warning("⚠️ No text extracted from the image.")
