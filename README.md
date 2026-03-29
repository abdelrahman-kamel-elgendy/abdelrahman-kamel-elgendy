<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,40:1e1b4b,100:24243e&height=220&section=header&text=Abdelrahman%20Kamel&fontSize=56&fontColor=ffffff&fontAlignY=40&desc=Backend%20Developer&descAlignY=62&descSize=25&animation=fadeIn"/>
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2800&pause=800&color=A78BFA&center=true&vCenter=true&width=650&lines=Building+robust+backend+systems;Crafting+clean+%26+scalable+APIs;Always+learning%2C+always+shipping;Coffee+%2B+Code+%3D+Production+Ready" alt="Typing SVG" />
</div>

---

<!-- ── THEME: REST API response ─────────────────────────── -->
## `GET /api/whoiam`

```json
{
    "status": 200,
    "data": {
        "name": "Abdelrahman Kamel",
        "title": "Backend Developer",
        "location": "Egypt 🇪🇬  [UTC+2]",
        "uptime": "available 24/7 for cool projects",
        "core_skills": [
            "RESTful & GraphQL API Design",
            "Microservices & Event-Driven Architecture",
            "Database Modeling & Query Optimization",
            "Auth Systems  (JWT · OAuth2 · Sessions)"
        ],
        "currently": {
            "building": "Scalable backend systems",
            "learning": [
                "System Design patterns",
                "AWS Cloud"
            ],
            "focus_on": [
                "REST APIs",
                "Microservices",
                "System Design"
            ],
            "open_to": "Exciting backend opportunities"
        },
        "config": {
            "coffee_dependency": true,
            "favourite_http": 418,
            "debug_strategy": "console.log first, ask questions later...",
            "principle": "Write code humans can read, machines can run, and future-you won't curse."
        }
    }
}
```

---

<!-- ── THEME: YAML config ───────────────────────────────── -->
## `stack.yml`
 
<div align="center">
<table width="80%">
<tr>
<td valign="middle" width="50%">
 
```yaml
developer:
  name: Abdelrahman Kamel
  title: Backend Developer
  status: production-ready

stack:
  languages:
    - C#
    - Java
    - JavaScript
    - TypeScript
    - Python

  frameworks_and_runtimes:
    - .NET
    - Spring
    - NodeJS
    - NestJS

  databases_and_orms:
    - MySQL
    - MongoDB
    - Redis
    - Prisma

  devops_and_tools:
    - Docker
    - Git
    - GitHub
    - Postman
```
 
</td>
<td valign="middle" width="50%">
<div align="center">
 
**Languages**
 
<img src="https://skillicons.dev/icons?i=cs,java,js,ts,py&theme=dark" />
 
<br/><br/>
 
**Frameworks & Runtimes**
 
<img src="https://skillicons.dev/icons?i=dotnet,spring,nodejs,nestjs&theme=dark" />
 
<br/><br/>
 
**Databases & ORMs**
 
<img src="https://skillicons.dev/icons?i=mysql,mongodb,redis,prisma&theme=dark" />
 
<br/><br/>
 
**DevOps & Tools**
 
<img src="https://skillicons.dev/icons?i=docker,git,github,postman&theme=dark" />
 
</div>
</td>
</tr>
</table>
</div>

---

<!-- ── THEME: SQL query ────────────────────────────────── -->
## `metrics.sql`

<table width="100%">
<tr>
<td valign="top" width="50%">

```sql
-- ──────────────────────────────────
--  Querying developer stats
--  from github.db
-- ──────────────────────────────────
SELECT
    total_commits,
    pull_requests,
    repositories,
    current_streak,
    longest_streak,
    top_languages
FROM
    github_stats
WHERE
    username = 'abdelrahman-kamel-elgendy'
    AND year = YEAR (CURDATE ())
ORDER BY
    contributions DESC;

-- ── Result ─────────────────────────
-- rows returned : 1
-- execution time: 0.003s
-- status        : 200 OK
-- cache         : HIT
-- ──────────────────────────────────

-- ── Indexes used ───────────────────
-- idx_username  (seek)
-- idx_year      (seek)
-- idx_contributions (sort)
-- ──────────────────────────────────
```
</td>
<td valign="top" width="60%">
<div align="center">
<!-- Stats auto-generated daily by GitHub Actions → .github/workflows/metrics.yml -->
<img width="100%" src="./assets/stats.svg" />
<img width="100%" src="./assets/streak.svg" />
<img width="100%" src="./assets/langs.svg" />
</div>
</td>
</tr>
</table>

---

<!-- ── THEME: Redis CLI ────────────────────────────────── -->
## `CMD`

```redis
127.0.0.1:6379> KEYS activity:*
1) "activity:contribution_graph"
2) "activity:streak"
3) "activity:last_commit"

127.0.0.1:6379> GET activity:contribution_graph
# ── rendering below ───────────────────────────
```

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=abdelrahman-kamel-elgendy&bg_color=0D1117&color=A78BFA&line=A78BFA&point=ffffff&area=true&hide_border=true" width="100%"/>
</div>

---

<!-- ── THEME: Application log ─────────────────────────── -->
## `daily-backend-tip.log`
 
<!-- TIP_START -->
```log
[2026-03-29 19:30:33.721 +02:00 INF] tip-service Fetching tip of the day...
[2026-03-29 19:30:33.721 +02:00 INF] tip-service Source: tips.json  offset: day_of_year % 365
[2026-03-29 19:30:33.721 +02:00 INF] tip-service Status: OK  →  tip loaded
─────────────────────────────────────────────────────────────────
[2026-03-29 19:30:33.721 +02:00 TIP] tip-service Use a schema registry when working with Kafka to version and validate message schemas.
─────────────────────────────────────────────────────────────────
```
<!-- TIP_END -->
 
---
 
<!-- ── THEME: Application log ─────────────────────────── -->
## `daily-quote.log`
 
<!-- QUOTE_START -->
```log
[2026-03-29 19:30:33.721 +02:00 INF] quote-service Connecting to quotes upstream...
[2026-03-29 19:30:33.721 +02:00 INF] quote-service GET https://zenquotes.io/api/today  →  200 OK
[2026-03-29 19:30:33.721 +02:00 INF] quote-service Message received  →  quote loaded
─────────────────────────────────────────────────────────────────
[2026-03-29 19:30:33.721 +02:00 QOT] quote-service Spend eighty percent of your time focusing on the opportunities of tomorrow rather than the problems of yesterday.
[2026-03-29 19:30:33.721 +02:00 AUT] quote-service Brian Tracy
─────────────────────────────────────────────────────────────────
```
<!-- QUOTE_END -->

---

<!-- ── THEME: TCP handshake ───────────────────────────── -->
## `POST /api/connect`

<div align="center">
<a href="mailto:abdelrahman.kamel.elgendy@gmail.com">
  <img src="https://img.shields.io/badge/Drop%20me%20an%20email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>
&nbsp;
<a href="https://www.linkedin.com/in/abdelrahman-kamel-elgendy/">
  <img src="https://img.shields.io/badge/Connect%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<br/>

> *The best backend is the one nobody notices until it's gone ;)*
</div>