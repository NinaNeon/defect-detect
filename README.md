# Defect Detection (defect-detect)

This project provides defect detection datasets along with their corresponding usage information.

# IMDD-1M: Towards Open-Vocabulary Industrial Defect Understanding

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository provides the **IMDD-1M** dataset 
---

## Dataset Overview

| Statistic | Value |
|-----------|-------|
| Total image-text pairs | 1,240,000+ |
| Industrial domains | 63 |
| Defect types | 421 |
| Annotation format | Image + CSV/JSON per domain |
| License | CC BY 4.0 |

---

## Quick Start

```bash
pip install gdown tqdm pillow pandas

# Download all domains
python prepare_dataset.py --output_dir ./data

# Download a single domain
python prepare_dataset.py --output_dir ./data --domain 266_353mvtec

# Verify existing downloads only
python prepare_dataset.py --output_dir ./data --verify_only
```



## Applicable to Classes 0–4: Aircraft Defect Detection

### Dataset Download

[Click here to download the Class 0–4 aircraft defect image dataset](https://drive.google.com/drive/folders/1Yzwp9QXh8pytgxvJWcKrW4gvRvwVQDxa?usp=drive_link)

### Data File

[Click here to download the Class 0–4 aircraft defect data file: 0-4aircraft4000.csv](https://github.com/NinaNeon/defect-detect/blob/5677959e66bba4c8f3b6c05b95515a3e6fcdca3e/0-4aircraft4000/0-4aircraft4000.csv)

---

## Applicable to Classes 5–10: MT Tile Defect Dataset

### Dataset Download

[Click here to download the Class 5–10 MT tile defect image dataset](https://drive.google.com/file/d/1Ojy6wHdz7RnIUIV6PNhz2c02Eruttg0j/view?usp=drive_link)

### Data File

[Click here to download the Class 5–10 MT tile defect data file: 5-10MT_Tiles.csv](https://github.com/NinaNeon/defect-detect/blob/b2bfb208f62917d0e1a2f904060d5c68a85ba5b1/5-10MT_tiles/5-10MT_Tiles.csv)

---

## Applicable to Classes 11–19: NEU-DET Detection

### Dataset Download

[Click here to download the Class 11–19 NEU-DET image dataset](https://drive.google.com/file/d/1CuMvi_VUqcywiMFDSEY8lbxSdbtUQ4Kr/view?usp=drive_link)

### Data File

[Click here to download the Class 11–19 NEU-DET data file: 11-19NEU-DET1816.csv](https://github.com/NinaNeon/defect-detect/blob/fed407f8e3b6fc27dbb89cdb692618e32a56dc8a/11-19NEU-DET/11-19NEU-DET1816.csv)

---

## Applicable to Classes 20–24: Wall Defect Detection

### Dataset Download

[Click here to download the Class 20–24 wall defect image dataset](https://drive.google.com/file/d/1ypZCvyC9hCKZ0Lm7ptBVs28_G6drEtMr/view?usp=drive_link)

### Data File

[Click here to download the Class 20–24 wall defect data file: 20-24wall1032.csv](https://github.com/NinaNeon/defect-detect/blob/1d6b14d680ee74bf220aa5078d56ef654320b781/20-24wall1000/20-24wall1032.csv)

---

## Applicable to Classes 25–30: OLED Defect Detection

### Dataset Download

[Click here to download the Class 25–30 OLED defect image dataset](https://drive.google.com/file/d/1Dh6lBKL6BkPWJcGU_DNeSI1AsJ10llqu/view?usp=drive_link)

### Data File

[Click here to download the Class 25–30 OLED defect data file: 25-30OLED.csv](https://github.com/NinaNeon/defect-detect/blob/69e7339b7220793d28fe831a83c692bb364f8b5a/25-30OLED/25-30OLED.csv)

---

## Applicable to Classes 31–38: Solar Cell Defect Detection

### Dataset Download

[Click here to download the Class 31–38 solar cell defect image dataset](https://drive.google.com/drive/folders/1mG6UydqG8asd9u5EnpuT20y5npIOPXHu?usp=drive_link)

### Data File

[Click here to download the Class 31–38 solar cell defect data file: 31-38SOLARCELL.csv](https://github.com/NinaNeon/defect-detect/blob/0afdb3767010ec4701a854aa1d5e0dec33a34466/31-38solarcell/31-38SOLARCELL.csv)

---

## Applicable to Classes 39–258: Fabric Defect Detection

### Dataset Download

[Click here to download the Class 39–258 fabric defect image dataset](https://drive.google.com/drive/folders/1fLXox6uaKebbOxWtQjRKV_C2sEg9ZZXY?usp=drive_link)

### Data File

[Click here to download the Class 39–258 fabric defect data file: 39-258fabric.csv](https://github.com/NinaNeon/defect-detect/blob/e34f02ef6228d9585566f567bd82ce8952d0c3ac/39-258fabric/39-258fabric.csv)

---

## Applicable to Classes 259–265: Gear Defect Detection

### Dataset Download

[Click here to download the Class 259–265 gear defect image dataset](https://drive.google.com/drive/folders/1KweVPT4JqtEbu94O18_viISoF9wrdYqC?usp=drive_link)

### Data File

[Click here to download the Class 259–265 gear defect data file: 259-265gear.csv](https://github.com/NinaNeon/defect-detect/blob/4bc7a0563b5ee42cb691d33daf600c57fb0e6f44/259-265gear/259-265gear.csv)

---





# 缺陷檢測（defect-detect）

本項目提供了缺陷檢測數據集及使用方法。

## 適用於 0-4 類 aircraft 檢測
### 數據集下載

[點擊此處下載 0-4 類 aircraft 檢測圖片集](https://drive.google.com/drive/folders/1Yzwp9QXh8pytgxvJWcKrW4gvRvwVQDxa?usp=drive_link)

### 數據文件

[點擊此處下載 0-4 類 aircraft 檢測數據文件 0-4aircraft4000.csv](https://github.com/NinaNeon/defect-detect/blob/5677959e66bba4c8f3b6c05b95515a3e6fcdca3e/0-4aircraft4000/0-4aircraft4000.csv)

## 適用於 5-10 類 MT 磁磚缺陷數據
### 數據集下載

[點擊此處下載 5-10 類 MT 磁磚缺陷圖片數據集](https://drive.google.com/file/d/1Ojy6wHdz7RnIUIV6PNhz2c02Eruttg0j/view?usp=drive_link)

### 數據文件
[點擊此處下載 5-10 類 MT 磁磚缺陷數據文件.csv](https://github.com/NinaNeon/defect-detect/blob/b2bfb208f62917d0e1a2f904060d5c68a85ba5b1/5-10MT_tiles/5-10MT_Tiles.csv)

## 適用於 11-19 類 NEU-DET 檢測
### 數據集下載

[點擊此處下載 11-19 類 NEU-DET 檢測圖片數據集](https://drive.google.com/file/d/1CuMvi_VUqcywiMFDSEY8lbxSdbtUQ4Kr/view?usp=drive_link)

### 數據文件
[點擊此處下載 11-19 類 NEU-DET 檢測數據文件 11-19NEU-DET1816.csv](https://github.com/NinaNeon/defect-detect/blob/fed407f8e3b6fc27dbb89cdb692618e32a56dc8a/11-19NEU-DET/11-19NEU-DET1816.csv)

## 適用於 20-24 類 Wall 檢測
### 數據集下載

[點擊此處下載 20-24 類 Wall 檢測圖片數據集](https://drive.google.com/file/d/1ypZCvyC9hCKZ0Lm7ptBVs28_G6drEtMr/view?usp=drive_link)

### 數據文件
[點擊此處下載 20-24 類 Wall 檢測數據文件 20-24wall1032.csv](https://github.com/NinaNeon/defect-detect/blob/1d6b14d680ee74bf220aa5078d56ef654320b781/20-24wall1000/20-24wall1032.csv)

## 適用於 25-30 類 OLED 檢測
### 數據集下載

[點擊此處下載 25-30 類 OLED 檢測圖片數據集](https://drive.google.com/file/d/1Dh6lBKL6BkPWJcGU_DNeSI1AsJ10llqu/view?usp=drive_link)

### 數據文件
[點擊此處下載 25-30 類 OLED 檢測數據文件 25-30OLED.csv](https://github.com/NinaNeon/defect-detect/blob/69e7339b7220793d28fe831a83c692bb364f8b5a/25-30OLED/25-30OLED.csv)

## 適用於 31-38 類 Solar Cell 檢測
### 數據集下載

[點擊此處下載 31-38 類 Solar Cell 檢測圖片數據集](https://drive.google.com/drive/folders/1mG6UydqG8asd9u5EnpuT20y5npIOPXHu?usp=drive_link)

### 數據文件
[點擊此處下載 31-38 類 Solar Cell 檢測數據文件 31-38SOLARCELL.csv](https://github.com/NinaNeon/defect-detect/blob/0afdb3767010ec4701a854aa1d5e0dec33a34466/31-38solarcell/31-38SOLARCELL.csv)

## 適用於 39-258 類 Fabric 檢測
### 數據集下載

[點擊此處下載 39-258 類 Fabric 檢測圖片數據集](https://drive.google.com/drive/folders/1fLXox6uaKebbOxWtQjRKV_C2sEg9ZZXY?usp=drive_link)

### 數據文件
[點擊此處下載 39-258 類 Fabric 檢測數據文件 39-258fabric.csv](https://github.com/NinaNeon/defect-detect/blob/e34f02ef6228d9585566f567bd82ce8952d0c3ac/39-258fabric/39-258fabric.csv)

## 適用於 259-265 類 Gear 檢測
### 數據集下載

[點擊此處下載 259-265 類 Gear 檢測圖片數據集](https://drive.google.com/drive/folders/1KweVPT4JqtEbu94O18_viISoF9wrdYqC?usp=drive_link)

### 數據文件
[點擊此處下載 259-265 類 Gear 檢測數據文件 259-265gear.csv](https://github.com/NinaNeon/defect-detect/blob/4bc7a0563b5ee42cb691d33daf600c57fb0e6f44/259-265gear/259-265gear.csv)


