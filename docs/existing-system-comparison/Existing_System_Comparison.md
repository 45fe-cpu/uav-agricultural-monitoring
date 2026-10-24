# UAM-4: Existing System Comparison

## 1. Introduction

Several existing software systems can be used to process UAV imagery and support agricultural monitoring. They differ in their image-processing capabilities, vegetation-index calculation, visualization features, accessibility, and support for machine learning.

This section compares four systems and projects related to the proposed Intelligent Software System for Agricultural Monitoring Using Multispectral UAV Imagery:

1. FCCImageProcessor
2. PIX4Dfields
3. WebODM
4. Anantam Agri Dashboard

The comparison is based on publicly available project descriptions and official documentation. A feature marked as "Not documented" means that its availability could not be confirmed from the reviewed sources. It does not necessarily mean that the feature is impossible to implement.

## 2. Overview of Existing Systems

### 2.1. FCCImageProcessor

FCCImageProcessor is an image-processing application designed for RGB and multispectral imagery. According to its project description, it supports vegetation-index calculation, visualization, and export of results.

The project is particularly relevant because it demonstrates how multispectral channels can be processed to calculate vegetation indices. Its implementation can be studied to understand possible approaches to image processing.

**Limitations for the proposed project:** The reviewed description does not confirm built-in training of a custom machine learning model or validation of detected anomalies against labelled agricultural data.

Source: https://github.com/Jakub-Espandr/FCCImageProcessor

### 2.2. PIX4Dfields

PIX4Dfields is a commercial agricultural mapping and analysis solution designed for drone imagery. It supports vegetation-index analysis, field zonation, annotations, and export of agricultural maps and other results.

It is a useful reference for understanding the functionality expected from agricultural monitoring software and how analytical results can be presented to users.

**Limitations for the proposed project:** The reviewed product documentation does not establish that custom machine learning training and labelled anomaly validation are available as built-in features.

Sources:
- https://www.pix4d.com/product/pix4dfields/outputs/
- https://support.pix4d.com/hc/en-us/articles/360000891623

### 2.3. WebODM

WebODM is an open-source platform for processing drone imagery and generating geospatial outputs, including orthophotos. Multispectral processing is possible with compatible cameras and appropriate workflows. Vegetation indices can also be calculated using additional tools such as QGIS.

WebODM is relevant because it provides an open-source alternative for drone-image processing and can serve as a reference for the geospatial processing workflow.

**Limitations for the proposed project:** Custom ML model training and labelled anomaly validation are not established as standard built-in features in the reviewed documentation. Some analytical functions may require additional tools.

Sources:
- https://docs.webodm.org/multispectral/
- https://webodm.org/

### 2.4. Anantam Agri Dashboard

Anantam Agri Dashboard is a student project featuring a React-based interface for agricultural monitoring and visualization. It is useful as a reference for designing a web interface with dashboards and agricultural data displays.

The project can help inform the visual structure of the proposed application, including its navigation, monitoring panels, and presentation of analytical results.

**Limitations for the proposed project:** The reviewed project description does not sufficiently establish support for direct multispectral image processing, vegetation-index calculation, custom ML model training, or validation against labelled anomaly data. These capabilities should not be assumed without further code inspection.

Source: https://github.com/mylifeastanmay-hub/anantam-agri-dashboard

## 3. Comparison Criteria

The systems are compared using the following criteria:

1. Support for multispectral UAV imagery.
2. Vegetation-index calculation.
3. Visualization of agricultural data.
4. Export of results.
5. Ability to train a custom machine learning model.
6. Validation of detected anomalies against labelled data.
7. Web-based access.
8. Suitability as a reference for the proposed system.

## 4. Comparative Analysis

| Criterion | FCCImageProcessor | PIX4Dfields | WebODM | Anantam Agri Dashboard |
|---|---|---|---|---|
| Multispectral imagery | Supported according to project description | Supported | Supported with compatible equipment and workflows | Not confirmed |
| Vegetation indices | Supported | Supported | Possible through additional tools and workflows | Not confirmed |
| Agricultural data visualization | Supported | Supported | Supported through generated geospatial outputs and compatible tools | Central purpose of the interface |
| Export of results | Described as supported | Supported | Geospatial outputs supported | Not confirmed |
| Custom ML model training | Not documented | Not documented as a built-in feature | Not documented as a built-in feature | Not documented |
| Validation against labelled anomaly data | Not documented | Not documented | Not documented | Not documented |
| Web-based access | Application interface; deployment details should be checked | Primarily a desktop application | Browser-based interface | React-based web interface |
| Main value for this project | Reference for spectral processing and indices | Reference for agricultural analysis and field zonation | Reference for open-source drone-image processing | Reference for web-interface design |

## 5. Identified Research and Development Gap

The reviewed systems demonstrate that several important functions already exist, including multispectral image processing, vegetation-index calculation, geospatial visualization, and agricultural mapping.

However, the reviewed public descriptions do not establish that all the planned functions of the proposed system are provided together in one application. In particular, they do not confirm an integrated workflow combining custom machine learning model training, anomaly detection, and evaluation against labelled agricultural data.

This creates an opportunity to develop a system that combines selected image-processing and visualization capabilities with a dedicated machine learning workflow.

The proposed system will focus on:

- Uploading and processing multispectral UAV imagery.
- Calculating selected vegetation indices.
- Training a custom machine learning model and comparing it with selected existing approaches.
- Visualizing analytical results and potentially anomalous areas.
- Evaluating anomaly-detection performance against labelled data, if a suitable labelled dataset is available.
- Providing user registration and authentication.
- Allowing users to view and export analysis results.

The exact crop, dataset, model architecture, and evaluation procedure will be finalized after the available data and its labels have been examined.

## 6. Conclusion

The comparison shows that existing agricultural software and open-source projects provide useful references for different parts of the proposed system. FCCImageProcessor is relevant to multispectral image processing, PIX4Dfields demonstrates agricultural analysis and field zonation, WebODM provides an open-source drone-processing workflow, and Anantam Agri Dashboard offers a reference for web-interface design.

The proposed project will not attempt to reproduce all the features of these systems. Instead, it will focus on developing an integrated software workflow for multispectral agricultural monitoring, including a custom machine learning model and an evaluation procedure appropriate to the selected dataset.

## 7. References

1. FCCImageProcessor. GitHub repository. https://github.com/Jakub-Espandr/FCCImageProcessor
2. PIX4Dfields. Outputs and product capabilities. https://www.pix4d.com/product/pix4dfields/outputs/
3. PIX4D Support. PIX4Dfields documentation. https://support.pix4d.com/hc/en-us/articles/360000891623
4. OpenDroneMap. WebODM Multispectral Documentation. https://docs.webodm.org/multispectral/
5. OpenDroneMap. WebODM website. https://webodm.org/
6. Anantam Agri Dashboard. GitHub repository. https://github.com/mylifeastanmay-hub/anantam-agri-dashboard
