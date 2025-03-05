# YOLOインストールと性能比較

## 機能
 
YOLOのインストールと性能比較を行うための資料

## 前提

* CUDA12.6
* Python3.12
  
## インストール(Windows11)
  
* gitのインストール
  * `git -v`で確認する．インストールされていなければ以下を実行する．
  * [ここ](https://git-scm.com/)からダウンロードし，インストールする．
* リポジトリをクローンする．
  ```bash
  git clone https://github.com/kitamura-lab/yolov8-eval.git
  ```
* NVIDIAドライバのインストール
  * [ここ](https://www.nvidia.co.jp/Download/index.aspx?lang=jp)からGPUに対応する最新のNVIDIAドライバをダウンロードし，インストールする．
* CUDAのインストール
  * `nvcc -V`で確認する．インストールされていなければ，以下を実行する．
  * [ここ](https://developer.nvidia.com/cuda-toolkit-archive)からCUDA12.6をダウンロードし，インストールする．
* Minicondaのインストール
  * `conda -V`で確認する．インストールされていなければ，以下を実行する．
  * [ここ](https://www.anaconda.com/download/success)からダウンロードし，インストールする．
  * Anaconda Promptで`conda init powershell`を実行する．
* 仮想環境の作成
  ```bash
  conda create -n yolo python=3.12
  conda activate yolo
  ```
* パッケージのインストール
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
  pip install ultralytics
  ```
* 確認
  ```bash
  python check_gpu.py
  ```
  * Trueが表示されればインストールが成功．

## インストール(Ubuntu 22.04)

* gitのインストール
  * `git --version`で確認する．インストールされていなければ以下を実行する．
  ```bash
  sudo apt install git
  ```

* リポジトリをクローンする．
  ```bash
  git clone https://github.com/kitamura-lab/yolov8-eval.git
  ```
* CUDAのインストール
  * `nvcc -V`で確認する．インストールされていなければ，以下を実行する．
  * [ここ](https://developer.nvidia.com/cuda-toolkit-archive)からCUDA12.6を手順に従い，インストールする．
  * 以下を~/.bashrcに追加する．
  ```bash
  export PATH=/usr/local/cuda/bin:$PATH
  export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
  ```

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
  * aptでインストール．XXXは推奨ドライバに置き換える．
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

* Minicondaのインストール
  * `conda -V`で確認する．インストールされていなければ，以下を実行する．
  * [ここ](https://www.anaconda.com/download/success)からダウンロードし，以下を実行する．
  ```bash
  bash Miniconda3-latest-Linux-x86_64.sh
  ```
   * 最後の質問にはyesとする．

* 仮想環境の作成
  ```bash
  conda create -n yolo python=3.12
  conda activate yolo
  ```

* パッケージのインストール
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
  pip install ultralytics
  ```

* 確認
  ```bash
  python check_gpu.py
  ```
  * Trueが表示されればインストールが成功．


## 性能比較
 
プログラムを実行する．
```bash
python eval_pose.py
```

### 実行結果(YOLO11+CUDA12.6)

| OS | PC | GPU | Time (sec) |
| ---- | ---- | ---- | ---- |
| Win11 | LEVELINF | RTX2070 | 125 |
| Ubuntu | LEVELINF | RTX2070 | 84 |
| Win11 | MSI | RTX3060 |98 |
| Win11 | GTUNE | RTX3070 |  89 |
| Win11 | Corei9 | RTX3070 | 87 |
| Ubuntu | Corei9 | RTX3070 | 56 |
| Win11 | ALIENWARE | RTX4060 | 87 |
| Ubuntu | ALIENWARE | RTX4060 | 71 |
| Win11 | GTUNE | RTX4060 |  74 |
| Win11 | Katana | RTX4070 | 59 |
| Win11 | Sword | RTX4070 | 64 |
| Win11 | DAIV | RTX4090 | 52 |

### 実行結果(YOLOv8+CUDA12.1)

| OS | PC | GPU | Time (sec) |
| ---- | ---- | ---- | ---- |
| Win11 | SurfaceBook3 | CPU | 3131 |
| Win11 | SurfaceBook3 | RTX3000 | 224 |
| Win11 | LEVELINF | RTX2070 | 115 |
| Ubuntu | LEVELINF | RTX2070 | 86 |
| Win11 | MSI | RTX3060 |100 |
| Win11 | Endeavor | RTX3060 | 90 |
| Win11 | Corei9 | RTX3070 | 86 |
| WSL | Corei9  |  RTX3070 | 87 |
| Ubuntu | Corei9 | RTX3070 | 60 |
| Win11 | ALIENWARE | RTX4060 | 93 |
| Win11 | GTUNE | RTX4060 |  84 |
| Win11 | Katana | RTX4070 | 75 |

## 開発者
 
* 作成者：北村泰彦
* 所属：関西学院大学工学部情報工学課程
* E-mail：ykitamura@kwansei.ac.jp
 
