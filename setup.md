#   環境設定マニュアル
Last updated: 2024/02/14 13:14:03

* labアカウントの設定
* Windows Updateの実行
* NVIDIAドライバのインストール
  * [ここ](https://www.nvidia.co.jp/Download/index.aspx?lang=jp)からGPUに対応する最新のNVIDIAドライバをダウンロードし，インストールする．
* CUDAのインストール
  * [ここ](https://developer.nvidia.com/cuda-toolkit-archive)からCUDA Toolkit 12.2をダウンロードし，インストールする．
* Minicondaのインストール
   * [ここ](https://docs.anaconda.com/free/miniconda/)からMinicondaをダウンロードし，インストールする．
   * Anaconda Promptで以下を実行する．
     * conda init powershell

* prepare.batの実行
* pytorch.batの実行
* check_gpu.pyの実行