# chem-7870-epr_svd_tool

# EPR SVD Tool

A Python package for loading, preprocessing, denoising, and visualizing kinetic EPR spectra using singular value decomposition (SVD).

## Purpose

Kinetic EPR data often contains weak radical signals and baseline drift noise. This package organizes EPR spectra into a field-by-scan matrix, applies baseline correction and normalization, and uses SVD to extract dominant kinetic components while reducing noise.

## Installation

```bash
pip install -e .
