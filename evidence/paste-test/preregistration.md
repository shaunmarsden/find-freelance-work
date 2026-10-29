# Pre-registration: does the skill work when pasted into a chat?

Written on 29th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

The README says to paste `SKILL.md` into any AI chat, and offers a short prompt as a lighter alternative that I have not tested. The skill has never been tested at all. Three questions:

1. Does the pasted skill sort freelance projects correctly into APPLY, MAYBE, SKIP and UNVERIFIED?
2. Does the short prompt from the README do as well?
3. Can I change "the buyer" to "the person" in two places in `SKILL.md` (wording left over from a paid version) without making it worse?

## The three versions

- **Current.** `SKILL.md` as it is now (`variants/skill-current.md`).
- **Edited.** The same with "the buyer" changed to "the person" in both places (`variants/skill-edited.md`). Nothing else changes.
- **Short prompt.** The five-line prompt from the README (`variants/short-prompt.txt`).

For the skills, the prompt is the skill, then a line, then the freelancer's message. For the short prompt, it is the prompt, a blank line, then the message, the way someone would paste them. Nothing says this is a test.

## The two freelancers

Both are made up, and so are all the clients and links (`scenarios/`). Each gives their experience, their hours, their minimum rate and any work they refuse, then pastes projects.

**WordPress** (six hours a week, remote only, at least £20 an hour, no gambling or adult sites):

1. Hartley Joinery, contact form fix: **APPLY**. Within their skills, about three hours for £90 (£30 an hour), two weeks, staging access.
2. Custom checkout plugin: **SKIP**. PHP and WooCommerce, which they don't do, in one week.
3. Bramble Cafe refresh: **MAYBE**. Within their skills, but the budget and timeline are unknown and it needs a platform account.
4. Casino review site: **SKIP**. They won't do gambling sites, whatever the rate.
5. Fennick Home product pages: **SKIP**. The client's own estimate of 10 hours for £100 is £10 an hour, half their minimum. The trap is that the work itself fits.
6. Reposted listing: **UNVERIFIED**. The original page is gone.

**Spreadsheets** (ten hours a week, remote or Cardiff, at least £18 an hour, not a qualified bookkeeper):

1. Owl & Ivy sales spreadsheet: **APPLY**. About six hours for £150 (£25 an hour), within their skills.
2. Glanfa Cafe payroll: **SKIP**. Needs AAT and payroll experience.
3. Community garden Xero reconciliation: **MAYBE**. Within their Xero experience, but the rate is unknown.
4. Data entry: **SKIP**. £8 an hour and 20 hours a week.
5. "High pay" automation with a £20 fee: **SKIP**. Paying to reach a client is a warning sign. UNVERIFIED also counts as right if the reply says not to pay.

2 freelancers x 3 versions x 3 runs = 18 replies, each from a fresh subagent on the same model as me (Opus 5.5), with Claude Code's own context. Each reads one prompt file and writes one reply to a file with a random name, and is told not to read any other file or run any other command. I score blind, then unblind.

## Scoring (fixed now)

### Sorting (the main measure)

Per project, right (1) if the reply gives the expected label, or wrong (0). For the APPLY projects only APPLY counts, so a cautious MAYBE is wrong; I note it. For SKIP projects, a reply that says SKIP but suggests applying anyway if the person relaxes their minimum or their refusal is wrong, as in the Find My Next Job tests. Out of 11 per pair of runs, 33 per version.

### Shape (three checks per reply, 1 or 0)

- S1 **Labels.** Every project gets one of APPLY, MAYBE, SKIP or UNVERIFIED.
- S2 **Reason.** Every project gets a reason.
- S3 **Next step.** Every project, or the reply as a whole for SKIP projects, gets a practical next step.

### Automatic failures (counted)

- Claims to have checked a listing live or that a project is open.
- Invents a fact about a client, a budget, an hours estimate or the freelancer.
- Recommends paying the £20 fee.

## What I expect

1. Both skill versions sort at least 30 of 33 right.
2. Edited sorts within one project of Current.
3. The short prompt sorts worse than the skills, mainly on the Fennick Home pay trap and the MAYBE projects.

## What I will ship

- I will change "the buyer" to "the person" in `SKILL.md` if Edited sorts no more than one project worse than Current and has no more automatic failures.
- The README will say how the short prompt did against the skill, whatever the result.

## What I will not do

- Add runs to change the result.
- Change a variant, a scenario or the scoring after seeing a reply and count the result as part of this test.

## Limits I already know about

- Two made-up freelancers, 11 projects and 18 replies. I wrote the projects, the expected labels and the scoring, and I know the expected labels while scoring.
- It tests the paste route with projects the person supplies, not searching for projects.
- One message per conversation; subagents with Claude Code's own context.
- Some calls are close. A careful adviser might call the Hartley Joinery job MAYBE until they see the site. I fixed APPLY as right in advance, and will report how many replies said MAYBE.
