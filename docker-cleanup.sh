#!/bin/bash
echo "🔹 Cleaning up unused Docker resources..."
docker system prune -af
docker volume prune -f
