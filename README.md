<!-- ═══════════════════════ 01 · HERO ═══════════════════════ Gradient header + typing animation. First 5 seconds: name, role, and what you do, in that order. --> <div align="center"> <img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:0f0c29,45:302b63,100:24243e&height=260&section=header&text=Abdelrahman%20Kamel&fontSize=58&fontColor=ffffff&fontAlignY=38&desc=Full%20Stack%20Developer%20%C2%B7%20.NET%20%C2%B7%20Java%20%C2%B7%20Angular&descAlignY=60&descSize=20&descColor=A78BFA&animation=fadeIn" alt="Abdelrahman Kamel - Full Stack Developer"/> <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2800&pause=900&color=A78BFA&center=true&vCenter=true&width=700&lines=Designing+backend+systems+that+scale;REST+APIs+%7C+Microservices+%7C+Auth+%7C+Angular;Writing+code+future-me+won't+curse;Open+to+full+stack+%26+backend+roles" alt="Typing animation"/> <br/> <img src="https://img.shields.io/badge/STATUS-OPEN%20TO%20WORK-22C55E?style=for-the-badge&labelColor=0D1117"/> <img src="https://img.shields.io/badge/ROLE-FULL%20STACK-7C3AED?style=for-the-badge&labelColor=0D1117"/> <img src="https://img.shields.io/badge/BASE-CAIRO%2C%20EG-60A5FA?style=for-the-badge&labelColor=0D1117"/> <img src="https://komarev.com/ghpvc/?username=abdelrahman-kamel-elgendy&style=for-the-badge&color=A78BFA&label=PROFILE+VIEWS&labelColor=0D1117"/> </div> <br/> <!-- ═══════════════════ 02 · IDENTITY (TERMINAL) ═══════════════════ Replaces "About Me" with a shell session. Reads like a real engineer's terminal and answers: who, what, now, next. -->
---

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

<!-- ── THEME: SQL query ────────────────────────────────── -->
<!-- ═══════════════════ GITHUB ANALYTICS ═══════════════════
     Three rows, one per widget: each SQL block is generated daily by
     scripts/update_metrics.py between its START/END markers.
       STATS  -> GitHub Stats card
       STREAK -> Streak card
       LANGS  -> Most Used Languages card
-->
## `metrics.sql`

<table width="100%">
<tr>
<td valign="top" width="50%">

<!-- STATS_START -->
```sql
-- ── github_stats ─────────────────
SELECT
    total_stars,
    total_commits,
    commits_this_year,
    pull_requests,
    merged_pull_requests,
    total_issues
FROM
    github_stats
WHERE
    username = 'abdelrahman-kamel-elgendy';

-- ── Result (2026-11-01) ──
-- +----------------------+-------+
-- | metric               | value |
-- +----------------------+-------+
-- | total_stars          |     0 |
-- | total_commits        |   565 |
-- | commits_this_year    |   452 |
-- | pull_requests        |    28 |
-- | merged_pull_requests |    28 |
-- | total_issues         |     0 |
-- +----------------------+-------+
-- 6 rows in set
```
<!-- STATS_END -->

</td>
<td valign="middle" width="50%" align="center">

<img width="100%" src="https://github-stats-extended.vercel.app/api?username=abdelrahman-kamel-elgendy&show_icons=true&hide_border=true&border_radius=12&bg_color=0D1117&title_color=A78BFA&icon_color=7C3AED&text_color=CDD6F4&rank_icon=github" alt="GitHub Stats"/>

</td>
</tr>
<tr>
<td valign="top" width="50%">

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

-- ── Result (2026-11-01) ──
-- +---------------------+-------------------------+
-- | metric              |                   value |
-- +---------------------+-------------------------+
-- | total_contributions |                     641 |
-- | tracking_since      |              2024-02-02 |
-- | current_streak      |                   216 d |
-- | current_window      | 2026-03-31 → 2026-11-01 |
-- | longest_streak      |                   216 d |
-- | longest_window      | 2026-03-31 → 2026-11-01 |
-- +---------------------+-------------------------+
-- 6 rows in set
```
<!-- STREAK_END -->

</td>
<td valign="middle" width="50%" align="center">

<img width="100%" src="https://streak-stats.demolab.com?user=abdelrahman-kamel-elgendy&hide_border=true&border_radius=12&background=0D1117&ring=A78BFA&fire=7C3AED&currStreakLabel=A78BFA&sideLabels=CDD6F4&currStreakNum=FFFFFF&sideNums=CDD6F4&dates=6B7280" alt="GitHub Streak"/>

</td>
</tr>
<tr>
<td valign="top" width="50%">

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

-- ── Result (2026-11-01) ──
-- +------------+--------+
-- | language   |  share |
-- +------------+--------+
-- | Java       | 48.50% |
-- | JavaScript | 20.15% |
-- | C#         | 16.37% |
-- | HTML       |  6.98% |
-- | TypeScript |  6.32% |
-- | Python     |  1.14% |
-- +------------+--------+
-- 6 rows in set
```
<!-- LANGS_END -->

</td>
<td valign="middle" width="50%" align="center">

<img width="100%" src="https://github-stats-extended.vercel.app/api/top-langs/?username=abdelrahman-kamel-elgendy&hide_border=true&border_radius=12&bg_color=0D1117&title_color=A78BFA&text_color=CDD6F4&layout=compact" alt="Top Languages"/>

</td>
</tr>
</table>

---

<!-- ── THEME: Application log ─────────────────────────── -->
## `daily-backend-tip.log`
 
<!-- TIP_START -->
```log
[2026-11-01 17:30:19.175 +02:00 INF] tip-service Fetching tip of the day...
[2026-11-01 17:30:19.175 +02:00 INF] tip-service GET https://raw.githubusercontent.com/abdelrahman-kamel-elgendy/abdelrahman-kamel-elgendy/main/tips.json  200 OK
[2026-11-01 17:30:19.175 +02:00 INF] tip-service Message received → tip loaded
[2026-11-01 17:30:19.175 +02:00 TIP] tip-service Tip → Database connection strings should never appear in source code or logs.
```
<!-- TIP_END -->
 
---
 
<!-- ── THEME: Application log ─────────────────────────── -->
## `daily-quote.log`
 
<!-- QUOTE_START -->
```log
[2026-11-01 17:30:19.175 +02:00 INF] quote-service Connecting to quotes upstream...
[2026-11-01 17:30:19.175 +02:00 INF] quote-service GET https://zenquotes.io/api/today  200 OK
[2026-11-01 17:30:19.175 +02:00 INF] quote-service Message received → quote loaded
[2026-11-01 17:30:19.175 +02:00 QOT] quote-service Quote → "When something comes from within, when it is a part of you, you have no choice but to live it, to express it."
[2026-11-01 17:30:19.175 +02:00 AUT] quote-service Author → Kamal Ravikant 
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