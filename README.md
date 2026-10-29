# Find Freelance Work

A free AI skill that helps you judge freelance projects against what you can actually do, the hours you have and the pay you need.

Paste in a project advert and it tells you **APPLY**, **MAYBE**, **SKIP** or **UNVERIFIED**, with the reason and one practical next step. It can also suggest legitimate places to look, and help you write a short, honest reply to a project that fits. It won't apply, send messages or sign you up to anything without your say-so.

**[See a worked example](examples/fictional-project-review.md)**

## Use it

The quickest way needs no install.

1. Open [SKILL.md](SKILL.md), click **Raw**, and copy the whole file.
2. Paste it into any AI chat (ChatGPT, Claude, Gemini, Copilot or similar).
3. Underneath, say what work you can offer, then paste a project advert. For example:

   > I've built a few WordPress sites for friends and can spend six hours a week. Is this project worth applying for?

If you'd rather not paste the whole skill, this shorter prompt matched or beat it in my two tests ([first](evidence/paste-test/results.md), [harder](evidence/harder-test/results.md)). The skill was a little more cautious, sometimes saying MAYBE where the prompt said APPLY. The prompt also suggests places to look:

```text
Help me find freelance work. Start by asking what I can actually deliver,
my location, hours per week and minimum pay. Recommend sensible places
to look. When I paste a project description, tell me APPLY, MAYBE, SKIP
or UNVERIFIED, with a reason and one practical next step. Don't invent
open jobs or pretend to browse sites you can't access.
```

### Or install it

If you use an AI tool that loads skills from a folder, such as Claude Code or Codex, download this repository (the green **Code** button, then **Download ZIP**) and install the folder. `agents/openai.yaml` holds a display name, short description and starter prompt for tools that read it.

## What it is good for, and what it isn't

**Good for: judging adverts you bring.** It checks the work asked for against your real experience, the deadline against your hours, and the pay against the likely work, and it says what is unknown.

**Not reliable for: finding open projects on its own.** If your AI tool can search the web, the skill may look, but it will tell you when it can't check a page. In an early feasibility check, which isn't published here, there were no suitable open projects for a made-up freelancer across eleven kinds of source. So treat it as a second opinion on adverts you find, not a job feed.

It doesn't promise earnings, and it won't call a project vetted or guaranteed.

## Things to know

- **Leave out private details.** Don't paste client data, logins or anything confidential from an employer.
- **Check before you apply.** Adverts close and change. Read the original listing and its terms yourself.
- **It only does what your AI tool can do.** Browsing and reading attachments depend on the tool, not the skill.

## Looking for a job instead?

[Find My Next Job](https://github.com/shaunmarsden/find-my-next-job) does the same kind of sorting for employed roles, against your hours, location and minimum pay.

## Licence

MIT. See [LICENSE](LICENSE).
