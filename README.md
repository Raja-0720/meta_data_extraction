Contract Metadata Extraction System

Internship Assessment Submission
Candidate: Raja Kumar
Technology: Machine Learning | NLP | FastAPI

1. Problem Statement

Build an AI/ML system to extract important metadata from rental agreement documents irrespective of template format.
The system should predict:

Party One

Party Two

Agreement Value

Agreement Start Date

Agreement End Date

Renewal Notice Period

2. Solution Overview

A lightweight NLP-based machine learning system was designed that learns patterns from contract corpus and predicts structured legal metadata.
The system is template-agnostic and deployed as a REST API using FastAPI.

3. Why CSV-Only Approach?

Due to system compatibility and time constraints, OCR and scanned document processing layers were modularized.
This implementation focuses on building and validating the core document intelligence layer using structured CSV corpus.

This follows the industry MVP development approach, where intelligence models are built first and OCR is integrated later as a plug-in layer.# meta_data_extraction

4. Architecture
Contract CSV Dataset

        ↓
Text Corpus Builder

        ↓
TF-IDF Vectorizer

        ↓
Multi-Output ML Classifier

        ↓
FastAPI REST API

        ↓
JSON Metadata Output


<img width="758" height="368" alt="image" src="https://github.com/user-attachments/assets/ce5f4089-7cd1-4c85-a88a-bf845e88de75" />


7. Evaluation Strategy

Metric used: Per-field Recall

The model was evaluated on unseen test contracts and showed correct extraction of:

Names

Dates

Amount values

Renewal notice periods

7. API Usage
Run Server
uvicorn app.app:app --reload

API Endpoint
POST /extract

Example Input
Balaji.R Kartheek R 3800 01.05.2010 31.04.2011 30

Example Output
{
  "party_one": "Balaji.R",
  "party_two": "Kartheek R",
  "agreement_value": "3800",
  "start_date": "01.05.2010",
  "end_date": "31.04.2011",
  "renewal_notice_days": "30"
}

8. Limitations

OCR layer not included in current version

Limited dataset size

Supports English rental agreements only

9. Future Enhancements

OCR & image document support

Transformer-based deep learning

Multilingual contract support

Layout-aware extraction

10. Conclusion

This project demonstrates a scalable approach to building AI-powered legal document intelligence systems and deploying them as production-ready APIs.
