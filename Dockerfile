FROM python:3.11-buster

WORKDIR /app

ENV PATH=/opt/poetry/bin:$PATH

ENV POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install poetry

COPY . .

RUN poetry config virtualenvs.in-project true && \
    poetry install --without dev && rm -rf $POETRY_CACHE_DIR

CMD ["/app/.venv/bin/streamlit", "run", "ecomm_agent/streamlit_app.py", "--server.headless","true"]
