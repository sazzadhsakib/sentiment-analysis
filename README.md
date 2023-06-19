# sentiment-analysis

https://huggingface.co/StatsGary/setfit-ft-sentinent-eval

## Docker Setup & Run

```shell
# If you have a GPU
docker-compose -f docker-compose.prod.gpu.yml up --build -d
# Otherwise
docker-compose -f docker-compose.prod.cpu.yml up --build -d
```

## Setup & Run (non docker)

Prepare Setfit preloaded models


1. Copy contents of [models in drive](https://drive.google.com/drive/folders/1DGUiY0_xV9ZKa7BKBjaEMi0-KTChdcMe\?usp\=sharing) to [src/rnd/models](src/rnd/models) folder

Install project dependencies:

```shell
sudo apt update
sudo apt install python3.8-dev
sudo apt-get install -y python3-venv
python3.8 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

```shell
uvicorn wsgi:app --host 0.0.0.0 --port 8000
```