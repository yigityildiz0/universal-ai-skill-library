---
name: primary-source-research
description: "Answer research questions from primary sources: official docs, specifications, source code and first-party records. Return cited findings in chat; create a repository memo only when requested. TR: resmi dokümandan araştır, API nasıl çalışıyor, birincil kaynaktan doğrula, kaynaklı not dosyası çıkar."
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


Use an authorized **background agent** when the host supports delegation and there is independent work to continue; otherwise do the reading inline. Never subdelegate from a worker.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Cite each consequential claim's primary source. Write a single Markdown memo when the user requests a file/repository note; otherwise return the cited findings in chat.
3. For a requested file, use the repo's existing notes convention or a sensible agreed path and report it. Do not overwrite user work or upload the memo automatically.

## Extensions (host-portable adaptation)

Upstream skill: [mattpocock/skills `research`](https://github.com/mattpocock/skills) (MIT). Renamed to `primary-source-research` because the Weizhena family also uses `research`. This is a local adaptation; `/research` is an upstream name, not a registered command here.

1. **Narrow the question first.** One API, one behaviour, one version claim; split broad "research X" requests. Stop when the question is answered or shown unanswerable from primary sources, and list what remains unknown.
2. **Delegation guard.** If you are already running as a background or sub-agent, do the work yourself and never spawn another research agent (prevents the duplicate-run bug). If the host forbids delegation or has none, do the reading inline.
3. For libraries prefer Context7 or vendor docs. Record the access date and version per claim. In chat-only hosts return the memo in the conversation.
4. Quality check: follow two random citations; they must land on an official doc, spec or source file, not a write-up of it.
