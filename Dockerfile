FROM python:3.11-bullseye

ARG ARTIFACT_FEED_ACCESS_TOKEN

WORKDIR /app

# https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15&tabs=debian18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline#18
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc \
    && curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && apt-get install -y unixodbc=2.3.11-1 \
    && ACCEPT_EULA=Y apt install -y msodbcsql18=18.3.2.1-1

COPY requirements.txt .
RUN pip install --no-cache-dir --extra-index-url "https://$ARTIFACT_FEED_ACCESS_TOKEN@pkgs.dev.azure.com/unirnet/_packaging/Architecture/pypi/simple/" --requirement requirements.txt

COPY src .
RUN python -m compileall .

RUN adduser nonroot && chown -R nonroot .
USER nonroot

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]