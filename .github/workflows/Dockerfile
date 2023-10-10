name: Build Docker Image

on:
  push:
    branches:
      - master
      - translator

jobs:
  build_image:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Build Docker Image
        run: |
          docker build -t your-image-name:latest .
