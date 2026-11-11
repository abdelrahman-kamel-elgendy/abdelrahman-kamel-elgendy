<div align="center">

  <img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:0f0c29,45:302b63,100:24243e&height=220&section=header&text=Abdelrahman%20Kamel%20Elgendy&fontSize=52&fontColor=ffffff&fontAlignY=42&desc=Full%20Stack%20Developer&descAlignY=64&descSize=26&descColor=A78BFA&stroke=7C3AED&strokeWidth=1&animation=twinkling" alt="Abdelrahman Kamel Elgendy - Full Stack Developer"/>

  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People%20with%20professions/Man%20Technologist%20Medium%20Skin%20Tone.png" alt="Man Technologist Medium Skin Tone" width="250" height="250" />

  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2800&pause=900&color=A78BFA&center=true&vCenter=true&repeat=true&width=780&height=32&lines=Designing+backend+systems+that+scale;REST+APIs+%7C+Microservices+%7C+Auth+%7C+Angular;Writing+code+future-me+won't+curse;Open+to+full+stack+%26+backend+roles" alt="Typing animation"/>
</div>


<!-- ── THEME: REST API response ─────────────────────────── -->
## `GET /api/whoiam`

```http
GET /api/whoiam HTTP/1.1
Host: abdelrahman-kamel-elgendy.dev
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: public, max-age=86400
X-Powered-By: Coffee
X-Debug-Strategy: console.log first, ask questions later...

{
    "name": "Abdelrahman Kamel",
    "title": "Full Stack Developer",
    "core_skills": [
        "RESTful & GraphQL API Design",
        "Microservices & Event-Driven Architecture",
        "Database Modeling & Query Optimization",
        "Auth Systems  (JWT · OAuth2 · Sessions)",
        "Frontend Development  (Angular · TypeScript)"
    ],
    "currently": {
        "building": "Full stack apps: .NET APIs + Angular clients",
        "learning": ["System Design patterns", "AWS Cloud"],
        "focus_on": ["REST APIs", "Angular", "System Design"],
        "open_to": "Exciting full stack opportunities"
    },
    "config": {
        "coffee_dependency": true,
        "favourite_http": 418,
        "principle": "Write code humans can read, machines can run, and future-you won't curse."
    }
}
```

---

<!-- ── THEME: YAML config ───────────────────────────────── -->
## `stack.yml`
 
<div align="center">
<table width="100%">
<tr>
<td valign="middle" width="50%">
 
```yaml
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
    - Angular

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


## Languages
<img src="https://skillicons.dev/icons?i=cs,java,js,ts,py&theme=dark" />
 
<br/>

## Frameworks & Runtimes
<img src="https://skillicons.dev/icons?i=dotnet,spring,nodejs,nestjs,angular&theme=dark" />

<br/>

## Databases & ORMs
<img src="https://skillicons.dev/icons?i=mysql,prisma,mongodb,redis&theme=dark" />

<br/>

## DevOps & Tools
<img src="https://skillicons.dev/icons?i=git,github,docker,postman&theme=dark" />
 
</div>
</td>
</tr>
</table>
</div>

---

## `metrics.sql`
<table width="100%">
<tr>
<td width=50%>

  <!-- LANGS_START -->
```sql
-- ── repo_languages ───────────────
SELECT
    language,
    ROUND(100 * SUM(bytes) / SUM(SUM(bytes)) OVER (), 2) AS share
FROM
    repo_languages
WHERE
    owner = 'abdelrahman-kamel-elgendy'
    AND is_fork = FALSE
GROUP BY
    language
ORDER BY
    share DESC
LIMIT 6;

-- ── Result (2026-11-11) ──
-- +------------+--------+
-- | language   |  share |
-- +------------+--------+
-- | Java       | 46.11% |
-- | C#         | 20.55% |
-- | JavaScript | 19.16% |
-- | HTML       |  6.64% |
-- | TypeScript |  6.01% |
-- | Python     |  1.02% |
-- +------------+--------+
-- 6 rows in set
```
<!-- LANGS_END -->

</td>
<td width=50%>

<!-- STREAK_START -->
```sql
-- ── contribution_calendar ────────
SELECT
    total_contributions,
    tracking_since,
    current_streak,
    current_window,
    longest_streak,
    longest_window
FROM
    contribution_calendar
WHERE
    username = 'abdelrahman-kamel-elgendy';

-- ── Result (2026-11-11) ──
-- +---------------------+-------------------------+
-- | metric              |                   value |
-- +---------------------+-------------------------+
-- | total_contributions |                     675 |
-- | tracking_since      |              2024-02-02 |
-- | current_streak      |                   225 d |
-- | current_window      | 2026-03-31 → 2026-11-10 |
-- | longest_streak      |                   225 d |
-- | longest_window      | 2026-03-31 → 2026-11-10 |
-- +---------------------+-------------------------+
-- 6 rows in set
```
<!-- STREAK_END -->

</td>
</tr>
<tr>
    <td width=50% align="center">
      <img width=100% hight=100% src="https://github-stats-extended.vercel.app/api/top-langs/?username=abdelrahman-kamel-elgendy&hide_border=true&border_radius=12&bg_color=0D1117&title_color=A78BFA&text_color=CDD6F4&layout=compact" alt="Top Languages"/>
    </td>
    <td width=50% align="center">
      <img width=100% hight=100% src="https://streak-stats.demolab.com?user=abdelrahman-kamel-elgendy&hide_border=true&border_radius=12&background=0D1117&ring=A78BFA&fire=7C3AED&currStreakLabel=A78BFA&sideLabels=CDD6F4&currStreakNum=FFFFFF&sideNums=CDD6F4&dates=6B7280" alt="GitHub Streak"/>
    </td>
  </tr>
</table>

<!-- ── THEME: Application log ─────────────────────────── -->
## `daily-backend-tip.log`
 
<!-- TIP_START -->
```log
[2026-11-11 06:59:30.388 +02:00 INF] tip-service Fetching tip of the day...
[2026-11-11 06:59:30.388 +02:00 INF] tip-service GET https://raw.githubusercontent.com/abdelrahman-kamel-elgendy/abdelrahman-kamel-elgendy/main/tips.json  200 OK
[2026-11-11 06:59:30.388 +02:00 INF] tip-service Message received → tip loaded
[2026-11-11 06:59:30.388 +02:00 TIP] tip-service Tip → Monorepos simplify dependency sharing across multiple services in a large codebase.
```
<!-- TIP_END -->
 
---
 
<!-- ── THEME: Application log ─────────────────────────── -->
## `daily-quote.log`
 
<!-- QUOTE_START -->
```log
[2026-11-11 06:59:30.388 +02:00 INF] quote-service Connecting to quotes upstream...
[2026-11-11 06:59:30.388 +02:00 INF] quote-service GET https://zenquotes.io/api/today  200 OK
[2026-11-11 06:59:30.388 +02:00 INF] quote-service Message received → quote loaded
[2026-11-11 06:59:30.388 +02:00 QOT] quote-service Quote → "A random act of kindness, no matter how small, can make a tremendous impact on someone else's life."
[2026-11-11 06:59:30.388 +02:00 AUT] quote-service Author → Roy T. Bennett 
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
</div>
