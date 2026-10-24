# UAM-5: Technology Comparison

## 1. Introduction

The proposed project is an intelligent software system for agricultural monitoring using multispectral UAV imagery. The system is expected to support image upload, vegetation-index calculation, machine learning, visualization of analytical results, user authentication, and result management.

Selecting suitable technologies is important because the system must process geospatial image data, support model training and inference, and provide an accessible web interface.

This section compares alternative technologies for five major development decisions. The choices are preliminary and may be refined after the dataset and model requirements are finalized.

## 2. Technology Selection Criteria

The technologies are evaluated according to the following criteria:

- Compatibility with multispectral image processing.
- Support for machine learning and model integration.
- Ease of development and maintenance.
- Compatibility with the proposed system architecture.
- Availability of documentation and learning resources.
- Suitability for a university diploma project.

## 3. Backend Framework Comparison

The backend will handle requests from the web interface, coordinate image processing, manage analysis operations, and communicate with the database and machine learning components.

Three alternatives were considered.

| Criterion | FastAPI | Flask | Django |
|---|---|---|---|
| Main purpose | API development | Lightweight web applications and APIs | Full-featured web applications |
| Learning curve | Moderate | Relatively easy | Moderate to high |
| Automatic API documentation | Built-in | Requires additional tools | Requires additional tools for a REST API |
| Request data validation | Integrated validation support | Usually requires additional libraries | Available through Django forms and related tools |
| Integration with Python ML libraries | Suitable | Suitable | Suitable |
| Main advantage | Clear API structure and automatic documentation | Simplicity and flexibility | Many built-in web application features |
| Main limitation | Authentication and application structure still require configuration | More features must be assembled separately | May introduce functionality that is unnecessary for a focused API |

### Selected technology: FastAPI

FastAPI is selected as the preliminary backend framework because the system requires communication between the web interface, image-processing modules, the machine learning model, and the database.

Its automatic interactive API documentation can also simplify development and testing. Authentication will still need to be configured and implemented appropriately.

Official documentation: https://fastapi.tiangolo.com/

## 4. Machine Learning Framework Comparison

The project requires training a custom machine learning model and comparing its performance with existing approaches. The final model type will depend on the selected dataset and its labels.

| Criterion | PyTorch | TensorFlow/Keras | Scikit-learn |
|---|---|---|---|
| Main purpose | Deep learning and neural networks | Deep learning and neural networks | Classical machine learning |
| Custom neural network development | Supported | Supported | Not its primary purpose |
| Transfer learning | Supported through its ecosystem | Supported through its ecosystem | Limited compared with deep learning frameworks |
| Classical ML algorithms | Requires additional libraries | Requires additional libraries | Broad selection of classical algorithms |
| Suitability for CNN-based image analysis | High | High | Limited for raw image learning compared with deep learning frameworks |
| Main advantage | Flexible model development and research workflows | Accessible high-level model development through Keras | Convenient baselines and standard evaluation tools |

### Selected technology: PyTorch

PyTorch is the preliminary choice for developing and training the project's own deep learning model. It supports neural network construction and experimentation, which may be useful for multispectral image analysis.

Scikit-learn may also be used for baseline models and evaluation metrics. TensorFlow/Keras remains a reasonable alternative if it proves more suitable for the selected model or available learning resources.

The final model architecture will be selected after inspecting the dataset, the number of spectral bands, and the availability of reliable labels.

Official documentation:
- PyTorch: https://pytorch.org/docs/stable/
- TensorFlow: https://www.tensorflow.org/tutorials
- Scikit-learn: https://scikit-learn.org/stable/

## 5. Multispectral Image Processing Comparison

The system must read multispectral image files, access individual spectral bands, preserve geospatial information where available, and calculate vegetation indices.

| Criterion | Rasterio with GDAL | OpenCV | xarray |
|---|---|---|---|
| Main purpose | Geospatial raster processing | General computer vision and image processing | Working with labelled multidimensional data |
| Reading raster bands | Supported | Supports many image formats; geospatial metadata may require additional tools | Supported through compatible data backends |
| Geospatial metadata and coordinates | Strong support | Not its primary focus | Supports labelled dimensions and coordinates |
| Image transformations | Supported through related geospatial tools | Extensive image-processing operations | Possible through compatible libraries |
| Suitability for GeoTIFF workflows | High | Usually requires complementary geospatial tools | Depends on the data format and processing workflow |
| Main advantage | Designed for geospatial raster data | Broad image-processing functionality | Convenient for multidimensional scientific datasets |

### Selected technology: Rasterio with GDAL

Rasterio with GDAL is selected for the initial geospatial processing workflow because the system may need to read GeoTIFF files, access spectral bands, and preserve information about geographic coordinates and image transformations.

OpenCV may be added for specific image-processing operations if necessary. The use of xarray can be considered if the selected dataset contains multidimensional or time-series data that would benefit from labelled dimensions.

The final implementation must be checked against the actual file formats and band structure of the selected dataset.

Official documentation:
- Rasterio: https://rasterio.readthedocs.io/
- GDAL: https://gdal.org/en/stable/
- OpenCV: https://docs.opencv.org/
- xarray: https://docs.xarray.dev/

## 6. Frontend Framework Comparison

The frontend will allow users to interact with the system, upload imagery, view vegetation indices, inspect analytical results, and manage their accounts.

| Criterion | React | Streamlit | Django Templates |
|---|---|---|---|
| Main purpose | Interactive user interfaces | Data and machine learning applications | Server-rendered web pages |
| Custom interface design | High flexibility | Convenient but more framework-driven | Flexible within a server-rendered approach |
| Interactive dashboards | Supported | Supported with built-in components | Usually requires additional frontend tools |
| Integration with a separate API | Suitable | Possible, but not its main design approach | Possible |
| Development speed for a simple demo | Moderate | Very fast | Moderate |
| Suitability for a customized multi-page interface | High | Moderate | Moderate |

### Selected technology: React

React is selected as the preliminary frontend technology because the proposed system is expected to have multiple pages and interactive components. These may include an upload page, a dashboard, vegetation-index visualizations, analysis history, and user account pages.

Streamlit would be a faster alternative for a basic research prototype. However, React provides greater flexibility for developing a customized interface connected to a separate backend API.

Official documentation:
- React: https://react.dev/learn
- Streamlit: https://docs.streamlit.io/
- Django: https://docs.djangoproject.com/

## 7. Database Comparison

The database will store structured information such as user accounts, analysis records, timestamps, selected indices, model versions, and references to generated results. Large image files will be stored separately rather than placing all image data directly in ordinary database records.

| Criterion | PostgreSQL | SQLite | MongoDB |
|---|---|---|---|
| Data model | Relational | Relational | Document-oriented |
| Setup | Requires a database service for a typical deployment | Minimal setup; database is stored in a file | Requires a MongoDB deployment or service |
| Multi-user web application | Suitable | Possible, but concurrent-write requirements must be considered | Suitable |
| Structured relationships between users and analyses | Strong support | Supported | Requires a different data-modelling approach |
| Main advantage | Robust relational database with extensive features | Simple and convenient for local prototypes | Flexible document structure |
| Main limitation | More setup and administration than SQLite | Less suitable for some concurrent-write workloads | Relational queries and constraints may require more application-level design |

### Selected technology: PostgreSQL

PostgreSQL is the preliminary choice because the application is expected to manage user accounts and multiple analysis records with relationships between them.

SQLite remains a reasonable option for an early local prototype because it requires very little setup. The final choice will also depend on the expected deployment environment and the actual concurrency requirements.

Image files and exported maps will be stored separately, while the database will retain their paths or references and associated metadata.

Official documentation:
- PostgreSQL: https://www.postgresql.org/docs/
- SQLite: https://www.sqlite.org/docs.html
- MongoDB: https://www.mongodb.com/docs/

## 8. Preliminary Technology Stack

Based on the comparison, the following stack is proposed for initial development.

| System component | Preliminary choice | Purpose |
|---|---|---|
| Backend API | FastAPI | Handle requests and coordinate system components |
| Machine learning | PyTorch | Train and run the custom model |
| Baseline models and metrics | Scikit-learn | Compare selected classical ML approaches and calculate evaluation metrics |
| Geospatial processing | Rasterio and GDAL | Read and process multispectral raster data |
| Frontend | React | Provide the user interface and interactive visualizations |
| Database | PostgreSQL | Store user and analysis metadata |
| Image and result storage | File storage or compatible object storage | Store uploaded imagery and generated outputs |

This stack is a proposed design, not a statement that these technologies have already been implemented.

## 9. Risks and Considerations

Several issues must be considered before implementation:

1. **Dataset compatibility:** The selected dataset must be compatible with the planned processing workflow, including its image formats, spectral bands, and geospatial metadata.

2. **Label availability:** Training and evaluating a supervised anomaly-detection model requires suitable labels. If reliable labels are unavailable, the modelling approach and evaluation plan must be adjusted.

3. **Model complexity:** The model must be appropriate for the available dataset and computational resources. A complex neural network is not automatically better than a simpler baseline.

4. **System complexity:** Using a separate frontend, backend, ML framework, and database requires integration work. The implementation should therefore proceed incrementally.

5. **Authentication and security:** User authentication, access control, upload validation, and protection of stored files must be designed and tested rather than assumed to be provided automatically by the selected technologies.

## 10. Conclusion

The technology comparison identifies a preliminary development stack consisting of FastAPI, PyTorch, Rasterio/GDAL, React, and PostgreSQL.

These technologies address the main requirements of the proposed system: web-based interaction, multispectral raster processing, custom machine learning, result visualization, and management of user and analysis data.

The choices remain subject to refinement after the dataset, model requirements, and deployment environment are examined. The next development stage should verify dataset compatibility and implement a small end-to-end prototype before committing to more complex functionality.

## 11. References

1. FastAPI Documentation. https://fastapi.tiangolo.com/
2. PyTorch Documentation. https://pytorch.org/docs/stable/
3. TensorFlow Tutorials. https://www.tensorflow.org/tutorials
4. Scikit-learn Documentation. https://scikit-learn.org/stable/
5. Rasterio Documentation. https://rasterio.readthedocs.io/
6. GDAL Documentation. https://gdal.org/en/stable/
7. OpenCV Documentation. https://docs.opencv.org/
8. xarray Documentation. https://docs.xarray.dev/
9. React Documentation. https://react.dev/learn
10. Streamlit Documentation. https://docs.streamlit.io/
11. Django Documentation. https://docs.djangoproject.com/
12. PostgreSQL Documentation. https://www.postgresql.org/docs/
13. SQLite Documentation. https://www.sqlite.org/docs.html
14. MongoDB Documentation. https://www.mongodb.com/docs/
