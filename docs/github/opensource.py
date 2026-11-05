"""Open source project analysis: catboost/catboost."""

# # Open Source project analysis

# The project I sent a pull request to:
# [catboost/catboost](https://github.com/catboost/catboost)
#
# CatBoost is a gradient boosting on decision trees library developed by
# Yandex. It is used for ranking, classification, regression and other machine
# learning tasks, and supports Python, R, Java and C++ with CPU and GPU
# computation.
#
# All numbers below are from 30 October 2026.

# ## 1. Does it have a license?

# Yes. The `LICENSE` file is in the root of the repository:
# **Apache License 2.0**.
#
# https://github.com/catboost/catboost/blob/master/LICENSE

# ## 2. Write the name of the company and a link to the repository.

# **Company:** Yandex
#
# **Repository:** https://github.com/catboost/catboost
#
# I chose CatBoost because it is a widely used data science tool, written
# mostly in Python and C++.

# ## 3. Does the project accept outside help?

# Yes. `CONTRIBUTING.md` explains the process: discuss the idea in an issue
# first, then send a pull request. There are 18 open issues labelled
# `help wanted` and 22 labelled `good first issue`.

# ## 4. What was your second improvement?

# I fixed spelling mistakes in the English documentation:
# https://github.com/catboost/catboost/pull/3241

# ## 5. How many commits are in the main branch?

# 50,893 commits on `master`.

# ## 6. When was the last commit?

# 30 October 2026.

# ## 7. How many contributors does the project have?

# 189 contributors with GitHub accounts, according to the GitHub API. The count
# is 1,461 with commit authors who have no linked account.

# ## 8. How often is the repository committed to?

# Several times a day on average: 23 commits in the last 7 days and 67 since 1
# October.

# ## 9. How many open issues are there?

# 674.

# ## 10. Do the maintainers respond quickly to new issues?

# Often not. Of the 19 newest issues from other people, 14 have no comments at
# all. Among the rest, the first comment came anywhere from a few hours to more
# than two weeks later.

# ## 11. Is there active discussion on the issues?

# Not much. Those same 19 issues have at most 2 comments each.

# ## 12. Are there recently created issues?

# Yes. The newest issue from someone else was opened on 28 October 2026.

# ## 13. Are there closed issues?

# Yes, 1,913.

# ## 14. How many open pull requests are there?

# 76, including 7 from Dependabot and my 2.

# ## 15. Do the maintainers respond quickly to new pull requests?

# It varies. #3237 and #3235 got their first review about 2 days after opening.
# #3200 waited 15 days, and #3217 and #3212 have had no reply for over 2 weeks.

# ## 16. Is there active discussion on the pull requests?

# Moderately. Pull requests that maintainers pick up get a review and a few
# comments, as in #3198 and #3184, but many others have none.

# ## 17. Are there recently submitted pull requests?

# Yes. The newest from someone else was opened on 28 October 2026.

# ## 18. How long ago were pull requests last merged?

# GitHub's last **Merged** status is from 11 January 2024 (#2566), but that is
# misleading. Accepted pull requests are now imported into Yandex's internal
# repository by `robot-magpie`, then closed and synced back. So they show as
# **Closed**, not **Merged**. The most recent one, #3237, was closed this way
# on 30 October 2026.

# # My contribution

# Links

# **PEP8 issue I created:** https://github.com/catboost/catboost/issues/3239
#
# **First improvement (linters, PEP8):**
# https://github.com/catboost/catboost/pull/3240
#
# **Second improvement (documentation typos):**
# https://github.com/catboost/catboost/pull/3241
#
# **first-contributions pull request:**
# https://github.com/firstcontributions/first-contributions/pull/127656
#
# Status on 5 November 2026:
#
# - first-contributions #127656 is merged.
# - CatBoost #3241 was approved by a maintainer, imported into Yandex's
#   internal repository and closed by `robot-magpie` on 30 October 2026. This
#   is how CatBoost accepts pull requests (see question 18).
# - CatBoost #3240 is approved by a maintainer and imported into the internal
#   repository. It is still open and waiting to be synced back.
