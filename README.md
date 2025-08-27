# Kubernetes Microservices Example

This project is a simple example of a microservices architecture deployed with Kubernetes. It consists of three services: a gateway, a payment service, and a documents service.

## Microservices

### Gateway Service

The Gateway service is the single entry point for all client requests. It is responsible for:

-   Authenticating users.
-   Routing requests to the appropriate microservice (`payment` or `documents`).
-   Service discovery, using environment variables to find the other services.

### Payment Service

The Payment service is responsible for processing payments. It has a single endpoint `/pay` that accepts POST requests.

### Documents Service

The Documents service is responsible for processing documents. It has a single endpoint `/documents` that accepts POST requests.

## Getting Started

To run this project, you will need to have Docker and Kubernetes installed.

1.  **Build the Docker images** for each service.
2.  **Apply the Kubernetes deployments** for each service.
3.  **Port-forward the gateway service** to access it from your local machine.
