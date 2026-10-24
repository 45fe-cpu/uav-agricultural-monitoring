# In-Depth Critical Synthesis of the Reviewed Literature

## 1. Comparison of Vegetation Indices

The reviewed literature demonstrates that vegetation-index performance depends on crop type, growth stage, spectral bands, and the target agricultural variable.

Aziz et al. (2024) compared six indices for paddy monitoring: NDREI, NDVI, OSAVI, SAVI, NRI, and GNDVI. NDREI showed the strongest classification performance in their study, while NRI performed less effectively. The authors also recommended additional monitoring across growth stages and further field-based verification.

Camenzind and Yu (2024) investigated wheat using multispectral reflectance, vegetation indices, and image texture features. NDRE provided strong yield-prediction results, with reported RMSE values of 49.1 and 60.6 g/m² across two study years.

**Critical interpretation:** NDVI is a suitable initial vegetation index because it is interpretable and widely used. However, it should not be assumed to be the best index for every crop or agricultural task.

**Implication for the proposed project:** Implement NDVI first, then consider NDRE or other indices supported by the selected dataset.

## 2. Comparison of Machine Learning Approaches

Shahi et al. (2023) classified UAV-based crop disease assessment approaches into statistical methods, conventional machine learning, and deep learning. Their review highlights the importance of sensor selection, data preparation, and labelled training samples.

Khose and Mailapalli (2024) compared Random Forest regression, Support Vector Regression, and Partial Least Squares Regression for rice nitrogen assessment. Random Forest performed well in their experiments.

Ndour et al. (2025) reviewed machine learning methods for crop phenotypic traits and found that model performance varied according to the prediction target. Their analysis supports selecting models based on empirical evidence rather than assuming that deep learning is always superior.

**Critical interpretation:** Results obtained from different crops and prediction tasks cannot be compared directly as if they were measured under identical conditions.

**Implication for the proposed project:** Evaluate a custom-trained model against simpler alternatives on the same dataset, using identical test conditions and task-appropriate metrics.

## 3. Dataset Availability and Ground Truth

Maulit et al. (2023) introduced a multispectral UAV dataset collected in East Kazakhstan during the 2022 growing season.

The dataset covers 27 hectares and includes wheat, barley, and soybean. It contains five spectral bands and processed imagery with an additional NDVI layer.

The dataset provides an important opportunity to work with agricultural imagery collected in Kazakhstan.

However, the availability of multispectral imagery and NDVI layers does not establish that independent ground-truth labels for crop diseases or vegetation anomalies are included.

**Critical interpretation:** Vegetation-index values must not automatically be treated as verified disease labels.

**Implication for the proposed project:** Inspect the dataset structure and annotations before choosing a supervised prediction task. If appropriate labels are unavailable, the project must use a clearly defined alternative evaluation strategy or obtain additional reference data.

## 4. Limitations of Spectral-Only Monitoring

Burchard-Levine et al. (2024) examined thermal, multispectral, and three-dimensional UAV information for monitoring vineyard water stress.

Their results showed that thermal variables were particularly important for estimating physiological water-stress indicators, while multispectral and three-dimensional variables contributed to other vegetation characteristics.

Combining different sensor types produced stronger results for the investigated monitoring task.

**Critical interpretation:** A single multispectral sensor cannot be assumed to measure every agricultural stress indicator accurately.

**Implication for the proposed project:** Present model outputs as task-specific analytical assessments rather than definitive agricultural diagnoses.

## 5. Comparison with Existing Integrated Systems

The 2026 AgriEngineering study titled "A Method for Automated Crop Health Monitoring in Large Areas Using Multi-Spectral Images and Deep Convolutional Neural Networks" presents a system integrating UAV imagery, image storage, semantic segmentation, NDVI calculation, and visualization.

The reported U-Net segmentation model achieved a mean Intersection over Union of 68.4%.

Importantly, the model classified crop and land-cover categories in a polyculture setting. This is not equivalent to independently validated detection of crop diseases or vegetation anomalies.

**Critical interpretation:** Integrating multispectral imagery, deep learning, and a visualization interface is not itself a novel concept.

**Implication for the proposed project:** The diploma contribution should focus on the selected crop, reproducible model comparison, validated processing workflow, and software engineering implementation rather than claiming a completely new monitoring concept.

## 6. Research and Engineering Gap

The literature demonstrates that UAV multispectral imagery and machine learning can support agricultural monitoring. However, several practical challenges remain relevant to the proposed project:

1. Selecting a model suitable for a specific crop and dataset.
2. Ensuring that spectral channels and vegetation indices are processed correctly.
3. Obtaining reliable reference labels for evaluation.
4. Comparing models under consistent experimental conditions.
5. Integrating analytical methods into a usable software application.
6. Communicating uncertainty and limitations in agricultural predictions.

The proposed project will address these challenges through the design and evaluation of a web-based system for one selected crop.

Its expected contribution is an integrated and reproducible software workflow, including multispectral processing, vegetation-index analysis, custom model training, baseline comparison, authentication, and visualization.

## 7. Evaluation Recommendations

The literature suggests the following evaluation strategy:

- Verify spectral band order and NDVI calculations.
- Split related images or field plots carefully to reduce data leakage.
- Compare the custom model with conventional baselines.
- Select classification, segmentation, or regression metrics according to the actual task.
- Use independent ground-truth labels where available.
- Report model limitations and avoid unsupported disease-diagnosis claims.
- Evaluate both machine learning performance and software functionality.



## 8. References

[1] Omia, E., et al. (2023). Remote Sensing in Field Crop Monitoring: A Comprehensive Review of Sensor Systems, Data Analyses and Recent Advances. *Remote Sensing, 15*(2), 354. https://doi.org/10.3390/rs15020354

[2] Matese, A., Czarnecki, J. M. P., Samiappan, S., & Moorhead, R. (2024). Are unmanned aerial vehicle-based hyperspectral imaging and machine learning advancing crop science? *Trends in Plant Science, 29*(2), 196–209. https://doi.org/10.1016/j.tplants.2023.09.001

[3] Aziz, N. H., et al. (2024). Utilizing Spectral Indices on UAV Multispectral Images for Paddy Healthiness Detection: A Case Study in Perlis, Malaysia. *E3S Web of Conferences, 557*, 03005. https://doi.org/10.1051/e3sconf/202455703005

[4] Camenzind, M. P., & Yu, K. (2024). Multi temporal multispectral UAV remote sensing allows for yield assessment across European wheat varieties already before flowering. *Frontiers in Plant Science, 14*, 1214931. https://doi.org/10.3389/fpls.2023.1214931

[5] Zhu, H., et al. (2024). Intelligent agriculture: deep learning in UAV-based remote sensing imagery for crop diseases and pests detection. *Frontiers in Plant Science, 15*, 1435016. https://doi.org/10.3389/fpls.2024.1435016

[6] Shahi, T. B., Xu, C.-Y., Neupane, A., & Guo, W. (2023). Recent Advances in Crop Disease Detection Using UAV and Deep Learning Techniques. *Remote Sensing, 15*(9), 2450. https://doi.org/10.3390/rs15092450

[7] Ndour, A., et al. (2025). Optimal machine learning algorithms and UAV multispectral imagery for crop phenotypic trait estimation: a comprehensive review and meta-analysis. *Environmental Research Communications, 7*, 072002. https://doi.org/10.1088/2515-7620/ade84f

[8] Khose, S. B., & Mailapalli, D. R. (2024). UAV-based multispectral image analytics and machine learning for predicting crop nitrogen in rice. *Geocarto International, 39*(1), 2373867. https://doi.org/10.1080/10106049.2024.2373867

[9] Maulit, A., Nugumanova, A., Apayev, K., Baiburin, Y., & Sutula, M. (2023). A Multispectral UAV Imagery Dataset of Wheat, Soybean and Barley Crops in East Kazakhstan. *Data, 8*(5), 88. https://doi.org/10.3390/data8050088

[10] Zhou, X., & Wu, Y. (2024). UAV-based multispectral imaging for real-time crop health assessment and yield estimation in wheat. *International Journal of Research in Agronomy, 7*(8), 218–221. https://doi.org/10.33545/2618060X.2024.v7.i8c.5216

[11] Burchard-Levine, V., et al. (2024). Evaluating the utility of combining high resolution thermal, multispectral and 3D imagery from unmanned aerial vehicles to monitor water stress in vineyards. *Precision Agriculture, 25*, 2447–2476. https://doi.org/10.1007/s11119-024-10179-0

[12] A Method for Automated Crop Health Monitoring in Large Areas Using Multi-Spectral Images and Deep Convolutional Neural Networks. (2026). *AgriEngineering, 8*(3), 109. https://doi.org/10.3390/agriengineering8030109






