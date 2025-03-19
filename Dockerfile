FROM python:3.12-alpine
RUN addgroup -S sandbox && adduser -S -G sandbox sandbox
USER sandbox
WORKDIR /sandbox
CMD ["python", "/sandbox/tester.py", "/sandbox/repo"]
