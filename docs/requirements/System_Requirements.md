# UAM-6: System Requirements Specification

**Project:** Development of an Intelligent Software System for Agricultural Monitoring Using Multispectral UAV Imagery

**Document Status:** Preliminary Requirements Specification

## 1. Introduction

The proposed project aims to develop a web-based intelligent software system for agricultural monitoring using multispectral UAV imagery.

The system will allow users to upload supported multispectral images, calculate vegetation indices, analyze agricultural data using a trained machine learning model, and visualize the results.

The project will focus on one selected crop. The specific crop and dataset will be finalized after evaluating the availability and suitability of existing agricultural datasets.

This document defines the preliminary functional and non-functional requirements, their priorities, and acceptance criteria.

## 2. Project Scope

### In Scope

The planned system will include:

- User registration and authentication.
- Upload and validation of supported multispectral imagery.
- Processing of spectral bands.
- Calculation of selected vegetation indices, including NDVI.
- Training and integration of a custom machine learning model.
- Comparison of the custom model with selected baseline approaches.
- Visualization of vegetation indices and model predictions.
- Storage of analysis records.
- Export of selected analysis results.

### Out of Scope

The following features are not planned for the initial version:

- Real-time UAV flight control.
- Direct drone hardware integration.
- Collection of a new UAV dataset.
- Automatic agricultural treatment or irrigation.
- Detection of every possible crop disease.
- Support for all UAV cameras and image formats.

## 3. Requirement Priorities

The MoSCoW method is used to classify requirements.

| Priority | Meaning |
|---|---|
| Must Have | Essential for the planned minimum viable system |
| Should Have | Important, but may be simplified if necessary |
| Could Have | Optional enhancement |
| Won't Have | Excluded from the initial project scope |

## 4. Functional Requirements

### FR-01: User Registration

**Priority:** Must Have

The system shall allow a new user to create an account using the required registration information.

**Acceptance Criteria:**
- A user can submit valid registration information.
- Invalid or incomplete registration data is rejected.
- Duplicate account identifiers are handled appropriately.

### FR-02: User Authentication

**Priority:** Must Have

The system shall allow registered users to log in and log out securely.

**Acceptance Criteria:**
- A registered user can log in with valid credentials.
- Invalid credentials are rejected.
- Protected analysis pages cannot be accessed without authentication.

### FR-03: Multispectral Image Upload

**Priority:** Must Have

The system shall allow authenticated users to upload multispectral image files in the supported format.

The initial supported formats will be finalized after dataset inspection, with GeoTIFF considered a preferred option where applicable.

**Acceptance Criteria:**
- A valid supported file can be uploaded.
- Unsupported or corrupted files are rejected with an understandable error message.
- The system can identify the spectral bands required for the selected processing workflow.

### FR-04: Image Preprocessing

**Priority:** Must Have

The system shall preprocess uploaded imagery as required by the selected dataset and model.

Processing may include band extraction, normalization, and preparation of model input.

**Acceptance Criteria:**
- Required spectral bands are extracted correctly.
- Preprocessing produces data in the format expected by the model.
- Invalid band configurations are detected.

### FR-05: Vegetation Index Calculation

**Priority:** Must Have

The system shall calculate NDVI using appropriate red and near-infrared spectral bands.

Additional indices may be supported depending on the dataset.

**Acceptance Criteria:**
- NDVI is calculated using the correct spectral bands.
- The calculation handles invalid input values appropriately.
- The resulting vegetation-index map can be visualized.

### FR-06: Machine Learning Analysis

**Priority:** Must Have

The project shall include a custom-trained machine learning model for the selected agricultural analysis task.

The task and model architecture will depend on the available crop dataset and labels.

**Acceptance Criteria:**
- A custom model is trained using a documented training procedure.
- The trained model can process prepared input data.
- The system produces predictions relevant to the selected analysis task.
- Model configuration and evaluation results are documented.

### FR-07: Model Comparison

**Priority:** Must Have

The custom model shall be compared with selected baseline or existing machine learning approaches.

**Acceptance Criteria:**
- At least two comparison approaches are identified.
- The approaches are evaluated on an appropriate common test dataset.
- Relevant evaluation metrics are reported.
- The results are presented in a comparison table.

### FR-08: Result Visualization

**Priority:** Must Have

The system shall visualize vegetation indices and machine learning results.

**Acceptance Criteria:**
- Users can view a vegetation-index map.
- Users can view the output of the trained model.
- The interface provides sufficient labels or legends to interpret the displayed results.

### FR-09: Analysis History

**Priority:** Should Have

The system should allow authenticated users to view their previous analysis records.

**Acceptance Criteria:**
- Completed analyses are recorded.
- Users can access their own analysis history.
- Each record contains relevant metadata, such as date and analysis type.

### FR-10: Result Export

**Priority:** Should Have

The system should allow users to export selected analytical results in a supported format.

**Acceptance Criteria:**
- Users can export at least one supported result format.
- Exported results correspond to the completed analysis.

### FR-11: Label-Based Anomaly Evaluation

**Priority:** Should Have — Conditional on Dataset Availability

If the selected dataset contains suitable labels, the system should evaluate anomaly detection or classification predictions against those labels.

**Acceptance Criteria:**
- Available labels are documented and their meaning is explained.
- Predictions are compared against the appropriate reference labels.
- Suitable metrics, such as precision, recall, F1-score, or IoU, are calculated according to the selected task.

If suitable labels are unavailable, the project must document this limitation and define an alternative evaluation strategy with the supervisor.

### FR-12: Interactive Geospatial Map

**Priority:** Could Have

The system may provide an interactive geographic map for viewing spatially referenced agricultural results.

**Acceptance Criteria:**
- Georeferenced outputs can be displayed at the correct geographic location.
- Users can navigate the map and inspect the relevant analysis layer.

## 5. Non-Functional Requirements

### NFR-01: Security

**Priority:** Must Have

The system shall protect user accounts and restrict access to protected resources.

**Acceptance Criteria:**
- Passwords are stored using a suitable password-hashing mechanism.
- Protected API endpoints require authentication.
- Users cannot access another user's private analysis records without authorization.

### NFR-02: Usability

**Priority:** Must Have

The interface shall be understandable for users who are not specialists in software development.

**Acceptance Criteria:**
- The main workflow can be completed through clearly labelled interface controls.
- File-upload errors are explained in understandable language.
- Analysis results include meaningful titles and legends.

### NFR-03: Reliability

**Priority:** Must Have

The system shall handle invalid input and processing failures without losing unrelated stored data.

**Acceptance Criteria:**
- Invalid image files do not cause the application to terminate unexpectedly.
- Processing errors are reported to the user.
- Failed analyses are distinguishable from completed analyses.

### NFR-04: Maintainability

**Priority:** Must Have

The software shall use a modular architecture separating the frontend, backend, image processing, and machine learning components.

**Acceptance Criteria:**
- Source code is organized into clearly identified modules.
- The repository includes setup instructions.
- Key processing functions and API endpoints are documented.

### NFR-05: Reproducibility

**Priority:** Must Have

Machine learning experiments shall be documented so that their main settings and results can be reproduced.

**Acceptance Criteria:**
- The dataset source and data splits are documented.
- Model configuration and evaluation metrics are recorded.
- The training procedure can be repeated using the provided instructions and required data.

### NFR-06: Performance

**Priority:** Should Have

The system should provide reasonable processing times for the selected test dataset and available hardware.

**Acceptance Criteria:**
- Processing time is measured on representative test images.
- The hardware and image sizes used during testing are documented.
- Performance limitations are reported.

A numerical performance target will be established after testing representative files.

### NFR-07: Compatibility

**Priority:** Should Have

The web interface should function in current versions of commonly used desktop browsers.

**Acceptance Criteria:**
- The main workflow is tested in at least two desktop browsers.
- Critical interface functions work without browser-specific modifications.

## 6. Main User Workflow

The proposed workflow is:

1. A user registers or logs in.
2. The user uploads a supported multispectral image.
3. The backend validates the file and extracts the required spectral bands.
4. The system calculates selected vegetation indices.
5. The trained machine learning model analyzes the processed data.
6. The user views the resulting maps and model predictions.
7. The user may save or export the results.

The model-training and comparison process will be performed as part of the project's development and evaluation activities. It is not required to be an end-user feature in the initial application.

## 7. Requirements Traceability

| Requirement | Planned Component | Verification Method |
|---|---|---|
| FR-01, FR-02 | Authentication module | Registration and login tests |
| FR-03, FR-04 | Upload and preprocessing modules | File validation and preprocessing tests |
| FR-05 | Vegetation index module | Numerical calculation tests |
| FR-06 | Machine learning module | Training and inference tests |
| FR-07 | ML evaluation workflow | Baseline comparison experiments |
| FR-08 | Visualization interface | Interface tests |
| FR-09 | Database and analysis history | Data access tests |
| FR-10 | Export module | Export verification |
| FR-11 | ML evaluation workflow | Label-based metric evaluation, if applicable |
| FR-12 | Geospatial visualization module | Map alignment and display tests |
| NFR-01 | Authentication and backend | Security and access-control tests |
| NFR-02 | Frontend | Usability testing |
| NFR-03 | Backend and processing modules | Error-handling tests |
| NFR-04 | Overall architecture | Code and documentation review |
| NFR-05 | ML experiments | Reproducibility review |
| NFR-06 | Processing pipeline | Performance measurements |
| NFR-07 | Frontend | Browser compatibility tests |

## 8. Assumptions and Dependencies

The current requirements are based on the following assumptions:

- An existing multispectral UAV dataset will be used.
- The system will focus on one selected crop.
- The selected dataset will provide sufficient spectral information for the planned analysis.
- The machine learning task will be finalized after reviewing the dataset and available labels.
- A custom machine learning model will be trained and compared with existing approaches.
- The application will be developed as a web-based system.
- Some requirements may be refined following supervisor feedback and dataset evaluation.

## 9. Conclusion

This document defines the preliminary functional and non-functional requirements for the proposed agricultural monitoring system.

The essential requirements include user authentication, multispectral image upload, vegetation-index calculation, custom machine learning analysis, model comparison, and result visualization.

Additional features, such as analysis history, result export, and interactive geospatial maps, will be prioritized according to implementation time and available resources.

The requirements will be reviewed and refined after the final crop, dataset, and machine learning approach have been selected.
