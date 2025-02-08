FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

WORKDIR /

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps chromium

ENV WEBSITE_URL=https://www.amazon.com/

CMD ["pytest", "tests"]
