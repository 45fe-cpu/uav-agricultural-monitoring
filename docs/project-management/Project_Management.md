# UAM-10: Project Management

**Project:** Development of an Intelligent Software System for Agricultural Monitoring Using Multispectral UAV Imagery

**Status:** Preliminary Project Management Report

## 1. Project Management Approach

The project uses a task-based management approach to organize diploma deliverables, track progress, and maintain development documentation.

GitHub is used for version control and storing project artifacts. YouTrack is used for task management, priorities, deadlines, and progress tracking.

## 2. Project Tools

| Tool | Purpose |
|---|---|
| GitHub | Version control, documentation, architecture diagrams, and prototype files |
| YouTrack | Task planning, assignment, progress tracking, and deadlines |
| Mermaid | Editable architecture diagrams |
| HTML/CSS/JavaScript | Interactive UX prototype |

**GitHub Repository:** [https://github.com/45fe-cpu/uav-agricultural-monitoring](https://github.com/45fe-cpu/uav-agricultural-monitoring)

**YouTrack Project:** [https://uav-diploma-aitu.youtrack.cloud](https://uav-diploma-aitu.youtrack.cloud/projects/UAM)

## 3. Work Breakdown Structure

The project documentation is organized into eleven tasks:

| Task ID | Deliverable |
|---|---|
| UAM-1 | Project Proposal |
| UAM-2 | Evidence of Relevance |
| UAM-3 | Literature Review |
| UAM-4 | Existing System Comparison |
| UAM-5 | Technology Comparison |
| UAM-6 | System Requirements |
| UAM-7 | System Architecture |
| UAM-8 | UX Prototype |
| UAM-9 | Verification and Evaluation Plan |
| UAM-10 | Project Management Documentation |
| UAM-11 | Supervisor Feedback |

Task ownership, priorities, deadlines, and current statuses are maintained in YouTrack.

## 4. Completed and Documented Work

The GitHub repository contains preliminary documentation for system relevance, existing system comparison, technology comparison, requirements, architecture, UX prototype, verification and evaluation, and supervisor feedback.

Examples of traceable work include:

- UAM-4: Existing system comparison.
- UAM-5: Technology comparison.
- UAM-6: System requirements.
- UAM-7: Architecture diagrams.
- UAM-8: Interactive UX prototype.
- UAM-9: Verification and evaluation plan.

These deliverables represent the preliminary design and documentation stage. The complete software system and machine learning model have not yet been implemented.

## 5. GitHub Traceability

Examples of documented commits:

- UAM-4: https://github.com/45fe-cpu/uav-agricultural-monitoring/commit/6f4c3a5
- UAM-5: https://github.com/45fe-cpu/uav-agricultural-monitoring/commit/f118772
- UAM-7: https://github.com/45fe-cpu/uav-agricultural-monitoring/commit/060b3c7
- UAM-9: https://github.com/45fe-cpu/uav-agricultural-monitoring/commit/23d8906

These links provide examples of version-controlled project artifacts associated with YouTrack tasks.

## 6. Project Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Limited labelled multispectral datasets | High | Inspect available datasets before finalizing the ML task |
| Insufficient model performance | High | Compare custom models with simpler baselines |
| Large image file sizes | Medium | Use representative subsets during development |
| Integration complexity | Medium | Develop and test components incrementally |
| Time constraints | High | Prioritize core requirements and track progress in YouTrack |
| Limited computational resources | Medium | Select models appropriate for available hardware |

## 7. Next Development Milestones

1. Finalize the selected crop and dataset.
2. Verify available spectral channels and labels.
3. Implement multispectral image processing.
4. Train the custom machine learning model.
5. Compare model performance against baseline approaches.
6. Integrate the model with the web application.
7. Perform software testing and document results.

## 8. Conclusion

GitHub and YouTrack provide a structured environment for managing the diploma project.

The preliminary stage focuses on requirements, research, architecture, technology selection, UX design, and evaluation planning.

Further work will focus on dataset selection, system implementation, machine learning experiments, and verification of the completed application.
