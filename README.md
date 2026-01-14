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
