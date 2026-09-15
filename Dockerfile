FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip uninstall -y streamlit && pip install --no-cache-dir streamlit==1.62.0

COPY . .

CMD ["streamlit", "run", "app.py"]