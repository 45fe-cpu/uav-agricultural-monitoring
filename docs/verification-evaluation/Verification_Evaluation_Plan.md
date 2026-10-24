# UAM-9: Verification and Evaluation Plan

**Project:** Development of an Intelligent Software System for Agricultural Monitoring Using Multispectral UAV Imagery

**Status:** Preliminary Evaluation Plan

## 1. Purpose

This document describes how the proposed agricultural monitoring system will be tested and evaluated.

The evaluation will cover software functionality, multispectral image processing, machine learning performance, usability, and system reliability.

The project will focus on one selected crop using an existing multispectral UAV dataset.

## 2. Software Verification

| Component | Test Method | Expected Result |
|---|---|---|
| User registration | Register with valid and invalid data | Valid accounts are created; invalid inputs are rejected |
| User authentication | Test valid and invalid credentials | Authorized users can log in; invalid access is denied |
| Image upload | Upload supported and unsupported files | Supported files are accepted; invalid files are rejected |
| Image preprocessing | Verify spectral band extraction | Correct bands and dimensions are preserved |
| NDVI calculation | Compare outputs with independently calculated reference values | Calculated values agree with the reference within an established numerical tolerance |
| ML inference | Process prepared test samples | The trained model produces outputs in the expected format |
| Visualization | Inspect vegetation-index and prediction maps | Maps and legends correspond to analysis results |
| Export | Export a completed analysis | Exported files contain the expected results |
| Data access | Attempt access to another user's private records | Unauthorized access is denied |

## 3. Machine Learning Evaluation

The project will train a custom machine learning model and compare it with at least two selected baseline approaches.

The final modelling task will depend on the selected crop dataset and the availability of suitable labels.

### 3.1. Dataset Preparation

The evaluation procedure will include:

1. Inspecting the dataset and available spectral bands.
2. Checking image formats and label availability.
3. Applying appropriate preprocessing and normalization.
4. Dividing data into training, validation, and test sets.
5. Preventing data leakage between related images or field plots.
6. Documenting the dataset source and experimental configuration.

Where multiple images come from the same field or acquisition session, the splitting strategy will account for their relationship to reduce overly optimistic evaluation results.

### 3.2. Model Comparison

The following approaches will be considered:

| Approach | Purpose |
|---|---|
| Vegetation-index-based baseline | Provide a simple reference using spectral information |
| Classical ML baseline, such as Random Forest | Compare against a conventional machine learning approach |
| Custom-trained model, potentially CNN-based | Evaluate the proposed machine learning solution |

The exact models will be finalized after dataset inspection.

All approaches will be evaluated using an appropriate common test set.

### 3.3. Evaluation Metrics

For classification tasks, the following metrics may be used:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

For pixel-level anomaly segmentation, additional metrics may include:

- Intersection over Union (IoU)
- Dice coefficient

If the selected task is regression, suitable regression metrics will be selected instead.

Metrics will be chosen according to the actual prediction task and available labels.

### 3.4. Label-Based Validation

If reliable reference labels are available, model predictions will be compared against them.

If labels are generated automatically from vegetation indices, they will be identified as pseudo-labels rather than independent ground truth.

If suitable labels are unavailable, the evaluation strategy will be revised and the limitation documented in consultation with the supervisor.

## 4. Vegetation Index Verification

NDVI will be calculated using:

**NDVI = (NIR - Red) / (NIR + Red)**

The calculation will be checked using known input values and reference calculations.

Testing will also cover missing spectral bands, invalid pixel values, and division-by-zero handling.

## 5. Non-Functional Evaluation

| Area | Evaluation Method |
|---|---|
| Performance | Measure processing time on representative images |
| Reliability | Test corrupted files and processing failures |
| Security | Test authentication and access restrictions |
| Usability | Test the main workflow with representative users |
| Compatibility | Test the interface in at least two desktop browsers |
| Reproducibility | Record dataset splits, model settings, and experimental results |

Performance measurements will report image sizes, hardware specifications, and processing times.

Numerical acceptance thresholds will be established after initial testing rather than invented before representative data is available.

## 6. Evaluation Procedure

The planned evaluation will follow these stages:

1. Select and inspect a suitable agricultural dataset.
2. Verify image formats, spectral channels, and labels.
3. Implement and test vegetation-index calculations.
4. Train the custom machine learning model.
5. Implement and evaluate baseline approaches.
6. Compare results using task-appropriate metrics.
7. Integrate the selected model with the application.
8. Perform functional and non-functional tests.
9. Document results, limitations, and possible improvements.

## 7. Expected Evaluation Deliverables

The project evaluation will produce:

- Dataset description and preprocessing documentation.
- Model training configuration.
- Baseline comparison table.
- Evaluation metrics and visual results.
- Software test cases and test results.
- Performance measurements.
- Discussion of limitations.

## 8. Risks and Limitations

Potential limitations include insufficient labelled data, differences between agricultural datasets, class imbalance, limited computational resources, and variation in spectral image quality.

These risks will be addressed through dataset inspection, appropriate validation procedures, documented assumptions, and comparison with simpler baseline approaches.

## 9. Conclusion

The proposed evaluation plan combines software testing with machine learning experiments.

The main objective is to verify that the system correctly processes multispectral imagery, calculates vegetation indices, provides the planned web functionality, and produces measurable machine learning results.

The final evaluation methods and success criteria will be refined after the crop, dataset, and prediction task are confirmed.
