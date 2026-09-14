# --- Estágio 1: Build ---
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./

# Substituído npm ci por npm install
RUN npm install

COPY . .


# --- Estágio 2: Imagem de Produção ---
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

# Substituído npm ci por npm install
RUN npm install --only=production

COPY --from=builder /app/server.js ./server.js

USER node

EXPOSE 3000

CMD ["node", "server.js"]