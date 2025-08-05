# 🎓 Eduvos Student Grade Calculator

A Python-based GUI application developed for Eduvos to calculate and visualize student grades per module. This tool helps students and educators compute **weighted final grades** based on assessment types and ensures data integrity through validation and unit testing.

---

## Project Overview

**Project Title**: Eduvos Student Grade Calculator  
**Goal**: Provide an easy-to-use interface for calculating student grades per module using weighted assessments.  
**Target Audience**: Eduvos students and educators needing accurate, transparent grade calculations.

---

## Assessment Weighting

The following assessment components contribute to the final grade:

| Assessment Type | Weight (%) |
|-----------------|------------|
| Quiz            | 10%        |
| Project         | 20%        |
| Final Exam      | 50%        |
| Practical Exam  | 20%        |

---

## Key Features

- **CSV File Upload** – Import student grades with a single click
- **Data Validation** – Detects missing columns or incomplete data
- **Automatic Grade Calculation** – Uses exact weightings to compute overall scores
- **Multithreaded Processing** – Improves performance for large datasets
- **GUI Interface** – Clean `tkinter` interface with buttons and text areas
- **Unit Testing** – Validates grade logic and catches missing/incomplete input
- **Error Handling** – Friendly popups for invalid or missing inputs

---

## How to Run the Application

1. **Install Python 3** (if not already installed)
2. Clone or download this repo
3. Ensure your CSV file follows this structure:

```csv
Module Name,Quiz,Project,Final Exam,Practical
Mathematics for Programming,80,90,85,95
Python Programming,70,85,80,90
