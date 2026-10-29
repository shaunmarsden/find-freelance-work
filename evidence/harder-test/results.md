# Results: a harder test for the freelance skill

Run on 29th October 2026. The [pre-registration](preregistration.md) was committed at 09:57 GMT, before any reply existed, and the [scores](scores-blind.md) at 11:04 GMT, before I looked at which version wrote which reply. The first launch failed on a usage limit before any reply was written, and I relaunched the same 18 prompts once it reset.

## The result

| Version | Projects sorted right | Shape (out of 3) | Automatic failures |
| --- | --- | --- | --- |
| Current skill | 30 of 33 | 3.00 | 0 |
| Edited skill ("buyer" to "person") | 31 of 33 | 3.00 | 0 |
| Short prompt from the README | 33 of 33 | 3.00 | 0 |

## What happened against what I predicted

1. **At least one version gets at least two projects wrong.** Held: the current skill got three wrong.
2. **The skill sorts better than the short prompt.** Did not hold. The short prompt matched my expected labels on all 33.
3. **Edited within one project of Current.** Held: Edited got one more right.

## What separated the versions

**One job.** Every miss in the test was the Ancoats Agency job, which I expected to be APPLY: £27 an hour, 10 hours a week, three days in a Manchester office, for a freelancer who works "remote or in Manchester". Five of the six skill replies called it MAYBE. The short-prompt replies all called it APPLY.

**The skill's reason was a fair one.** None of the five misread the office days as breaking the location limit. Each said that 10 hours over three office days means short days with an unpaid commute, which could pull the real rate below £25, and that it would take 10 of the freelancer's 12 hours. I hadn't thought of that when I wrote the expected labels. I scored them wrong because I fixed APPLY in advance, but I wouldn't call the skill's answer worse advice.

**Everything else was the same.** Every reply, in every version:
- caught the 20% platform fee that took £24 an hour down to £19.20;
- caught the dental posts at £20 an hour, against a £22 minimum;
- treated "preferred, not essential" medical experience as no reason to skip;
- refused the 1,000-word unpaid sample and the unpaid competition;
- called the cafe reels MAYBE, because the rate ranged from £20 to £33 an hour depending on hours.

## Across both tests

| Version | Paste test | Harder test | Total |
| --- | --- | --- | --- |
| Current skill | 33 of 33 | 30 of 33 | 63 of 66 |
| Edited skill | 31 of 33 | 31 of 33 | 62 of 66 |
| Short prompt | 33 of 33 | 33 of 33 | 66 of 66 |

All seven skill misses across the two tests were MAYBE where I expected APPLY, each for a stated, reasonable caution. The short prompt never did this. On these made-up projects, the short prompt is at least as good as the full skill, and the skill leans more cautious.

## What I will ship

- **The "buyer" change.** My rule was to ship it if Edited sorted no worse than Current here and had no more automatic failures. It sorted one better (31 against 30) with none, so I will change "the buyer" to "the person" in a separate pull request. The two versions are within one project of each other in both tests, so I read this as the wording making no difference, not as an improvement.
- **The README.** It will say that the short prompt matched or beat the skill on both sets, and that the skill leaned more cautious.

## How much weight this bears

- **It is small.** 18 replies, two made-up freelancers and 11 projects, all written by me, scored by me while knowing the expected labels.
- **The differences rest on one job.** Ancoats accounts for every miss. A different set might reverse it.
- **Two projects allowed two right answers** (Brightpath, Northdale), which made them easier.
- **It tests projects the freelancer supplies,** not searching for projects.
- **The replies came from subagents** with Claude Code's own context, on the same model as me (Opus 5.5).

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 18 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version, freelancer and run.
- `analyse.py`: unblinds and adds up the totals. Run `python3 evidence/harder-test/analyse.py evidence/harder-test`.
