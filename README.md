# weekend-app03

Small Python service used to demonstrate secret injection without returning secret material.

## Test and run

```sh
python3 -m unittest discover -s tests -v
hadolint Dockerfile
podman build -t weekend-app03:dev .
podman run --rm -p 8080:8080 -e API_KEY=local-only weekend-app03:dev
curl --fail http://localhost:8080/healthz
```

Commits to `main` publish `ghcr.io/phelun/weekend-app03:<full-git-sha>`. Pull requests test, lint, build, and scan without publishing. Never commit a real `API_KEY`.
