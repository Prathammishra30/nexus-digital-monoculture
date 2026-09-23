# Frontend Dockerfile Skeleton for NEXUS
FROM node:20-alpine

WORKDIR /app

COPY package.json ./
# Run install if package.json has dependencies defined
RUN if [ -f package.json ]; then npm install || true; fi

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
