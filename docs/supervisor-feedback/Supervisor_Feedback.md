# UAM-11: Supervisor Feedback and Project Decisions

**Project Title:** Development of an Intelligent Software System for Agricultural Monitoring Using Multispectral UAV Imagery

**Document Status:** Preliminary Supervisor Feedback Record

**Consultation Date:** 23.10.2026

**Supervisor:** Praveen Kumar

**Consultation Method:** Written communication

## 1. Purpose

This document summarizes the feedback received from the diploma project supervisor and explains how it influences the proposed system's scope, requirements, and implementation plan.

The consultation focused on dataset selection, target crop, machine learning requirements, system functionality, and evaluation.

## 2. Supervisor Feedback Summary

| ID | Discussion Topic | Supervisor Feedback | Project Decision |
|---|---|---|---|
| SF-01 | Dataset origin | "You can use any dataset, as it is not mandatory to collect in Kazakhstan." | Publicly available international datasets may be used for training and evaluation. |
| SF-02 | Target crop | "Take any specific crop." | The system will focus on one crop. Spring wheat is currently being considered, subject to dataset feasibility. |
| SF-03 | Machine learning | "You have to train own machine learning model in addition to show the comparison with few existings." | A project-specific ML model will be trained and compared with existing methods. |
| SF-04 | Agricultural validation | "For Justification it would be better to test with agricultural data." | Agricultural datasets will be used for technical assessment. Kazakhstan-specific testing remains desirable but is not confirmed as mandatory. |
| SF-05 | Proposed functionality | "It seems ok, also add User authentication and Validate anomaly detection against labelled data (if you can add)." | The proposed web application is retained. User authentication is added, and evaluation against labelled data is planned where feasible. |

## 3. Changes Made Based on Feedback

### 3.1 Scope Definition

The initial project concept involved processing multispectral UAV imagery, calculating vegetation indices, detecting potential vegetation anomalies, and visualizing results.

Following supervisor feedback, the scope was refined to focus on one agricultural crop.

Spring wheat is considered a promising candidate based on preliminary relevance research. The final decision depends on the availability of suitable machine learning data.

### 3.2 Machine Learning Requirements

The project must include a machine learning model trained as part of the diploma work.

The trained model will be compared with existing baseline approaches. The final model architecture and evaluation metrics will depend on the selected task and available labels.

### 3.3 User Authentication

User registration and authentication have been added to the proposed system requirements and architecture.

### 3.4 Dataset Selection

The supervisor confirmed that internationally available datasets are acceptable.

A publicly available multispectral UAV dataset from East Kazakhstan has been examined for preliminary image processing and vegetation index analysis.

However, reliable independent anomaly labels have not been confirmed in the examined files. Further dataset evaluation is required before finalizing the supervised learning methodology.

### 3.5 Model Evaluation

Evaluation against labelled data is planned where feasible.

The project will distinguish between independently verified ground truth and automatically generated weak labels. Model performance claims will depend on the quality of the available reference data.

## 4. Implemented Documentation Updates

The following preliminary project materials have been developed:

- Initial system architecture diagrams.
- Software requirements specification.
- Preliminary NDVI processing experiment.
- Problem relevance assessment based on agricultural context and expert consultations.

These materials support the planned system design. They do not represent a fully implemented application or a completed machine learning evaluation.

## 5. Outstanding Decisions

The following matters remain open:

1. Final selection of one agricultural crop.
2. Confirmation of a suitable labelled dataset.
3. Definition of the exact ML prediction task.
4. Selection of the model architecture and baseline methods.
5. Confirmation of the final evaluation protocol.

Any major adjustment to the ML task will be discussed with the supervisor.

## 6. Conclusion

The supervisor's feedback has clarified the technical expectations of the diploma project.

The system will retain its general focus on multispectral UAV-based agricultural monitoring while incorporating user authentication, a trained machine learning model, comparison with existing methods, and an evidence-based evaluation strategy.

The remaining decisions will be finalized according to dataset feasibility and further supervisor guidance.

