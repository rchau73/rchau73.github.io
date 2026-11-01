"""Generate the watch pages (one per film) and the sitemap for rchau73.github.io."""
import html, json, os, sys

SITE = sys.argv[1]
BASE = "https://rchau73.github.io"
DEFAULT_SCOPE = "It shows the agentic approach: how AI agents and people share the work."

FILMS = [
 dict(slug="ai-agent-team", file="video1-ai-agent-team.mp4", poster="video1-poster.jpg", secs=36, date="2026-10-30",
  title="An engineering team made of AI agents",
  desc="One real ticket through a loop of AI agents (domain expert, product manager, developer, reviewer) and the change that stops at a person; then October in numbers: over 300 pull requests merged and, in the last week, 4 minutes from merge to live with a 1 % change failure rate.",
  lede="I run an engineering team made of AI agents on optionsBot, a trading system on an exchange's test environment. This film follows one real ticket through it, and shows what I still decide myself.",
  scenes=[
   ("0:04","One ticket, five roles.","Issue #553: a repair picked a strike from a broken quote. The domain-expert agent spots it in the live bots and files the issue with evidence. The product-manager agent places it in the strategy epic and moves it to Ready. The Dev agent writes the fix and its tests and opens PR #556. The Reviewer agent checks the diff against the repository's rules. It changes a trading rule, which is policy, so I read it and merge it."),
   ("0:16","Agents propose everything. A person merges what carries risk.","Docs and monitor pages, tests and tooling, and agent-workflow fixes ship on their own once reviewed clean with CI green. Trading and risk rules, configuration and CI, agent permissions and every release to stable wait for me."),
   ("0:24","One month of delivery, October 2026.","Over 300 pull requests merged, 167 of them written by the Dev agent. The film's other two figures come from the last week of October, on mvp, the test environment: 4 minutes from merge to live (median) and a 1 % change failure rate (1 of 85 changes)."),
   ("0:32","AI writes the code. I decide what ships.",""),
  ]),
 dict(slug="two-mistakes-caught", file="video2-two-mistakes-caught.mp4", poster="video2-poster.jpg", secs=36, date="2026-10-30",
  title="Two AI mistakes in one day",
  desc="On 30 October 2026 an AI agent made two mistakes on optionsBot: fake but realistic keys in a test file, and a rebuild on the wrong base that reverted merged work. A secret scan and the Reviewer agent stopped both before they reached main.",
  lede="Two mistakes by AI agents on the same day, 30 October 2026. Neither reached the main branch, because the guardrails were already in place.",
  scenes=[
   ("0:04","Mistake 1, 03:44 UTC.","The Dev agent opens PR #545 with realistic-looking fake keys in a test file, in a public repository. Go tests and lint pass; the secret scan, which checks every commit, fails and stops the PR."),
   ("0:14","Mistake 2, 16:18 UTC.","An AI rebuild of that PR, made on the wrong base, adds the intended API-key permission check (#538) but also removes two merged features: a clearer connection error (#524) and account deletion (#543). The Reviewer agent reads the diff and blocks it: the PR reverts merged work unrelated to #538."),
   ("0:25","Fixed at 18:32 UTC.","Rebuilt as PR #552 with only the intended change: secret scan clean, nothing deleted, reviewed and merged by me. Neither mistake cost anything."),
   ("0:32","Agents make mistakes. Guardrails make them cheap.",""),
  ]),
 dict(slug="delivery-measured", file="video3-delivery-measured.mp4", poster="video3-poster.jpg", secs=36, date="2026-10-30",
  title="Delivery, measured",
  desc="The four DORA metrics for a team of AI agents in the week of 26 October 2026, one change from issue to live in 50 minutes, and why the test and stable environments move at different speeds.",
  lede="How fast does a team of AI agents ship? I don't guess; I measure it, with the four DORA metrics per environment.",
  scenes=[
   ("0:04","The four DORA metrics, week of 26 October 2026, mvp.","84 deploys in one week; 4 minutes from merge to live (median, p90 7 minutes); 1 % change failure rate (1 of 85); 57 minutes to restore (one incident). Elite on three of the four by DORA bands; time to restore has one sample, too few to rate."),
   ("0:13","One change, 30 October 2026 (UTC).","18:55 issue #553 filed with evidence; 19:31 the Dev agent opens PR #556 with tests; 19:40 it changes a trading rule, so I merge it; 19:45 live on mvp, the test environment. From a filed issue to live in 50 minutes, with a person on the risky step."),
   ("0:24","Two speeds, on purpose.","mvp: 4 minutes from merge to live, on every merge. stable: 3.1 days median, because every release soaks 3 days on mvp first."),
   ("0:32","Fast where it's safe. Slow where it matters.",""),
  ]),
 dict(slug="ai-reviewer", file="video4-ai-reviewer.mp4", poster="video4-poster.jpg", secs=36, date="2026-10-30",
  title="What an AI reviewer catches",
  desc="158 AI code reviews on optionsBot: 19 blocked a merge. Three real bugs it caught, and what an AI reviewer still can't decide.",
  lede="Every pull request on optionsBot gets a review from a Reviewer agent. Here is what 158 of those reviews caught, and what they can't do.",
  scenes=[
   ("0:04","158 reviews, by verdict.","132 clean, 19 blocked a merge, 4 runs failed and were retried, 3 incomplete and re-run. About 1 in 8 reviews stopped a change before it merged."),
   ("0:13","Three of the 19 blocks.","PR #241: a deploy could lose the realised P&L of a close that filled while resting. PR #271: re-running setup regenerated the admin password, so sign-in failed. PR #551: the rebuild would have reverted two merged features."),
   ("0:24","What it can't do.","Decide whether a trading rule is right: those changes wait for me. Review files it didn't read: 3 reviews said so and were run again. Replace the pipeline: CI still gates every merge."),
   ("0:32","A second pair of eyes. Not the last one.",""),
  ]),
 dict(slug="agile-board", file="videoA-agile-board.mp4", poster="videoA-poster.jpg", secs=44, date="2026-10-31",
  title="Agile with AI agents",
  desc="How a team of AI agents runs Agile on a real GitHub Projects board: epics from an approved PRD, triage, a Dev agent pull request and a Reviewer agent block. For engineering managers and Agile leaders.",
  lede="A real board and a real ticket: how the AI agents on optionsBot work in Kanban, with epics from an approved product requirements document and a person owning the decisions.",
  scenes=[
   ("0:04","The board.","GitHub Projects, with epics from an approved PRD. The PM agent places every new ticket in one of them."),
   ("0:11","Every story lives in one epic.","Epic E1 (issue #134): 21 of 22 stories done, each linked to the pull request that closed it."),
   ("0:18","The flow.","Triage → Ready → Build → Review → Done. Agents move the cards; Blocked waits for a person. 235 cards are Done."),
   ("0:25","PR #556, opened by the Dev agent.","Every pull request states its plan, changes, tests, risk and rollout. This one changes a trading rule, so a person merges it."),
   ("0:32","PR #551, the Reviewer agent.","A blocking finding sends it back: the Reviewer agent read the diff and blocked a PR that would have deleted shipped work."),
   ("0:39","Agents do the work. A person owns the decisions.",""),
  ]),
 dict(slug="devops", file="videoB-devops.mp4", poster="videoB-poster.jpg", secs=42, date="2026-10-31",
  title="DevOps for a team of AI agents",
  desc="A scheduler wakes the AI agents every 6 minutes; one ticket goes from epic to Done in 45 minutes; CI runs on GitHub Actions on every push; stable takes a release only after a 3-day soak or an escalation with its reason on record.",
  lede="Every 6 minutes a scheduler wakes the agents that work on optionsBot, a trading system I run on an exchange's test environment. CI, deploys and releases do the rest; the changes that carry risk wait for a person.",
  scenes=[
   ("0:04","The scheduler.","One macOS launchd job, every 360 seconds. Each tick runs, in order: <code>deploy.sh</code> (main to the mvp environment, health check, cards to Done), <code>pr_gate.sh</code> (CI green → ready; reviewed clean → merge), the Reviewer agent, the Dev agent (one Ready card → a pull request) and the PM agent (triage, epics, board ranking). Daily and weekly jobs add DORA metrics, flaky-test checks, backups and reports. The Dev and Reviewer agents each work in their own git worktree."),
   ("0:12","One ticket in the logs.","Ticket #553 on 30 October 2026, local time (UTC−3): tagged with its epic at 16:00, the Dev agent starts at 16:08, the pull request with tests opens at 16:31, CI is green at 16:36, I merge it at 16:40 (it changes a trading rule, so a person merges it), it is deployed and healthy at 16:45 and the card moves to Done. From epic to Done in 45 minutes."),
   ("0:22","CI on GitHub Actions.","Every push and pull request runs a secret scan, lint, tests under the race detector, a coverage floor, the frontend build, a vulnerability scan and a Docker build."),
   ("0:31","Audited releases.","Every deploy is recorded in <code>deploys.tsv</code>. Stable moves only by release: after 3 days on mvp, or by an escalation whose reason is kept on record."),
   ("0:38","Engineering excellence, automated. Judgement, kept human.",""),
  ]),
 dict(slug="product", file="videoC-product.mp4", poster="videoC-poster.jpg", secs=56, date="2026-10-31",
  title="The product the agents built",
  desc="A tour of the optionsBot monitor, built by a team of AI agents: the overview, positions in a short strangle, a one-legged position in a negative gamma regime, the worst case, income with losses shown, the activity journal and an AI assistant with sourced answers.",
  lede="What the agents built: a monitor for an options bot running on Deribit testnet, designed to give the answer first and to show losses as clearly as gains.",
  scope="It shows the product the agents built, at a glance.",
  scenes=[
   ("0:04","Overview.","The answer first, coin before dollars: what it earned, what is open, the worst case and the margin used."),
   ("0:10","Each bot.","Each bot's market and positions, and a one-line reason for its last trade."),
   ("0:16","Positions: a short strangle.","A call and a put, sold together: what it pays at expiry, what it costs to close now, and the bot's exit lines."),
   ("0:22","One leg, on purpose.","In a negative gamma regime with a bear trend, the bot stops selling puts, and the page says why."),
   ("0:28","Worst case.","Risk in plain words: what a very bad day would cost, in coin and dollars, and what the estimate can't promise."),
   ("0:34","Income.","Losses shown as clearly as gains: October is a loss so far on testnet, and the page says so in the same place as the gains."),
   ("0:40","Activity.","What the bot did, and why: every decision comes from the bot's journal, written in plain English."),
   ("0:46","Assistant.","An AI assistant answers from the docs and the bot's own journal, and links its sources."),
   ("0:52","Built by agents. Made for people.",""),
  ]),
]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} — Roberto Chau</title>
<meta name="description" content="A {secs}-second film: {desc_attr} By Roberto Chau.">
<meta name="author" content="Roberto Chau">
<link rel="canonical" href="{url}">
<meta property="og:type" content="video.other">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc_attr}">
<meta property="og:image" content="{base}/media/{poster}">
<meta property="og:video" content="{base}/media/{file}">
<meta property="og:video:type" content="video/mp4">
<meta property="og:video:width" content="1080">
<meta property="og:video:height" content="1080">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="../../style.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<header class="top">
  <div class="wrap top-row">
    <a class="mark" href="../../" aria-label="Roberto Chau, home">RCH</a>
    <nav>
      <a href="../../#work">Work</a>
      <a href="../../#films">Films</a>
      <a href="../../#sdlc">AI SDLC</a>
      <a href="../../#contact">Contact</a>
    </nav>
  </div>
</header>

<main>
  <section class="wrap watch">
    <p class="eyebrow">Film · {secs} seconds · captioned</p>
    <h1>{title}</h1>
    <figure class="video watch-video">
      <video controls muted playsinline preload="metadata" poster="../../media/{poster}" width="1080" height="1080">
        <source src="../../media/{file}" type="video/mp4">
      </video>
    </figure>
    <p class="lede">{lede}</p>
    <aside class="scope" role="note"><b>About this page.</b> {scope} It is not a detailed account of the implementation. For the scripts, the agents' rules and the full workflow, see the <a href="https://github.com/rchau73/optionsBot">repository on GitHub</a>.</aside>

    <h2 class="sub">What the film shows</h2>
    <ol class="scenes">
{scenes}
    </ol>

    <h2 class="sub">More films</h2>
    <ul class="more-films">
{more}
    </ul>

    <p class="note">A personal study project on testnet: not a commercial product and not investment advice.</p>
    <div class="cta">
      <a class="btn primary" href="../../#work">Read the case study</a>
      <a class="btn" href="https://www.linkedin.com/in/robertochau">LinkedIn</a>
      <a class="btn" href="https://github.com/rchau73/optionsBot">Code on GitHub</a>
    </div>
  </section>
</main>

<footer class="wrap foot">
  <span>© 2026 Roberto Chau</span>
  <span>Built with Claude Code; hosted on GitHub Pages.</span>
</footer>
</body>
</html>
"""

def scene_li(ts, head, body):
    text = f"<b>{head}</b>" + (f" {body}" if body else "")
    return f'      <li><span class="ts">{ts}</span><div>{text}</div></li>'

for f in FILMS:
    url = f"{BASE}/videos/{f['slug']}/"
    ld = {"@context": "https://schema.org", "@type": "VideoObject", "name": f["title"], "description": f["desc"],
          "thumbnailUrl": f"{BASE}/media/{f['poster']}", "uploadDate": f["date"], "duration": f"PT{f['secs']}S",
          "contentUrl": f"{BASE}/media/{f['file']}", "embedUrl": url, "inLanguage": "en",
          "creator": {"@type": "Person", "name": "Roberto Chau", "url": f"{BASE}/"}}
    more = "\n".join(f'      <li><a href="../{o["slug"]}/">{o["title"]}</a></li>' for o in FILMS if o is not f)
    page = PAGE.format(title=f["title"], secs=f["secs"], desc_attr=html.escape(f["desc"]), url=url, base=BASE,
                       poster=f["poster"], file=f["file"], ld=json.dumps(ld, ensure_ascii=False),
                       lede=f["lede"], scope=f.get("scope", DEFAULT_SCOPE),
                       scenes="\n".join(scene_li(*s) for s in f["scenes"]), more=more)
    os.makedirs(f"{SITE}/videos/{f['slug']}", exist_ok=True)
    open(f"{SITE}/videos/{f['slug']}/index.html", "w").write(page)

def x(s): return html.escape(s, quote=False)
urls = [f"  <url><loc>{BASE}/</loc><lastmod>2026-11-01</lastmod></url>"]
for f in FILMS:
    urls.append(f"""  <url>
    <loc>{BASE}/videos/{f['slug']}/</loc><lastmod>2026-11-01</lastmod>
    <video:video>
      <video:thumbnail_loc>{BASE}/media/{f['poster']}</video:thumbnail_loc>
      <video:title>{x(f['title'])}</video:title>
      <video:description>{x(f['desc'])}</video:description>
      <video:content_loc>{BASE}/media/{f['file']}</video:content_loc>
      <video:duration>{f['secs']}</video:duration>
      <video:publication_date>{f['date']}</video:publication_date>
    </video:video>
  </url>""")
open(f"{SITE}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n' + "\n".join(urls) + "\n</urlset>\n")
print("ok", len(FILMS))
