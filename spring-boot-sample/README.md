# Spring Boot Monitoring and Redis Caching Sample

This sample demonstrates a Spring Boot microservice with Redis caching and Prometheus/Grafana observability.

## Features

- Spring Boot REST endpoint for caching values in Redis.
- Redis cache configuration with `LettuceConnectionFactory`.
- Actuator metrics exposed via `/actuator/prometheus`.
- Application settings for observability and monitoring.

## Run

1. Start Redis locally on port `6379`.
2. Build and run with Maven:

```bash
mvn clean package spring-boot:run
```

3. Use the sample endpoints:

- `POST /api/cache/{key}` with raw text body to cache a value.
- `GET /api/cache/{key}` to retrieve a value.

4. Access Prometheus metrics at:

- `http://localhost:8080/actuator/prometheus`

## Monitoring integration

- `prometheus.yml` includes a scrape configuration for the Spring Boot app.
- `grafana-dashboard.json` provides a starter dashboard outline for key metrics.

## Notes

This skeleton is intended as a reference for the agentic POC and is not production hardened.
