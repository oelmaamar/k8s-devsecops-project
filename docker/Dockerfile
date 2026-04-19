FROM python:3.10-slim

# Define application user and uid for security consistency with kubernetes
ENV APP_USER=flask
ENV APP_UID=10001

# Create a system group and user without a login shell for maximum security
RUN groupadd --system --gid ${APP_UID} ${APP_USER} && \
    useradd --system \
            --uid ${APP_UID} \
            --gid ${APP_USER} \
            --create-home \
            --shell /sbin/nologin \
            ${APP_USER}


# Set the working directory inside the container
WORKDIR /app


# copy requirements first

COPY --chown=${APP_USER}:${APP_USER} app/requirements.txt .

# Upgrade core tools to fix Trivy-detected CVEs and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application source code with correct ownership
COPY --chown=${APP_USER}:${APP_USER} app/app.py .

# Switch to the non-root user defined above
USER ${APP_UID}


EXPOSE 5000
# Production-ready entrypoint using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

