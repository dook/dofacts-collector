FROM python:3.8-slim AS collector_builder

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app
RUN pip install --upgrade pip && pip install pip-tools
COPY ./requirements/prod.txt ./requirements/
RUN pip-sync ./requirements/prod.txt


FROM python:3.8-slim AS collector_prod

COPY --from=collector_builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app
COPY . ./
RUN chmod -R +x ./scripts

CMD ./scripts/run.sh


FROM collector_builder AS collector_dev

COPY ./requirements ./requirements/
RUN pip-sync ./requirements/prod.txt ./requirements/dev.txt

COPY . ./
RUN chmod -R +x ./scripts
EXPOSE 8000

CMD ./scripts/run-dev.sh
