# YOLO性能比較

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
  * [ここ](https://developer.nvidia.com/cuda-toolkit-archive)からCUDA12.6をダウンロードし，インストールする．
* Python3.12のインストール
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
* CUDAのインストール
  * [ここ](https://developer.nvidia.com/cuda-toolkit-archive)からCUDA12.6を手順に従い，インストールする．

* 古いドライバーを削除する．
```bash
sudo apt --purge remove nvidia-*
```

* NVIDIAドライバのインストール
  * Nouveauの無効化
  ```bash
  sudo gedit /etc/modprobe.d/blacklist-nouveau.conf
  ```
  で，以下を保存する．
  ```txt
  blacklist nouveau
  options nouveau modeset=0
  ```
  以下を実行する．
  ```bash
  sudo update-initramfs -u
  ```
  * 推奨ドライバを確認する．recommendedのものを選択する．
  ```bash
  ubuntu-drivers devices
  ```
  * aptからインストール．XXXは推奨ドライバに置き換える．
  ```bash
  sudo add-apt-repository ppa:graphics-drivers/ppa
  sudo apt update
  sudo apt install nvidia-driver-XXX
  ```
  * 再起動
  * 確認
  ```bash
  nvidia-smi
  ```
  * [参考資料](https://qiita.com/porizou1/items/74d8264d6381ee2941bd)

* Pythonのインストール
  ```bash
  sudo apt install python3-pip
  ```

* 仮想環境作成
  ```bash
  python3 -m venv ../venv/yolo11
  source ../venv/yolo11/bin/activate
  ```

* パッケージのインストール
  ```bash
  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
  pip3 install ultralytics
  ```
* 確認
  ```bash
  python3 check_gpu.py
  ```

## 実行
 
* プログラムを実行する．
```bash
python3 eval_pose.py
```

## 実行結果(YOLOv8)

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
| Ubuntu | LEVELINF | RTX2070 | 86 |
| Win11 | Katana | RTX4070 | 75 |

## 実行結果(YOLO11+CUDA12.6)

| OS | PC | GPU | Time (sec) |
| ---- | ---- | ---- | ---- |
| Win11 | LEVELINF | RTX2070 | 125 |
| Ubuntu | LEVELINF | RTX2070 | 84 |
| Win11 | Corei9 | RTX3070 | 87 |
| Win11 | Katana | RTX4070 | 66 |
| Win11 | DAIV | RTX4090 | 52 |

## 開発者
 
* 作成者：北村泰彦
* 所属：関西学院大学工学部情報工学課程
* E-mail：ykitamura@kwansei.ac.jp
 
