FROM python:alpine

RUN pip install --no-cache-dir pyotp

WORKDIR /2FA

COPY 2FA.py 2FA.py

ENTRYPOINT ["python","2FA.py"]
