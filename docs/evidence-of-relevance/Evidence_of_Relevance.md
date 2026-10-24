# UAM-2: Evidence of Relevance

**Project:** Development of an Intelligent Software System for Agricultural Monitoring Using Multispectral UAV Imagery

**Document Status:** Preliminary Problem Validation

## 1. Problem Background

Agricultural monitoring is essential for identifying changes in crop conditions and supporting timely field management decisions.

In Kazakhstan, agricultural fields can cover large areas, making regular monitoring challenging. Traditional field inspections require significant time and resources, while satellite imagery can be affected by cloud coverage and spatial resolution limitations.

Multispectral UAV imagery provides detailed information about vegetation characteristics. However, processing and interpreting these images can require specialized knowledge, and identifying potentially problematic areas remains a challenging task.

These limitations create a need for accessible software tools that can process multispectral imagery, support vegetation analysis, and present results in an understandable format.

## 2. Relevance Assessment

The relevance of the proposed system was examined through agricultural monitoring context analysis, preliminary dataset investigation, and consultations with specialists in agricultural technology, UAV applications, and computer vision.

Three expert consultations were documented. The discussions addressed current agricultural monitoring challenges, the availability of multispectral data, machine learning feasibility, and the functionality expected from an intelligent monitoring system.

The consultations identified several recurring concerns:

- Difficulties in identifying vegetation stress at an early stage.
- Variations in multispectral image quality caused by environmental conditions and sensor calibration.
- Limited availability of reliable labelled agricultural datasets.
- Challenges in interpreting vegetation indices and machine learning predictions.
- The need for clear visualization, temporal comparison, and exportable analysis results.

These findings support the relevance of developing a system that combines multispectral image processing, vegetation analysis, and machine learning within a unified application.

## 3. Proposed Solution

The proposed project is a web-based intelligent software system for agricultural monitoring using multispectral UAV imagery.

The system is planned to provide:

- Secure user authentication.
- Multispectral UAV image upload and validation.
- Spectral band processing.
- Vegetation index calculation, including NDVI and NDRE where supported by the data.
- Machine learning-based identification of potential vegetation anomalies.
- Visualization of analysis results.
- Comparison of observations across different acquisition dates.
- Export of maps and analytical results.

Spring wheat is currently considered a promising target crop due to its agricultural relevance in Kazakhstan and the availability of preliminary multispectral imagery.

The exact machine learning task will be finalized after evaluating the quality and availability of suitable training and validation data.

## 4. Key Findings and Their Impact on the System

| Identified Need | Proposed System Response |
|---|---|
| Early identification of potentially problematic vegetation areas | ML-based anomaly analysis |
| Difficult interpretation of multispectral information | Vegetation indices and visual maps |
| Variation in image quality and calibration | Input validation and preprocessing |
| Need to observe seasonal changes | Multi-temporal image comparison |
| Limited reliable ground truth | Explicit evaluation strategy and model limitations |
| Need for actionable outputs | Exportable maps, statistics, and reports |
| Need for trustworthy analysis | Comparison with baseline methods and available reference data |

The identified needs inform the initial functional and non-functional requirements and provide a foundation for further system design.

## 5. Preliminary Dataset Feasibility

An openly available multispectral UAV dataset from East Kazakhstan was selected for preliminary technical examination.

**Dataset:** A Multispectral UAV Imagery Dataset of Wheat, Soybean, and Barley Crops in East Kazakhstan

**Source:** https://doi.org/10.5281/zenodo.7860751

The dataset contains imagery acquired during the 2022 growing season, including five multispectral channels and an additional NDVI band.

A preliminary analysis was conducted using five wheat images from one experimental plot. This supported the feasibility of reading and processing multispectral GeoTIFF data and conducting temporal vegetation index analysis.

However, independent ground-truth labels for crop stress or diseases have not been confirmed in the examined materials. Therefore, this dataset cannot yet be considered sufficient for supervised anomaly detection evaluation.

Additional publicly available datasets are being evaluated for model training and validation.

## 6. Limitations and Further Validation

This relevance assessment represents an initial stage of project investigation.

The following limitations remain:

1. The final target crop and exact machine learning task are subject to dataset feasibility.
2. The availability of reliable labels for vegetation stress detection is limited.
3. Expert consultations provide preliminary qualitative evidence rather than a representative survey of agricultural users.
4. The proposed system has not yet been validated through deployment or formal usability testing with agricultural end users.
5. Claims about specific crop stress causes will require independent reference data.

Further work will include dataset assessment, comparison with existing agricultural monitoring solutions, development of a trained machine learning model, and evaluation against available reference data.

## 7. Conclusion

The preliminary investigation indicates a practical need for software that simplifies multispectral UAV image analysis and helps users identify potentially problematic areas within agricultural fields.

The expert consultations highlight the importance of accessible visualization, reliable processing, temporal analysis, and transparent machine learning evaluation.

These findings provide an initial justification for the proposed intelligent agricultural monitoring system and guide its subsequent requirements, architecture, and evaluation plan.

---

## Appendix A. Supporting Consultation Records

The relevance assessment is supported by three consultation documents:

- **Consultation A:** UAV and agricultural monitoring specialist.
- **Consultation B:** AgroTech AITU specialist.
- **Consultation C:** Computer Vision instructor.

For final submission, each supporting record should include the verified respondent's name or approved identifier, role, consultation date, communication method, and an accessible link to the original evidence where permission allows.

The original consultation records should be preserved separately rather than reproduced in full within the main report.
