# DocJur SRP/ARP Municipal

Ferramenta vertical para geração de minuta SRP/ARP municipal ancorada no template-mestre **ARP_Modelo - VF_final**, com frontend web, API FastAPI e persistência SQLite.

## Stack
- Frontend: React + Vite (código em `app/frontend`)
- Backend: FastAPI
- Banco: SQLite
- Exportação: DOCX, PDF e JSON
- Orquestração: Docker Compose

## Execução local
```bash
cd docjur_srp_real
docker compose up --build
```

A aplicação ficará disponível em `http://localhost:8000`.

## Rotas principais
- `GET /` interface web
- `GET /health`
- `POST /projects`
- `GET /projects/{id}`
- Endpoints de território, estratégia, itens, qualificação, requisitos técnicos, POC, anti-glosa, compilação, validação e exportação.

## Premissas implementadas
- Estrutura documental fixa com Edital + Anexos I a XI.
- Sem fonte, sem número (territorial/epidemiológico).
- Valores em formato BRL (`R$ 1.234,56`).
- Simulação estratégica assistencial/estruturante/territorial com sugestão automática e seleção final do usuário.
- POC objetiva eliminatória.
- Matriz anti-glosa robusta.
- Validador de publicabilidade.
