# Sentimientos App – MVP Serverless

Servicio SaaS para empresas que recolecta y analiza menciones públicas en redes sociales (X, YouTube, Instagram), determina su sentimiento (positivo, neutro, negativo) y entrega dashboards de métricas en tiempo real. Arquitectura serverless, escalable y segura, con planes Free/Premium según volumen de datos.

**Stack:**
- Frontend: Next.js (React, TypeScript, Tailwind, Chart.js, Recharts, Firebase Auth)
- Backend: FastAPI (Python 3.11, Uvicorn, Tweepy, Requests)
- Procesamiento: Google Cloud Functions, Google Cloud Natural Language API
- Almacenamiento: Firestore, BigQuery (opcional)
- Visualización: Looker Studio, React Charts
- DevOps: GitHub Actions, Google IAM

**Estructura:**
- `backend/`: API y lógica de negocio
- `frontend/`: SPA Next.js
- `scripts/`: CI/CD y utilidades

---

# Instrucciones rápidas

1. Clona el repositorio y entra a la carpeta `sentimientos-app`.
2. Instala dependencias en backend y frontend.
3. Levanta ambos servidores de desarrollo:
   - Backend: `uvicorn main:app --reload`
   - Frontend: `npm run dev`
4. Configura tus variables de entorno en `.env` y `.env.local`.


