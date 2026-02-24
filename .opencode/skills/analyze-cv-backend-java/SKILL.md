---
name: analyze-cv-backend-java
description: DEBE usarse para analizar CVs de desarrolladores Backend Java. Evalúa la experiencia técnica contra requisitos definidos y clasifica cada requisito como Cumple, Cumple parcialmente o No cumple. No debe inferir experiencia no declarada.
metadata:
  author: tu-org-o-nombre
  version: "1.0.0"
---

Analiza el texto completo de un CV y determina si el perfil cumple con los requisitos técnicos para un rol Backend Java.

---

## Reglas generales de evaluación

- Debes analizar el CV completo.
- Debes basarte únicamente en tecnologías explícitamente mencionadas.
- No debes asumir ni inferir experiencia no declarada.
- Si una tecnología se menciona sin versión y el requisito lo indica, clasifica como **Cumple parcialmente**.
- Cuando no haya información suficiente, clasifica como **No cumple**.
- El resultado debe ser consistente y explicable.

---

## Clasificación permitida

Usa únicamente los siguientes valores:

- Cumple  
- Cumple parcialmente  
- No cumple  

No utilices sinónimos ni variaciones.

---

## Requisitos técnicos

### Req 1: Java y Spring Boot

**Cumple**
- Experiencia explícita con **Java 11 y Spring Boot 2**
- O experiencia con **Java 17** y/o **Spring Boot 3**

**Cumple parcialmente**
- Menciona **Java** o **Spring Boot** sin indicar versión

**No cumple**
- No menciona Java ni Spring Boot

---

### Req 2: APIs REST y seguridad básica

**Cumple**
- Desarrollo de **API REST**, **RESTful**, **REST**
- O conocimiento de seguridad básica: **TLS**, **tokens**, **JWT**, **OAuth**

**No cumple**
- No menciona APIs REST ni conceptos de seguridad

---

### Req 3: Pruebas unitarias

**Cumple**
- Experiencia en **pruebas unitarias**
- Uso de **JUnit** y/o **Mockito**

**No cumple**
- No menciona pruebas unitarias

---

### Req 4: Bases de datos

**Cumple**
- Uso de **MongoDB**
- Uso de **PostgreSQL**

**Cumple parcialmente**
- Uso de **MySQL**
- **Oracle**
- **SQL Server**

**No cumple**
- No menciona bases de datos

---

### Req 5: Herramientas y CI/CD

**Cumple**
- Menciona explícitamente el uso de **Postman**
- Y uso básico de **Docker**
- Y comprensión o uso de **pipelines CI/CD**

Debe mencionarse **todas** las herramientas y conceptos anteriores.

**Cumple parcialmente**
- Menciona **al menos una**, pero **no todas**, de las siguientes:
  - Postman
  - Docker
  - CI/CD o pipelines

**No cumple**
- No menciona herramientas ni conceptos de CI/CD

---

### Req 6: Mensajería

**Cumple**
- Menciona explícitamente **RabbitMQ**
- Y **Kafka**
- Y/o experiencia clara con **otros sistemas de mensajería**

Debe evidenciar **experiencia completa en mensajería**, incluyendo
al menos **RabbitMQ y Kafka** o un conjunto equivalente claramente especificado.

**Cumple parcialmente**
- Menciona **solo uno** de los siguientes:
  - RabbitMQ
  - Kafka
  - Otro sistema de mensajería

**No cumple**
- No menciona sistemas de mensajería

---

## Ventajas adicionales (booleanas)

Las ventajas adicionales deben marcarse solo como **true** o **false**.

---

### VA 1: Kafka avanzado

Marcar como **true** si menciona:
- Kafka
- Kafka Connect
- KSQL

---

### VA 2: Arquitectura distribuida

Marcar como **true** si menciona:
- Microservicios
- Microservices
- Microservicios distribuidos
- Logging
- Trazabilidad
- Observabilidad
- Tracing

---

### VA 3: Metodologías ágiles

Marcar como **true** si menciona:
- Agile
- Scrum
- Kanban

---

## Formato de salida esperado

El resultado debe ser estructurado e incluir:

- Cada requisito (Req1 a Req6) con su clasificación
- Una breve justificación basada en el texto del CV
- Las ventajas adicionales marcadas como true o false
