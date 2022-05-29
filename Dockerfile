FROM teamvaders/jmthon:latest

RUN git clone https://github.com/RR77R/jmthon.git /root/jmthon

WORKDIR /root/jmthon

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/jmthon/bin:$PATH"

CMD ["python3", "-m", "jmthon"]
