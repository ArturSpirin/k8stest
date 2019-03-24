FROM python:2

WORKDIR /home/pi/k8stest

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/Main.py"]
