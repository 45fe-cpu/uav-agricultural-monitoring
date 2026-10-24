# UAM-1: Project Proposal

**Project Title:** Development of an Intelligent Software System for Agricultural Monitoring Using Multispectral UAV Imagery

**Project Type:** Software Engineering Diploma Project

**Status:** Preliminary Project Proposal

## 1. Problem Statement

Agricultural monitoring is important for assessing crop conditions and identifying areas that may require further investigation. Traditional field inspection can be time-consuming, particularly for large agricultural areas.

Unmanned Aerial Vehicles (UAVs) equipped with multispectral cameras can capture information about vegetation across different spectral bands. However, processing and interpreting these images requires appropriate software tools and analytical methods.

The proposed project addresses the need for an integrated web-based system that combines multispectral image processing, vegetation-index calculation, machine learning analysis, and visualization.

## 2. Project Aim

The aim of this project is to develop an intelligent software system for monitoring agricultural vegetation using multispectral UAV imagery.

The system will support vegetation-index analysis, machine learning-based assessment, and visualization of results through a web interface.

## 3. Project Objectives

The main objectives are:

1. Review existing agricultural monitoring systems and relevant scientific literature.
2. Select a suitable multispectral UAV dataset focusing on one agricultural crop.
3. Develop a workflow for preprocessing multispectral imagery.
4. Implement vegetation-index calculations, including NDVI.
5. Train a custom machine learning model for the selected agricultural analysis task.
6. Compare the trained model with selected baseline approaches.
7. Develop a web interface with user authentication, image upload, and result visualization.
8. Evaluate the software functionality and machine learning performance.

## 4. Proposed Solution

The proposed solution is a web application that allows authenticated users to upload supported multispectral UAV images and perform agricultural analysis.

The system will contain the following main components:

- User authentication module.
- Multispectral image upload and preprocessing module.
- Vegetation-index calculation module.
- Machine learning inference module.
- Result visualization interface.
- Database for user and analysis metadata.
- Storage for uploaded imagery and generated results.

The initial system will focus on one selected crop. The final crop and dataset will be determined after reviewing available data and labels.

## 5. Preliminary Technology Stack

The proposed technologies are:

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Machine Learning | PyTorch, Scikit-learn |
| Image Processing | Rasterio, GDAL |
| Frontend | React |
| Database | PostgreSQL |
| Version Control | GitHub |
| Project Management | YouTrack |

These technologies are preliminary selections and may be refined during implementation.

## 6. Project Relevance

The project is relevant to agricultural monitoring because multispectral UAV imagery can provide information about vegetation conditions and spatial differences within agricultural fields.

For Kazakhstan, where agricultural monitoring may involve large cultivated areas, the proposed approach is a relevant subject for software engineering research and development.

The project does not require collecting a new UAV dataset. Existing datasets, including international sources, will be considered.

## 7. Expected Contribution

The main expected contribution is the development and evaluation of an integrated software workflow combining multispectral image processing, vegetation indices, a custom-trained machine learning model, and a web interface.

The project will also compare the proposed machine learning approach with selected baselines.

The contribution is primarily software engineering integration and experimental evaluation. A novel machine learning algorithm is not claimed at this preliminary stage.

## 8. Expected Deliverables

The expected project deliverables include:

- A documented software architecture.
- A web-based agricultural monitoring application.
- A multispectral image-processing workflow.
- Vegetation-index calculation functionality.
- A custom-trained machine learning model.
- Baseline comparison and evaluation results.
- Visualization of analytical outputs.
- Software testing documentation.
- Source code and technical documentation.

## 9. Project Limitations

The initial version will not include real-time drone control, direct UAV hardware integration, or automatic agricultural treatment.

The system will focus on one crop and selected supported image formats.

The feasibility of supervised anomaly detection and label-based validation will depend on the available dataset.

## 10. Conclusion

The proposed project aims to develop an integrated software system for agricultural monitoring using multispectral UAV imagery.

By combining image processing, machine learning, and web technologies, the project will investigate how agricultural imagery can be transformed into interpretable analytical results.

The next stages will focus on final dataset selection, model development, software implementation, and evaluation.
