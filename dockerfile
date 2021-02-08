FROM python:3.8

WORKDIR /usr/src

# Copy dependencies definition
COPY src/poetry.lock src/pyproject.toml ./

# Install deps
RUN pip install 'poetry~=1.1.4' \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy source code
COPY ./src .

EXPOSE 8000

CMD hypercorn -w 4 -k uvloop -b 0.0.0.0:8000 app.main:app
