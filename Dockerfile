FROM python
COPY . /app
WORKDIR /app
EXPOSE 8777
RUN pip install -r requirements.txt
CMD ["python","MainScores.py"]