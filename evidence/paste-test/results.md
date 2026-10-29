# Results: does the skill work when pasted into a chat?

Run on 29th October 2026. The [pre-registration](preregistration.md) was committed at 09:25 GMT, before any reply existed, and the [scores](scores-blind.md) at 09:28 GMT, before I looked at which version wrote which reply.

## The result

Six replies per version (two made-up freelancers, three runs each):

| Version | Projects sorted right | Shape (out of 3) | Automatic failures |
| --- | --- | --- | --- |
| Current skill | 33 of 33 | 3.00 | 0 |
| Edited skill ("buyer" to "person") | 31 of 33 | 3.00 | 0 |
| Short prompt from the README | 33 of 33 | 3.00 | 0 |

## What happened against what I predicted

1. **Both skill versions sorted at least 30 of 33.** Held: 33 and 31.
2. **Edited within one project of Current.** Did not hold: two worse.
3. **The short prompt sorts worse than the skill.** Did not hold. It sorted all 33 right, the same as the current skill.

## What this means

**The skill works when pasted.** Every reply gave each project one of the four labels, a reason and a next step. Every reply held the freelancer's limits. All nine WordPress replies skipped the gambling site whatever the rate, and worked out that Fennick Home paid £10 an hour against a £20 minimum. None of the nine spreadsheet replies told the freelancer to pay the £20 fee.

**The short prompt did just as well.** On these projects, the five-line prompt in the README matched the full skill. The short-prompt replies also suggested places to look (PeoplePerHour, Upwork, Fiverr, local networks), because the prompt asks for that. The README now says the short prompt matched the skill in this test.

**I am not making the "buyer" change.** Both of the Edited version's misses were the Hartley Joinery contact-form job, which it called MAYBE instead of APPLY. Every reply, whichever version, flagged the same real risk: fixing email after a hosting move is new to this freelancer. I fixed APPLY as the only right answer in advance, and my rule was that Edited could be at most one project worse. It was two worse, so `SKILL.md` keeps "the buyer". I doubt the word caused the MAYBEs, since it appears only in the section about searching for projects, and these messages only asked for projects to be judged. But changing the rule after seeing the result would defeat the point of setting it first.

## How much weight this bears

- **It is small.** 18 replies, two made-up freelancers and 11 projects, all written by me, scored by me while knowing the expected labels.
- **The projects may have been too easy to separate the versions.** Every version got almost everything right. A harder set (vaguer briefs, mixed signals, a rate just under the minimum) might show differences this one didn't.
- **It tests the paste route with projects the freelancer supplies,** not searching for projects.
- **The replies came from subagents** with Claude Code's own context, on the same model as me (Opus 5.5).

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 18 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, freelancer and run.
- `analyse.py`: unblinds and adds up the totals. Run `python3 evidence/paste-test/analyse.py evidence/paste-test`.
