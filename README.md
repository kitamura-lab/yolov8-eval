# YOLOv8性能比較

## 機能
 
* PCやOSごとにYOLOv8の性能比較を行う．
  
## インストール(Windows11)
  
* gitのインストール
  * [ここ](https://git-scm.com/)からダウンロードし，インストールする．
* リポジトリをクローンする．
```bash
git clone https://github.com/kitamura-lab/yolov8-eval.git
```
* NVIDIAドライバのインストール
  * [ここ](https://www.nvidia.co.jp/Download/index.aspx?lang=jp)からGPUに対応する最新のNVIDIAドライバをダウンロードし，インストールする．
* CUDAのインストール
  * [ここ](https://developer.nvidia.com/cuda-toolkit-archive)からCUDA12.1をダウンロードし，インストールする．
* Pythonのインストール
* pytorch-gpu.batの実行
  * 最後にTrueが表示されれば環境設定が終了．

## インストール(Ubuntu)

* gitのインストール
```bash
sudo apt install git
```

* リポジトリをクローンする．
```bash
git clone https://github.com/kitamura-lab/yolov8-eval.git
```
  * アクセスにはユーザ名とPersonal Access Tokenが必要である．
* NVIDIAドライバのインストール
  * [参考資料](https://qiita.com/porizou1/items/74d8264d6381ee2941bd)
* CUDAのインストール
  * [ここ](https://developer.nvidia.com/cuda-toolkit-archive)からCUDA12.1をダウンロードし，インストールする．
* Pythonのインストール
* pytorch-gpu.batの実行
  * 最後にTrueが表示されれば環境設定が終了．

## 実行
 
* プログラムを実行する．
```bash
python eval_pose.py
```

## 実行結果

| OS | PC | GPU | Time (sec) |
| ---- | ---- | ---- | ---- |
| Win11 | SurfaceBook3 | RTX3000 | 224 |
| Win11 | SurfaceBook3 | CPU | 3131 |
| Ubuntu | Corei9 | RTX3070 | 60 |
| Win11 | Corei9 | RTX3070 | 86 |
| WSL | Corei9  |  RTX3070 | 87 |
| Win11 | GTUNE | RTX4060 |  84 |
| Win11 | ALIENWARE | RTX4060 | 93 |
| Win11 | MSI | RTX3060 |100 |
| Win11 | Endeavor | RTX3060 | 90 |
| Win11 | LEVELINF | RTX2070 | 115 |
| Win11 | Katana | RTX4070 | 75 |


## 開発者
 
* 作成者：北村泰彦
* 所属：関西学院大学工学部情報工学課程
* E-mail：ykitamura@kwansei.ac.jp
 
