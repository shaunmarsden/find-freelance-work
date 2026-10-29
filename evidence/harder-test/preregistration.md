# Pre-registration: a harder test for the freelance skill

Written on 29th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## Why

In the [paste test](../paste-test/results.md), the current skill and the README's short prompt both sorted 33 of 33 projects right, and the version with "the buyer" changed to "the person" sorted 31. The results said the projects were probably too easy to separate the versions. This test uses projects that sit close to a line.

This is a new test with new freelancers and projects. It is not more runs of the paste test.

## The three versions

The same three as the paste test, copied unchanged into `variants/`:

- **Current.** `SKILL.md` as it is now.
- **Edited.** The same with "the buyer" changed to "the person" in both places.
- **Short prompt.** The five-line prompt from the README.

For the skills, the prompt is the skill, then a line, then the freelancer's message. For the short prompt, it is the prompt, a blank line, then the message. Nothing says this is a test.

## The two freelancers

Both are made up, and so are all the clients and links (`scenarios/`).

**Writer** (eight hours a week, remote, at least £22 an hour, no unpaid samples over 200 words; no SEO, technical or medical writing experience):

1. Larchmere annual report proofread: **APPLY**. £240 for the client's estimate of 10 hours is £24 an hour, just above the minimum, with three weeks to do it.
2. Seaview Dental blog posts: **SKIP**. £30 a post at the client's own 1.5 hours a post is £20 an hour, just under the minimum.
3. Brightpath content writer: **SKIP**, or **MAYBE** only if the reply makes it conditional on a sample of 200 words or less, or a paid sample. Wrong if it says APPLY or suggests writing the 1,000-word unpaid sample.
4. Quillhub newsletter editing: **SKIP**. £24 an hour less the 20% platform fee is £19.20, under the minimum. The trap is the headline rate.
5. Northdale patient leaflets: **APPLY** or **MAYBE**. Medical writing is preferred, not essential, a clinician checks every leaflet, and the rate is well above the minimum. Wrong only if it says SKIP. The trap is treating a preferred skill as a requirement.

**Video editor** (12 hours a week, remote or Manchester, at least £25 an hour; no After Effects, motion graphics or colour grading):

1. Ironbark reels: **APPLY**. £320 for the client's 12 hours is £26.67 an hour, just above the minimum, with three weeks.
2. Tidewater YouTube editor: **SKIP**. After Effects is essential.
3. Copper Kettle weekly reels: **MAYBE**. £100 for three to five hours is between £33 and £20 an hour, so it meets the minimum only at the low end of the range. The reply should name the hours as the thing to pin down.
4. Elmstead wedding film: **SKIP**. Colour grading is required, despite £30 an hour.
5. Ancoats Agency: **APPLY**. Three office days in Manchester fits "remote or in Manchester", and £27 an hour for 10 hours fits. The trap is reading the office days as a mismatch.
6. Vantage promo competition: **SKIP**. Unpaid spec work.

2 freelancers x 3 versions x 3 runs = 18 replies, each from a fresh subagent on the same model as me (Opus 5.5), with Claude Code's own context. Each reads one prompt file and writes one reply to a file with a random name, and is told not to read any other file or run any other command. I score blind, then unblind.

## Scoring (fixed now)

### Sorting (the main measure)

Per project, right (1) or wrong (0) against the labels above. For a SKIP project, a reply that says SKIP but suggests applying anyway if the freelancer lowers their minimum or drops a refusal is wrong. Suggesting the freelancer ask the client for more money, a shorter sample or fewer hours is not dropping a limit, and counts as right. Out of 11 per pair of runs, 33 per version.

### Shape (three checks per reply, as in the paste test)

S1 every project gets one of the four labels; S2 every project gets a reason; S3 every project, or the reply as a whole for SKIP projects, gets a next step.

### Automatic failures (counted)

- Claims to have checked a listing live.
- Invents a fact about a client, a budget, an hours estimate or the freelancer.
- Recommends writing the 1,000-word unpaid sample or entering the unpaid competition.

## What I expect

1. At least one version gets at least two projects wrong. These projects are hard enough to separate the versions.
2. The two skill versions sort better than the short prompt, mainly on the platform fee, the hours range and the preferred-not-essential leaflet job.
3. Edited sorts within one project of Current.

## What I will ship

- I will change "the buyer" to "the person" in `SKILL.md` if Edited sorts no worse than Current in this test and has no more automatic failures. (The paste test's rule was "at most one worse". This one is stricter, because Edited already failed once.)
- The README will say how the short prompt did against the skill on these harder projects, whatever the result.

## What I will not do

- Add runs to change the result.
- Change a variant, a scenario or the scoring after seeing a reply and count the result as part of this test.

## Limits I already know about

- Two made-up freelancers, 11 projects and 18 replies. I wrote the projects, the expected labels and the scoring, and I know the expected labels while scoring.
- Some projects allow two right answers (Brightpath, Northdale), which makes them easier to get right.
- It tests projects the freelancer supplies, not searching for projects.
- One message per conversation; subagents with Claude Code's own context.
